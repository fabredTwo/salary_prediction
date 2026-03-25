FROM public.ecr.aws/lambda/python:3.11

RUN microdnf install -y gcc && microdnf clean all

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . ${LAMBDA_TASK_ROOT}

CMD ["app.handler"]
