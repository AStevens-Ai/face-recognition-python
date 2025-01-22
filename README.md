# Face Recognition App

This app uses the Face Recognition API to scan an initial image and compare it against a directory of other images to identify matching faces. The app is executed via Python, passing arguments for the initial image and the directory of images.

## Example Command
```bash
python3 main.py ./elon_1.jpg ./photoDirectory

Setting Up the Virtual Environment

Before testing the app, ensure that Python version 3.10.13 is installed. The current dependencies do not work with the latest Python version yet (I learned the hard way!). If you're having issues setting Python to version 3.10.13, you can globally set it using the following command on Linux:

pyenv global 3.10.13

Note: I can't confirm if this works on Windows or macOS, so apologies in advance.
Steps to Prepare

    Confirm your Python version is 3.10.13.

    Activate the virtual environment with:

source venv/bin/activate

After activation, you should see (venv) in front of your terminal path.

With the virtual environment activated, install the required dependencies:

    pip install face-recognition
    pip install git+https://github.com/ageitgey/face_recognition_models

    These libraries are essential for the app to function properly.

Running the App

Once the dependencies are installed, you can execute the app as follows:

python3 main.py ./elon_1.jpg ./photoDirectory

This will analyze the images in the specified directory and tell you which ones contain Elon Musk's face!
Troubleshooting
Virtual Environment Issues

If you're having issues with the virtual environment not working (e.g., the global Python version isn't being used in the venv), here’s a solution:

    Delete the current venv directory:

sudo rm -r venv

Recreate the virtual environment:

    python3 -m venv venv

    This should ensure the virtual environment uses your global Python version.

Follow these steps, and you should be ready to use the Face Recognition App without issues!
