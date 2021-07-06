import os
import random

from MemeEngine.Meme_Engine import generate_meme
from Ingestor import Ingestor
import argparse

from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.Ingestor_Interface import IngestorInterface


def process_args(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            print(root, dirs, files)
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       # Been able to get everything working
                       # but the PDF file so commented it out
                       # './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            print("Quote files", f)
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = generate_meme('./static/output')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, help='path to image')
    parser.add_argument('--body', type=str, help='quote from author')
    parser.add_argument('--author', type=str, help='author of quote')
    args = parser.parse_args()
    print(process_args(args.path, args.body, args.author))
