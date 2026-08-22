import sqlite3

conn= sqlite3.connect("cards.db")
cursor= conn.cursor()
 
 #create card tables
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTs cards (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       KOREAN TEXT NOT NULL,
       ENGLISH TEXT NOT NULL,
       CATEGORY TEXT NOT NULL
    )
    """
 )

 # CLEAR TABLE TO AVOID RERUNS
cursor.execute("DELETE FROM CARDS")

 # 100 Essential TOPIK level 1 and 2
words=[
    # Greetings & Etiquette
    ("안녕하세요", "Hello / Good day", "Greetings"),
    ("감사합니다", "Thank you", "Greetings"),
    ("죄송합니다", "I am sorry", "Greetings"),
    ("안녕히 계세요", "Goodbye (to someone staying)", "Greetings"),
    ("안녕히 가세요", "Goodbye (to someone leaving)", "Greetings"),
    ("반갑습니다", "Nice to meet you", "Greetings"),
    ("네", "Yes", "Greetings"),
    ("아니요", "No", "Greetings"),
    ("괜찮아요", "It's okay / I'm fine", "Greetings"),
    ("주세요", "Please give me", "Greetings"),
    # People & Family
    ("사람", "Person / Human", "People"),
    ("친구", "Friend", "People"),
    ("가족", "Family", "People"),
    ("아버지", "Father", "People"),
    ("어머니", "Mother", "People"),
    ("형", "Older brother (male speaker)", "People"),
    ("누나", "Older sister (male speaker)", "People"),
    ("오빠", "Older brother (female speaker)", "People"),
    ("언니", "Older sister (female speaker)", "People"),
    ("선생님", "Teacher", "People"),
    ("학생", "Student", "People"),
    # Common Verbs
    ("가다", "To go", "Verbs"),
    ("오다", "To come", "Verbs"),
    ("먹다", "To eat", "Verbs"),
    ("마시다", "To drink", "Verbs"),
    ("하다", "To do", "Verbs"),
    ("보다", "To see / watch", "Verbs"),
    ("듣다", "To listen / hear", "Verbs"),
    ("읽다", "To read", "Verbs"),
    ("쓰다", "To write / use", "Verbs"),
    ("자다", "To sleep", "Verbs"),
    ("일어나다", "To wake up / get up", "Verbs"),
    ("살다", "To live", "Verbs"),
    ("사다", "To buy", "Verbs"),
    ("알다", "To know", "Verbs"),
    ("모르다", "To not know", "Verbs"),
    ("배우다", "To learn", "Verbs"),
    ("공부하다", "To study", "Verbs"),
    ("일하다", "To work", "Verbs"),
    ("만나다", "To meet", "Verbs"),
    ("이야기하다", "To talk / speak", "Verbs"),
    # Adjectives & Descriptive Words
    ("크다", "To be big", "Adjectives"),
    ("작다", "To be small", "Adjectives"),
    ("좋다", "To be good / like", "Adjectives"),
    ("나쁘다", "To be bad", "Adjectives"),
    ("많다", "To be many / much", "Adjectives"),
    ("적다", "To be few / little", "Adjectives"),
    ("비싸다", "To be expensive", "Adjectives"),
    ("싸다", "To be cheap", "Adjectives"),
    ("맛있다", "To be delicious", "Adjectives"),
    ("맛없다", "To be undelicious", "Adjectives"),
    ("바쁘다", "To be busy", "Adjectives"),
    ("어렵다", "To be difficult", "Adjectives"),
    ("쉬운", "Easy", "Adjectives"),
    ("예쁘다", "To be pretty", "Adjectives"),
    ("더우다", "To be hot (weather)", "Adjectives"),
    ("춥다", "To be cold (weather)", "Adjectives"),
    # Food & Drink
    ("물", "Water", "Food"),
    ("밥", "Rice / Meal", "Food"),
    ("고기", "Meat", "Food"),
    ("김치", "Kimchi", "Food"),
    ("사과", "Apple", "Food"),
    ("빵", "Bread", "Food"),
    ("커피", "Coffee", "Food"),
    ("차", "Tea", "Food"),
    ("우유", "Milk", "Food"),
    ("식당", "Restaurant", "Food"),
    # Places
    ("집", "House / Home", "Places"),
    ("학교", "School", "Places"),
    ("회사", "Company / Office", "Places"),
    ("병원의", "Hospital", "Places"),
    ("약국", "Pharmacy", "Places"),
    ("은행", "Bank", "Places"),
    ("공항", "Airport", "Places"),
    ("역", "Station", "Places"),
    ("화장실", "Restroom / Bathroom", "Places"),
    ("방", "Room", "Places"),
    # Daily Objects
    ("책", "Book", "Objects"),
    ("시계", "Clock / Watch", "Objects"),
    ("돈", "Money", "Objects"),
    ("전화기", "Telephone / Phone", "Objects"),
    ("컴퓨터", "Computer", "Objects"),
    ("옷", "Clothes", "Objects"),
    ("신발", "Shoes", "Objects"),
    ("가방", "Bag", "Objects"),
    ("문", "Door", "Objects"),
    ("창문", "Window", "Objects"),
    # Time & Numbers
    ("오늘", "Today", "Time"),
    ("내일", "Tomorrow", "Time"),
    ("어제", "Yesterday", "Time"),
    ("지금", "Now", "Time"),
    ("시간", "Time / Hour", "Time"),
    ("일", "Day / One", "Time"),
    ("월", "Month", "Time"),
    ("년", "Year", "Time"),
    ("하나", "One (Native Korean)", "Numbers"),
    ("둘", "Two (Native Korean)", "Numbers"),
    ("셋", "Three (Native Korean)", "Numbers"),
    ("넷", "Four (Native Korean)", "Numbers"),
    ("다섯", "Five (Native Korean)", "Numbers"),
]
cursor.executemany(
    "INSERT INTO cards (korean, english, category) Values(?,?,?)",words
)
conn.commit()
conn.close()
print("Successfully created card db with 100 korean words")