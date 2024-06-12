# DALL-E Image Generator for Senior Care Homes

This project uses OpenAI's DALL-E model to generate images based on text prompts, specifically designed for senior residents living in care homes. The generated images are then cropped to the desired dimensions without stretching.

## Features

- **Contextual Image Generation**: Prepend a specific context to the prompt for generating images tailored for senior care homes.
- **High-Quality Images**: Generate images using DALL-E with a size of 1024x1024 pixels.
- **Center Cropping**: Crop the generated images to 1280x800 pixels from the center to avoid stretching.

## Installation

1. **Clone the Repository**
    ```sh
    git clone https://github.com/yourusername/dalle-senior-care-home.git
    cd dalle-senior-care-home
    ```

2. **Create a Virtual Environment**
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set Your OpenAI API Key**
    ```sh
    export OPENAI_API_KEY='your-api-key-here'  # On Windows use `set OPENAI_API_KEY=your-api-key-here`
    ```

## Usage

1. **Edit the Context and Prompt**
    Modify the `context` and `prompt` variables at the top of the `script.py` file to suit your needs:
    ```python
    context = "This is for senior residents living in a care home"
    prompt = "ping pong"
    ```

2. **Run the Script**
    ```sh
    python script.py
    ```

3. **Output**
    The generated and cropped image will be saved in the current directory with a filename based on the prompt.

## Example

Given the <context> And the <prompt>

The script will generate an image of seniors playing ping pong in a care home setting and save it as `ping_pong.jpg`.

## Requirements

- Python 3.7+
- OpenAI library
- Pillow library
- Requests library

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
