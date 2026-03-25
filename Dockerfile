FROM public.ecr.aws/lambda/python:3.11

RUN dnf install -y gcc && dnf clean all

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . ${LAMBDA_TASK_ROOT}

CMD ["app.handler"]
