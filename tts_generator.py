from lxml import etree as et
from gtts import gTTS
import os
import subprocess
import argparse


def create_new_dir(path):

	current_path = os.getcwd()
	new_path = current_path + path

	try:  
		os.mkdir(new_path)
	except OSError:  
		print("Creation of the directory %s failed or already exists" % new_path)
	else:  
		print("Successfully created the directory %s " % new_path)

	return new_path

# better approach: get names and text from existing csv/xlsx file.
# audio config should be generated automatically from the prompt list instead


def create_prompts_dict(root):

	d = {}
	for idx, c in enumerate(root.getchildren()):
		d[idx] = (c.get('file').replace('.wav', ''), c.get('utterance').replace('[1P]', ''), c.get('locale')[:2])
	return d


def store_tts(dir_name):

	for k, v in prompts_dict.items():
		tts = gTTS(text=v[1], lang=v[2])
		tts.save(dir_name + '/' + v[0] + "_" + v[2] + ".mp3")


def to_wav(path):
	for directory, subdirectories, files in os.walk(path):
		for f in files:
			subprocess.call(['ffmpeg', '-i', f, "${f%.*}.wav"])


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", dest="file_path", help="prompt list file", metavar="FILE")

args = parser.parse_args()

xml_parser = et.XMLParser(encoding='utf-8')

tree = et.parse(args.file_path, xml_parser)

xml_root = tree.getroot()

prompts_dict = create_prompts_dict(xml_root)

new_dir = create_new_dir('/tmp/%s' % args.file_path)

store_tts(new_dir)

to_wav(new_dir)

# p1 = subprocess.Popen(['', '', ], stdout=subprocess.PIPE)
