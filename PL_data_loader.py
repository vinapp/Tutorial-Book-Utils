# taken from this repo: https://stackoverflow.com/questions/38511444/python-download-files-from-google-drive-using-url

import gdown
import argparse

file_destinations = {'NatarajaAbhayaMudraDetection':'nataraja-fasterrcnn-labelled.zip'}

file_id_dic = {'NatarajaAbhayaMudraDetection':'1ZDNhhqTzGrl1gBy4AyapAk137BszrGnF'}

def download_file_from_google_drive(id_, destination):
    url = f'https://drive.google.com/uc?id={id_}'
    output = destination
    gdown.download(url, output, quiet=False)
    print(f'{output} download complete!')
    
parser = argparse.ArgumentParser(description = 'data loader for PseudoLab Tutorial Book')

parser.add_argument('--data', type = str, help = 'key for selecting data')

args = parser.parse_args()

download_file_from_google_drive(id_=file_id_dic[args.data], destination=file_destinations[args.data])
