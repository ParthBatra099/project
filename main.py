"""
AI-Powered Dungeon RPG Game - PRODUCTION VERSION
Main entry point with enhanced AI integration and story memory.
"""

import sys
from game_engine import GameEngine


def main():
    """
    Main entry point for the RPG game.
    Initializes the game engine and starts the game loop.
    """
    try:
        print("\n" + "=" * 70)
        print("🎮 THE FORGOTTEN WARLORD: DUNGEON RPG 🎮".center(70))
        print("=" * 70)
        print("\n📖 OPENING SCENE:\n")
        print("   Your eyes flutter open. Golden light filters through cracks")
        print("   in what appears to be ancient stone. Your body aches—but not")
        print("   from injury. This ache runs deeper: the echo of a sealed power.\n")
        print("   You were a warlord once. That life is hazy now, like a dream.")
        print("   But your combat instincts remain. Your will remains.\n")
        print("   A mysterious road stretches before you. The air crackles with")
        print("   an unfamiliar magic. Strange runes glow faintly on your wrist.\n")
        print("   Your adventure begins NOW.\n")
        print("=" * 70 + "\n")
        
        game = GameEngine()
        game.initialize_player()
        game.start_game()
        
    except KeyboardInterrupt:
        print("\n\n[Game terminated by player]")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Critical Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
