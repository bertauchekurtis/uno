FROM python:3

COPY UnoCard.py WildUnoCard.py UnoDeck.py Hand.py UnoGame.py main.py /app/

WORKDIR /app

ENTRYPOINT [ "python", "main.py" ]