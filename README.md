# WebScanner
WebScanner is a multifunctional tool designed to analyze websites and extract essential information. It is aimed at users who need to retrieve data such as the contents of robots.txt and sitemap.xml files, WHOIS information, IP addresses, email addresses, phone numbers, and links found on web pages. The tool simplifies the process of website analysis for security testers and developers.
## Features
- **Comprehensive Site Analysis**: The tool provides multiple functions such as fetching the contents of `robots.txt` and `sitemap.xml` files, extracting email addresses, phone numbers, and links from web pages.

- **WHOIS Information Retrieval**: Easily obtain detailed WHOIS data for any domain, allowing you to gather important information about domain ownership and registration.

- **IP Address Retrieval**: Quickly fetch the IP address associated with any website, useful for network diagnostics and further analysis.

- **Multi-Display Options**: Choose to view extracted information directly in the command-line interface or open relevant files (like `robots.txt` or `sitemap.xml`) in a web browser for more convenient access.

- **Colored User Interface**: Enjoy a visually appealing and easy-to-navigate interface that enhances the user experience through color-coded output.

- **Flexible Task Execution**: Execute individual tasks as needed or run all available operations at once using the `--all` option, providing versatility based on your specific requirements.

- **Continuous Development**: The tool is actively developed by Adam Zayene, with a focus on improving functionality and maintaining a high level of code professionalism and efficiency.
- ## Why Use WebScanner Instead of Other Tools?

- **Task Integration**: Instead of using separate tools for each task (such as WHOIS tools or link analysis tools), WebScanner combines all these functions into one integrated tool.

- **Ease of Use**: The tool does not require complex setups; you simply download it and run it directly from the command line.

- **Flexibility**: Users can choose to perform specific tasks or execute all tasks simultaneously using the `--all` option.

- **Open Source**: The tool is open source, allowing users to customize it according to their needs.
## How to Download and Use
### 1. Download the Tool from GitHub
To download the tool, clone the repository from GitHub using the following command:
```bash
git clone https://github.com/Adamzayene/web_scanner.git
```
### 2.Then navigate to the tool's directory:
```bash
cd Web_scanner
```
## How to Use
```bash
python3 webscanner.py [options] -u [URL]
```
### Available Options

- **-r, --robots**: Check the `robots.txt` file of the site and display its contents in the terminal.

- **-b, --browser**: Open the `robots.txt` or `sitemap.xml` file in a web browser.

- **-s, --sitemap**: Access the site's `sitemap.xml` file and display it in the terminal.

- **-w, --whois**: Retrieve WHOIS information for the specified domain.

- **-i, --get-ip**: Retrieve the IP address of the specified website.

- **-e, --extract-emails**: Extract email addresses from the specified web page.

- **-p, --extract-phone**: Extract phone numbers from the specified web page.

- **-l, --extract-links**: Extract all links from the specified web page.

- **--all**: Execute all available operations on the specified URL.
## Usage Example

To retrieve all possible information about a specific site, use the following command:

```bash
python3 webscanner.py --all -u www.example.com
```
## Contributing
If you want to contribute to the development of the tool, you can fork the repository, make the necessary changes, and then submit a pull request to have your changes merged.
