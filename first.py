from datetime import datetime
odds=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
this_min=datetime.today().minute
if this_min in odds:
    print("This minute seems a lil' odd.")
else:
    print("No chill...it's just fine...")
