import streamlit as st
import random
from datetime import datetime
import json
from typing import Dict, List, Optional
                                               #MADE BY KAIF TARASGAR
st.set_page_config(
    page_title="Ultimate Gift Genius 🎁",
    page_icon="🎁",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "### Gift Genius\nNever struggle to find the perfect gift again!",
    }
)

GIFT_IDEAS = {
    "Technology": {
        "icon": "💻",
        "low": ["Smartwatch", "Portable charger", "Phone stand"],
        "medium": ["Wireless earbuds", "Tablet", "Smart speaker"],
        "high": ["Gaming PC", "Professional camera", "VR headset"],
        "tags": ["innovative", "practical", "cutting-edge"]
    },
    "Books": {
        "icon": "📚",
        "low": ["Bestselling novel", "Bookmark set", "Reading light"],
        "medium": ["Special edition book", "Book subscription", "Cookbook set"],
        "high": ["First edition collectible", "Antique book", "Author-signed copy"],
        "tags": ["intellectual", "thoughtful", "creative"]
    },
    "Fashion": {
        "icon": "👗",
        "low": ["Designer socks", "Silk scarf", "Trendy sunglasses"],
        "medium": ["Leather wallet", "Quality watch", "Designer perfume"],
        "high": ["Designer handbag", "Custom suit/dress", "Luxury watch"],
        "tags": ["stylish", "personal", "luxury"]
    },
    "Toys & Games": {
        "icon": "🎮",
        "low": ["Board game", "Puzzle set", "Stuffed animal"],
        "medium": ["LEGO set", "Remote control car", "Interactive toy"],
        "high": ["Dollhouse", "Gaming console", "Drone"],
        "tags": ["fun", "interactive", "playful"]
    },
    "Sports & Fitness": {
        "icon": "⚽",
        "low": ["Yoga mat", "Fitness tracker", "Water bottle"],
        "medium": ["Running shoes", "Bicycle", "Smart jump rope"],
        "high": ["Golf set", "Tennis racket", "Home gym equipment"],
        "tags": ["active", "healthy", "energetic"]
    },
    "Home & Kitchen": {
        "icon": "🏠",
        "low": ["Scented candles", "Recipe book", "Herb garden kit"],
        "medium": ["Air fryer", "Coffee maker", "Quality knife set"],
        "high": ["Stand mixer", "Smart fridge", "Wine cooler"],
        "tags": ["practical", "homely", "culinary"]
    },
    "Music & Audio": {
        "icon": "🎧",
        "low": ["Bluetooth speakers", "Headphones", "Portable microphone"],
        "medium": ["Noise-canceling headphones", "Vinyl record player", "Smart home sound system"],
        "high": ["Home theater system", "High-end speakers", "Professional studio equipment"],
        "tags": ["music", "audio", "entertainment"]
    },
    "Gaming": {
        "icon": "🎮",
        "low": ["Board game", "Card game", "Miniature set"],
        "medium": ["Console games", "Game controller", "VR headset"],
        "high": ["Gaming chair", "Gaming PC", "VR setup"],
        "tags": ["fun", "competitive", "immersive"]
    },
    "Art & Craft": {
        "icon": "🎨",
        "low": ["Acrylic paint set", "Sketchbook", "Art supplies organizer"],
        "medium": ["Easel set", "Watercolor painting set", "DIY craft kit"],
        "high": ["Premium art supplies", "Custom portrait", "Painting workshop"],
        "tags": ["creative", "crafty", "artistic"]
    },
    "Outdoor Adventure": {
        "icon": "🏕️",
        "low": ["Camping lantern", "Backpack", "Sleeping bag"],
        "medium": ["Hiking boots", "Tent", "Portable grill"],
        "high": ["Camping stove", "Hiking gear set", "Outdoor survival kit"],
        "tags": ["outdoor", "adventure", "nature"]
    },
    "Food & Drink": {
        "icon": "🍴",
        "low": ["Chocolate box", "Gourmet coffee", "Fruit basket"],
        "medium": ["Wine set", "Gourmet spice rack", "Cooking class voucher"],
        "high": ["Luxury chocolate assortment", "Wine club subscription", "Caviar set"],
        "tags": ["foodie", "gourmet", "delicious"]
    },
    "Health & Wellness": {
        "icon": "💆",
        "low": ["Aromatherapy oils", "Massage roller", "Herbal teas"],
        "medium": ["Fitness tracker", "Yoga mat", "Essential oils set"],
        "high": ["Massage chair", "Smart sleep system", "Home sauna kit"],
        "tags": ["wellness", "self-care", "relaxation"]
    },
    "Pet Lovers": {
        "icon": "🐾",
        "low": ["Pet toys", "Personalized pet bowl", "Pet grooming set"],
        "medium": ["Pet bed", "Interactive pet toy", "Pet camera"],
        "high": ["Pet grooming kit", "Luxury pet bed", "Pet stroller"],
        "tags": ["pets", "animal lovers", "companions"]
    },
    "Eco-Friendly": {
        "icon": "🌱",
        "low": ["Reusable water bottle", "Eco-friendly bags", "Sustainable straws"],
        "medium": ["Solar-powered gadgets", "Recycled clothing", "Eco-friendly tech gadgets"],
        "high": ["Solar panels", "Zero waste starter kit", "Electric car charger"],
        "tags": ["green", "sustainable", "eco-friendly"]
    },
    "Cooking & Baking": {
        "icon": "🍳",
        "low": ["Baking utensils", "Cupcake molds", "Mixing bowls"],
        "medium": ["Stand mixer", "Cookbook set", "Baking mat"],
        "high": ["Custom oven", "Gourmet kitchen set", "Professional chef's knife"],
        "tags": ["culinary", "baking", "kitchen"]
    },
    "Crafting": {
        "icon": "✂️",
        "low": ["Scrapbooking kit", "Knitting set", "Stitching tools"],
        "medium": ["Embroidery kit", "Crafting organizer", "DIY jewelry kit"],
        "high": ["Laser cutting machine", "3D printing kit", "Advanced crafting tools"],
        "tags": ["crafty", "DIY", "hands-on"]
    },
    "Gardening": {
        "icon": "🌻",
        "low": ["Seed packets", "Gardening gloves", "Planters"],
        "medium": ["Vertical garden system", "Compost bin", "Indoor garden kit"],
        "high": ["Greenhouse setup", "Garden irrigation system", "Smart garden system"],
        "tags": ["outdoors", "green thumb", "sustainable"]
    },
    "Photography": {
        "icon": "📸",
        "low": ["Camera strap", "Tripod", "Lens cleaning kit"],
        "medium": ["DSLR camera", "Photography lighting kit", "Drone camera"],
        "high": ["Full-frame camera", "Lens set", "Professional studio equipment"],
        "tags": ["photography", "artistic", "creative"]
    },
    "Music": {
        "icon": "🎶",
        "low": ["Ukulele", "Portable keyboard", "Guitar picks"],
        "medium": ["Electric guitar", "Drum kit", "Piano"],
        "high": ["Grand piano", "Custom electric guitar", "Sound system"],
        "tags": ["musician", "instrument", "performer"]
    },
    "Running": {
        "icon": "👟", #MADE BY KAIF TARASGAR
        "low": ["Running socks", "Reflective gear", "Water bottle"],
        "medium": ["Running shoes", "Fitness tracker", "Compression gear"],
        "high": ["Running watch", "Running coach session", "Sports massage"],
        "tags": ["active", "fit", "endurance"]
    },
    "Cycling": {
        "icon": "🚴",
        "low": ["Cycling gloves", "Helmet", "Bike lock"],
        "medium": ["Road bike", "Cycling shoes", "Cycling backpack"],
        "high": ["Electric bike", "High-end road bike", "Cycling tech accessories"],
        "tags": ["active", "outdoor", "adventure"]
    },
    "Yoga": {
        "icon": "🧘",
        "low": ["Yoga mat", "Block set", "Water bottle"],
        "medium": ["Yoga blanket", "Aromatherapy kit", "Yoga app subscription"],
        "high": ["Personal yoga instructor", "Yoga retreat", "Advanced yoga gear"],
        "tags": ["wellness", "calm", "mindfulness"]
    },
    "Team Sports": {
        "icon": "🏀",
        "low": ["Team T-shirt", "Water bottle", "Sports ball"],
        "medium": ["Sports shoes", "Jersey", "Team gear"],
        "high": ["Custom sports equipment", "Private coaching", "Team experience package"],
        "tags": ["teamwork", "competitive", "sports"]
    },
    "Movies & TV": {
        "icon": "🎬",
        "low": ["Movie poster", "DVD box set", "Popcorn machine"],
        "medium": ["Projector", "Movie subscription", "Collector's edition box set"],
        "high": ["Home theater system", "Custom movie night package", "Private screening experience"],
        "tags": ["cinema", "entertainment", "TV"]
    },
    "Anime/Fandom": {
        "icon": "👾",
        "low": ["Anime poster", "Action figure", "Anime book"],
        "medium": ["Anime subscription", "Custom merch", "Anime plush"],
        "high": ["Limited edition figurine", "Anime convention tickets", "Signed anime art"],
        "tags": ["anime", "fandom", "collectibles"]
    },
    "Tech Enthusiast": {
        "icon": "🔧",
        "low": ["Smartphone holder", "Portable speaker", "Gadget organizer"],
        "medium": ["Smart lighting system", "Robotic vacuum", "Tech toolkit"],
        "high": ["Smart home automation", "3D printer", "Advanced tech gadgets"],
        "tags": ["innovation", "gadgets", "cutting-edge"]
    },
    "Entrepreneur": {
        "icon": "💼",
        "low": ["Notebook", "Desk organizer", "Coffee mug"],
        "medium": ["Business book", "Personalized stationery", "Smart planner"],
        "high": ["Business coaching session", "Custom office furniture", "Entrepreneurship course"],
        "tags": ["business", "startup", "motivational"]
    },
    "Creative Professionals": {
        "icon": "🎨",
        "low": ["Notebook", "Pen set", "Desk lamp"],
        "medium": ["Drawing tablet", "Graphic design software", "Desk organizer"],
        "high": ["Custom workspace setup", "Professional portfolio case", "Creative workshop session"],
        "tags": ["artistic", "creative", "professionals"]
    }
}


RECIPIENT_TYPES = {
    "Mom": [
        "Personalized jewelry", "Spa day package", "Family photo book", "Customized tote bag", 
        "Cooking class", "Luxury skincare set", "Personalized family calendar", "Subscription box", 
        "Floral arrangement", "Weekend getaway", "Personalized cutting board", "Home cleaning service"
    ],
    "Dad": [
        "Tech gadget", "Wine tasting set", "Grill tools", "Custom leather wallet", 
        "Outdoor gear", "Bluetooth speaker", "BBQ rub & seasoning set", "Smart home device", 
        "Luxury shaving kit", "Craft beer set", "Tool set", "Personalized whiskey glass"
    ],
    "Partner": [
        "Romantic getaway", "Customized jewelry", "Couple's massage", "Personalized photo album", 
        "Engraved love letter box", "Experience day", "Customized watch", "Couple's cooking class", 
        "Personalized artwork", "Luxury dinner set", "Matching custom apparel", "Home date night kit"
    ],
    "Friend": [
        "Experience voucher", "Gift card", "Personalized tumbler", "Board game", 
        "Travel accessories", "DIY craft kit", "Customized phone case", "Scented candles", 
        "Personalized keychain", "Wine subscription", "Funny socks", "Fashionable backpack"
    ],
    "Child": [
        "Educational toy", "Interactive book", "Bicycle", "Building blocks", 
        "Action figures", "Art set", "Plush toy", "Outdoor adventure set", "Toy robot", 
        "Music instrument", "Storytime app subscription", "Learning game"
    ],
    "Teen": [
        "Concert tickets", "Trendy headphones", "Gaming gift card", "Skateboard", 
        "Stylish backpack", "Fitness tracker", "Bluetooth speaker", "Graphic hoodie", 
        "Self-care kit", "DIY jewelry kit", "Streaming service subscription", "Tech gadget"
    ],
    "Coworker": [
        "Desk organizer", "Gourmet coffee set", "Notebook", "Personalized pen", 
        "Eco-friendly tumbler", "Succulent plant", "Desk toy", "Inspirational calendar", 
        "Corporate gift card", "Personalized planner", "Tech gadget", "Portable charger"
    ],
    "Teacher": [
        "Personalized mug", "Bookstore gift card", "Classroom supplies", "Custom tote bag", 
        "Inspirational poster", "Desk organizer", "Planner", "Relaxation gift set", 
        "Teacher appreciation plaque", "Handmade thank-you card", "Gift card for a coffee shop", 
        "Notebook set"
    ],
    "Grandparent": [
        "Digital photo frame", "Memory journal", "Comfy blanket", "Personalized family tree", 
        "Luxury slippers", "Classic photo album", "Gardening kit", "Customized puzzle", 
        "Bird feeder", "Subscription to a magazine", "Family game set", "Personalized mug"
    ],
    "Pet Lover": [
        "Personalized pet collar", "Pet grooming kit", "Pet-themed home decor", 
        "Interactive pet toy", "Pet portrait", "Pet care subscription box", "Portable water bottle for pets", 
        "Comfortable pet bed", "Customized pet bowl", "Pet camera", "Treat dispenser", 
        "Pet adoption kit"
    ],
    "Health & Wellness Enthusiast": [
        "Yoga mat", "Fitness tracker", "Aromatherapy diffuser", "Massage gun", 
        "Self-care kit", "Organic skincare set", "Water bottle with time markers", "Herbal tea set", 
        "Personalized water bottle", "Sleep aid device", "Mindfulness journal", "Spa robe"
    ],
    "Artist": [
        "Professional paint set", "Canvas and easel", "Watercolor pencils", "Art class voucher", 
        "Customized sketchbook", "Sculpture toolset", "Artistic calendar", "Framed art print", 
        "Drawing tablet", "Painting workshop", "Personalized paint palette", "Artist’s apron" #MADE BY KAIF TARASGAR
    ],
    "Foodie": [
        "Gourmet chocolate box", "Cooking class", "Spice rack set", "Cooking utensils set", 
        "Subscription to a food delivery service", "Personalized apron", "Specialty kitchen gadgets", 
        "Olive oil gift set", "Cheese platter", "Recipe book", "Gourmet coffee gift basket", 
        "Cooking wine"
    ]
}


OCCASION_TYPES = {
    "Birthday": [
        "Personalized gift", "Experience day", "Subscription box", "Customized jewelry", "Gift card", 
        "Themed party kit", "Memory book", "Adventure experience", "DIY gift set", "Spa day voucher"
    ],
    "Anniversary": [
        "Romantic dinner", "Custom artwork", "Weekend getaway", "Personalized photo frame", 
        "Couple's massage", "Customized wine glasses", "Memory jar", "Engraved keepsake box", 
        "Romantic escape", "Luxury bathrobe set"
    ],
    "Wedding": [
        "Kitchen appliance", "Luxury bedding", "Honeymoon fund", "Custom wedding vows book", 
        "Engraved wedding plate", "Personalized cake topper", "His & hers matching robes", "Gift registry voucher",
        "Wedding photo album", "Wedding planning journal"
    ],
    "Baby Shower": [
        "Baby clothes set", "Nursery decor", "Diaper cake", "Baby memory book", "Personalized baby blanket", 
        "Baby care kit", "Toddler toys", "Baby sleep sound machine", "Maternity robe", "Baby monitor"
    ],
    "Graduation": [
        "Professional watch", "Laptop bag", "Inspirational book", "Graduation ring", "College survival kit", 
        "Customized graduation cap", "Smartphone", "Class ring", "Desk organizer", "Personalized diploma frame"
    ],
    "Holidays": [
        "Festive decor", "Gourmet basket", "Personalized ornament", "Holiday-themed sweater", 
        "Scented candle set", "Christmas tree topper", "Holiday baking kit", "Seasonal mug set", 
        "Stocking stuffer set", "Christmas lights set"
    ],
    "Valentine's Day": [
        "Heart jewelry", "Love letter kit", "Couple's cooking class", "Romantic getaway", "Personalized chocolates", 
        "Couple's photo album", "Personalized playlist", "Matching sweaters", "Love coupon book", 
        "Customized couple's portrait"
    ],
    "Housewarming": [
        "Smart home device", "Plants", "Art piece", "Personalized doormat", "Customized kitchenware", 
        "Essential oil diffuser", "Indoor herb garden", "Candles in decorative holders", "Personalized throw blanket", 
        "Coffee station kit"
    ],
    "Retirement": [
        "Travel voucher", "Hobby starter kit", "Memory book", "Retirement plaque", "Customized compass", 
        "Luxury robe", "Experience gift", "Timepiece", "Adventure tour", "Personalized golf set"
    ],
    "Mother's Day": [
        "Spa day kit", "Personalized jewelry", "Floral bouquet", "Mom's day off experience", "Customized tote bag", 
        "Cookbook", "Mom's favorite wine", "Luxury skincare set", "Home-cooked meal kit", "Personalized mug"
    ],
    "Father's Day": [
        "Barbecue grill set", "Sports memorabilia", "Personalized wallet", "Tech gadget", "Customized beer mug", 
        "Golf accessories", "Outdoor adventure experience", "Leather belt", "Classic watch", "Home bar kit"
    ],
    "Thanksgiving": [
        "Gourmet food basket", "Personalized table settings", "Autumn-themed decor", "Cookware", 
        "Pumpkin pie kit", "Scented candles", "Thanksgiving-themed gift basket", "Wine pairing set", "Holiday serving tray"
    ],
    "New Year's Eve": [
        "Sparkling wine set", "Party decoration kit", "Luxury party hat", "New Year's Eve party games", 
        "Customized 2025 planner", "Champagne glasses", "Countdown clock", "Personalized photo booth props", 
        "New Year's resolution journal", "Exclusive event tickets"
    ],
    "Back to School": [
        "Backpack", "Stationery kit", "Personalized water bottle", "Laptop stand", "Desk organizer", 
        "Academic planner", "Noise-canceling headphones", "Tablet stand", "Portable charger", "Personalized lunch box"
    ],
    "Easter": [
        "Chocolate gift box", "Easter egg decorating kit", "Easter-themed basket", "Spring bouquet", 
        "Personalized Easter bunny plush", "Decorative Easter egg set", "Easter-themed candles", "Easter weekend getaway", 
        "Easter egg hunt kit", "Gourmet chocolate eggs"
    ]
}
#MADE BY KAIF TARASGAR
CUSTOM_CSS = """
<style>
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}
.stApp {
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    color: white;
}
.header {
    text-align: center;
    padding: 2rem;
    background: rgba(0,0,0,0.5);
    border-radius: 15px;
    margin-bottom: 2rem;
    animation: fadeIn 1s ease-out;
}
.gift-card {
    background: rgba(255,255,255,0.9);
    border-radius: 15px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    color: #333;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    transition: all 0.3s ease;
    animation: float 4s ease-in-out infinite;
}
.gift-card:hover {
    transform: translateY(-5px) scale(1.02);
    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
}
.stButton>button {
    background: linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%);
    border: none;
    color: white;
    font-weight: bold;
    padding: 0.8rem 1.5rem;
    border-radius: 50px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    transition: all 0.3s;
    width: 100%;
}
.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}
.budget-chip {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    margin-right: 0.5rem;
}
.low-budget { background-color: #e3f2fd; color: #1976d2; }
.medium-budget { background-color: #e8f5e9; color: #388e3c; }
.high-budget { background-color: #fce4ec; color: #c2185b; }
.interest-chip {
    display: inline-block;
    padding: 0.2rem 0.6rem;
    border-radius: 15px;
    font-size: 0.75rem;
    background: rgba(255,255,255,0.2);
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
}
/* Staggered animations */
.gift-card:nth-child(1) { animation-delay: 0.1s; }
.gift-card:nth-child(2) { animation-delay: 0.2s; }
.gift-card:nth-child(3) { animation-delay: 0.3s; }
.gift-card:nth-child(4) { animation-delay: 0.4s; }
.gift-card:nth-child(5) { animation-delay: 0.5s; }
.gift-card:nth-child(6) { animation-delay: 0.6s; }
</style>
"""
#MADE BY KAIF TARASGAR
def get_gift_tip(gift: str) -> str:
    tips = {
        'tech': "💡 Pair with accessories for a complete package",
        'book': "📚 Include a handwritten note on the first page",
        'fashion': "👔 Present in a luxury gift box",
        'toy': "🎁 Wrap with colorful paper and ribbons",
        'sport': "🏅 Add a motivational note",
        'home': "🏠 Include a recipe or care instructions"
    }
    for keyword, tip in tips.items():
        if keyword in gift.lower():
            return tip
    return random.choice([
        "✨ Add a personal handwritten note",
        "💝 Present it creatively",
        "🎀 Use premium wrapping",
        "📸 Capture their reaction"
    ])

def show_personalization_tips():
    with st.expander("💎 Make It Extra Special", expanded=False):
        tab1, tab2, tab3, tab4 = st.tabs(["🎁 Wrapping Ideas", "💌 Personal Touches", "🎉 Experience Gifts", "🎨 Creative Customization"])
        
        with tab1:
            st.markdown("""
            - **Themed wrapping**: Choose paper and accessories that match their favorite hobbies (e.g., gaming, travel, pets)  
            - **Luxury gift boxes** with satin lining or velvet pouches for an elegant feel  
            - **Handmade wrapping**: Add your personal artistic touch with hand-painted wrapping paper or recycled materials  
            - **Interactive unwrapping**: Use multiple layers, hidden compartments, or puzzle boxes to create excitement  
            - **Eco-friendly options**: Wrap gifts in reusable cloth bags or furoshiki for a sustainable touch
            """)
        #MADE BY KAIF TARASGAR
        with tab2:
            st.markdown("""
            - **Handwritten note**: A heartfelt message, sharing a special memory or inside joke  
            - **Engraving**: Personalize the gift with their name, a date, or a short quote  
            - **Custom packaging**: Use personalized stickers or tags with their favorite colors or photos  
            - **Photo collage**: A framed collection of memorable moments together  
            - **Interactive gift card**: Instead of a simple card, include a QR code linking to a video or message for them to discover
            """)
        
        with tab3:
            st.markdown("""
            - **Scavenger hunt**: Organize a series of clues around your home or neighborhood leading to the gift  
            - **Memory-making activity**: Plan an activity to experience together, like a pottery class or cooking workshop  
            - **Surprise delivery**: Have the gift delivered to their workplace, home, or a meaningful spot  
            - **Video message**: Create a heartfelt video message from friends or family to accompany the gift  
            - **Flash mob or surprise event**: If you're feeling adventurous, gather friends or family for a flash mob or surprise gathering
            """)
        
        with tab4:
            st.markdown("""
            - **Custom illustrations**: Commission or create an illustration that reflects their personality, hobby, or interests  
            - **Engraved items**: Personalized gifts like engraved jewelry, watches, or even tools  
            - **Customized home decor**: Create a piece of art, such as a custom canvas print or throw pillow, based on their favorite quotes or places  
            - **DIY kits**: If they enjoy hands-on experiences, assemble a DIY kit that they can personalize (e.g., craft set, build-your-own plant terrarium)  
            - **Upcycled items**: Give a second life to vintage or retro items with a personal twist, like custom painted furniture or refurbished electronics
            """)
def main():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="header">
        <h1 style="color:white; font-size:3rem; margin-bottom:0.5rem;">🎁 Ultimate Gift Genius</h1>
        <p style="color:white; font-size:1.2rem; margin-top:0;">Find the perfect present for every occasion!</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("gift_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("👤 About the Recipient")
            recipient = st.selectbox(
                "Who are you shopping for?",
                options=["Select"] + list(RECIPIENT_TYPES.keys()),
                index=0
            )
            
            age_group = st.selectbox(
                "Age Group",
                options=['Select', 'Child (0-12)', 'Teen (13-19)', 'Adult (20-64)', 'Senior (65+)'],
                index=0
            )
            
            interests = st.multiselect(
                "Their Interests (select up to 3)",
                options=[f"{GIFT_IDEAS[cat]['icon']} {cat}" for cat in GIFT_IDEAS.keys()],
                max_selections=3,
                format_func=lambda x: x
            )
            
        with col2:
            st.subheader("🎉 About the Occasion")
            occasion = st.selectbox(
                "What's the occasion?",
                options=["Select"] + list(OCCASION_TYPES.keys()),
                index=0
            )
            
            budget = st.radio(
                "Your Budget",
                options=['low', 'medium', 'high'],
                index=1,
                horizontal=True,
                help="Low: $10-50 | Medium: $50-200 | High: $200+"
            )
            
            show_tips = st.checkbox("Include gift-giving tips", True)
        
        submitted = st.form_submit_button("✨ Generate Gift Ideas", use_container_width=True)
    #MADE BY KAIF TARASGAR
    if submitted:
        if recipient == "Select" and occasion == "Select" and not interests:
            st.warning("Please provide at least one filter to generate suggestions!")
        else:
            with st.spinner("🧠 Finding perfect gift ideas..."):
                suggestions = []
                
                interest_names = [i.split(" ")[1] for i in interests if len(i.split(" ")) > 1]
                for interest in interest_names:
                    if interest in GIFT_IDEAS:
                        suggestions.extend(GIFT_IDEAS[interest][budget])

                if recipient != "Select":
                    suggestions.extend(RECIPIENT_TYPES[recipient])
                if occasion != "Select":
                    suggestions.extend(OCCASION_TYPES[occasion])

                if age_group != "Select":
                    age_key = age_group.split(" ")[0].lower()
                    age_map = {
                        'child': ['Educational toy set', 'Interactive book', 'Building blocks'],
                        'teen': ['Trendy tech gadget', 'Gift card', 'Concert tickets'],
                        'adult': ['Wine tasting set', 'Luxury skincare', 'Experience voucher'],
                        'senior': ['Digital photo frame', 'Comfortable blanket', 'Family history book']
                    }
                    suggestions.extend(age_map.get(age_key, []))

                suggestions = list(set(suggestions))
                random.shuffle(suggestions)
                
                if not suggestions:
                    st.error("Couldn't find matching gifts. Try broadening your search criteria.")
                else:
                    st.success(f"Found {len(suggestions)} gift ideas!")
                    st.balloons()

                    cols = st.columns(2)
                    for i, idea in enumerate(suggestions[:12]): 
                        with cols[i % 2]:
                            budget_class = {
                                'low': 'low-budget',
                                'medium': 'medium-budget',
                                'high': 'high-budget'
                            }[budget]
                            
                            st.markdown(f"""
                            <div class="gift-card" style="animation-delay: {i*0.1}s">
                                <h3>{idea}</h3>
                                <div style="margin-bottom: 0.5rem;">
                                    <span class="budget-chip {budget_class}">{budget.capitalize()} Budget</span>
                                    {random.choice(["✨", "🌟", "🎯", "💎"])} Top Pick
                                </div>
                                <p style="color: #666; font-size: 0.9rem;">
                                    💡 {get_gift_tip(idea)}
                                </p>
                            </div>
                            """, unsafe_allow_html=True)
                    
                    if show_tips:
                        show_personalization_tips()

                    st.download_button(
                        label="📩 Download Gift Ideas",
                        data="\n".join([f"Gift Ideas for {recipient if recipient != 'Select' else 'Your Recipient'}" + 
                                        (f" ({occasion})" if occasion != "Select" else "") + ":"] + 
                                        [f"- {gift}" for gift in suggestions]),
                        file_name="gift_ideas.txt",
                        mime="text/plain"
                    )

    st.markdown("---")
    st.markdown(f"""
    <div style="text-align: center; color: white; padding: 1rem;">
        <p>© {datetime.now().year} Ultimate Gift Genius | Made Kaif Tarasgar</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()




                                                                     #MADE BY KAIF TARASGAR
                                                            
                                                            #https://www.linkedin.com/in/kaif-tarasgar-0b5425326/
                                              
                                              #https://x.com/Kaif_T_200-->