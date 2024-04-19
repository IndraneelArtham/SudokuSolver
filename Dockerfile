FROM python:3.9
WORKDIR /sudokusolver
RUN pip install flask opencv-python tensorflow numpy flask-wtf flask-reuploaded
RUN pip install opencv-python-headless
RUN pip install pillow
COPY . /sudokusolver
EXPOSE 5000
CMD python ./app.py