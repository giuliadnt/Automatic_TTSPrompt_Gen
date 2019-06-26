from lxml import etree as et
from gtts import gTTS
import os
import spacy
from spacy_langdetect import LanguageDetector
import subprocess
import argparse
import pandas


class PromptsListParser:

    def __init__(self, extension="xml"):

        self.extension = extension


    @staticmethod
    def dict_from_xml(data):
        xml_parser = et.XMLParser(encoding='utf-8')
        tree = et.parse(data, xml_parser)
        xml_root = tree.getroot()
        d = {}
        for idx, c in enumerate(xml_root.getchildren()):
            d[idx] = (c.get('file').replace('.wav', ''), c.get('prompt'))
        return d

    @staticmethod
    def dict_from_csv(data):

        pass

    @staticmethod
    def get_language(data):
        nlp = spacy.load("en")
        nlp.add_pipe(LanguageDetector(), name="language_detector", last=True)
        for i, sent in enumerate(data):
            print(sent._.language["language"])
        pass

    # TODO:
    # complete the get language method
    # review class argument: method to get the file extension???
    # review methods to store the parsed utterances in a dictionary/dataframe
    # (better create a pandas dataframe than a dictionary, modify the existing static method for xml parsing)
    # the dataframe should have three columns: filename, utterance, language (plus the id column)
    # test all


class PromptsBatchHandler:

    def __init__(self, language="en"):
        self.language = language

    @staticmethod
    def store_tts(self, prompts_dict, dir_name):

        for k, v in prompts_dict.items():
            tts = gTTS(text=v[1], lang=self.language)
            tts.save(dir_name + '/' + v[0] + "_" + self.language + ".mp3")

    @staticmethod
    def convert_to_wav(path):
        for directory, subdirectories, files in os.walk(path):
            for f in files:
                subprocess.call(['ffmpeg', '-i', f, "${f%.*}.wav"])

    @staticmethod
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


# new_dir = create_new_dir('/tmp/%s' % args.file_path)


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", dest="file_path", help="prompt list file", metavar="FILE")

args = parser.parse_args()

promptParser = PromptsListParser()



