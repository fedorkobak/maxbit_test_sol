FROM python:3.10
COPY prod_req.txt requrements.txt
COPY app.py app.py
COPY model.pck model.pck
COPY ml_test_rec_sys.parquet ml_test_rec_sys.parquet
RUN pip3 install -r requrements.txt
EXPOSE 8000
CMD ["uvicorn", "--host", "0.0.0.0", "app:app"]