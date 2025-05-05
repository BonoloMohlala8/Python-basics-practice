def send_messages(text_messages,sent_messages):
    while text_messages:
        current_messages = text_messages.pop()
        sent_messages.append(current_messages)
        print(f"This text is still being sent: {current_messages}")
        
      
def show_text_messages(sent_messages):
    print("\nThe following texts have been delivered: ")
    for text in sent_messages:
        print(text)
    
text_messages = ["Hi sweetheart","who are you","not ready yet"]
sent_messages = []

send_messages(text_messages,sent_messages)
show_text_messages(sent_messages)

print(f"\nUnsent list: {text_messages}")
print(f"New list: {sent_messages}")