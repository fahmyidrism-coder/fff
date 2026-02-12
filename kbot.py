import os
import sys
import time
import json
import uuid
from datetime import datetime, timedelta
from getpass import getpass
import random
import string

class LicenseManager:
    def __init__(self):
        self.licenses = {}
    
    def generate_license_key(self):
        """Generate a unique license key"""
        return str(uuid.uuid4()).replace('-', '')[:32]
    
    def generate_expiry_date(self, days=120):
        """Generate expiry date"""
        expiry = datetime.now() + timedelta(days=days)
        return expiry.strftime("%d %b %Y")
    
    def create_license(self, username):
        """Create a new license for a user"""
        return {
            "version": "50d66e5",
            "username": username,
            "license_key": self.generate_license_key(),
            "expired_at": self.generate_expiry_date(days=120),
            "selected": "Whosfan"
        }

class KBOTApplication:
    def __init__(self):
        self.license_manager = LicenseManager()
        self.current_user = None
        self.current_license = None
        self.accounts = []
        self.is_running = True
    
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_box(self, title, data):
        """Print a formatted box with data"""
        width = 75
        print("\n" + "─" * width)
        print(title.center(width))
        print("─" * width)
        for key, value in data.items():
            label = key.replace("_", " ").title()
            line = f"{label:<20}: {str(value)}"
            print(line)
        print("─" * width + "\n")
    
    def main_menu(self):
        """Display main menu"""
        self.clear_screen()
        print("\n" + "=" * 75)
        print("KBOT MAIN MENU".center(75))
        print("=" * 75)
        print("1. Login / Create Account")
        print("2. View All Accounts")
        print("3. Exit")
        print("=" * 75)
        return input("\nEnter your choice: ").strip()
    
    def login_menu(self):
        """Handle login"""
        self.clear_screen()
        print("\n" + "=" * 75)
        print("LOGIN / CREATE ACCOUNT".center(75))
        print("=" * 75)
        
        username = input("Enter username: ").strip()
        
        # Create new account with license
        self.current_license = self.license_manager.create_license(username)
        self.current_user = username
        
        # Add to accounts list if new
        if username not in [acc.get("username") for acc in self.accounts]:
            self.accounts.append(self.current_license.copy())
        
        self.display_license_info()
        self.whosfan_menu()
    
    def display_license_info(self):
        """Display license information"""
        self.clear_screen()
        print("\n" + "▓" * 75)
        print("KBOT APPLICATION".center(75))
        print("▓" * 75)
        print(f"{'Version':<20}: {self.current_license['version']}")
        print(f"{'Username':<20}: {self.current_license['username']}")
        print(f"{'License Key':<20}: {self.current_license['license_key']}")
        print(f"{'Expired At':<20}: {self.current_license['expired_at']}")
        print(f"{'Selected':<20}: {self.current_license['selected']}")
        print("▓" * 75 + "\n")
    
    def whosfan_menu(self):
        """Display Whosfan menu"""
        while True:
            print("─" * 75)
            print("WHOSFAN MENU".center(75))
            print("─" * 75)
            print("1. Watch Ads")
            print("2. Check Balance")
            print("0. Back to Main Menu")
            print("─" * 75)
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == "1":
                self.watch_ads()
            elif choice == "2":
                self.check_balance()
            elif choice == "0":
                break
            else:
                print("\n✗ Invalid choice. Please try again.")
                time.sleep(1)
    
    def watch_ads(self):
        """Watch ads action"""
        print("\n")
        email = f"{self.current_user}@gmail.com"
        print(f"{email}")
        print("  ✓ Watch ads claimed successfully!")
        print("  ⏳ Waiting for 299 seconds before continuing to the next account...")
        
        # Simulate countdown
        for i in range(5, 0, -1):
            print(f"  [{i}] Waiting...", end="\r")
            time.sleep(0.5)
        print("\n")
        time.sleep(1)
    
    def check_balance(self):
        """Check balance action"""
        print("\n")
        print(f"  Checking balance for {self.current_user}...")
        balance = round(random.uniform(10, 500), 2)
        print(f"  💰 Current Balance: ${balance}")
        print("\n")
        input("  Press Enter to continue...")
    
    def view_all_accounts(self):
        """View all created accounts"""
        self.clear_screen()
        print("\n" + "=" * 75)
        print("ALL ACCOUNTS".center(75))
        print("=" * 75)
        
        if not self.accounts:
            print("\nNo accounts created yet.\n")
        else:
            for i, account in enumerate(self.accounts, 1):
                print(f"\n{i}. Account: {account['username']}")
                print(f"   License Key: {account['license_key']}")
                print(f"   Expires: {account['expired_at']}")
        
        print("\n" + "=" * 75)
        input("\nPress Enter to continue...")
    
    def run(self):
        """Run the application"""
        while self.is_running:
            choice = self.main_menu()
            
            if choice == "1":
                self.login_menu()
            elif choice == "2":
                self.view_all_accounts()
            elif choice == "3":
                print("\nExiting KBOT Application...")
                self.is_running = False
                break
            else:
                print("\n✗ Invalid choice. Please try again.")
                time.sleep(1)

if __name__ == "__main__":
    app = KBOTApplication()
    app.run()