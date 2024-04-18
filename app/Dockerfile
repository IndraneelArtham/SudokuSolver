FROM python:3.9
WORKDIR /sudokusolver
COPY requirements.txt /sudokusolver
RUN pip install -r requirements.txt
COPY . /sudokusolver
EXPOSE 5000
CMD python ./app.py