# Snow
Snow is a Python script that defines several functions to download and update a website from a given source URL to a local destination directory.

The main function of the script, download_website, takes two arguments: the source URL of the website to download and the local destination directory where the website should be saved. It performs the following tasks:

1. It downloads a file called sourcechecksums.txt from the source URL and saves it to the destination directory. This file contains SHA-256 checksums for all the files in the website, and is used to detect changes and updates to the website.
2. It reads the contents of sourcechecksums.txt and compares the checksums of the local files in the destination directory to those in the file. If a local file is missing or has a different checksum, the script downloads the updated file from the source URL and saves it to the destination directory.
3. It downloads the HTML content of the website from the source URL and saves it to the destination directory as index.html.
4. It parses the HTML content of index.html to extract all the links to other files in the website (images, stylesheets, scripts, etc.) and saves them to a list.
5. It uses a thread pool to download all the linked files that belong to the website and saves them to the destination directory. It skips files that are already up-to-date or have already been downloaded and verified.
6. It updates the links in index.html to point to the local copies of the files in the destination directory.

Overall, the script provides a simple and efficient way to synchronize a website between a source URL and a local destination directory. It ensures that all the files in the website are up-to-date and consistent with the checksums in sourcechecksums.txt, and handles parallel downloads of multiple files to speed up the synchronization process.
