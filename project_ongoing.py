"""
🎮 PROJECT: ONGOING - Python Terminal Version
================================================

A Game Theory RPG demonstrating cognitive biases in decision-making.

This is the ORIGINAL Python implementation that served as the base for 
the web version. Experience the same psychological gameplay mechanics 
in a classic terminal interface with retro ASCII art.

🌐 Web Version: https://trgr-karasutoragara.github.io/project-ongoing/
📁 Repository: https://github.com/trgr-karasutoragara/project-ongoing

Features:
- Classic 1990s terminal RPG experience
- Real-time cognitive bias simulation
- ASCII art and retro formatting
- Educational game theory concepts

Usage:
    python project_ongoing.py

Author: trgr-karasutoragara
License: MIT
"""


import random
import time
import os

class GameTheoryRPG:
    def __init__(self):
        self.player_name = ""
        self.turn = 0
        self.total_investment = 50000  # Starting investment
        self.project_success_chance = 0.7  # Starts optimistic
        self.risk_level = 0.2
        self.team_morale = 0.8
        self.player_reputation = 100
        self.players_left = 4  # NPCs + player
        self.game_over = False
        self.winner = None
        
        # NPCs with different personalities
        self.npcs = {
            "Dr. Sunk": {"reputation": 100, "bias": "sunk_cost", "active": True},
            "Manager Defer": {"reputation": 100, "bias": "responsibility_avoid", "active": True},
            "Prof. Frame": {"reputation": 100, "bias": "framing", "active": True}
        }
        
        self.story_log = []

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_ascii_art(self):
        art = """
╔══════════════════════════════════════════════════════════════╗
║  ____  ____   ___     _ _____ ____ _____   ___  _   _  ____  ║
║ |  _ \|  _ \ / _ \   | | ____/ ___|_   _| / _ \| \ | |/ ___| ║
║ | |_) | |_) | | | |_ | |  _|| |     | |  | | | |  \| | |  _  ║
║ |  __/|  _ <| |_| | |_| | |__| |___  | |  | |_| | |\  | |_| | ║
║ |_|   |_| \_\\___/ \___/|_____\____| |_|   \___/|_| \_|\____| ║
║                                                              ║
║           ⚠️  ONGOING: A Game Theory Adventure ⚠️            ║
╚══════════════════════════════════════════════════════════════╝
        """
        print(art)

    def print_status(self):
        print("=" * 60)
        print(f"🎯 PROJECT STATUS - TURN {self.turn}")
        print("=" * 60)
        print(f"💰 Total Investment: ${self.total_investment:,}")
        print(f"📈 Success Chance: {self.project_success_chance:.1%}")
        print(f"⚠️  Risk Level: {self.risk_level:.1%}")
        print(f"👥 Team Morale: {self.team_morale:.1%}")
        print(f"⭐ Your Reputation: {self.player_reputation}")
        print(f"👤 Players Remaining: {self.players_left}")
        print("-" * 60)

    def get_narrative_frame(self):
        """Generate biased narrative framing"""
        frames = [
            "We're so close to a breakthrough! The data shows promise...",
            "Canceling now would waste all our progress so far.",
            "The market conditions are finally aligning in our favor.",
            "Our competitors are struggling - this is our chance!",
            "The team has worked so hard, we can't let them down now.",
            "Just one more investment round and we'll turn the corner."
        ]
        return random.choice(frames)

    def print_story_beat(self, text):
        print(f"\n📖 {text}")
        time.sleep(1.5)

    def setup_game(self):
        self.clear_screen()
        self.print_ascii_art()
        print("\n🎮 Welcome to PROJECT: ONGOING")
        print("A game about the hidden costs of 'rational' decisions...\n")
        
        self.player_name = input("Enter your character name: ").strip()
        if not self.player_name:
            self.player_name = "Player"
            
        print(f"\nWelcome, {self.player_name}!")
        print("\n" + "="*60)
        print("🎯 THE SETUP:")
        print("="*60)
        print("You're part of a research team working on Project Phoenix.")
        print("Your goal: Achieve success and maintain your reputation.")
        print("The catch: Anyone can stop the project, but...")
        print("→ Stopping makes YOU the 'quitter' (reputation damage)")
        print("→ Continuing increases costs and risks")
        print("→ Passing responsibility doubles the risk but protects you")
        print("\nThe last person standing wins... or loses everything.")
        input("\nPress Enter to begin...")

    def npc_decision(self, npc_name, npc_data):
        """AI decision making based on NPC bias"""
        if not npc_data["active"]:
            return None
            
        bias = npc_data["bias"]
        reputation = npc_data["reputation"]
        
        # Calculate decision weights based on bias
        if bias == "sunk_cost":
            # Dr. Sunk hates wasting investment
            continue_weight = min(0.8, self.total_investment / 100000)
            stop_weight = 0.1
            defer_weight = 0.1
        elif bias == "responsibility_avoid":
            # Manager Defer avoids being the one to stop
            continue_weight = 0.3
            stop_weight = 0.1
            defer_weight = 0.6
        elif bias == "framing":
            # Prof. Frame is swayed by positive narratives
            continue_weight = 0.6 if self.project_success_chance > 0.3 else 0.2
            stop_weight = 0.2
            defer_weight = 0.2
        
        # Add randomness
        roll = random.random()
        if roll < continue_weight:
            return "continue"
        elif roll < continue_weight + stop_weight:
            return "stop"
        else:
            return "defer"

    def execute_npc_turn(self, npc_name, npc_data):
        if not npc_data["active"]:
            return True
            
        decision = self.npc_decision(npc_name, npc_data)
        
        if decision == "stop":
            print(f"\n💥 {npc_name} says: 'I think we should stop this project.'")
            print(f"💔 {npc_name} takes a reputation hit but ends the madness!")
            npc_data["reputation"] -= 30
            npc_data["active"] = False
            self.players_left -= 1
            return False
        elif decision == "continue":
            print(f"\n✅ {npc_name} says: 'We must continue! We're so close!'")
            return True
        else:  # defer
            print(f"\n🔄 {npc_name} says: 'I'll go with whatever the team decides.'")
            self.risk_level *= 1.5  # Responsibility diffusion increases risk
            return True

    def player_turn(self):
        self.clear_screen()
        self.print_status()
        
        # Show narrative framing
        narrative = self.get_narrative_frame()
        print(f"\n💭 Current Narrative: '{narrative}'")
        
        print(f"\n🎲 {self.player_name}'s Turn:")
        print("What do you choose?")
        print("\n1. 🟢 CONTINUE - Invest more and push forward")
        print("2. 🔴 STOP - Be the one to end this project")
        print("3. 🟡 DEFER - Pass the decision to others")
        
        while True:
            choice = input("\nEnter your choice (1-3): ").strip()
            if choice in ['1', '2', '3']:
                break
            print("Please enter 1, 2, or 3")
        
        return choice

    def process_player_decision(self, choice):
        if choice == '1':  # Continue
            investment_increase = random.randint(10000, 30000)
            self.total_investment += investment_increase
            self.project_success_chance -= 0.05  # Diminishing returns
            self.risk_level += 0.1
            
            print(f"\n✅ You decide to continue!")
            print(f"💰 Additional investment: ${investment_increase:,}")
            print(f"📉 Success chance decreased due to complexity...")
            
            return True
            
        elif choice == '2':  # Stop
            print(f"\n🛑 You decide to stop the project!")
            print(f"💔 You take the blame but save everyone from disaster.")
            self.player_reputation -= 40
            self.game_over = True
            self.winner = "rationality"
            return False
            
        else:  # Defer
            print(f"\n🔄 You defer the decision to others.")
            print(f"⚠️ Risk level increases due to diffused responsibility!")
            self.risk_level *= 1.3
            self.player_reputation -= 5  # Small hit for not leading
            return True

    def check_disaster(self):
        """Check if the project has catastrophically failed"""
        disaster_chance = self.risk_level * (1 - self.project_success_chance)
        
        if disaster_chance > 0.8 or self.total_investment > 500000:
            print("\n" + "💥" * 20)
            print("🚨 CATASTROPHIC FAILURE! 🚨")
            print("💥" * 20)
            print(f"💸 Total loss: ${self.total_investment:,}")
            print(f"💀 Project Phoenix has crashed and burned!")
            print(f"🎭 Everyone loses reputation and careers are ruined!")
            
            # Everyone loses
            self.player_reputation = 0
            for npc in self.npcs.values():
                npc["reputation"] = 0
                
            self.game_over = True
            self.winner = "disaster"
            return True
        return False

    def update_game_state(self):
        """Update various game parameters each turn"""
        self.turn += 1
        
        # Team morale decreases over time
        self.team_morale -= 0.05
        
        # Market conditions change
        market_change = random.uniform(-0.1, 0.05)
        self.project_success_chance += market_change
        self.project_success_chance = max(0.1, min(0.9, self.project_success_chance))

    def play_turn(self):
        """Execute one complete turn"""
        self.update_game_state()
        
        # Player turn
        choice = self.player_turn()
        if not self.process_player_decision(choice):
            return False
            
        if self.check_disaster():
            return False
        
        # NPC turns
        active_npcs = [(name, data) for name, data in self.npcs.items() if data["active"]]
        
        for npc_name, npc_data in active_npcs:
            if not self.execute_npc_turn(npc_name, npc_data):
                return False
            if self.check_disaster():
                return False
            time.sleep(1)
        
        # Check if only player left
        if self.players_left <= 1:
            print(f"\n🏆 {self.player_name} is the last one standing!")
            print(f"🎭 But at what cost? You're trapped in the project alone!")
            self.game_over = True
            self.winner = "pyrrhic"
            return False
            
        return True

    def show_ending(self):
        self.clear_screen()
        print("\n" + "🎬" * 20)
        print(" GAME OVER - FINAL ANALYSIS ")
        print("🎬" * 20)
        
        if self.winner == "rationality":
            print(f"\n🎯 {self.player_name} chose RATIONALITY!")
            print(f"💡 You stopped the madness before disaster struck.")
            print(f"💔 Reputation hit: {100 - self.player_reputation} points")
            print(f"🏆 But you saved ${self.total_investment:,} from being lost!")
            print(f"\n📚 LESSON: Sometimes being 'the bad guy' is the right choice.")
            
        elif self.winner == "disaster":
            print(f"\n💥 TOTAL SYSTEM FAILURE!")
            print(f"💸 Everyone lost everything: ${self.total_investment:,}")
            print(f"🎭 All reputations destroyed by collective blindness.")
            print(f"\n📚 LESSON: When everyone avoids responsibility, disaster follows.")
            
        elif self.winner == "pyrrhic":
            print(f"\n🏆 {self.player_name} 'won' by outlasting everyone!")
            print(f"😱 But you're now trapped in an unstoppable project.")
            print(f"💰 Investment: ${self.total_investment:,}")
            print(f"📉 Success chance: {self.project_success_chance:.1%}")
            print(f"\n📚 LESSON: Being the last rational person can be its own prison.")
        
        print(f"\n" + "="*60)
        print("🧠 COGNITIVE BIASES DEMONSTRATED:")
        print("="*60)
        print("🔹 Sunk Cost Fallacy - 'We've invested too much to quit now'")
        print("🔹 Responsibility Diffusion - 'Someone else will decide'")
        print("🔹 Framing Effects - 'We're so close to success!'")
        print("🔹 Groupthink - 'Nobody wants to be the quitter'")
        print("🔹 Loss Aversion - 'Stopping feels like admitting failure'")
        
        print(f"\n🎯 Final Scores:")
        print(f"   {self.player_name}: {self.player_reputation} reputation")
        for name, data in self.npcs.items():
            print(f"   {name}: {data['reputation']} reputation")

    def run(self):
        """Main game loop"""
        self.setup_game()
        
        while not self.game_over and self.turn < 20:  # Max 20 turns
            if not self.play_turn():
                break
        
        if not self.game_over:
            print(f"\n⏰ Time limit reached! The project continues indefinitely...")
            self.winner = "stalemate"
        
        self.show_ending()
        
        print(f"\n🎮 Thanks for playing PROJECT: ONGOING!")
        print(f"💭 Remember: The most rational choice often feels the most irrational.")

def main():
    """Run the game"""
    game = GameTheoryRPG()
    game.run()

if __name__ == "__main__":
    main()