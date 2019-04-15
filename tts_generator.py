from lxml import etree as et
from gtts import gTTS
import os
import spacy
from spacy_langdetect import LanguageDetector
import subprocess
import argparse


class PromptParser:

    def __init__(self):
        pass

    @staticmethod
    def create_dict_from_xml(self):
        xml_parser = et.XMLParser(encoding='utf-8')
        tree = et.parse(self, xml_parser)
        xml_root = tree.getroot()
        d = {}
        for idx, c in enumerate(xml_root.getchildren()):
            d[idx] = (c.get('file').replace('.wav', ''), c.get('prompt'))
        return d

    @staticmethod
    def create_dict_from_csv(self):
        pass

    #  PERHAPS create separate class or handling for manipulation of data???

    # @staticmethod
    # def store_tts(dir_name):
    #
    # 	for k, v in prompts_dict.items():
    # 		tts = gTTS(text=v[1], lang=v[2])
    # 		tts.save(dir_name + '/' + v[0] + "_" + v[2] + ".mp3")
    #
    # @staticmethod
    # def to_wav(path):
    # 	for directory, subdirectories, files in os.walk(path):
    # 		for f in files:
    # 			subprocess.call(['ffmpeg', '-i', f, "${f%.*}.wav"])


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


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", dest="file_path", help="prompt list file", metavar="FILE")

args = parser.parse_args()

new_dir = create_new_dir('/tmp/%s' % args.file_path)


