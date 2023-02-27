# Rain
Rain is a Python script that can be used to download a website and save it to the local disk. The script takes two command-line arguments: the first argument specifies the destination folder where the website should be saved, and the second argument is the URL of the website to be downloaded.

Rain works by first downloading the HTML content of the website from the specified URL using the urllib library. The script then parses the HTML using an HTML parser called LinkParser that extracts all the links to other resources such as images, scripts, and stylesheets. The script then creates a ThreadPoolExecutor that downloads all these resources concurrently to speed up the download process.

The script also checks if a file with the same name already exists in the local directory before downloading and overwriting it. If a file with the same name exists, and the contents of the existing file and the downloaded file are identical, then the script skips the download to save bandwidth. If the contents are different, the script renames the existing file with a ".bak" extension before downloading the new file.

Finally, the script updates the links in the downloaded HTML file to point to the local copies of the downloaded resources, and saves the updated HTML file to the local disk.
