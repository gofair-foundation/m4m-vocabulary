import os
import requests

FILE_NAME = os.environ['FILE_NAME']
RENDERING_UPDATE = os.environ['RENDERING_PROPERTIES']

vocab_file = open(f"./{FILE_NAME}.ttl", "r")
vocab = vocab_file.read()
vocab_file.close()

vocab = vocab.replace("@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .", RENDERING_UPDATE)

vocab_file = open(f"./{FILE_NAME}.ttl", "w")
vocab_file.write(vocab)
vocab_file.close()
