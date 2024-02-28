# Base64ImageEmbedder

Base64ImageEmbedder is a Python utility designed to convert images within HTML files to base64 encoded strings directly embedded within the HTML. This can be particularly useful for email templates, embedding small images into web pages to reduce HTTP requests, or for packaging HTML content with its images for offline use.

## Features

- Converts images to base64 encoding.
- Supports multiple image formats.
- Allows exclusion of specific images from being encoded.
- Supports processing multiple HTML files within a directory structure.
- Automatically detects character encoding of HTML files using `chardet`.

## Requirements

To install the necessary dependencies, run the following command:

``` bash
pip install -r requirements.txt
```

Make sure you have Python 3.x installed on your system to use Base64ImageEmbedder.

## Usage

``` bash
python main.py

```

1. Place your HTML files in a directory.
2. Run the script in the same directory as your HTML files or specify the path to the directory containing your HTML files.
3. Specify any images you wish to exclude from conversion in the `exclusions` list within the `main` function.
4. Optionally, adjust the `supported_extensions` list in the `main` function to include or exclude specific image file types.

The script will recursively search through the specified directory for HTML files and convert all images (except those excluded) to base64 encoded strings directly within the HTML file.

## How It Works

1. The script iterates over each HTML file in the specified directory.
2. It reads the HTML file and searches for `<img>` tags.
3. For each image, it checks if the image is excluded or not supported based on its file extension.
4. If the image is supported and not excluded, it converts the image to a base64 encoded string and replaces the `src` attribute of the `<img>` tag with the base64 encoded data.
5. The modified HTML content is then written back to the original file.

## Example

Before running the script:

```html
<img src="image.png" />
```
After running the script:
``` html
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA..." />
```
## License
Specify your license here or indicate that the project is open-source and free to use.

## Contributing
Contributions to Base64ImageEmbedder are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.
