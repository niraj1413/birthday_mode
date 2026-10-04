import os

# Read the base64 dog images from dog_b64.js
with open('dog_b64.js', 'r', encoding='utf-8') as f:
    dog_b64_content = f.read()

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover, maximum-scale=1.0, user-scalable=no">
  <title>Happy Birthday, Sam! 🌸✨</title>
  <meta name="description" content="A special birthday celebration made just for you, Sam!">
  
  <!-- Google Fonts: Cormorant Garamond + Pacifico + Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Pacifico&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    /* ==========================================================================
       DESIGN TOKENS & BASE PALETTE
       ========================================================================== */
    :root {
      --bg-blush: #fff0f5;
      --bg-lavender: #f3e6ff;
      --btn-rose: #ff6fa5;
      --btn-orchid: #c65bd6;
      --text-plum: #5a2750;
      --text-plum-light: #7e396e;
      --text-plum-subtle: #9c608e;
      --accent-gold: #d9a441;
      --accent-gold-light: #fbe3a1;
      --accent-gold-dark: #b58025;
      --envelope-wine: #8e2848;
      --envelope-wine-dark: #6b1a33;
      --envelope-wine-light: #a83a5c;
      --paper-cream: #fffdf9;
      --white: #ffffff;
      --shadow-soft: 0 10px 30px rgba(90, 39, 80, 0.08);
      --shadow-hover: 0 16px 36px rgba(90, 39, 80, 0.16);
      --shadow-gold: 0 0 20px rgba(217, 164, 65, 0.35);
      --radius-sm: 12px;
      --radius-md: 20px;
      --radius-lg: 32px;
      --font-display: 'Pacifico', cursive;
      --font-serif: 'Cormorant Garamond', Georgia, serif;
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    html, body {
      width: 100%;
      min-height: 100%;
      min-height: -webkit-fill-available;
      background: linear-gradient(135deg, var(--bg-blush) 0%, var(--bg-lavender) 100%);
      color: var(--text-plum);
      font-family: var(--font-sans);
      overflow-x: hidden;
      position: relative;
    }

    body {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      padding-top: env(safe-area-inset-top, 20px);
      padding-bottom: env(safe-area-inset-bottom, 20px);
      padding-left: env(safe-area-inset-left, 16px);
      padding-right: env(safe-area-inset-right, 16px);
      line-height: 1.6;
    }

    /* Ambient Falling Canvas */
    #bg-canvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 0;
    }

    /* Music Controller Button (Modern Frosted Glass Pill) */
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
    }

    /* App Container */
    #app {
      position: relative;
      z-index: 2;
      width: 100%;
      max-width: 500px;
      min-height: calc(100vh - 40px);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 16px 0;
    }

    /* Typography & Gradients */
    .gradient-heading {
      font-family: var(--font-display);
      background: linear-gradient(135deg, #ff4f8b 0%, #c65bd6 50%, #8a3bf2 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      text-align: center;
      line-height: 1.3;
      filter: drop-shadow(0 2px 8px rgba(198, 91, 214, 0.2));
    }

    .serif-text {
      font-family: var(--font-serif);
      font-style: italic;
    }

    /* Button Styles with glossy light gleam */
    .btn-primary {
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

    .btn-primary:hover:not(:disabled)::after {
      left: 130%;
    }

    .btn-primary:hover:not(:disabled) {
      transform: translateY(-3px) scale(1.03);
      box-shadow: 0 16px 32px rgba(255, 111, 165, 0.45), 0 6px 14px rgba(198, 91, 214, 0.35);
      border-color: var(--accent-gold);
    }

    .btn-primary:active:not(:disabled) {
      transform: translateY(1px) scale(0.98);
    }

    .btn-primary:disabled {
      background: linear-gradient(135deg, #d3c0cb 0%, #baa8b7 100%);
      cursor: not-allowed;
      box-shadow: none;
      opacity: 0.65;
      transform: none;
    }

    /* Screen Transition System */
    .screen {
      display: none;
      width: 100%;
      flex-direction: column;
      align-items: center;
      opacity: 0;
      transform: translateY(24px);
      transition: opacity 0.55s cubic-bezier(0.2, 0.8, 0.2, 1), transform 0.55s cubic-bezier(0.2, 0.8, 0.2, 1);
    }

    .screen.active {
      display: flex;
      opacity: 1;
      transform: translateY(0);
    }

    /* Glass Card Style */
    .glass-card {
      background: rgba(255, 255, 255, 0.88);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1.5px solid rgba(255, 255, 255, 0.95);
      border-radius: var(--radius-lg);
      padding: 36px 28px;
      box-shadow: var(--shadow-soft), 0 0 0 1px rgba(217, 164, 65, 0.15);
      text-align: center;
      width: 100%;
      position: relative;
    }

    /* ==========================================================================
       SCREEN 1: START SCREEN
       ========================================================================== */
    .warning-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 18px;
      background: rgba(255, 111, 165, 0.12);
      border: 1px solid rgba(255, 111, 165, 0.35);
      border-radius: 999px;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.8px;
      color: #df4482;
      margin-bottom: 22px;
      animation: soft-pulse 2.5s infinite ease-in-out;
    }

    @keyframes soft-pulse {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.04); }
    }

    .start-title {
      font-size: 32px;
      margin-bottom: 14px;
      color: var(--text-plum);
      font-weight: 700;
      line-height: 1.25;
    }

    .start-subtitle {
      font-size: 17px;
      color: var(--text-plum-light);
      margin-bottom: 34px;
      font-family: var(--font-serif);
      font-size: 21px;
    }

    .maybe-later {
      margin-top: 18px;
      color: var(--text-plum-subtle);
      font-size: 14px;
      text-decoration: underline;
      cursor: pointer;
      background: none;
      border: none;
      font-family: var(--font-sans);
      transition: color 0.2s;
    }

    .maybe-later:hover {
      color: var(--btn-rose);
    }

    /* Playful Rejection Modal */
    .cute-modal {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(90, 39, 80, 0.45);
      backdrop-filter: blur(8px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 999;
      padding: 20px;
    }

    .cute-modal.show {
      display: flex;
    }

    .cute-modal-content {
      background: #fff;
      border: 2px solid var(--accent-gold);
      border-radius: var(--radius-md);
      padding: 32px 24px;
      max-width: 380px;
      text-align: center;
      animation: pop-modal 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
      box-shadow: 0 20px 45px rgba(90, 39, 80, 0.3);
    }

    @keyframes pop-modal {
      0% { transform: scale(0.7); opacity: 0; }
      100% { transform: scale(1); opacity: 1; }
    }

    /* ==========================================================================
       SCREEN 2: BIRTHDAY DOG SCREEN (REAL CUTOUT ANIMATION)
       ========================================================================== */
    .dog-stage {
      position: relative;
      width: 260px;
      height: 310px;
      margin: 10px auto 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      user-select: none;
    }

    .dog-shadow {
      position: absolute;
      bottom: 6px;
      left: 50%;
      transform: translateX(-50%);
      width: 150px;
      height: 20px;
      background: radial-gradient(ellipse at center, rgba(90, 39, 80, 0.35) 0%, rgba(90, 39, 80, 0) 72%);
      border-radius: 50%;
      animation: dog-shadow-anim 2.4s cubic-bezier(0.4, 0, 0.2, 1) infinite;
    }

    .dog-actor {
      position: relative;
      width: 185px;
      height: 295px;
      animation: dog-jump-anim 2.4s cubic-bezier(0.4, 0, 0.2, 1) infinite;
      transform-origin: bottom center;
      transition: filter 0.3s ease;
    }

    .dog-stage:hover .dog-actor {
      filter: drop-shadow(0 6px 18px rgba(217, 164, 65, 0.45));
    }

    .dog-frame {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: contain;
      pointer-events: none;
      -webkit-user-drag: none;
    }

    .dog-sit {
      animation: dog-sit-fade 2.4s infinite;
    }

    .dog-jump {
      animation: dog-jump-fade 2.4s infinite;
    }

    /* Candle flame sparkle glow effect over the cake */
    .cake-flame-glow {
      position: absolute;
      top: 96px;
      left: 50%;
      transform: translateX(-50%);
      width: 120px;
      height: 35px;
      background: radial-gradient(ellipse at center, rgba(255, 200, 50, 0.6) 0%, rgba(255, 120, 50, 0.25) 50%, rgba(255, 120, 50, 0) 80%);
      border-radius: 50%;
      animation: candle-glow-flicker 0.6s infinite alternate ease-in-out;
      pointer-events: none;
      z-index: 5;
    }

    @keyframes candle-glow-flicker {
      0% { opacity: 0.6; transform: translateX(-50%) scale(0.92); }
      100% { opacity: 1; transform: translateX(-50%) scale(1.18); }
    }

    /* Seamless frame switching between sitting and jumping dog */
    @keyframes dog-sit-fade {
      0%, 20% { opacity: 1; }
      22%, 74% { opacity: 0; }
      76%, 100% { opacity: 1; }
    }

    @keyframes dog-jump-fade {
      0%, 20% { opacity: 0; }
      22%, 74% { opacity: 1; }
      76%, 100% { opacity: 0; }
    }

    /* Excited squash, jump, tilt and rotation keyframes */
    @keyframes dog-jump-anim {
      0% {
        transform: translateY(0) scale(1, 1) rotate(0deg);
      }
      14% {
        transform: translateY(6px) scale(1.09, 0.91) rotate(0deg);
      }
      22% {
        transform: translateY(-16px) scale(0.95, 1.06) rotate(-4deg);
      }
      38% {
        transform: translateY(-56px) scale(1, 1) rotate(-8deg);
      }
      48% {
        transform: translateY(-62px) scale(1.02, 0.98) rotate(7deg);
      }
      58% {
        transform: translateY(-52px) scale(1, 1) rotate(-5deg);
      }
      72% {
        transform: translateY(-12px) scale(0.96, 1.04) rotate(2deg);
      }
      76% {
        transform: translateY(4px) scale(1.13, 0.87) rotate(0deg);
      }
      86% {
        transform: translateY(-7px) scale(0.97, 1.03) rotate(0deg);
      }
      94%, 100% {
        transform: translateY(0) scale(1, 1) rotate(0deg);
      }
    }

    @keyframes dog-shadow-anim {
      0% {
        transform: translateX(-50%) scale(1);
        opacity: 0.55;
      }
      14% {
        transform: translateX(-50%) scale(1.22);
        opacity: 0.75;
      }
      38%, 58% {
        transform: translateX(-50%) scale(0.48);
        opacity: 0.16;
      }
      76% {
        transform: translateX(-50%) scale(1.28);
        opacity: 0.85;
      }
      86% {
        transform: translateX(-50%) scale(0.92);
        opacity: 0.48;
      }
      94%, 100% {
        transform: translateX(-50%) scale(1);
        opacity: 0.55;
      }
    }

    /* Cute Woof Speech Bubble on Click */
    .dog-speech-bubble {
      position: absolute;
      top: -12px;
      right: 0px;
      background: #ffffff;
      border: 1.5px solid var(--accent-gold);
      border-radius: 16px;
      padding: 6px 14px;
      font-size: 13px;
      font-weight: 700;
      color: var(--text-plum);
      box-shadow: 0 6px 18px rgba(90, 39, 80, 0.18);
      opacity: 0;
      transform: scale(0.7) translateY(10px);
      transition: all 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
      pointer-events: none;
      z-index: 10;
      white-space: nowrap;
    }

    .dog-speech-bubble.show {
      opacity: 1;
      transform: scale(1) translateY(0);
    }

    .dog-actor.tap-bounce {
      animation: dog-extra-spin 0.9s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
    }

    @keyframes dog-extra-spin {
      0% { transform: translateY(0) rotate(0deg) scale(1); }
      40% { transform: translateY(-75px) rotate(18deg) scale(1.12); }
      70% { transform: translateY(-35px) rotate(-14deg) scale(1.05); }
      100% { transform: translateY(0) rotate(0deg) scale(1); }
    }

    .bday-text {
      font-size: 34px;
      margin-bottom: 24px;
      padding: 0 10px;
    }

    /* Confetti Canvas for Screen 2 */
    #confetti-canvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 10;
    }

    /* ==========================================================================
       SCREEN 3: SCRATCH CARDS SCREEN
       ========================================================================== */
    .scratch-header {
      text-align: center;
      margin-bottom: 24px;
    }

    .scratch-header h2 {
      font-size: 32px;
      margin-bottom: 6px;
    }

    .scratch-header p {
      font-family: var(--font-serif);
      font-size: 19px;
      color: var(--text-plum-light);
    }

    .scratch-cards-container {
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 20px;
      padding-bottom: 120px;
    }

    .scratch-card {
      position: relative;
      width: 100%;
      height: 170px;
      border-radius: var(--radius-md);
      overflow: hidden;
      background: #ffffff;
      border: 2px solid var(--accent-gold-light);
      box-shadow: 0 8px 24px rgba(90, 39, 80, 0.08);
      user-select: none;
      touch-action: none;
      transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    }

    .scratch-card.revealed {
      border-color: var(--accent-gold);
      box-shadow: 0 10px 28px rgba(217, 164, 65, 0.25);
    }

    .scratch-secret {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      padding: 22px 24px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      background: linear-gradient(135deg, #fff9fb 0%, #fbf5ff 100%);
      z-index: 1;
    }

    .secret-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      color: var(--accent-gold-dark);
      margin-bottom: 10px;
    }

    .secret-message {
      font-family: var(--font-serif);
      font-size: 20px;
      font-weight: 600;
      line-height: 1.45;
      color: var(--text-plum);
    }

    .secret-sparkle {
      position: absolute;
      bottom: 10px;
      right: 14px;
      font-size: 18px;
      opacity: 0.8;
    }

    .scratch-canvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 2;
      touch-action: none;
      cursor: crosshair;
      transition: opacity 0.5s ease;
    }

    .scratch-card.revealed .scratch-canvas {
      opacity: 0;
      pointer-events: none;
    }

    /* Sticky Bottom Bar */
    .sticky-scratch-bar {
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-top: 1.5px solid rgba(217, 164, 65, 0.3);
      padding: 16px 20px max(18px, env(safe-area-inset-bottom));
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      z-index: 90;
      box-shadow: 0 -8px 25px rgba(90, 39, 80, 0.08);
      max-width: 500px;
      left: 50%;
      transform: translateX(-50%);
      border-top-left-radius: var(--radius-md);
      border-top-right-radius: var(--radius-md);
    }

    .reveal-progress-wrapper {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .reveal-count-text {
      font-size: 14px;
      font-weight: 700;
      color: var(--text-plum);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .progress-track {
      width: 130px;
      height: 8px;
      background: #f0e1ea;
      border-radius: 999px;
      overflow: hidden;
    }

    .progress-fill {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, var(--btn-rose), var(--btn-orchid));
      border-radius: 999px;
      transition: width 0.4s ease;
    }

    /* ==========================================================================
       SCREEN 4: LETTER SCREEN
       ========================================================================== */
    .letter-screen-title {
      font-size: 32px;
      margin-bottom: 24px;
      text-align: center;
    }

    .envelope-container {
      width: 100%;
      max-width: 380px;
      perspective: 1200px;
      margin: 10px auto 20px;
      position: relative;
    }

    .envelope-box {
      width: 100%;
      height: 240px;
      position: relative;
      cursor: pointer;
      transform-style: preserve-3d;
      transition: transform 0.4s ease;
    }

    .envelope-box:hover {
      transform: translateY(-4px);
    }

    .envelope-back {
      position: absolute;
      inset: 0;
      background: var(--envelope-wine);
      border: 2px solid var(--accent-gold);
      border-radius: 14px;
      box-shadow: var(--shadow-hover);
      z-index: 1;
    }

    .envelope-flap {
      position: absolute;
      top: 0;
      left: 0;
      width: 0;
      height: 0;
      border-left: 190px solid transparent;
      border-right: 190px solid transparent;
      border-top: 130px solid var(--envelope-wine-light);
      transform-origin: top center;
      transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1), z-index 0.2s;
      z-index: 5;
      filter: drop-shadow(0 2px 4px rgba(0,0,0,0.15));
    }

    .envelope-pocket {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 4;
      pointer-events: none;
    }

    .envelope-pocket-front {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 0;
      height: 0;
      border-left: 190px solid var(--envelope-wine-dark);
      border-right: 190px solid var(--envelope-wine-dark);
      border-top: 125px solid transparent;
      border-bottom: 115px solid var(--envelope-wine);
      border-bottom-left-radius: 14px;
      border-bottom-right-radius: 14px;
    }

    .wax-seal {
      position: absolute;
      top: 110px;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 58px;
      height: 58px;
      background: radial-gradient(circle, #f0c366 0%, var(--accent-gold) 65%, #a6731e 100%);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #6b4408;
      font-size: 26px;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.35), inset 0 2px 4px rgba(255, 255, 255, 0.45);
      border: 2px dashed rgba(255, 255, 255, 0.4);
      z-index: 6;
      transition: transform 0.4s ease, opacity 0.4s ease;
      cursor: pointer;
    }

    .wax-seal:hover {
      transform: translate(-50%, -50%) scale(1.12);
    }

    .envelope-box.opened .envelope-flap {
      transform: rotateX(180deg);
      z-index: 0;
    }

    .envelope-box.opened .wax-seal {
      opacity: 0;
      transform: translate(-50%, -50%) scale(0.4);
      pointer-events: none;
    }

    .envelope-hint {
      margin-top: 14px;
      font-size: 15px;
      color: var(--text-plum-light);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      animation: bounce-subtle 1.8s infinite;
    }

    @keyframes bounce-subtle {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-4px); }
    }

    .letter-paper-wrapper {
      width: 100%;
      max-width: 440px;
      background: var(--paper-cream);
      border: 1.5px solid var(--accent-gold);
      border-radius: var(--radius-md);
      box-shadow: 0 16px 40px rgba(90, 39, 80, 0.12), inset 0 0 25px rgba(217, 164, 65, 0.08);
      padding: 36px 30px;
      position: relative;
      margin-top: 10px;
      display: none;
      animation: paper-unfold 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
      background-image: repeating-linear-gradient(
        transparent,
        transparent 31px,
        rgba(217, 164, 65, 0.15) 31px,
        rgba(217, 164, 65, 0.15) 32px
      );
      line-height: 32px;
    }

    @keyframes paper-unfold {
      0% {
        opacity: 0;
        transform: translateY(40px) scale(0.9);
      }
      100% {
        opacity: 1;
        transform: translateY(0) scale(1);
      }
    }

    .stamp-decoration {
      position: absolute;
      top: 18px;
      right: 18px;
      width: 48px;
      height: 56px;
      border: 2px dashed var(--accent-gold);
      border-radius: 4px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      color: var(--btn-rose);
      background: rgba(255, 240, 245, 0.6);
      transform: rotate(4deg);
    }

    .stamp-text {
      font-size: 8px;
      font-weight: 700;
      color: var(--accent-gold-dark);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .letter-body {
      font-family: var(--font-serif);
      font-size: 20px;
      color: var(--text-plum);
      white-space: pre-wrap;
      min-height: 180px;
      position: relative;
    }

    .typing-cursor {
      display: inline-block;
      width: 2px;
      height: 1.2em;
      background: var(--btn-rose);
      margin-left: 2px;
      vertical-align: text-bottom;
      animation: blink-cursor 0.75s infinite;
    }

    @keyframes blink-cursor {
      0%, 100% { opacity: 1; }
      50% { opacity: 0; }
    }

    .letter-signature {
      margin-top: 28px;
      text-align: right;
      font-family: var(--font-display);
      font-size: 24px;
      color: var(--btn-orchid);
      opacity: 0;
      transform: translateY(10px);
      transition: all 0.6s ease;
    }

    .letter-signature.visible {
      opacity: 1;
      transform: translateY(0);
    }

    .letter-actions {
      margin-top: 26px;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 12px;
    }

    .skip-typing-btn {
      font-size: 13px;
      color: var(--text-plum-subtle);
      background: none;
      border: none;
      text-decoration: underline;
      cursor: pointer;
      padding: 6px;
    }

    /* ==========================================================================
       SCREEN 5: CORE MEMORIES SCREEN
       ========================================================================== */
    .memories-header {
      text-align: center;
      margin-bottom: 30px;
    }

    .memories-header h2 {
      font-size: 34px;
      margin-bottom: 6px;
    }

    .memories-header p {
      font-family: var(--font-serif);
      font-size: 19px;
      color: var(--text-plum-light);
    }

    .memories-list {
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 36px;
      margin-bottom: 40px;
    }

    .polaroid-card {
      background: #ffffff;
      padding: 16px 16px 26px 16px;
      border-radius: 6px;
      box-shadow: 0 12px 35px rgba(90, 39, 80, 0.12), 0 2px 6px rgba(0, 0, 0, 0.04);
      position: relative;
      transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s ease;
      cursor: pointer;
    }

    .polaroid-card:hover {
      transform: scale(1.02) rotate(0deg) !important;
      box-shadow: 0 20px 42px rgba(90, 39, 80, 0.18);
      z-index: 5;
    }

    .washi-tape {
      position: absolute;
      top: -12px;
      left: 50%;
      transform: translateX(-50%);
      width: 90px;
      height: 24px;
      background: rgba(255, 111, 165, 0.35);
      border: 1px dashed rgba(255, 111, 165, 0.5);
      backdrop-filter: blur(4px);
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
      border-radius: 2px;
      z-index: 3;
    }

    .photo-frame {
      width: 100%;
      aspect-ratio: 1 / 1;
      border-radius: 4px;
      overflow: hidden;
      background: linear-gradient(135deg, #fff0f5 0%, #f3e6ff 100%);
      border: 1px solid rgba(217, 164, 65, 0.2);
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .photo-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: none;
    }

    .photo-placeholder {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 20px;
      text-align: center;
      gap: 8px;
    }

    .placeholder-emoji {
      font-size: 52px;
      filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.1));
      animation: float-emoji 3s ease-in-out infinite alternate;
    }

    @keyframes float-emoji {
      0% { transform: translateY(0); }
      100% { transform: translateY(-8px); }
    }

    .upload-prompt {
      font-size: 13px;
      font-weight: 600;
      color: var(--btn-orchid);
      background: rgba(255, 255, 255, 0.85);
      padding: 6px 14px;
      border-radius: 999px;
      border: 1px dashed var(--btn-rose);
      margin-top: 6px;
    }

    .polaroid-caption {
      margin-top: 18px;
      text-align: center;
      padding: 0 8px;
    }

    .polaroid-title {
      font-family: var(--font-serif);
      font-size: 22px;
      font-weight: 700;
      color: var(--text-plum);
      margin-bottom: 4px;
    }

    .polaroid-desc {
      font-size: 14px;
      color: var(--text-plum-light);
      font-family: var(--font-serif);
      font-style: italic;
    }

    .memories-next-wrap {
      width: 100%;
      display: flex;
      justify-content: center;
      margin: 10px 0 35px;
    }

    /* ==========================================================================
       SCREEN 6: 5 CLOUDS SCREEN (BOLLYWOOD KK SONG & 3-4 WORD MESSAGES)
       ========================================================================== */
    .clouds-header {
      text-align: center;
      margin-bottom: 26px;
    }

    .clouds-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 7px 16px;
      background: rgba(198, 91, 214, 0.12);
      border: 1px solid rgba(198, 91, 214, 0.35);
      border-radius: 999px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 1px;
      color: var(--btn-orchid);
      margin-bottom: 12px;
      text-transform: uppercase;
    }

    .clouds-subtitle {
      font-family: var(--font-serif);
      font-size: 20px;
      color: var(--text-plum-light);
      margin-top: 6px;
    }

    .clouds-list {
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
    }

    .cloud-top-row {
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
    }

    .cloud-number-pill {
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--accent-gold-dark);
      background: rgba(217, 164, 65, 0.15);
      padding: 4px 12px;
      border-radius: 999px;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }

    .cloud-tap-hint {
      font-size: 12px;
      color: var(--btn-orchid);
      font-weight: 600;
      animation: soft-pulse 2s infinite;
    }

    .cloud-unopened-view {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 8px;
      padding: 10px 0;
    }

    .cloud-puffy-icon {
      font-size: 44px;
      filter: drop-shadow(0 4px 8px rgba(198, 91, 214, 0.2));
      animation: float-drift 3s ease-in-out infinite alternate;
    }

    @keyframes float-drift {
      0% { transform: translateY(0) scale(1); }
      100% { transform: translateY(-6px) scale(1.05); }
    }

    .cloud-unopened-title {
      font-size: 16px;
      font-weight: 600;
      color: var(--text-plum);
    }

    /* Opened Content: 3-4 Word Image Sentiment */
    .cloud-opened-view {
      display: none;
      flex-direction: column;
      align-items: center;
      animation: pop-modal 0.45s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
      width: 100%;
    }

    .cloud-card.opened .cloud-unopened-view {
      display: none;
    }

    .cloud-card.opened .cloud-opened-view {
      display: flex;
    }

    .cloud-card.opened .cloud-tap-hint {
      display: none;
    }

    .cloud-opened-sticker {
      font-size: 46px;
      margin-bottom: 8px;
      filter: drop-shadow(0 4px 10px rgba(0,0,0,0.1));
    }

    .cloud-words-title {
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
    }

    /* Sticky Clouds Tracker */
    .clouds-status-bar {
      margin-bottom: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      font-size: 14px;
      font-weight: 700;
      color: var(--text-plum);
      background: rgba(255, 255, 255, 0.85);
      padding: 8px 18px;
      border-radius: 999px;
      border: 1px solid var(--accent-gold-light);
      box-shadow: 0 4px 14px rgba(90, 39, 80, 0.06);
    }

    /* Grand Finale Card */
    .clouds-finale-card {
      width: 100%;
      background: linear-gradient(135deg, rgba(255,255,255,0.96) 0%, rgba(255,245,252,0.96) 100%);
      border: 2px solid var(--accent-gold);
      border-radius: var(--radius-lg);
      padding: 40px 26px;
      text-align: center;
      box-shadow: 0 20px 50px rgba(217, 164, 65, 0.25), var(--shadow-soft);
      position: relative;
      margin-top: 15px;
      animation: paper-unfold 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
    }

    .finale-cake-anim {
      font-size: 64px;
      margin-bottom: 12px;
      animation: float-drift 2.2s infinite ease-in-out alternate;
    }

    .finale-humanoid-text {
      font-family: var(--font-serif);
      font-size: 21px;
      font-weight: 600;
      color: var(--text-plum);
      line-height: 1.55;
      margin: 20px 0 26px;
      padding: 0 10px;
    }

    .bday-signoff {
      font-family: var(--font-display);
      font-size: 32px;
      background: linear-gradient(135deg, #ff4f8b, #c65bd6);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 24px;
    }

    /* Responsive adjustments */
    @media (max-width: 420px) {
      .envelope-box {
        height: 210px;
      }
      .envelope-flap {
        border-left-width: 160px;
        border-right-width: 160px;
        border-top-width: 110px;
      }
      .envelope-pocket-front {
        border-left-width: 160px;
        border-right-width: 160px;
        border-bottom-width: 100px;
      }
      .bday-text {
        font-size: 30px;
      }
      .letter-body {
        font-size: 18px;
      }
      .cloud-words-title {
        font-size: 23px;
      }
    }
  </style>
</head>
<body>

  <!-- Ambient Falling Petals, Hearts, and Bows Canvas -->
  <canvas id="bg-canvas"></canvas>

  <!-- Audio Toggle Button (Plays gentle melody / KK Bollywood song) -->
  <button class="audio-btn" id="audio-toggle" title="Play birthday music" aria-label="Toggle music">
    <span class="music-icon" id="music-icon">🎵</span>
    <span id="music-text">Music</span>
    <span class="equalizer-wave">
      <span></span><span></span><span></span>
    </span>
  </button>

  <!-- Optional HTML5 audio element for direct MP3 file -->
  <audio id="kk-audio" preload="auto"></audio>

  <!-- Main Application Wrapper -->
  <main id="app">

    <!-- =======================================================================
         SCREEN 1: START SCREEN
         ======================================================================= -->
    <section class="screen active" id="screen-start">
      <div class="glass-card">
        <div class="warning-badge">
          <span>🌸</span> A Birthday Celebration
        </div>
        <h1 class="start-title gradient-heading">Made For You, Sam</h1>
        <p class="start-subtitle">A little celebration full of smiles & good vibes ✨</p>
        
        <button class="btn-primary" id="start-btn">
          <span>Let's Celebrate</span>
          <span style="font-size: 20px;">➔</span>
        </button>
        
        <div>
          <button class="maybe-later" id="maybe-later-btn">Maybe Later</button>
        </div>
      </div>
    </section>

    <!-- Playful Rejection Modal -->
    <div class="cute-modal" id="cute-modal">
      <div class="cute-modal-content">
        <div style="font-size: 48px; margin-bottom: 12px;">🎉😊</div>
        <h3 style="font-size: 22px; margin-bottom: 10px; color: var(--text-plum);">Hey, no skipping out!</h3>
        <p style="font-family: var(--font-serif); font-size: 19px; color: var(--text-plum-light); margin-bottom: 22px;">
          Today is all about you! Come on, your birthday celebration is waiting 😉✨
        </p>
        <button class="btn-primary" id="modal-proceed-btn" style="padding: 12px 28px; font-size: 16px;">
          Okay, Let's Go! 🌸
        </button>
      </div>
    </div>

    <!-- =======================================================================
         SCREEN 2: BIRTHDAY ANIMATED DOG SCREEN
         ======================================================================= -->
    <section class="screen" id="screen-birthday">
      <div class="glass-card" style="position: relative; overflow: hidden;">
        <canvas id="confetti-canvas"></canvas>

        <div class="dog-stage" id="dog-stage" title="Tap to see me jump! 🐾">
          <div class="dog-speech-bubble" id="dog-bubble">Woof! Happy Birthday, Sam! 🐾✨</div>
          <!-- Animated Dynamic Shadow below dog -->
          <div class="dog-shadow" id="dog-shadow"></div>

          <!-- Excited Jumping Dog Actor -->
          <div class="dog-actor" id="dog-actor">
            <div class="cake-flame-glow"></div>
            <img id="dog-img-sit" class="dog-frame dog-sit" alt="Happy Birthday Dog Sitting" />
            <img id="dog-img-jump" class="dog-frame dog-jump" alt="Happy Birthday Dog Jumping" />
          </div>
        </div>

        <h2 class="bday-text gradient-heading" id="bday-heading">Happy Birthday, Sam!</h2>
        
        <button class="btn-primary" id="open-wish-btn">
          <span>Open Your Wishes</span>
          <span style="font-size: 20px;">✨</span>
        </button>
      </div>
    </section>

    <!-- =======================================================================
         SCREEN 3: SCRATCH CARDS SCREEN
         ======================================================================= -->
    <section class="screen" id="screen-scratch">
      <div class="scratch-header">
        <h2 class="gradient-heading">5 Reasons You're Amazing ✨</h2>
        <p>Scratch each card to reveal a little message ✦</p>
      </div>

      <div class="scratch-cards-container" id="scratch-cards-wrap">
        <!-- 5 Scratch cards dynamically populated from CONFIG -->
      </div>

      <!-- Sticky Bottom Navigation Bar -->
      <div class="sticky-scratch-bar">
        <div class="reveal-progress-wrapper">
          <div class="reveal-count-text">
            <span>✨</span>
            <span id="revealed-count-display">0 / 5 revealed</span>
          </div>
          <div class="progress-track">
            <div class="progress-fill" id="progress-fill-bar"></div>
          </div>
        </div>

        <button class="btn-primary" id="scratch-next-btn" disabled style="padding: 12px 24px; font-size: 16px;">
          <span>Next</span>
          <span>➔</span>
        </button>
      </div>
    </section>

    <!-- =======================================================================
         SCREEN 4: LETTER SCREEN (HUMANOID, HONEST SPARK, NO FRIEND, NO WIFE/GF)
         ======================================================================= -->
    <section class="screen" id="screen-letter">
      <h2 class="letter-screen-title gradient-heading">A Birthday Note For You 💌</h2>

      <!-- Wine-Rose Envelope with Gold Wax Seal -->
      <div class="envelope-container" id="envelope-wrapper">
        <div class="envelope-box" id="envelope-box">
          <div class="envelope-back"></div>
          <div class="envelope-flap" id="envelope-flap"></div>
          
          <div class="envelope-pocket">
            <div class="envelope-pocket-front"></div>
          </div>

          <!-- Gold Wax Seal -->
          <div class="wax-seal" id="wax-seal" title="Tap to open letter">
            <span>💌</span>
          </div>
        </div>

        <div class="envelope-hint" id="envelope-hint">
          <span>👆</span> Tap the wax seal to open
        </div>
      </div>

      <!-- Realistic Lined Paper that slides out and types letter -->
      <div class="letter-paper-wrapper" id="letter-paper">
        <div class="stamp-decoration">
          <span>🌸</span>
          <span class="stamp-text">Wish</span>
        </div>

        <div class="letter-body" id="letter-text-container"></div>

        <div class="letter-signature" id="letter-signature">
          Always in your corner,<br>
          <span id="sender-name-display" style="font-size: 28px;">Niraj</span>
        </div>

        <div class="letter-actions">
          <button class="skip-typing-btn" id="skip-typing-btn">Show all words ⚡</button>
          <button class="btn-primary" id="to-memories-btn" style="display: none; width: 100%; margin-top: 10px;">
            <span>Memories & Moments</span>
            <span>📸</span>
          </button>
        </div>
      </div>
    </section>

    <!-- =======================================================================
         SCREEN 5: CORE MEMORIES SCREEN
         ======================================================================= -->
    <section class="screen" id="screen-memories">
      <div class="memories-header">
        <h2 class="gradient-heading">Memories & Moments 📸</h2>
        <p>Looking back at some of our favorite times ✨</p>
      </div>

      <!-- Hidden file input for uploading images to polaroids -->
      <input type="file" id="global-photo-input" accept="image/*" style="display: none;">

      <div class="memories-list" id="memories-container">
        <!-- Rendered dynamically from CONFIG.memories -->
      </div>

      <!-- Button leading to the brand new Screen 6: 5 Clouds Screen -->
      <div class="memories-next-wrap">
        <button class="btn-primary" id="to-clouds-btn" style="padding: 16px 36px; font-size: 18px; width: 100%;">
          <span>One Last Surprise</span>
          <span style="font-size: 22px;">☁️</span>
        </button>
      </div>
    </section>

    <!-- =======================================================================
         SCREEN 6: 5 FLOATING CLOUDS SCREEN (BOLLYWOOD KK SONG & 3-4 WORD IMAGES)
         ======================================================================= -->
    <section class="screen" id="screen-clouds">
      <div class="clouds-header">
        <div class="clouds-badge">
          <span>☁️</span> One Last Surprise
        </div>
        <h2 class="gradient-heading">Up In The Clouds</h2>
        <p class="clouds-subtitle">5 little thoughts I kept for you — tap each cloud ✨</p>
      </div>

      <div class="clouds-status-bar">
        <span>☁️</span>
        <span id="clouds-opened-count">0 / 5 clouds opened</span>
      </div>

      <!-- 5 Interactive Clouds -->
      <div class="clouds-list" id="clouds-list">
        <!-- Rendered dynamically from CONFIG.clouds -->
      </div>

      <!-- Grand Finale Birthday Celebration Card (Revealed after all 5 clouds are opened) -->
      <div class="clouds-finale-card" id="clouds-finale-card" style="display: none;">
        <div class="finale-cake-anim">🎂✨</div>
        <h3 class="gradient-heading" style="font-size: 32px; margin-bottom: 12px;">Happy Birthday, Sam</h3>
        <p class="finale-humanoid-text">
          No big labels, no complicated words—just you, being completely unforgettable to me.<br><br>
          I hope today brings you as much happiness, warmth, and laughter as you bring into my world.
        </p>
        <div class="bday-signoff">♡ Happy Birthday, Sam! ♡</div>

        <button class="btn-primary" id="replay-all-btn" style="margin-top: 10px; padding: 14px 34px;">
          <span>Replay From Start</span>
          <span>↺</span>
        </button>
      </div>
    </section>

  </main>

  <!-- =======================================================================
       JAVASCRIPT LOGIC
       ======================================================================= -->
  <script>
    ''' + dog_b64_content + '''

    /* =========================================================================
       CONFIG - EDITABLE CONFIGURATION (HUMANOID TONE, NO FRIEND, NO WIFE/GF)
       ========================================================================= */
    const CONFIG = {
      // The birthday star's name:
      name: "Sam",

      // Your name:
      sender: "Niraj",

      // Optional URL or local filename for KK Bollywood song:
      // (If not provided or not found, it automatically synthesizes KK's "Aankhon Mein Teri"!)
      kkSongUrl: "kk_song.mp3",

      // 5 Sweet, uplifting thoughts (Screen 3):
      scratchMessages: [
        "Your smile catches me off guard every single time ✨",
        "That spark and warmth you bring wherever you go 🌸",
        "Our conversations that effortlessly bounce from silly banter to real talks 💫",
        "The way you just make ordinary moments feel electric 🥂",
        "Wishing you a year as bright, unforgettable, and special as you are 🌟"
      ],

      // Humanoid, real letter (she knows you like her, no "friend", no "wife/gf"):
      letterText: "Hey Sam,\\n\\nI sat down thinking about what to write for your birthday, and I realized I just wanted to be real with you.\\n\\nThere's something about you that's impossible not to notice. The effortless way you carry yourself, that smile that catches me off guard every single time, and how our conversations can bounce from completely ridiculous banter to something quiet and real without missing a beat.\\n\\nYou know I like you—and honestly, getting to know you, hearing your thoughts, and having you in my days has been one of the best parts of this year. You bring a kind of warmth that makes everything feel lighter and brighter just by being around.\\n\\nI hope today gives you every ounce of that back. I hope you feel celebrated, I hope you laugh until your cheeks hurt, and I hope this next chapter brings you everything you've been secretly wishing for.\\n\\nHappy Birthday, Sam. I'm really glad you're in my life. ✨",

      // Polaroids (Screen 5):
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
      ],

      // 5 Clouds with 3-4 word images & sentiments (Screen 6):
      clouds: [
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
      ]
    };

    /* =========================================================================
       STATE MANAGEMENT
       ========================================================================= */
    let currentScreen = "start";
    let revealedCount = 0;
    const TOTAL_SCRATCH_CARDS = 5;
    let isTypingLetter = false;
    let typingTimer = null;
    let activePolaroidPhotoEl = null;
    let openedCloudsCount = 0;

    /* =========================================================================
       AUDIO SYNTHESIZER (MUSIC BOX & BOLLYWOOD KK SONG "AANKHON MEIN TERI")
       ========================================================================= */
    class HybridMusicPlayer {
      constructor() {
        this.ctx = null;
        this.isPlaying = false;
        this.timeoutId = null;
        this.noteIndex = 0;
        this.currentMode = "musicbox"; // "musicbox" or "kk"

        // Mode 1: Gentle Romantic Music Box Melody
        this.melodyMusicBox = [
          { note: 261.63, dur: 400 },
          { note: 261.63, dur: 350 },
          { note: 293.66, dur: 700 },
          { note: 261.63, dur: 700 },
          { note: 349.23, dur: 700 },
          { note: 329.63, dur: 1200 },
          { note: 261.63, dur: 400 },
          { note: 261.63, dur: 350 },
          { note: 293.66, dur: 700 },
          { note: 261.63, dur: 700 },
          { note: 392.00, dur: 700 },
          { note: 349.23, dur: 1200 },
          { note: 261.63, dur: 400 },
          { note: 261.63, dur: 350 },
          { note: 523.25, dur: 700 },
          { note: 440.00, dur: 700 },
          { note: 349.23, dur: 700 },
          { note: 329.63, dur: 700 },
          { note: 293.66, dur: 1000 },
          { note: 466.16, dur: 400 },
          { note: 466.16, dur: 350 },
          { note: 440.00, dur: 700 },
          { note: 349.23, dur: 700 },
          { note: 392.00, dur: 700 },
          { note: 349.23, dur: 1400 }
        ];

        // Mode 2: KK - "Aankhon Mein Teri Ajab Si" (Om Shanti Om)
        // Iconic mukhda notes synthesized warmly with nylon guitar / music box harmonics:
        this.melodyKK = [
          // "Aan-khon mein te-ri..."
          { note: 493.88, dur: 480 }, // B4
          { note: 493.88, dur: 450 }, // B4
          { note: 440.00, dur: 450 }, // A4
          { note: 415.30, dur: 480 }, // G#4
          { note: 369.99, dur: 500 }, // F#4
          { note: 329.63, dur: 950 }, // E4

          // "A-jab si a-jab si a-daa-yein hain..."
          { note: 369.99, dur: 380 }, // F#4
          { note: 415.30, dur: 380 }, // G#4
          { note: 440.00, dur: 450 }, // A4
          { note: 415.30, dur: 400 }, // G#4
          { note: 369.99, dur: 420 }, // F#4
          { note: 329.63, dur: 550 }, // E4
          { note: 369.99, dur: 400 }, // F#4
          { note: 415.30, dur: 1100 }, // G#4

          // "Dil ko bana de jo patang saansein ye teri vo hawayein hain..."
          { note: 493.88, dur: 480 }, // B4
          { note: 493.88, dur: 450 }, // B4
          { note: 440.00, dur: 450 }, // A4
          { note: 415.30, dur: 480 }, // G#4
          { note: 369.99, dur: 500 }, // F#4
          { note: 329.63, dur: 950 }, // E4

          { note: 369.99, dur: 380 }, // F#4
          { note: 415.30, dur: 380 }, // G#4
          { note: 440.00, dur: 450 }, // A4
          { note: 415.30, dur: 400 }, // G#4
          { note: 369.99, dur: 420 }, // F#4
          { note: 329.63, dur: 550 }, // E4
          { note: 369.99, dur: 400 }, // F#4
          { note: 415.30, dur: 1100 }, // G#4

          // "Ho... aankhon mein teri..."
          { note: 659.25, dur: 600 }, // E5
          { note: 622.25, dur: 500 }, // D#5
          { note: 554.37, dur: 550 }, // C#5
          { note: 493.88, dur: 1200 } // B4
        ];
      }

      init() {
        if (!this.ctx) {
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          this.ctx = new AudioContext();
        }
        if (this.ctx.state === "suspended") {
          this.ctx.resume();
        }
      }

      playTone(freq, duration) {
        if (!this.ctx || !this.isPlaying) return;
        try {
          const now = this.ctx.currentTime;
          const osc1 = this.ctx.createOscillator();
          const osc2 = this.ctx.createOscillator();
          const gain = this.ctx.createGain();

          osc1.type = this.currentMode === "kk" ? "triangle" : "sine";
          osc1.frequency.setValueAtTime(freq, now);

          osc2.type = "sine";
          osc2.frequency.setValueAtTime(freq * (this.currentMode === "kk" ? 1.002 : 2.01), now);

          gain.gain.setValueAtTime(0.001, now);
          gain.gain.linearRampToValueAtTime(0.2, now + 0.04);
          gain.gain.exponentialRampToValueAtTime(0.0001, now + (duration / 1000) * 1.5);

          osc1.connect(gain);
          osc2.connect(gain);
          gain.connect(this.ctx.destination);

          osc1.start(now);
          osc2.start(now);
          osc1.stop(now + (duration / 1000) * 1.6);
          osc2.stop(now + (duration / 1000) * 1.6);
        } catch (e) {
          console.warn("Audio note play exception:", e);
        }
      }

      start(mode = null) {
        this.init();
        if (mode) this.currentMode = mode;
        this.isPlaying = true;
        this.noteIndex = 0;
        if (this.timeoutId) clearTimeout(this.timeoutId);

        const playLoop = () => {
          if (!this.isPlaying) return;
          const currentMelody = this.currentMode === "kk" ? this.melodyKK : this.melodyMusicBox;
          const current = currentMelody[this.noteIndex];
          this.playTone(current.note, current.dur);
          this.noteIndex = (this.noteIndex + 1) % currentMelody.length;
          this.timeoutId = setTimeout(playLoop, current.dur + (this.currentMode === "kk" ? 110 : 140));
        };
        playLoop();
      }

      stop() {
        this.isPlaying = false;
        if (this.timeoutId) clearTimeout(this.timeoutId);
      }

      toggle() {
        if (this.isPlaying) {
          this.stop();
          return false;
        } else {
          this.start();
          return true;
        }
      }

      switchToKK() {
        this.currentMode = "kk";
        // Check if external mp3 audio can play:
        const kkAudio = document.getElementById("kk-audio");
        if (kkAudio && CONFIG.kkSongUrl) {
          kkAudio.src = CONFIG.kkSongUrl;
          kkAudio.loop = true;
          const promise = kkAudio.play();
          if (promise !== undefined) {
            promise.then(() => {
              // Successfully playing real mp3! Stop synthesized notes
              this.stop();
              return;
            }).catch(() => {
              // Fall back to synthesized KK melody!
              this.start("kk");
            });
          }
        } else {
          this.start("kk");
        }
      }
    }

    const musicPlayer = new HybridMusicPlayer();
    const audioBtn = document.getElementById("audio-toggle");

    audioBtn.addEventListener("click", () => {
      const active = musicPlayer.toggle();
      const musicText = document.getElementById("music-text");
      const musicIcon = document.getElementById("music-icon");
      if (active) {
        audioBtn.classList.add("playing");
        if (musicIcon) musicIcon.textContent = "🎶";
        if (musicText) musicText.textContent = musicPlayer.currentMode === "kk" ? "KK Song" : "Playing";
      } else {
        audioBtn.classList.remove("playing");
        if (musicIcon) musicIcon.textContent = "🎵";
        if (musicText) musicText.textContent = "Music";
      }
    });

    /* =========================================================================
       BACKGROUND CANVAS: FALLING PETALS, HEARTS, AND GOLD BOWS
       ========================================================================= */
    const bgCanvas = document.getElementById("bg-canvas");
    const bgCtx = bgCanvas.getContext("2d");
    let bgParticles = [];

    function resizeBgCanvas() {
      bgCanvas.width = window.innerWidth;
      bgCanvas.height = window.innerHeight;
    }
    window.addEventListener("resize", resizeBgCanvas);
    resizeBgCanvas();

    class AmbientParticle {
      constructor() {
        this.reset(true);
      }

      reset(init = false) {
        this.x = Math.random() * bgCanvas.width;
        this.y = init ? Math.random() * bgCanvas.height : -30;
        this.size = Math.random() * 12 + 10;
        this.speedY = Math.random() * 0.9 + 0.6;
        this.speedX = (Math.random() - 0.5) * 0.7;
        this.rotation = Math.random() * Math.PI * 2;
        this.rotSpeed = (Math.random() - 0.5) * 0.02;
        this.opacity = Math.random() * 0.45 + 0.35;
        this.sway = Math.random() * 2;
        this.swaySpeed = Math.random() * 0.02 + 0.01;
        this.type = Math.floor(Math.random() * 3);
        const colors = ["#ff9ebc", "#f3b0c3", "#d9a441", "#c65bd6", "#ffd1dc"];
        this.color = colors[Math.floor(Math.random() * colors.length)];
      }

      update() {
        this.y += this.speedY;
        this.sway += this.swaySpeed;
        this.x += Math.sin(this.sway) * 0.6 + this.speedX;
        this.rotation += this.rotSpeed;

        if (this.y > bgCanvas.height + 40) {
          this.reset(false);
        }
      }

      draw(ctx) {
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(this.rotation);
        ctx.globalAlpha = this.opacity;

        if (this.type === 0) {
          ctx.fillStyle = this.color;
          ctx.beginPath();
          ctx.moveTo(0, -this.size * 0.8);
          ctx.quadraticCurveTo(this.size * 0.6, -this.size * 0.4, 0, this.size * 0.8);
          ctx.quadraticCurveTo(-this.size * 0.6, -this.size * 0.4, 0, -this.size * 0.8);
          ctx.fill();
        } else if (this.type === 1) {
          ctx.fillStyle = this.color;
          const s = this.size * 0.5;
          ctx.beginPath();
          ctx.moveTo(0, s * 0.3);
          ctx.bezierCurveTo(-s, -s * 0.7, -s * 1.5, s * 0.5, 0, s * 1.4);
          ctx.bezierCurveTo(s * 1.5, s * 0.5, s, -s * 0.7, 0, s * 0.3);
          ctx.fill();
        } else {
          ctx.fillStyle = "#d9a441";
          const s = this.size * 0.4;
          ctx.beginPath();
          ctx.arc(0, 0, s * 0.5, 0, Math.PI * 2);
          ctx.fill();
          ctx.strokeStyle = "#fbe3a1";
          ctx.lineWidth = 1;
          ctx.stroke();
        }

        ctx.restore();
      }
    }

    function initBgParticles() {
      bgParticles = [];
      const count = window.innerWidth < 600 ? 26 : 42;
      for (let i = 0; i < count; i++) {
        bgParticles.push(new AmbientParticle());
      }
    }
    initBgParticles();

    function renderBg() {
      bgCtx.clearRect(0, 0, bgCanvas.width, bgCanvas.height);
      for (const p of bgParticles) {
        p.update();
        p.draw(bgCtx);
      }
      requestAnimationFrame(renderBg);
    }
    renderBg();

    /* =========================================================================
       SCREEN NAVIGATION CONTROLLER
       ========================================================================= */
    const screens = {
      start: document.getElementById("screen-start"),
      birthday: document.getElementById("screen-birthday"),
      scratch: document.getElementById("screen-scratch"),
      letter: document.getElementById("screen-letter"),
      memories: document.getElementById("screen-memories"),
      clouds: document.getElementById("screen-clouds")
    };

    function showScreen(screenKey) {
      currentScreen = screenKey;
      Object.keys(screens).forEach(key => {
        const el = screens[key];
        if (key === screenKey) {
          el.classList.add("active");
          window.scrollTo({ top: 0, behavior: "smooth" });
        } else {
          el.classList.remove("active");
        }
      });

      if (screenKey === "birthday") {
        triggerConfettiExplosion();
      } else if (screenKey === "scratch") {
        initScratchCards();
      } else if (screenKey === "clouds") {
        initCloudsScreen();
        // Switch to KK Bollywood Song!
        musicPlayer.switchToKK();
        audioBtn.classList.add("playing");
        const mt = document.getElementById("music-text");
        if (mt) mt.textContent = "KK: Aankhon Mein Teri";
        const mi = document.getElementById("music-icon");
        if (mi) mi.textContent = "🎶";
      }
    }

    /* =========================================================================
       SCREEN 1 LOGIC: START & CUTE MODAL
       ========================================================================= */
    const startBtn = document.getElementById("start-btn");
    const maybeLaterBtn = document.getElementById("maybe-later-btn");
    const cuteModal = document.getElementById("cute-modal");
    const modalProceedBtn = document.getElementById("modal-proceed-btn");

    startBtn.addEventListener("click", () => {
      if (!musicPlayer.isPlaying) {
        musicPlayer.start();
        audioBtn.classList.add("playing");
        const mt = document.getElementById("music-text"); if (mt) mt.textContent = "Playing";
        const mi = document.getElementById("music-icon"); if (mi) mi.textContent = "🎶";
      }
      showScreen("birthday");
    });

    maybeLaterBtn.addEventListener("click", () => {
      cuteModal.classList.add("show");
    });

    modalProceedBtn.addEventListener("click", () => {
      cuteModal.classList.remove("show");
      if (!musicPlayer.isPlaying) {
        musicPlayer.start();
        audioBtn.classList.add("playing");
        const mt = document.getElementById("music-text"); if (mt) mt.textContent = "Playing";
        const mi = document.getElementById("music-icon"); if (mi) mi.textContent = "🎶";
      }
      showScreen("birthday");
    });

    /* =========================================================================
       SCREEN 2 LOGIC: BIRTHDAY DOG & CONFETTI
       ========================================================================= */
    document.getElementById("bday-heading").textContent = `Happy Birthday, ${CONFIG.name}!`;

    const dogImgSit = document.getElementById("dog-img-sit");
    const dogImgJump = document.getElementById("dog-img-jump");
    if (dogImgSit) dogImgSit.src = DOG_SIT_B64;
    if (dogImgJump) dogImgJump.src = DOG_JUMP_B64;

    const dogStage = document.getElementById("dog-stage");
    const dogActor = document.getElementById("dog-actor");
    const dogBubble = document.getElementById("dog-bubble");

    if (dogStage) {
      dogStage.addEventListener("click", () => {
        dogActor.classList.remove("tap-bounce");
        void dogActor.offsetWidth;
        dogActor.classList.add("tap-bounce");

        dogBubble.classList.add("show");
        setTimeout(() => {
          dogBubble.classList.remove("show");
        }, 2200);

        triggerConfettiExplosion();
      });
    }

    const openWishBtn = document.getElementById("open-wish-btn");
    openWishBtn.addEventListener("click", () => {
      showScreen("scratch");
    });

    const confettiCanvas = document.getElementById("confetti-canvas");
    const confettiCtx = confettiCanvas.getContext("2d");
    let confettiPieces = [];
    let confettiActive = false;

    function resizeConfetti() {
      const parent = confettiCanvas.parentElement;
      if (parent) {
        confettiCanvas.width = parent.clientWidth;
        confettiCanvas.height = parent.clientHeight;
      }
    }

    class ConfettiPiece {
      constructor() {
        this.reset();
      }

      reset() {
        this.x = confettiCanvas.width * 0.5 + (Math.random() - 0.5) * 60;
        this.y = confettiCanvas.height * 0.6;
        this.vx = (Math.random() - 0.5) * 12;
        this.vy = -(Math.random() * 12 + 6);
        this.gravity = 0.35;
        this.size = Math.random() * 8 + 6;
        this.rotation = Math.random() * Math.PI * 2;
        this.rotSpeed = (Math.random() - 0.5) * 0.2;
        this.colors = ["#ff6fa5", "#c65bd6", "#d9a441", "#fbe3a1", "#8a3bf2", "#ffffff"];
        this.color = this.colors[Math.floor(Math.random() * this.colors.length)];
        this.alpha = 1;
      }

      update() {
        this.x += this.vx;
        this.y += this.vy;
        this.vy += this.gravity;
        this.rotation += this.rotSpeed;
        if (this.vy > 0) {
          this.alpha -= 0.009;
        }
      }

      draw(ctx) {
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(this.rotation);
        ctx.globalAlpha = Math.max(0, this.alpha);
        ctx.fillStyle = this.color;
        ctx.fillRect(-this.size / 2, -this.size / 2, this.size, this.size * 0.6);
        ctx.restore();
      }
    }

    function triggerConfettiExplosion() {
      resizeConfetti();
      confettiPieces = [];
      for (let i = 0; i < 90; i++) {
        confettiPieces.push(new ConfettiPiece());
      }
      confettiActive = true;
      runConfetti();
    }

    function runConfetti() {
      if (!confettiActive) return;
      confettiCtx.clearRect(0, 0, confettiCanvas.width, confettiCanvas.height);
      let alive = false;
      for (const p of confettiPieces) {
        p.update();
        if (p.alpha > 0 && p.y < confettiCanvas.height + 50) {
          p.draw(confettiCtx);
          alive = true;
        }
      }
      if (alive) {
        requestAnimationFrame(runConfetti);
      } else {
        confettiActive = false;
        confettiCtx.clearRect(0, 0, confettiCanvas.width, confettiCanvas.height);
      }
    }

    /* =========================================================================
       SCREEN 3 LOGIC: SCRATCH CARDS
       ========================================================================= */
    const scratchContainer = document.getElementById("scratch-cards-wrap");
    const progressFillBar = document.getElementById("progress-fill-bar");
    const revealedCountDisplay = document.getElementById("revealed-count-display");
    const scratchNextBtn = document.getElementById("scratch-next-btn");
    let scratchInitialized = false;

    function initScratchCards() {
      if (scratchInitialized) return;
      scratchInitialized = true;
      scratchContainer.innerHTML = "";
      revealedCount = 0;
      updateScratchProgress();

      CONFIG.scratchMessages.forEach((msg, index) => {
        const card = document.createElement("div");
        card.className = "scratch-card";
        card.dataset.index = index;

        const secret = document.createElement("div");
        secret.className = "scratch-secret";
        secret.innerHTML = `
          <div class="secret-badge">
            <span>✦</span> Note #${index + 1}
          </div>
          <p class="secret-message">"${msg}"</p>
          <div class="secret-sparkle">🌸✨</div>
        `;
        card.appendChild(secret);

        const canvas = document.createElement("canvas");
        canvas.className = "scratch-canvas";
        card.appendChild(canvas);
        scratchContainer.appendChild(card);

        setTimeout(() => setupCanvasScratchLayer(canvas, card, index), 50);
      });
    }

    function setupCanvasScratchLayer(canvas, card, index) {
      const rect = card.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      const w = rect.width;
      const h = rect.height;

      canvas.width = w * dpr;
      canvas.height = h * dpr;
      const ctx = canvas.getContext("2d");
      ctx.scale(dpr, dpr);

      const grad = ctx.createLinearGradient(0, 0, w, h);
      grad.addColorStop(0, "#fbe3a1");
      grad.addColorStop(0.3, "#ff9ebd");
      grad.addColorStop(0.65, "#d8a8f0");
      grad.addColorStop(1, "#d9a441");

      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, w, h);

      ctx.fillStyle = "rgba(255, 255, 255, 0.4)";
      for (let i = 0; i < 35; i++) {
        const sx = Math.random() * w;
        const sy = Math.random() * h;
        const sr = Math.random() * 2 + 1;
        ctx.beginPath();
        ctx.arc(sx, sy, sr, 0, Math.PI * 2);
        ctx.fill();
      }

      ctx.fillStyle = "#ffffff";
      ctx.font = "bold 15px 'Plus Jakarta Sans', sans-serif";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.shadowColor = "rgba(90, 39, 80, 0.35)";
      ctx.shadowBlur = 6;
      ctx.fillText("✦ Scratch to reveal ✦", w / 2, h / 2);
      ctx.shadowBlur = 0;

      let isScratching = false;
      let lastPoint = null;
      let strokeCount = 0;
      let isCardRevealed = false;

      function getPos(e) {
        const cRect = canvas.getBoundingClientRect();
        return {
          x: e.clientX - cRect.left,
          y: e.clientY - cRect.top
        };
      }

      function scratchAt(pos) {
        ctx.globalCompositeOperation = "destination-out";
        ctx.beginPath();
        ctx.arc(pos.x, pos.y, 22, 0, Math.PI * 2);
        ctx.fill();

        if (lastPoint) {
          ctx.lineWidth = 44;
          ctx.lineCap = "round";
          ctx.lineJoin = "round";
          ctx.beginPath();
          ctx.moveTo(lastPoint.x, lastPoint.y);
          ctx.lineTo(pos.x, pos.y);
          ctx.stroke();
        }
      }

      function checkRevealThreshold() {
        if (isCardRevealed) return;
        strokeCount++;
        if (strokeCount % 12 === 0) {
          try {
            const imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
            const data = imgData.data;
            let transparentPixels = 0;
            const totalSamples = 1000;
            const step = Math.max(1, Math.floor(data.length / (totalSamples * 4)));

            for (let i = 3; i < data.length; i += step * 4) {
              if (data[i] < 128) {
                transparentPixels++;
              }
            }

            const ratio = transparentPixels / totalSamples;
            if (ratio >= 0.28) {
              isCardRevealed = true;
              card.classList.add("revealed");
              revealedCount++;
              updateScratchProgress();
            }
          } catch (err) {
            if (strokeCount > 45) {
              isCardRevealed = true;
              card.classList.add("revealed");
              revealedCount++;
              updateScratchProgress();
            }
          }
        }
      }

      canvas.addEventListener("pointerdown", (e) => {
        if (isCardRevealed) return;
        isScratching = true;
        canvas.setPointerCapture(e.pointerId);
        lastPoint = getPos(e);
        scratchAt(lastPoint);
      });

      canvas.addEventListener("pointermove", (e) => {
        if (!isScratching || isCardRevealed) return;
        const currentPos = getPos(e);
        scratchAt(currentPos);
        lastPoint = currentPos;
        checkRevealThreshold();
      });

      const stopScratch = (e) => {
        if (!isScratching) return;
        isScratching = false;
        lastPoint = null;
        if (e.pointerId) {
          try { canvas.releasePointerCapture(e.pointerId); } catch(ex){}
        }
      };

      canvas.addEventListener("pointerup", stopScratch);
      canvas.addEventListener("pointercancel", stopScratch);
    }

    function updateScratchProgress() {
      const percentage = (revealedCount / TOTAL_SCRATCH_CARDS) * 100;
      progressFillBar.style.width = `${percentage}%`;
      revealedCountDisplay.textContent = `${revealedCount} / ${TOTAL_SCRATCH_CARDS} revealed`;

      if (revealedCount >= TOTAL_SCRATCH_CARDS) {
        scratchNextBtn.disabled = false;
        scratchNextBtn.classList.add("pulse-glow");
      }
    }

    scratchNextBtn.addEventListener("click", () => {
      showScreen("letter");
    });

    /* =========================================================================
       SCREEN 4 LOGIC: ENVELOPE & HUMANOID LETTER
       ========================================================================= */
    const envelopeWrapper = document.getElementById("envelope-wrapper");
    const envelopeBox = document.getElementById("envelope-box");
    const envelopeHint = document.getElementById("envelope-hint");
    const letterPaper = document.getElementById("letter-paper");
    const letterTextContainer = document.getElementById("letter-text-container");
    const letterSignature = document.getElementById("letter-signature");
    const senderNameDisplay = document.getElementById("sender-name-display");
    const toMemoriesBtn = document.getElementById("to-memories-btn");
    const skipTypingBtn = document.getElementById("skip-typing-btn");

    senderNameDisplay.textContent = CONFIG.sender;

    let envelopeOpened = false;

    envelopeBox.addEventListener("click", () => {
      if (envelopeOpened) return;
      envelopeOpened = true;

      envelopeBox.classList.add("opened");
      envelopeHint.style.display = "none";

      setTimeout(() => {
        letterPaper.style.display = "block";
        envelopeWrapper.style.display = "none";
        startTypewriter();
      }, 700);
    });

    function startTypewriter() {
      if (isTypingLetter) return;
      isTypingLetter = true;
      letterTextContainer.innerHTML = "";
      
      const fullText = CONFIG.letterText;
      let charIndex = 0;

      const cursor = document.createElement("span");
      cursor.className = "typing-cursor";
      letterTextContainer.appendChild(cursor);

      function typeNext() {
        if (charIndex < fullText.length) {
          const char = fullText.charAt(charIndex);
          if (char === "\\n") {
            cursor.insertAdjacentHTML("beforebegin", "<br>");
          } else {
            cursor.insertAdjacentText("beforebegin", char);
          }
          charIndex++;
          typingTimer = setTimeout(typeNext, 40);
        } else {
          cursor.remove();
          letterSignature.classList.add("visible");
          toMemoriesBtn.style.display = "inline-flex";
          skipTypingBtn.style.display = "none";
          isTypingLetter = false;
        }
      }

      typeNext();
    }

    skipTypingBtn.addEventListener("click", () => {
      if (!isTypingLetter) return;
      clearTimeout(typingTimer);
      isTypingLetter = false;
      const formatted = CONFIG.letterText.replace(/\\n/g, "<br>");
      letterTextContainer.innerHTML = formatted;
      letterSignature.classList.add("visible");
      toMemoriesBtn.style.display = "inline-flex";
      skipTypingBtn.style.display = "none";
    });

    toMemoriesBtn.addEventListener("click", () => {
      showScreen("memories");
    });

    /* =========================================================================
       SCREEN 5 LOGIC: CORE MEMORIES
       ========================================================================= */
    const memoriesContainer = document.getElementById("memories-container");
    const globalPhotoInput = document.getElementById("global-photo-input");
    const toCloudsBtn = document.getElementById("to-clouds-btn");

    function renderMemories() {
      memoriesContainer.innerHTML = "";
      CONFIG.memories.forEach((mem, idx) => {
        const polaroid = document.createElement("div");
        polaroid.className = "polaroid-card";
        polaroid.style.transform = `rotate(${mem.rotation || (idx % 2 === 0 ? -2 : 2)}deg)`;

        polaroid.innerHTML = `
          <div class="washi-tape"></div>
          <div class="photo-frame">
            <img class="photo-img" alt="${mem.title}">
            <div class="photo-placeholder">
              <div class="placeholder-emoji">${mem.emoji}</div>
              <div class="upload-prompt">📷 Tap to add photo</div>
            </div>
          </div>
          <div class="polaroid-caption">
            <div class="polaroid-title">${mem.title}</div>
            <div class="polaroid-desc">${mem.caption}</div>
          </div>
        `;

        const photoFrame = polaroid.querySelector(".photo-frame");
        photoFrame.addEventListener("click", () => {
          activePolaroidPhotoEl = polaroid;
          globalPhotoInput.click();
        });

        memoriesContainer.appendChild(polaroid);
      });
    }
    renderMemories();

    globalPhotoInput.addEventListener("change", (e) => {
      const file = e.target.files[0];
      if (!file || !activePolaroidPhotoEl) return;

      const reader = new FileReader();
      reader.onload = (event) => {
        const img = activePolaroidPhotoEl.querySelector(".photo-img");
        const placeholder = activePolaroidPhotoEl.querySelector(".photo-placeholder");
        if (img && placeholder) {
          img.src = event.target.result;
          img.style.display = "block";
          placeholder.style.display = "none";
        }
      };
      reader.readAsDataURL(file);
      e.target.value = "";
    });

    // Advance to Screen 6: Clouds
    toCloudsBtn.addEventListener("click", () => {
      showScreen("clouds");
    });

    /* =========================================================================
       SCREEN 6 LOGIC: 5 CLOUDS SCREEN (BOLLYWOOD KK SONG & 3-4 WORD IMAGES)
       ========================================================================= */
    const cloudsList = document.getElementById("clouds-list");
    const cloudsOpenedCountEl = document.getElementById("clouds-opened-count");
    const cloudsFinaleCard = document.getElementById("clouds-finale-card");
    const replayAllBtn = document.getElementById("replay-all-btn");
    let cloudsInitialized = false;

    function initCloudsScreen() {
      if (cloudsInitialized) return;
      cloudsInitialized = true;
      cloudsList.innerHTML = "";
      openedCloudsCount = 0;
      cloudsOpenedCountEl.textContent = `0 / ${CONFIG.clouds.length} clouds opened`;
      cloudsFinaleCard.style.display = "none";

      CONFIG.clouds.forEach((cloudData) => {
        const card = document.createElement("div");
        card.className = "cloud-card";
        card.dataset.id = cloudData.id;

        card.innerHTML = `
          <div class="cloud-top-row">
            <span class="cloud-number-pill">☁️ ${cloudData.badge}</span>
            <span class="cloud-tap-hint">✦ Tap to open ✦</span>
          </div>
          
          <!-- Unopened view -->
          <div class="cloud-unopened-view">
            <div class="cloud-puffy-icon">☁️</div>
            <div class="cloud-unopened-title">${cloudData.unopenedHint}</div>
          </div>

          <!-- Opened view: 3-4 Word Image Sentiment -->
          <div class="cloud-opened-view">
            <div class="cloud-opened-sticker">${cloudData.emoji}</div>
            <h3 class="cloud-words-title">${cloudData.words}</h3>
            <p class="cloud-subnote">"${cloudData.subnote}"</p>
          </div>
        `;

        card.addEventListener("click", () => {
          if (!card.classList.contains("opened")) {
            card.classList.add("opened");
            openedCloudsCount++;
            cloudsOpenedCountEl.textContent = `${openedCloudsCount} / ${CONFIG.clouds.length} clouds opened`;
            triggerConfettiExplosion();

            if (openedCloudsCount >= CONFIG.clouds.length) {
              setTimeout(() => {
                cloudsFinaleCard.style.display = "block";
                cloudsFinaleCard.scrollIntoView({ behavior: "smooth", block: "start" });
              }, 400);
            }
          }
        });

        cloudsList.appendChild(card);
      });
    }

    // Replay from beginning
    replayAllBtn.addEventListener("click", () => {
      revealedCount = 0;
      scratchInitialized = false;
      envelopeOpened = false;
      isTypingLetter = false;
      cloudsInitialized = false;
      openedCloudsCount = 0;
      if (typingTimer) clearTimeout(typingTimer);

      envelopeBox.classList.remove("opened");
      envelopeHint.style.display = "flex";
      letterPaper.style.display = "none";
      envelopeWrapper.style.display = "block";
      letterSignature.classList.remove("visible");
      toMemoriesBtn.style.display = "none";
      skipTypingBtn.style.display = "inline-block";

      musicPlayer.start("musicbox");
      const mt = document.getElementById("music-text"); if (mt) mt.textContent = "Music";

      showScreen("start");
    });
  </script>
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("SUCCESS: index.html has been completely written with all 6 screens and KK Bollywood song!")
