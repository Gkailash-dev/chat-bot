training_data = [
    # Greetings
    ("Hello", "greeting"),
    ("Hi there", "greeting"),
    ("Hey", "greeting"),
    ("Good morning", "greeting"),
    ("Good afternoon", "greeting"),
    ("Good evening", "greeting"),
    
    # Pricing queries
    ("What are your prices?", "pricing"),
    ("How much is a cake?", "pricing"),
    ("Can I get a price list?", "pricing"),
    ("What is the price of chocolate cake?", "pricing"),
    ("How much does a cheesecake cost?", "pricing"),
    # Purchase-related queries
    ("I want to place an order", "purchase"),
    ("Can I buy some cookies?", "purchase"),
    ("Do you sell cupcakes?", "purchase"),
    ("I want to order a cake for delivery", "purchase"),
    ("Can I reserve a cake for tomorrow?", "purchase"),
    # Location inquiries
    ("Where is your shop?", "location"),
    ("Can you tell me your branches?", "location"),
    ("Do you have any branches in Chennai?", "location"),
    ("Is there a branch near my home?", "location"),
    ("Do you deliver to Coimbatore?", "location"),
    # Items or menu inquiries
    ("What cake do you sell?", "items"),
    ("Show me your menu", "items"),
    ("Do you sell breads and pastries?", "items"),
    ("What are your best-selling items?", "items"),
    ("Do you have eggless options?", "items"),
     ("which product you have", "items"),
    # Contact information
    ("How can I contact you?", "contact"),
    ("What's your phone number?", "contact"),
    ("Give me your contact details", "contact"),
    ("Do you have an email address?", "contact"),
    ("Can I chat with you directly?", "contact"),
    # Order status inquiries
    ("Where is my order?", "orderstatus"),
    ("When will my cake arrive?", "orderstatus"),
    ("I want to track my order", "orderstatus"),
    ("Can you check my order status?", "orderstatus"),
    ("Is my order on the way?", "orderstatus"),
    # Support or issue resolution
    ("I need help with my order", "support"),
    ("There's a problem with my delivery", "support"),
    ("I need support", "support"),
    ("My order is delayed", "support"),
    ("The cake I received was damaged", "support"),
    ("I want to cancel my order", "support"),
    # Thank you messages
    ("Thanks for the help", "thank"),
    ("Thank you", "thank"),
    ("Thanks a lot!", "thank"),
    ("Much appreciated", "thank"),
    ("Thank you for assisting me", "thank"),
    # Feedback or suggestions
    ("I have a suggestion", "support"),
    ("Can I give feedback?", "support"),
    ("I want to share my experience", "support"),
    ("How can I leave a review?", "support"),
    ("I want to compliment your service", "support"),
    # Complaints or issues
    ("I have a complaint", "support"),
    ("I am not satisfied with my order", "support"),
    ("I want to report an issue", "support"),
    ("My cake was not fresh", "support"),
    ("I received the wrong order", "support"),
    # Miscellaneous inquiries
    ("Do you have any offers?", "offers"),
    ("Do you have any offer?", "offers"),
    ("Are there any discounts?", "offers"),
    ("What are your operating hours?", "hours"),
    ("Are you open on weekends?", "hours"),
    ("Are you open on weekend?", "hours"),
    ("Can I customize my cake?", "customization"),
    ("Do you make themed cakes?", "customization"),
    ("Can I choose the flavor of my cake?", "customization")

]
responses = {
    # Greetings
    "greeting": "Hello! Welcome to Sweet Treats Bakery. How can I assist you today?",
    # Pricing
    "pricing": (
        "Here are some cake price details:\n"
        "- Chocolate Truffle Cake: ₹500 (0.5 kg), ₹900 (1 kg)\n"
        "- Red Velvet Cake: ₹550 (0.5 kg), ₹950 (1 kg)\n"
        "- Black Forest Cake: ₹450 (0.5 kg), ₹850 (1 kg)\n"
        "- Butterscotch Delight: ₹480 (0.5 kg), ₹880 (1 kg)\n"
        "- Pineapple Cream Cake: ₹430 (0.5 kg), ₹820 (1 kg)\n"
        "Let me know if you'd like to place an order or need more details!"
    ),
    # Purchase
    "purchase": "You can place your order directly through our website, visit any of our branches, or call us at +91-9876543210. Let us know if you need assistance!",
    # Location
    "location": "We have branches in Chennai, Bangalore, and Hyderabad. Let me know if you’d like more details or directions!",
    # Items
    "items": (
        "Here’s our menu:\n"
        "- Chocolate Truffle Cake\n"
        "- Red Velvet Cake\n"
        "- Black Forest Cake\n"
        "- Butterscotch Delight\n"
        "- Pineapple Cream Cake\n"
        "- Cheesecakes, Cookies, Pastries, and more!\n"
        "Would you like to know prices or place an order?"
    ),
    # Contact information
    "contact": "You can contact us at +91-9876543210 or email us at contact@sweettreats.com.",
    # Support
    "support": (
        "I’m here to help! Could you share more details about the issue?\n"
        "For urgent assistance, you can also call us at +91-9876543210."
    ),
    # Thank you
    "thank": "You're welcome! Have a sweet day! 🍰",
    # Offers
    "offers": "We currently have a 'Buy 1 Get 1 Free' offer on select cookies and cupcakes! Check our website or visit our store for more details.",
    # Hours
    "hours": "Our bakery operates from 9:00 AM to 9:00 PM, Monday to Sunday.",
    # Customization
    "customization": (
        "Yes, we do offer cake customizations! You can choose flavors, themes, and designs for your cakes. "
        "Let us know your preferences, and we’ll make it happen!"
    ),
    # Order status
    "orderstatus": (
        "To check your order status, please provide your order number or the name under which the order was placed. "
        "You can also call us at +91-9876543210 for immediate assistance."
    ),
}
