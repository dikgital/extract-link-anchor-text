# Web Link & Anchor Text Extractor

A lightweight Python automation tool to audit internal and external links from a list of URLs. This script extracts every `<a>` tag, captures the associated **Anchor Text**, and converts relative paths into absolute URLs for easy SEO analysis.

## 💡 Why Use This?

In Technical SEO, auditing your link profile is crucial for:

  * **Anchor Text Optimization:** Ensuring your internal links use descriptive, keyword-rich text.
  * **Link Equity Distribution:** Mapping how authority flows through your site.
  * **Audit Efficiency:** Automating the discovery of links across hundreds of pages instead of manual inspection.

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed. You will also need the following libraries:

  * **Requests**: To handle HTTP connections.
  * **BeautifulSoup4**: To parse HTML content.
  * **Pandas**: To manage data and export to CSV.

Install them via terminal:

```bash
pip install requests beautifulsoup4 pandas
```

### File Structure

1.  **`input.csv`**: Create a CSV file with a column named `url` containing the list of pages you want to scrape.
2.  **`script.py`**: The main Python file.
3.  **`output_links.csv`**: The file where your results will be saved (generated automatically).

## 🛠️ Script Breakdown

The script operates in four main stages:

### 1\. Configuration & Input

It starts by defining the file paths and loading your target URLs into a Pandas DataFrame.

```python
INPUT_FILE = r"YOUR_PATH_HERE\input.csv"
df = pd.read_csv(INPUT_FILE)
```

### 2\. Request & Parse

For every URL in your list, the script fetches the HTML source code. It uses `BeautifulSoup` with the `html.parser` to navigate the document structure.

```python
response = requests.get(url, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")
```

### 3\. Extraction Logic

The script identifies all `<a>` tags. It specifically looks for the `href` attribute (the destination) and the `link_text` (the clickable part).

  * **URL Normalization**: Using `urljoin`, it converts relative links (e.g., `/about`) into absolute URLs (e.g., `https://example.com/about`) by combining them with the source page URL.

### 4\. Data Export

Finally, the collected data is structured into a table and saved.

```python
output_df = pd.DataFrame(results)
output_df.to_csv(OUTPUT_FILE, index=False)
```

## 📋 Example Output

The generated CSV will contain the following columns:
| source\_page | link\_url | anchor\_text |
| :--- | :--- | :--- |
| [https://site.com/blog](https://www.google.com/search?q=https://site.com/blog) | [https://site.com/contact](https://www.google.com/search?q=https://site.com/contact) | Contact Us |
| [https://site.com/blog](https://www.google.com/search?q=https://site.com/blog) | [https://twitter.com/user](https://www.google.com/search?q=https://twitter.com/user) | Follow on Twitter |

## ⚖️ License

This project is open-source and free to use for your SEO projects.
