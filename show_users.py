import sqlite3

conn = sqlite3.connect("bot_users.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT chat_id, username, first_name, last_name, joined_at FROM users"
)
users = cursor.fetchall()

print(f"Всего пользователей в базе: {len(users)}\n")
for user in users:
  chat_id, username, first_name, last_name, joined_at = user
  print(
      f"ID: {chat_id} | @{username} | {first_name} {last_name} | Дата: {joined_at}"
  )

conn.close()