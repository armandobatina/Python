from jenkinsapi.jenkins import Jenkins
import sqlite3


def get_server_instance():
    server = Jenkins('http://localhost:8080')
    return server


def store_db(name, is_running, active):
    conn = sqlite3.connect('jenkins_backup.db')
    c = conn.cursor()
    c.execute(
            'CREATE TABLE IF NOT EXISTS jenkins_jobs (ID INTEGER PRIMARY KEY NOT NULL, job_name TEXT NOT NULL, job_status TEXT NOT NULL, job_active INTEGER, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')

    array = [name, is_running, active]
    c.execute('INSERT INTO jenkins_jobs (job_name, job_status, job_active) VALUES (?, ?, ?)', array)

    print "jobs stored successfully"
    conn.close()


def get_job_details():
    server = get_server_instance()
    for j in server.get_jobs():
        job_instance = server.get_job(j[0])
        store_db(job_instance.name, job_instance.is_running(), job_instance.is_enabled())


if __name__ == '__main__':
    get_job_details()
