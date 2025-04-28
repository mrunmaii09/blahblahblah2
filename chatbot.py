def simple_restaurant_chatbot():
    menu = {'pizza': 8, 'burger': 5, 'pasta': 7}
    print("Welcome to Foodie's Restaurant!")
    
    while True:
        user = input("You: ").lower()
        
        if user == 'menu':
            print("Chatbot: Here's the menu:")
            for item, price in menu.items():
                print(f"- {item.capitalize()} : ${price}")
        
        elif user == 'order':
            choice = input("Chatbot: What would you like to order? ").lower()
            if choice in menu:
                print(f"Chatbot: {choice.capitalize()} ordered! It costs ${menu[choice]}.")
            else:
                print("Chatbot: Sorry, we don't have that.")
        
        elif user == 'bye':
            print("Chatbot: Thanks for visiting! Come again!")
            break
        
        else:
            print("Chatbot: You can type 'menu', 'order', or 'bye'.")

simple_restaurant_chatbot()
