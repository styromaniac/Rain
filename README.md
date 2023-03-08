![SNOWFLAKE](https://user-images.githubusercontent.com/43807387/223344700-f0cb2109-52a1-48f7-9769-af673d11102d.svg)

# Snow (because every file is unique)
Snow is a Python script that defines several functions to download and update a website from a given source URL to a local destination directory.

The main function of the script, download_website, takes two arguments: the source URL of the website to download and the local destination directory where the website should be saved. It performs the following tasks:

1. It downloads a file called snow.txt from the source URL and saves it to the destination directory. This file contains SHA-256 checksums for all the files in the website, and is used to detect changes and updates to the website.
2. It reads the contents of snow.txt and compares the checksums of the local files in the destination directory to those in the file. If a local file is missing or has a different checksum, the script downloads the updated file from the source URL and saves it to the destination directory.
3. It downloads the HTML content of the website from the source URL and saves it to the destination directory as index.html.
4. It parses the HTML content of index.html to extract all the links to other files in the website (images, stylesheets, scripts, etc.) and saves them to a list.
5. It uses a thread pool to download all the linked files that belong to the website and saves them to the destination directory. It skips files that are already up-to-date or have already been downloaded and verified.
6. It updates the links in index.html to point to the local copies of the files in the destination directory.

Overall, the script provides a simple and efficient way to synchronize a website between a source URL and a local destination directory. It ensures that all the files in the website are up-to-date and consistent with the checksums in snow.txt, and handles parallel downloads of multiple files to speed up the synchronization process.

Snow depends on a PHP script that provides the file path with the current SHA256sum for each file to download/update on a destination computing device in the text file known as snow.txt.

## Here are examples from a snow.txt file:

dep/Lightbox.js	63f78ec2b2450b7dad3b25cc533db2c9df6078df3a339f221d0c0976d9db281f

OpenCamera/example.mp4	df6b731b11f381fc90400b7c0e072a79fd96535c28ac10433659420e07626195

OpenCamera/example.webp	9e9b62b53f4e24df8514203cc235fa86346d4605aedd21df6263b84569e7e9d3

## Usage:
```
snow <destination_folder> <source_URL>
```

If you want older copies to save as backup copies, then use --bank.
```
snow --bank <destination_folder> <source_URL>
```

If you want another feature, please [create an issue for it.](https://github.com/styromaniac/Snow/issues/new)
