from prefect import flow, task
@task
def say_hello(name: str):
    print(f"Hello, {name}!")
@flow
def hello_flow():
    say_hello("MLOps Student")
if __name__ == "__main__":
       hello_flow()