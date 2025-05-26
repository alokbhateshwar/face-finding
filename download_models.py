import urllib.request
import os

def download_file(url, filename):
    print(f"Downloading {filename}...")
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Downloaded {filename} successfully!")
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")

# Define paths
current_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(current_dir, 'models')

# Create models directory if it doesn't exist
if not os.path.exists(models_dir):
    os.makedirs(models_dir)

# Model URLs
model_urls = {
    'age_deploy.prototxt': 'https://raw.githubusercontent.com/GilLevi/AgeGenderDeepLearning/master/models/age_net.caffemodel',
    'age_net.caffemodel': 'https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/age_net.caffemodel',
    'gender_deploy.prototxt': 'https://raw.githubusercontent.com/GilLevi/AgeGenderDeepLearning/master/models/gender_net.caffemodel',
    'gender_net.caffemodel': 'https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/gender_net.caffemodel'
}

# Download all files
for filename, url in model_urls.items():
    filepath = os.path.join(models_dir, filename)
    download_file(url, filepath)

print("\nAll model files have been downloaded successfully!")
print(f"Model files are stored in: {models_dir}") 