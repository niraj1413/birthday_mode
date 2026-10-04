with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update scratchMessages (Highlighting her mesmerizing eyes & talents: dance, sing, cook, events, decor, gift packing, office work)
old_scratch = '''      // 5 Sweet, uplifting thoughts (Screen 3):
      scratchMessages: [
        "That effortless smile that lights up the whole room ✨",
        "Our hilarious banter that always makes me laugh out loud 😂",
        "How you're always completely, unapologetically yourself 🌸",
        "Late-night chats and random stories that never get boring 🌙",
        "Wishing you a year packed with big wins and endless reasons to smile 🌟"
      ],'''

new_scratch = '''      // 5 Highlights (Screen 3):
      scratchMessages: [
        "Those mesmerizing eyes ✨",
        "The effortless style and grace you carry yourself with 👗✨",
        "Dancing, singing & all that talent 💃🎤",
        "The chef skills (always 10/10) 🍳",
        "Crushing it at work with dedication 💼🌟"
      ],'''

if old_scratch in html:
    html = html.replace(old_scratch, new_scratch)
    print("1. Replaced scratchMessages with her specific talents and mesmerizing eyes!")
else:
    print("Warning: old_scratch not found directly, checking regex")
    import re
    html = re.sub(r'scratchMessages:\s*\[.*?\],', new_scratch, html, flags=re.DOTALL)
    print("1. Replaced scratchMessages via regex")

# 2. Update letterText (One mention of weekly talks as best part, touches on her skills naturally)
old_letter = '''      // Natural, cool, non-cringe letter:
      letterText: "Hey Sam,\\n\\nHappy Birthday! 🎉\\n\\nJust wanted to write a quick note to say I hope you have an incredible day.\\n\\nYou're genuinely one of the easiest people to talk to, and our random conversations and ridiculous laughs are always the highlight of my week. You just have this natural, effortless vibe that's impossible not to appreciate.\\n\\nI hope today is full of great food, good music, and lots of laughs. Wishing you a year ahead packed with big wins, fun adventures, and everything you've been aiming for.\\n\\nHave the best birthday, Sam. You definitely deserve it! ✨",'''

new_letter = '''      // Natural, grounded letter (celebrating her talents & weekly talks):
      letterText: "Hey Sam,\\n\\nHappy Birthday! 🎉\\n\\nJust wanted to write a quick note to wish you an incredible day.\\n\\nBetween your dancing, your cooking, the creative flair you bring to organizing events and decor, and how dedicated you are with your work—you're genuinely one of the most multitalented people I know. And of course, our weekly talks are always the best part of my week.\\n\\nI hope today is packed with great celebration, good food, and lots of laughs. Wishing you a year ahead full of big wins, exciting adventures, and everything you've been working towards.\\n\\nHave the best birthday, Sam. You definitely deserve it! ✨",'''

if old_letter in html:
    html = html.replace(old_letter, new_letter)
    print("2. Replaced letterText")
else:
    import re
    html = re.sub(r'letterText:\s*"Hey Sam,.*?"\s*,', new_letter, html, flags=re.DOTALL)
    print("2. Replaced letterText via regex")

# 3. Update memories (Screen 5) to balance her talents
old_memories = '''      // Polaroids (Screen 5):
      memories: [
        {
          title: "When We First Talked",
          caption: "That conversation where hours felt like minutes and I didn't want it to end.",
          emoji: "☕",
          rotation: -2.2
        },
        {
          title: "Uncontrollable Laughter",
          caption: "Laughing so hard we couldn't breathe over the most random inside jokes.",
          emoji: "😂",
          rotation: 2.4
        },
        {
          title: "Late-Night Chats",
          caption: "Sharing crazy stories, random thoughts, and songs that now remind me of you.",
          emoji: "🌙",
          rotation: -1.8
        },
        {
          title: "Moments We Stole",
          caption: "Every drive and hangout that turned into something I'll always remember.",
          emoji: "🚗",
          rotation: 2.1
        },
        {
          title: "Right Here, Right Now",
          caption: "Celebrating you today and looking forward to whatever comes next.",
          emoji: "✨",
          rotation: -2
        }
      ],'''

new_memories = '''      // Polaroids (Screen 5):
      memories: [
        {
          title: "Late-Night Chats & Banter",
          caption: "Trading ridiculous laughs and stories that never get boring.",
          emoji: "🌙",
          rotation: -2.2
        },
        {
          title: "Effortless Style",
          caption: "Always looking aesthetic, put-together, and naturally stunning.",
          emoji: "👗✨",
          rotation: 2.4
        },
        {
          title: "Creative Flair",
          caption: "Seeing your aesthetic touch in event decor, gift wrapping, and creativity.",
          emoji: "🎨",
          rotation: -1.8
        },
        {
          title: "Delicious Moments",
          caption: "Every hangout, food trip, and celebration that turned into a great memory.",
          emoji: "🍽️",
          rotation: 2.1
        },
        {
          title: "Right Here, Right Now",
          caption: "Celebrating all your talents today and looking forward to whatever comes next.",
          emoji: "✨",
          rotation: -2
        }
      ],'''

if old_memories in html:
    html = html.replace(old_memories, new_memories)
    print("3. Replaced memories with balanced highlights")
else:
    import re
    html = re.sub(r'memories:\s*\[.*?\],', new_memories, html, flags=re.DOTALL)
    print("3. Replaced memories via regex")

# 4. Update CONFIG.clouds (3-4 word phrases celebrating Mesmerizing Eyes, Weekly Talks, Dance/Song, Chef Skills, Creative Event Decor & Office Work)
old_clouds = '''      // 5 Clouds with 3-4 word images & sentiments (Screen 6):
      clouds: [
        {
          id: 1,
          badge: "Cloud 1",
          unopenedHint: "Tap to reveal ✨",
          emoji: "☀️",
          words: "Pure Golden Sunshine",
          subnote: "Brightens up any day effortlessly."
        },
        {
          id: 2,
          badge: "Cloud 2",
          unopenedHint: "Tap to reveal ✨",
          emoji: "😊✨",
          words: "That Unmatched Smile",
          subnote: "Genuinely bright and contagious."
        },
        {
          id: 3,
          badge: "Cloud 3",
          unopenedHint: "Tap to reveal ✨",
          emoji: "🌸",
          words: "Effortlessly Cool Vibe",
          subnote: "Always completely yourself."
        },
        {
          id: 4,
          badge: "Cloud 4",
          unopenedHint: "Tap to reveal ✨",
          emoji: "💫",
          words: "Our Silly Banter",
          subnote: "Laughing at the most random things."
        },
        {
          id: 5,
          badge: "Cloud 5",
          unopenedHint: "Tap to reveal ✨",
          emoji: "🌟",
          words: "Always Cheering You",
          subnote: "Wishing you the absolute best."
        }
      ]'''

new_clouds = '''      // 5 Clouds with 3-4 word sentiments describing her:
      clouds: [
        {
          id: 1,
          badge: "Cloud 1",
          unopenedHint: "Tap to reveal ✨",
          emoji: "👀✨",
          words: "Those Mesmerizing Eyes",
          subnote: "Deep, expressive, and impossible to forget."
        },
        {
          id: 2,
          badge: "Cloud 2",
          unopenedHint: "Tap to reveal ✨",
          emoji: "🌙✨",
          words: "Serene Like The Moon",
          subnote: "A soothing, graceful presence that glows softly."
        },
        {
          id: 3,
          badge: "Cloud 3",
          unopenedHint: "Tap to reveal ✨",
          emoji: "🎨✨",
          words: "Pure Creative Spirit",
          subnote: "An aesthetic eye that turns simple things into magic."
        },
        {
          id: 4,
          badge: "Cloud 4",
          unopenedHint: "Tap to reveal ✨",
          emoji: "☀️✨",
          words: "Warm Radiant Energy",
          subnote: "Effortlessly bringing light and warmth everywhere."
        },
        {
          id: 5,
          badge: "Cloud 5",
          unopenedHint: "Tap to reveal ✨",
          emoji: "🌸✨",
          words: "Effortless Natural Grace",
          subnote: "Confident, genuine, and beautifully herself."
        }
      ]'''

if old_clouds in html:
    html = html.replace(old_clouds, new_clouds)
    print("4. Replaced CONFIG.clouds with personalized skills & mesmerizing eyes!")
else:
    import re
    html = re.sub(r'clouds:\s*\[.*?\n      \]', new_clouds, html, flags=re.DOTALL)
    print("4. Replaced CONFIG.clouds via regex")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: index.html has been updated with personalized skills, mesmerizing eyes & weekly talks!")
