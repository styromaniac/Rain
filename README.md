# Rain
Rain is a Python script that downloads a website from a given URL and saves it to a specified destination directory. The script starts by downloading the HTML content of the website and then parses it to extract all the links in the page. It then downloads all the linked pages recursively and updates the links in the downloaded pages to point to the local copies.

To extract links from the HTML content, the script uses a LinkParser class that inherits from the HTMLParser class. The LinkParser class extracts links from a, link, script, img, video, and audio tags, and adds them to a list of links.

To download linked pages, the script uses a ThreadPoolExecutor object to submit a task for each link to download the linked page to a local file. It skips any links that do not belong to the same website as the source URL. After all the tasks are submitted, the script waits for all the tasks to complete and then saves the downloaded HTML content to a file named index.html. It also updates the links in the downloaded HTML content to point to the local copies.

The script also includes a download_url_to_file function that downloads the content of a URL to a file. This function checks if the destination file already exists and only downloads the content if it doesn't already exist.

Rain takes two command-line arguments: the destination directory and the URL of the website to download. The script is useful for creating local copies of websites for offline use, backup, or archiving purposes.
