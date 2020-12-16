from datetime import date

def start_sprint():
    f = open('sprint_info', "w")
    f.write("START SPRINT")
    f.write("Start date: %s" % date.today())
    f.close()
