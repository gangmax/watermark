Make sure you have "[pipenv](https://github.com/pypa/pipenv) installed. Then run the following commands to create/run this project. This project is an example how to use Python to add watermark to a image file.

```bash
# Enter directory.
cd watermark
# Set the Python version for the current project.
pipenv --python 3.6
# Install dependencies.
pipenv install Pillow
# Write the script content.
vi watermark.py
# Run the script.
pipenv run python watermark.py
# Lock the dependencies versions. 
pipenv lock
# Enter virtualenv shell. 
pipenv shell
# Print dependencies info.
pip freeze
# List all the pip packages of the current virtualenv.
pip list
# Run the script.
python watermark.py
# Exit current virtualenv environment.
exit
```

From [here](https://www.blog.pythonlibrary.org/2017/10/17/how-to-watermark-your-photos-with-python/) and [here](http://www.thecodingcouple.com/watermark-images-python-pillow-pil/).
