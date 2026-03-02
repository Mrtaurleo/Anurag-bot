bot_name: str = 'Anurag'
print(f"Hello'! I'm {bot_name}! How can I assist you today?")

while True:
  user_input: str = input ('you: ').lower()
  
  if user_input in ['hi', 'hello']:
    print(f"{bot_name}: Hi there! How can I help you?")
    
  elif user_input in ['bye', 'see you' ]:
      print(f"{bot_name}: Goodbye! Have a great day!")
  elif user_input in ['+', 'add']:
    print(f" {bot_name}: Sure! let\'s do some addition! Please enter two numbers.")