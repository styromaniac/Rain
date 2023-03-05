# Rain
Rain.py is a Python script that can be used to download and archive a website. It can be run from the command line, taking two arguments: the destination directory where the website will be saved and the source URL of the website to be downloaded.

The script first downloads a file called sourcechecksums.txt from the source URL, which contains a list of checksums for all the files on the website. It then compares these checksums to the files in the destination directory and downloads any files that are missing or have been updated.

The script then downloads the HTML of the website and parses it for links to other files on the site, such as images, scripts, and stylesheets. It uses a LinkParser class to extract these links and then uses a ThreadPoolExecutor to download each file in parallel.

Finally, the script saves the downloaded HTML as index.html and updates all the links in the file to point to the local copies of the files.

The script uses the following Python modules:

    os: provides a way to interact with the file system
    re: provides regular expression matching for parsing HTML tags
    urllib.parse and urllib.request: provide tools for making HTTP requests and parsing URLs
    sys: provides access to system-specific parameters and functions
    html.parser: provides a class for parsing HTML
    concurrent.futures: provides a way to run functions asynchronously in a separate thread pool
    hashlib: provides tools for calculating file checksums.
