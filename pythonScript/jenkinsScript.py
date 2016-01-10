import jenkinsapi
from jenkinsapi.jenkins import Jenkins


def main():
    J = Jenkins('http://localhost:8080')
    print J.version