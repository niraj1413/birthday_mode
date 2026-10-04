import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update meta description
html = html.replace(
    '<meta name="description" content="A special birthday surprise made with all my love for you.">',
    '<meta name="description" content="A special birthday celebration made just for you, Sam!">'
)

# 2. Update Audio Button CSS
old_audio_css = '''    /* Music Controller Button */
    .audio-btn {
      position: fixed;
      top: max(16px, env(safe-area-inset-top));
      right: max(16px, env(safe-area-inset-right));
      z-index: 100;
      background: rgba(255, 255, 255, 0.85);
      backdrop-filter: blur(10px);
      border: 1.5px solid var(--accent-gold);
      color: var(--text-plum);
      width: 44px;
      height: 44px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 18px;
      box-shadow: 0 4px 15px rgba(90, 39, 80, 0.1);
      transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    }

    .audio-btn:hover {
      transform: scale(1.1) rotate(10deg);
      box-shadow: var(--shadow-gold);
    }

    .audio-btn.playing {
      animation: music-spin 4s linear infinite;
    }

    @keyframes music-spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }'''

new_audio_css = '''    /* Music Controller Button (Modern Frosted Glass Pill) */
    .audio-btn {
      position: fixed;
      top: max(16px, env(safe-area-inset-top));
      right: max(16px, env(safe-area-inset-right));
      z-index: 100;
      background: rgba(255, 255, 255, 0.9);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1.5px solid var(--accent-gold);
      color: var(--text-plum);
      padding: 7px 15px;
      border-radius: 999px;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      cursor: pointer;
      font-size: 13px;
      font-weight: 700;
      box-shadow: 0 4px 16px rgba(90, 39, 80, 0.1);
      transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
      user-select: none;
    }

    .audio-btn:hover {
      transform: translateY(-2px) scale(1.03);
      box-shadow: var(--shadow-gold);
      background: #ffffff;
    }

    .music-icon {
      font-size: 15px;
      line-height: 1;
    }

    .equalizer-wave {
      display: inline-flex;
      align-items: flex-end;
      gap: 2.5px;
      height: 14px;
    }

    .equalizer-wave span {
      display: block;
      width: 2.5px;
      background: linear-gradient(180deg, var(--btn-rose), var(--btn-orchid));
      border-radius: 2px;
      height: 4px;
      transition: height 0.2s ease;
    }

    .audio-btn.playing .equalizer-wave span:nth-child(1) {
      animation: eq-bounce 0.8s ease-in-out infinite alternate;
    }
    .audio-btn.playing .equalizer-wave span:nth-child(2) {
      animation: eq-bounce 0.6s ease-in-out 0.2s infinite alternate;
    }
    .audio-btn.playing .equalizer-wave span:nth-child(3) {
      animation: eq-bounce 0.9s ease-in-out 0.4s infinite alternate;
    }

    @keyframes eq-bounce {
      0% { height: 3px; }
      100% { height: 13px; }
    }'''

if old_audio_css in html:
    html = html.replace(old_audio_css, new_audio_css)
    print("1. Replaced audio CSS")
else:
    print("Audio CSS not matched, skipping")

# 3. Update Audio Button HTML element
old_audio_html = '''  <!-- Audio Toggle Button (Plays gentle romantic music box melody) -->
  <button class="audio-btn" id="audio-toggle" title="Toggle gentle romantic music" aria-label="Toggle romantic music">
    🎵
  </button>'''

new_audio_html = '''  <!-- Audio Toggle Button (Plays gentle birthday music box melody) -->
  <button class="audio-btn" id="audio-toggle" title="Play birthday music" aria-label="Toggle music">
    <span class="music-icon" id="music-icon">🎵</span>
    <span id="music-text">Music</span>
    <span class="equalizer-wave">
      <span></span><span></span><span></span>
    </span>
  </button>'''

if old_audio_html in html:
    html = html.replace(old_audio_html, new_audio_html)
    print("2. Replaced audio HTML")

# 4. Update Screen 1 Markup (Friendly & Special, not Wife/GF)
old_screen1_html = '''        <div class="warning-badge">
          <span>💖</span> Warning: Too much love ahead
        </div>
        <h1 class="start-title gradient-heading">Proceed Carefully</h1>
        <p class="start-subtitle">A special surprise is waiting for you 🌸</p>
        
        <button class="btn-primary" id="start-btn">
          <span>Come With Me</span>
          <span style="font-size: 20px;">➔</span>
        </button>'''

new_screen1_html = '''        <div class="warning-badge">
          <span>🌸</span> A Special Birthday Surprise
        </div>
        <h1 class="start-title gradient-heading">Made For You, Sam</h1>
        <p class="start-subtitle">A little celebration full of smiles & good vibes ✨</p>
        
        <button class="btn-primary" id="start-btn">
          <span>Let's Celebrate</span>
          <span style="font-size: 20px;">➔</span>
        </button>'''

if old_screen1_html in html:
    html = html.replace(old_screen1_html, new_screen1_html)
    print("3. Replaced screen1 HTML")

# 5. Update Cute Modal Markup
old_modal_html = '''        <div style="font-size: 48px; margin-bottom: 12px;">🙈💕</div>
        <h3 style="font-size: 22px; margin-bottom: 10px; color: var(--text-plum);">Nice try!</h3>
        <p style="font-family: var(--font-serif); font-size: 19px; color: var(--text-plum-light); margin-bottom: 22px;">
          You can't escape my love that easily! Come on, your special surprise is waiting for you 😉
        </p>
        <button class="btn-primary" id="modal-proceed-btn" style="padding: 12px 28px; font-size: 16px;">
          Okay, Take Me There! 🌸
        </button>'''

new_modal_html = '''        <div style="font-size: 48px; margin-bottom: 12px;">🎉😊</div>
        <h3 style="font-size: 22px; margin-bottom: 10px; color: var(--text-plum);">Hey, no skipping out!</h3>
        <p style="font-family: var(--font-serif); font-size: 19px; color: var(--text-plum-light); margin-bottom: 22px;">
          Today is all about you! Come on, your birthday celebration is waiting 😉✨
        </p>
        <button class="btn-primary" id="modal-proceed-btn" style="padding: 12px 28px; font-size: 16px;">
          Okay, Let's Go! 🌸
        </button>'''

if old_modal_html in html:
    html = html.replace(old_modal_html, new_modal_html)
    print("4. Replaced modal HTML")

# 6. Screen 2 button text & dog speech bubble
html = html.replace(
    '<div class="dog-speech-bubble" id="dog-bubble">Woof! Happy Birthday, Sam! 🐾🎂</div>',
    '<div class="dog-speech-bubble" id="dog-bubble">Woof! Happy Birthday, Sam! 🐾✨</div>'
)
html = html.replace(
    '<span>Open Your Wish</span>',
    '<span>Open Your Wishes</span>'
)

# 7. Screen 3 Header
old_scratch_header = '''      <div class="scratch-header">
        <h2 class="gradient-heading">5 Little Secrets</h2>
        <p>Gently scratch each card with your finger or mouse ✦</p>
      </div>'''

new_scratch_header = '''      <div class="scratch-header">
        <h2 class="gradient-heading">5 Reasons You're Amazing ✨</h2>
        <p>Scratch each card to reveal a little message ✦</p>
      </div>'''

if old_scratch_header in html:
    html = html.replace(old_scratch_header, new_scratch_header)
    print("5. Replaced scratch header")

# 8. Screen 4 Header, stamp & signature
html = html.replace(
    '<h2 class="letter-screen-title gradient-heading">A letter from my heart…</h2>',
    '<h2 class="letter-screen-title gradient-heading">A Birthday Note For You 💌</h2>'
)
html = html.replace(
    '<span class="stamp-text">Love</span>',
    '<span class="stamp-text">Wish</span>'
)
html = html.replace(
    'With all my love,<br>',
    'Always cheering for you,<br>'
)
html = html.replace(
    '<span>Our Memories</span>',
    '<span>Memories & Moments</span>'
)

# 9. Screen 5 Header and Final Card
old_memories_header = '''      <div class="memories-header">
        <h2 class="gradient-heading">Our Core Memories</h2>
        <p>Moments I'll cherish for a lifetime 🌸</p>
      </div>'''

new_memories_header = '''      <div class="memories-header">
        <h2 class="gradient-heading">Memories & Moments 📸</h2>
        <p>Looking back at some of our favorite times ✨</p>
      </div>'''

if old_memories_header in html:
    html = html.replace(old_memories_header, new_memories_header)
    print("6. Replaced memories header")

old_final_card = '''      <div class="final-bday-card">
        <div class="cake-icon-wrap">🎂</div>
        <h3 class="gradient-heading" style="font-size: 28px;">Forever & Always</h3>
        <p class="final-message-text" id="final-message-display"></p>
        <div class="bday-signoff">♡ Happy Birthday ♡</div>

        <button class="btn-primary" id="restart-btn" style="padding: 14px 32px;">
          <span>Start Over</span>
          <span>↺</span>
        </button>
      </div>'''

new_final_card = '''      <div class="final-bday-card">
        <div class="cake-icon-wrap">🎂</div>
        <h3 class="gradient-heading" style="font-size: 28px;">Wishing You The Best!</h3>
        <p class="final-message-text" id="final-message-display"></p>
        <div class="bday-signoff">♡ Happy Birthday, Sam! ♡</div>

        <button class="btn-primary" id="restart-btn" style="padding: 14px 32px;">
          <span>Replay Celebration</span>
          <span>↺</span>
        </button>
      </div>'''

if old_final_card in html:
    html = html.replace(old_final_card, new_final_card)
    print("7. Replaced final card")

# 10. Update CONFIG Object
config_match = re.search(r'const CONFIG = \{.*?\n    \};', html, re.DOTALL)
if config_match:
    new_config = '''const CONFIG = {
      // The birthday star's name:
      name: "Sam",

      // Your name:
      sender: "Niraj",

      // 5 Thoughtful & Sweet Scratch messages (friendly & uplifting):
      scratchMessages: [
        "Your smile and positive energy can genuinely brighten anyone's entire day ✨",
        "Thank you for always bringing so much laughter and good vibes wherever you go 🌸",
        "Having an awesome person like you around makes everything a hundred times more fun 💫",
        "Here's to all our crazy conversations, hilarious laughs, and future adventures 🥂",
        "May this year bring you all the success, happiness, and big dreams you deserve 🌟"
      ],

      // Heartfelt birthday letter (warm, friendly & celebratory):
      letterText: "Hey Sam,\\n\\nHappy Birthday! 🎉\\n\\nI wanted to take a moment today to celebrate you and remind you how truly special of a person you are. Your kindness, your quick humor, and the bright energy you bring whenever we talk make you one of a kind.\\n\\nThank you for being such an awesome friend, for all the hilarious laughs and great conversations, and for just being unapologetically you. Having you in my life is something I truly appreciate.\\n\\nI hope this upcoming year brings you countless reasons to smile, exciting new adventures, and all the success and happiness you deserve.\\n\\nCheers to another fantastic chapter of your life! 🎂✨",

      // Polaroid memories (User can also tap each polaroid to upload real photos!):
      memories: [
        {
          title: "When We First Met",
          caption: "That first conversation where we immediately clicked and couldn't stop talking.",
          emoji: "☕",
          rotation: -2.2
        },
        {
          title: "Uncontrollable Laughter",
          caption: "Laughing until our stomachs hurt over the most random inside jokes.",
          emoji: "😂",
          rotation: 2.4
        },
        {
          title: "Late-Night Chats",
          caption: "Sharing crazy stories, random thoughts, and the best music recommendations.",
          emoji: "🌙",
          rotation: -1.8
        },
        {
          title: "Adventures & Hangouts",
          caption: "Every trip, drive, and hangout that turned into an unforgettable memory.",
          emoji: "🚗",
          rotation: 2.1
        },
        {
          title: "Celebrating You Today",
          caption: "Here's to celebrating the amazing person you are and many more great memories ahead!",
          emoji: "✨",
          rotation: -2
        }
      ],

      // Final celebration message on the last card:
      finalMessage: "May all your birthday wishes come true, today and always. Keep shining bright and staying awesome!"
    };'''
    html = html[:config_match.start()] + new_config + html[config_match.end():]
    print("8. Replaced CONFIG object")
else:
    print("CONFIG match not found!")

# 11. Update audio button script logic
old_audio_js = '''    audioBtn.addEventListener("click", () => {
      const active = musicPlayer.toggle();
      if (active) {
        audioBtn.classList.add("playing");
        audioBtn.textContent = "🎶";
      } else {
        audioBtn.classList.remove("playing");
        audioBtn.textContent = "🎵";
      }
    });'''

new_audio_js = '''    audioBtn.addEventListener("click", () => {
      const active = musicPlayer.toggle();
      const musicText = document.getElementById("music-text");
      const musicIcon = document.getElementById("music-icon");
      if (active) {
        audioBtn.classList.add("playing");
        if (musicIcon) musicIcon.textContent = "🎶";
        if (musicText) musicText.textContent = "Playing";
      } else {
        audioBtn.classList.remove("playing");
        if (musicIcon) musicIcon.textContent = "🎵";
        if (musicText) musicText.textContent = "Music";
      }
    });'''

if old_audio_js in html:
    html = html.replace(old_audio_js, new_audio_js)
    print("9. Replaced audio JS listener")

html = html.replace(
    'audioBtn.classList.add("playing");\n        audioBtn.textContent = "🎶";',
    'audioBtn.classList.add("playing");\n        const mt = document.getElementById("music-text"); if (mt) mt.textContent = "Playing";\n        const mi = document.getElementById("music-icon"); if (mi) mi.textContent = "🎶";'
)

# 12. Add subtle glossy gleam to .btn-primary
old_btn_css = '''    .btn-primary {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      background: linear-gradient(135deg, var(--btn-rose) 0%, var(--btn-orchid) 100%);
      color: var(--white);
      border: 1.5px solid rgba(255, 255, 255, 0.4);
      padding: 16px 36px;
      font-size: 18px;
      font-weight: 700;
      font-family: var(--font-sans);
      border-radius: 999px;
      cursor: pointer;
      box-shadow: 0 10px 25px rgba(255, 111, 165, 0.38), 0 4px 10px rgba(198, 91, 214, 0.25);
      transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
      text-decoration: none;
      user-select: none;
    }'''

new_btn_css = '''    .btn-primary {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      background: linear-gradient(135deg, var(--btn-rose) 0%, var(--btn-orchid) 100%);
      color: var(--white);
      border: 1.5px solid rgba(255, 255, 255, 0.5);
      padding: 16px 36px;
      font-size: 18px;
      font-weight: 700;
      font-family: var(--font-sans);
      border-radius: 999px;
      cursor: pointer;
      box-shadow: 0 10px 25px rgba(255, 111, 165, 0.38), 0 4px 10px rgba(198, 91, 214, 0.25);
      transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
      text-decoration: none;
      user-select: none;
      position: relative;
      overflow: hidden;
    }

    .btn-primary::after {
      content: '';
      position: absolute;
      top: -50%;
      left: -60%;
      width: 40%;
      height: 200%;
      background: linear-gradient(
        to right,
        rgba(255, 255, 255, 0) 0%,
        rgba(255, 255, 255, 0.35) 50%,
        rgba(255, 255, 255, 0) 100%
      );
      transform: rotate(25deg);
      transition: all 0.75s ease;
      pointer-events: none;
    }

    .btn-primary:hover::after {
      left: 130%;
    }'''

if old_btn_css in html:
    html = html.replace(old_btn_css, new_btn_css)
    print("10. Replaced button CSS with glossy gleam")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: index.html has been completely updated!")
