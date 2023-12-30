import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///testDB.db', echo=True)

metadata = sqlalchemy.MetaData()

movies_table = sqlalchemy.Table("Users", metadata,
    sqlalchemy.Column("User_Id", sqlalchemy.Integer),
    sqlalchemy.Column("First Name", sqlalchemy.Text),
    sqlalchemy.Column("Last Name", sqlalchemy.Text),
    sqlalchemy.Column("Email", sqlalchemy.Text))

metadata.create_all(engine)

users = [
    (1, "Roman", "Kolton", "rkolton@polsat.pl"),
    (2, "Adam", "Nowak", "nowaczek@o2.pl"),
    (3, "Norman", "James", "njames@gmail.com"),
    (4, "Test", "User", "test.user@gmail.com"),
    (5, "Dupa", "Romana", "email1@poczta.fm")]

with engine.connect() as conn:
    conn.execute(movies_table.insert().values(users))

    for row in conn.execute(sqlalchemy.select(movies_table)):
        print(row)
