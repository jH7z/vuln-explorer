# Vuln-Explorer

Vuln-Explorer is a command-line tool that helps security professionals and penetration testers quickly search, list, and filter vulnerabilities from a JSON file containing security vulnerabilities. It provides an interactive interface with a variety of commands to help you easily explore the vulnerabilities database.

## Features

- Search vulnerabilities based on keywords.
- List all vulnerabilities in a tabular format.
- Filter vulnerabilities by CVSS score or type.
- View details about each vulnerability, including its title, CVSS score, description, and remediation.
- Interactive CLI with a friendly prompt.

## Installation

Clone the repository:
```
git clone https://github.com/your-username/vuln-explorer.git
cd vuln-explorer
```

Install dependencies:
Ensure you have Python 3.x installed. You can install required libraries using pip:
```
pip install -r requirements.txt
```

The `requirements.txt` file includes:

- `prettytable`: For displaying the vulnerability table in a readable format.
- `textwrap`: For wrapping long text descriptions and remediation.

Run the tool:
Make sure your JSON file with vulnerabilities (e.g., `vulnerabilities.json`) is in the same directory as the script or update the path accordingly. Run the tool by executing:
```
python vuln-db.py
```
## Commands:

`list`

Displays all the vulnerabilities in a well-organized table. The table shows:

- **ID:** The unique identifier for the vulnerability.
- **Title:** The title of the vulnerability.
- **CVSS Score:** The CVSS score associated with the vulnerability.
- **Description:** A brief description of the vulnerability (HTML tags will be removed).
- **Remediation:** The suggested remediation to fix the vulnerability.
- **Type:** The type of vulnerability (e.g., Web Application, Mobile, etc.).
- **Created At:** The date when the vulnerability was first created.

Example:
```
(vuln-explorer) list
```
`search <term>`

Search for vulnerabilities that contain a specific keyword in any field (title, description, remediation, etc.). You can use any term or partial keyword for the search.

Example:
```
(vuln-explorer) search clickjacking
```
`filter <field> <value>`

Filter vulnerabilities by a specific field (e.g., `cvss_score` or `type`) and value. Only vulnerabilities that match the filter criteria will be shown.

Available fields for filtering:

- `cvss_score`: Filter by the CVSS score (e.g., `3.1`, `7.5`).
- `type`: Filter by the type of vulnerability (e.g., `Web Application`, `Mobile`).

Example:
```
(vuln-explorer) filter cvss_score 3.1
(vuln-explorer) filter type Web Application
```
`exit` / `quit`

Exit the `Vuln-Explorer` CLI tool.

Example:
```
(vuln-explorer) exit
```
`help` or `?`

Shows a list of available commands and usage instructions.

Example:
```
(vuln-explorer) help
```

## Example Usage

**Listing vulnerabilities:**
```
(vuln-explorer) list
+-----+-------------------------+------------+------------------------------------------+------------------------------------------+------------------+---------------------------+
| ID  | Title                   | CVSS Score | Description                              | Remediation                              | Type             | Created At               |
+-----+-------------------------+------------+------------------------------------------+------------------------------------------+------------------+---------------------------+
| 2   | User-Interface Redressing| 3.1        | The application fails to prevent...      | Prevent websites from loading...        | Web Application  | 2015-06-09T10:10:43+00:00 |
| 4   | TLS Certificate Pinning  | 3.7        | The application does not make use of...  | Implement TLS certificate pinning...    | Mobile           | 2016-07-12T15:04:36+00:00 |
+-----+-------------------------+------------+------------------------------------------+------------------------------------------+------------------+---------------------------+
```

**Searching vulnerabilities:**
```
(vuln-explorer) search clickjacking
+-----+-------------------------+------------+------------------------------------------+------------------------------------------+------------------+---------------------------+
| ID  | Title                   | CVSS Score | Description                              | Remediation                              | Type             | Created At               |
+-----+-------------------------+------------+------------------------------------------+------------------------------------------+------------------+---------------------------+
| 2   | User-Interface Redressing| 3.1        | The application fails to prevent...      | Prevent websites from loading...        | Web Application  | 2015-06-09T10:10:43+00:00 |
+-----+-------------------------+------------+------------------------------------------+------------------------------------------+------------------+---------------------------+
```

**Filtering by CVSS Score:**
```
(vuln-explorer) filter cvss_score 3.7
+-----+-------------------------+------------+------------------------------------------+------------------------------------------+------------------+---------------------------+
| ID  | Title                   | CVSS Score | Description                              | Remediation                              | Type             | Created At               |
+-----+-------------------------+------------+------------------------------------------+------------------------------------------+------------------+---------------------------+
| 4   | TLS Certificate Pinning  | 3.7        | The application does not make use of...  | Implement TLS certificate pinning...    | Mobile           | 2016-07-12T15:04:36+00:00 |
+-----+-------------------------+------------+------------------------------------------+------------------------------------------+------------------+---------------------------+
```
## Customization

**Modify Column Width:**

You can adjust the column width for the table display by changing the `max_width` value in the code:
```
table.max_width = 40  # Adjust this number to set the desired column width
```
**Update Vulnerability Data:**

Simply update the `vulnerabilities.json` file with your new vulnerability data. Make sure the format follows the structure shown in the example file.
