FROM python

RUN mkdir /app
WORKDIR /app
ADD . .
RUN pip install -r requirements.txt

CMD ["sh"]
