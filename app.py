import random
import os
import requests
from flask import Flask, render_template, abort, request, url_for

from MemeEngine.Meme_Engine import generate_meme
from Ingestor import Ingestor

app = Flask(__name__)

meme = generate_meme('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    
    for file in quote_files:
        #ingestor_var = Ingestor.parse(file)
        ingestor_var = Ingestor.parse(file)
        # if ingestor_var is NOT None or False then extend
        if ingestor_var:
            quotes.extend(ingestor_var)

    images_path = "./_data/photos/dog"

    print(os.listdir(images_path))

    final_path = os.path.join('.', '_data', 'photos', 'dog')

    #imgs = [f'{os.path.join(final_path, image)}'  for image in os.listdir(images_path)]
    imgs = [f'./_data/photos/dog/{image}' for image in os.listdir(images_path)]

    print("images ---> ", imgs)

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array
    img = random.choice(imgs)
    default_quote = {
        "body": "default quote",
        "author": "Kobby",
    }
    #quote = random.choice(quotes) if len(quotes) != 0 else default_quote

    if len(quotes) != 0:
        quote = random.choices(quotes)
        path = meme.make_make(img, quote.body, quote.author)
    else:
        path = meme.make_meme(img, default_quote["body"], default_quote["author"])

    # path = meme.make_meme(img, quote["body"], quote["author"])
    print('image here: ----> ', img)
    return render_template('meme.html', path=img)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    r = requests.get(image_url, allow_redirects = True)
    tmp = f'./tmp/{random.randint(0, 100000000)}.png'
    img = open(tmp, 'wb').write(r.content)
    path = meme.make_meme(tmp,body,author)
    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run(debug = True)
