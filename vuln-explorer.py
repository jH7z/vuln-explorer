import json
import cmd
import re
from prettytable import PrettyTable
from html import unescape
import textwrap

def clean_html(raw_html):
    clean_text = re.sub(r'<.*?>', '', raw_html)
    return unescape(clean_text) 

def wrap_text(text, max_width=40):
    return "\n".join(textwrap.wrap(text, width=max_width))

# Modify the JSON path if needed
def load_vulnerabilities(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

def search_vulnerabilities(vulnerabilities, search_term, filter_by=None):
    results = []
    for vuln in vulnerabilities:
        if filter_by:
            if filter_by.lower() in vuln.get(search_term, '').lower():
                results.append(vuln)
        else:
            if any(search_term.lower() in str(vuln[key]).lower() for key in vuln):
                results.append(vuln)
    return results

def display_vulnerabilities(vulnerabilities):
    table = PrettyTable()
    table.field_names = ["ID", "Title", "CVSS Score", "Description", "Remediation", "Type", "Created At"]

    table.max_width = 40
    table.align = "l" 

    for vuln in vulnerabilities:
        description = clean_html(vuln.get('description', ''))
        remediation = clean_html(vuln.get('recommendation', ''))
        
        # Wrap text to fit within the max width
        description = wrap_text(description, max_width=40)
        remediation = wrap_text(remediation, max_width=40)

        table.add_row([
            vuln.get('id', ''),
            vuln.get('title', ''),
            vuln.get('cvss_score', ''),
            description,
            remediation,
            vuln.get('type', ''),
            vuln.get('created_at', '')
        ])

    print(table)

class VulnExplorerCLI(cmd.Cmd):
    intro = 'Welcome to Vuln-Explorer! Type help or ? to list commands.'
    prompt = '(vuln-explorer) '

    def __init__(self, vulnerabilities, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vulnerabilities = vulnerabilities

    def do_search(self, arg):
        """Search for vulnerabilities. Example: search clickjacking"""
        search_term = arg.strip()
        if not search_term:
            print("Please provide a search term!")
            return
        results = search_vulnerabilities(self.vulnerabilities, search_term)
        if results:
            display_vulnerabilities(results)
        else:
            print(f"No vulnerabilities found matching '{search_term}'.")

    def do_list(self, arg):
        """List all vulnerabilities"""
        display_vulnerabilities(self.vulnerabilities)

    def do_filter(self, arg):
        """Filter vulnerabilities by CVSS score or type. Example: filter cvss_score 3.1"""
        if not arg:
            print("Please provide a filter field and value (e.g., cvss_score 3.1).")
            return
        parts = arg.split()
        if len(parts) != 2:
            print("Invalid filter format. Use: filter <field> <value>")
            return
        field, value = parts
        results = search_vulnerabilities(self.vulnerabilities, value, field)
        if results:
            display_vulnerabilities(results)
        else:
            print(f"No vulnerabilities found for {field} = {value}.")

    def do_exit(self, arg):
        """Exit the tool"""
        print("Exiting Vuln-Explorer. Goodbye!")
        return True

    def do_quit(self, arg):
        """Quit the tool (alias for exit)"""
        return self.do_exit(arg)

def run_tool(json_file):
    vulnerabilities = load_vulnerabilities(json_file)
    VulnExplorerCLI(vulnerabilities).cmdloop()

if __name__ == "__main__":
    json_file = 'VulnDB.json'  # Replace this with your JSON file path
    run_tool(json_file)

