def find_job(queue, name):
    for job in queue.jobs():
        print(job.name)
        if job.name == name:
            return True
    return False
