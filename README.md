# RandomGenerator

> A project that generates a random UUID with a timestamp


## development setup

After the project clone, create a virtual environment and install dependencies

```bash
pip install -r requirements.txt

```

Run the project with:
```bash
python manage.py runserver 
```

To test the endpoint:

`http://localhost:8000/api/v1/`

This gives a list of key-value pairs: `time generated` against `unique id`, with the latest item first