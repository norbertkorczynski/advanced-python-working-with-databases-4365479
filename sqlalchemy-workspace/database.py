import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///testDB.db', echo=True)

metadata = sqlalchemy.MetaData()

users_table = sqlalchemy.Table("Users", metadata,
    sqlalchemy.Column("User_Id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("First Name", sqlalchemy.Text),
    sqlalchemy.Column("Last Name", sqlalchemy.Text),
    sqlalchemy.Column("Email", sqlalchemy.Text))

metadata.create_all(engine)

users = [
    {"First Name":"Roman", "Last Name":"Kolton", "Email":"rkolton@polsat.pl"},
    {"First Name":"Adam", "Last Name":"Nowak", "Email":"nowaczek@o2.pl"},
    {"First Name":"Norman", "Last Name":"James", "Email":"njames@gmail.com"},
    {"First Name":"Test", "Last Name":"User", "Email":"test.user@gmail.com"},
    {"First Name":"Dupa", "Last Name":"Romana", "Email":"email1@poczta.fm"}]

with engine.connect() as conn:
    conn.execute(sqlalchemy.insert(users_table).values(users))

    for row in conn.execute(sqlalchemy.select(users_table)):
        print(row)
    conn.commit()
