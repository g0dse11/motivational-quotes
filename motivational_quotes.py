import random

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "It always seems impossible until it's done. - Nelson Mandela",
    "Don’t watch the clock; do what it does. Keep going. - Sam Levenson",
    "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis",
    "Everything you’ve ever wanted is on the other side of fear. - George Addair",
    "The best way to predict the future is to create it. - Abraham Lincoln",
    "Don’t let yesterday take up too much of today. - Will Rogers",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Success is not how high you have climbed, but how you make a positive difference to the world. - Roy T. Bennett",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Don’t wait. The time will never be just right. - Napoleon Hill",
    "Act as if what you do makes a difference. It does. - William James",
    "The secret of getting ahead is getting started. - Mark Twain",
    "The only place where success comes before work is in the dictionary. - Vidal Sassoon",
    "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
    "You miss 100% of the shots you don’t take. - Wayne Gretzky",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Everything you’ve ever wanted is on the other side of fear. - George Addair",
    "Success is not in what you have, but who you are. - Bo Bennett",
    "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
    "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
    "If you can dream it, you can do it. - Walt Disney",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "Perseverance is not a long race; it is many short races one after the other. - Walter Elliot",
    "The best revenge is massive success. - Frank Sinatra",
    "You must do the things you think you cannot do. - Eleanor Roosevelt",
    "The only thing standing between you and your goal is the story you keep telling yourself. - Jordan Belfort",
    "Success doesn’t just find you. You have to go out and get it. - Unknown",
    "Don’t stop when you’re tired. Stop when you’re done. - Unknown",
    "Everything you can imagine is real. - Pablo Picasso",
    "The road to success and the road to failure are almost exactly the same. - Colin R. Davis",
    "Success is liking yourself, liking what you do, and liking how you do it. - Maya Angelou",
    "Do not wait to strike till the iron is hot, but make it hot by striking. - William Butler Yeats",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
    "Start where you are. Use what you have. Do what you can. - Arthur Ashe",
    "Don’t wish it were easier. Wish you were better. - Jim Rohn",
    "The only way to achieve the impossible is to believe it is possible. - Charles Kingsleigh",
    "It is never too late to be what you might have been. - George Eliot",
    "The harder you work for something, the greater you’ll feel when you achieve it. - Unknown",
    "Dream it. Wish it. Do it. - Unknown",
    "Success is what happens after you have survived all of your mistakes. - An Unknown",
    "Success is not in what you have, but who you are. - Bo Bennett",
    "Don’t be afraid to give up the good to go for the great. - John D. Rockefeller",
    "Nothing is impossible, the word itself says ‘I’m possible!’ - Audrey Hepburn",
    "Success is the sum of small efforts, repeated day in and day out. - Robert Collier",
    "Life isn’t about waiting for the storm to pass, it’s about learning to dance in the rain. - Unknown",
    "Life is what happens when you’re busy making other plans. - John Lennon",
    "You can never cross the ocean until you have the courage to lose sight of the shore. - Christopher Columbus",
    "Success is not measured by what you accomplish, but by the opposition you have encountered, and the courage with which you have maintained the struggle against overwhelming odds. - Orison Swett Marden",
    "Success is liking yourself, liking what you do, and liking how you do it. - Maya Angelou",
    "To live a creative life, we must lose our fear of being wrong. - Joseph Chilton Pearce",
    "Do one thing every day that scares you. - Eleanor Roosevelt"
]

def get_random_quote():
    return random.choice(quotes)

def main():
    print("Welcome to the Random Motivational Quote Generator!")
    while True:
        input("Press Enter to get a new quote (Ctrl+C to exit)...")
        print("\n" + get_random_quote() + "\n")

if __name__ == "__main__":
    main()
