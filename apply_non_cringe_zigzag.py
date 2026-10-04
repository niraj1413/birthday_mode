with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update letterText in CONFIG
old_letter = '''      // Humanoid, real letter (she knows you like her):
      letterText: "Hey Sam,\\n\\nI sat down thinking about what to write for your birthday, and I realized I just wanted to be real with you.\\n\\nThere's something about you that's impossible not to notice. The effortless way you carry yourself, that smile that catches me off guard every single time, and how our conversations can bounce from completely ridiculous banter to something quiet and real without missing a beat.\\n\\nYou know I like you—and honestly, getting to know you, hearing your thoughts, and having you in my days has been one of the best parts of this year. You bring a kind of warmth that makes everything feel lighter and brighter just by being around.\\n\\nI hope today gives you every ounce of that back. I hope you feel celebrated, I hope you laugh until your cheeks hurt, and I hope this next chapter brings you everything you've been secretly wishing for.\\n\\nHappy Birthday, Sam. I'm really glad you're in my life. ✨",'''

new_letter = '''      // Natural, cool, non-cringe letter:
      letterText: "Hey Sam,\\n\\nHappy Birthday! 🎉\\n\\nJust wanted to write a quick note to say I hope you have an incredible day.\\n\\nYou're genuinely one of the easiest people to talk to, and our random conversations and ridiculous laughs are always the highlight of my week. You just have this natural, effortless vibe that's impossible not to appreciate.\\n\\nI hope today is full of great food, good music, and lots of laughs. Wishing you a year ahead packed with big wins, fun adventures, and everything you've been aiming for.\\n\\nHave the best birthday, Sam. You definitely deserve it! ✨",'''

if old_letter in html:
    html = html.replace(old_letter, new_letter)
    print("1. Replaced letterText")
else:
    print("Warning: old_letter not found directly, checking regex")
    import re
    html = re.sub(r'letterText:\s*"Hey Sam,.*?"\s*,', new_letter + '\n', html, flags=re.DOTALL)
    print("1. Replaced letterText via regex")

# 2. Update signature in Screen 4
html = html.replace('Always in your corner,<br>', 'Best always,<br>')

# 3. Update scratch messages to be super fun and non-cringe
old_scratch = '''      scratchMessages: [
        "Your smile catches me off guard every single time ✨",
        "That spark and warmth you bring wherever you go 🌸",
        "Our conversations that effortlessly bounce from silly banter to real talks 💫",
        "The way you just make ordinary moments feel electric 🥂",
        "Wishing you a year as bright, unforgettable, and special as you are 🌟"
      ],'''

new_scratch = '''      scratchMessages: [
        "That effortless smile that lights up the whole room ✨",
        "Our hilarious banter that always makes me laugh out loud 😂",
        "How you're always completely, unapologetically yourself 🌸",
        "Late-night chats and random stories that never get boring 🌙",
        "Wishing you a year packed with big wins and endless reasons to smile 🌟"
      ],'''

if old_scratch in html:
    html = html.replace(old_scratch, new_scratch)
    print("2. Replaced scratchMessages")

# 4. Update Clouds CSS for Zig-Zag Small Cards layout
old_clouds_css = '''    .clouds-list {
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 20px;
      margin-bottom: 30px;
    }

    /* Floating Cloud Card */
    .cloud-card {
      position: relative;
      width: 100%;
      background: linear-gradient(135deg, rgba(255, 255, 255, 0.94) 0%, rgba(248, 240, 255, 0.94) 100%);
      border: 1.5px solid rgba(217, 164, 65, 0.35);
      border-radius: var(--radius-lg);
      padding: 22px 24px;
      box-shadow: 0 10px 25px rgba(90, 39, 80, 0.08), 0 0 15px rgba(255, 255, 255, 0.6);
      cursor: pointer;
      user-select: none;
      transition: all 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }

    .cloud-card:hover {
      transform: translateY(-4px) scale(1.02);
      box-shadow: 0 16px 32px rgba(90, 39, 80, 0.14), var(--shadow-gold);
      border-color: var(--accent-gold);
    }

    .cloud-card.opened {
      background: linear-gradient(135deg, #ffffff 0%, #fff6fb 100%);
      border-color: var(--btn-rose);
      box-shadow: 0 12px 30px rgba(255, 111, 165, 0.2);
    }'''

new_clouds_css = '''    .clouds-list {
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 16px;
      margin-bottom: 24px;
      position: relative;
      padding: 10px 0;
    }

    /* Small Puffy Cloud Card (Zig-Zag Staggered Layout) */
    .cloud-card {
      position: relative;
      width: 220px;
      max-width: 78%;
      background: linear-gradient(135deg, rgba(255, 255, 255, 0.96) 0%, rgba(248, 240, 255, 0.94) 100%);
      border: 1.5px solid rgba(217, 164, 65, 0.35);
      border-radius: 40px 40px 32px 32px;
      padding: 16px 18px;
      box-shadow: 0 8px 22px rgba(90, 39, 80, 0.08), 0 0 12px rgba(255, 255, 255, 0.8);
      cursor: pointer;
      user-select: none;
      transition: all 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }

    /* Alternating Zig-Zag Positioning */
    .cloud-card:nth-child(1) {
      align-self: flex-start;
      margin-left: 10px;
      animation: cloud-float-left 3.5s ease-in-out infinite alternate;
    }

    .cloud-card:nth-child(2) {
      align-self: flex-end;
      margin-right: 10px;
      animation: cloud-float-right 3.8s ease-in-out infinite alternate;
    }

    .cloud-card:nth-child(3) {
      align-self: flex-start;
      margin-left: 22px;
      animation: cloud-float-left 3.2s ease-in-out infinite alternate;
    }

    .cloud-card:nth-child(4) {
      align-self: flex-end;
      margin-right: 20px;
      animation: cloud-float-right 3.6s ease-in-out infinite alternate;
    }

    .cloud-card:nth-child(5) {
      align-self: center;
      animation: cloud-float-center 3.4s ease-in-out infinite alternate;
    }

    @keyframes cloud-float-left {
      0% { transform: translateY(0) rotate(-2deg); }
      100% { transform: translateY(-7px) rotate(-1deg); }
    }

    @keyframes cloud-float-right {
      0% { transform: translateY(0) rotate(2deg); }
      100% { transform: translateY(-7px) rotate(1deg); }
    }

    @keyframes cloud-float-center {
      0% { transform: translateY(0) scale(1); }
      100% { transform: translateY(-6px) scale(1.02); }
    }

    .cloud-card:hover {
      box-shadow: 0 14px 28px rgba(90, 39, 80, 0.15), var(--shadow-gold);
      border-color: var(--accent-gold);
      filter: brightness(1.02);
    }

    .cloud-card.opened {
      background: linear-gradient(135deg, #ffffff 0%, #fff4fa 100%);
      border-color: var(--btn-rose);
      box-shadow: 0 10px 25px rgba(255, 111, 165, 0.22);
      width: 235px;
    }'''

if old_clouds_css in html:
    html = html.replace(old_clouds_css, new_clouds_css)
    print("3. Replaced clouds CSS with zig-zag")

# 5. Update typography sizes in cloud-words-title
old_title_css = '''    .cloud-words-title {
      font-family: var(--font-display);
      font-size: 26px;
      background: linear-gradient(135deg, #ff4f8b 0%, #c65bd6 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 6px;
      line-height: 1.3;
    }

    .cloud-subnote {
      font-family: var(--font-serif);
      font-size: 18px;
      color: var(--text-plum-light);
      font-style: italic;
    }'''

new_title_css = '''    .cloud-words-title {
      font-family: var(--font-display);
      font-size: 21px;
      background: linear-gradient(135deg, #ff4f8b 0%, #c65bd6 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 4px;
      line-height: 1.25;
    }

    .cloud-subnote {
      font-family: var(--font-serif);
      font-size: 15px;
      color: var(--text-plum-light);
      font-style: italic;
      line-height: 1.35;
    }'''

if old_title_css in html:
    html = html.replace(old_title_css, new_title_css)
    print("4. Replaced cloud title typography sizes")

# 6. Update 3-4 word sentiments in CONFIG.clouds
old_clouds_config = '''      clouds: [
        {
          id: 1,
          badge: "Cloud 1",
          unopenedHint: "A little burst of light",
          emoji: "☀️",
          words: "Pure Unfiltered Sunshine",
          subnote: "Your energy lights up everything around you."
        },
        {
          id: 2,
          badge: "Cloud 2",
          unopenedHint: "The one I notice most",
          emoji: "😊✨",
          words: "My Favorite Smile",
          subnote: "Catches me completely off guard every single time."
        },
        {
          id: 3,
          badge: "Cloud 3",
          unopenedHint: "Something rare",
          emoji: "🌸",
          words: "Effortlessly Beautiful Soul",
          subnote: "Inside, outside, and in everything you do."
        },
        {
          id: 4,
          badge: "Cloud 4",
          unopenedHint: "Our vibe",
          emoji: "💫",
          words: "Our Favorite Chaos",
          subnote: "The silly banter, the late talks, the unspoken connection."
        },
        {
          id: 5,
          badge: "Cloud 5",
          unopenedHint: "A promise",
          emoji: "🌟",
          words: "Always In Your Corner",
          subnote: "Rooting for you, celebrating you, always."
        }
      ]'''

new_clouds_config = '''      clouds: [
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

if old_clouds_config in html:
    html = html.replace(old_clouds_config, new_clouds_config)
    print("5. Replaced CONFIG.clouds sentiments")

# 7. Update finale card text to be completely non-cringe
old_finale_text = '''        <p class="finale-humanoid-text">
          No big labels, no complicated words—just you, being completely unforgettable to me.<br><br>
          I hope today brings you as much happiness, warmth, and laughter as you bring into my world.
        </p>'''

new_finale_text = '''        <p class="finale-humanoid-text">
          Here's to celebrating you today and wishing you the most amazing year ahead.<br><br>
          May it be filled with great moments, huge wins, and lots of laughs!
        </p>'''

if old_finale_text in html:
    html = html.replace(old_finale_text, new_finale_text)
    print("6. Replaced finale text with clean, non-cringe message")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: index.html updated with zig-zag small clouds and non-cringe letter!")
