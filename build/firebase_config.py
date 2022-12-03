import pyrebase

# firebaseConfig = {
#     "apiKey": "AIzaSyDIfq7M-T-4UJrIO82lzIqG_8E2PC7ETTg",
#     "authDomain": "testlienket-56e1c.firebaseapp.com",
#     "databaseURL": "https://testlienket-56e1c-default-rtdb.firebaseio.com/",
#     "projectId": "testlienket-56e1c",
#     "storageBucket": "testlienket-56e1c.appspot.com",
#     "messagingSenderId": "813859433634",
#     "appId": "1:813859433634:web:a007fdc59b67fd4be37bfb"
# }

firebaseConfig = {
    "apiKey": "AIzaSyArOYvnhGhC97nGd39gZYYjfH1GqFwG-3Y",
    "authDomain": "videodetect-ae8df.firebaseapp.com",
    "databaseURL": "https://videodetect-ae8df-default-rtdb.firebaseio.com",
    "projectId": "videodetect-ae8df",
    "storageBucket": "videodetect-ae8df.appspot.com",
    "messagingSenderId": "96213974195",
    "appId": "1:96213974195:web:d7413851a7b0b6852804c6"
}

firebase = pyrebase.initialize_app(firebaseConfig)
