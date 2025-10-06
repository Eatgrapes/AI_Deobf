import Config
import AI

def run_initialization():
    print("--- AI Deobfuscator Initialization ---")
    print("Please select your AI service:")
    print("1. DeepSeek")
    print("2. Gemini")
    print("3. ChatGPT")
    
    service_choice = input("Enter your choice (1, 2, or 3): ")
    
    ai_service = ""
    if service_choice == '1':
        ai_service = "DeepSeek"
    elif service_choice == '2':
        ai_service = "Gemini"
    elif service_choice == '3':
        ai_service = "ChatGPT"
    else:
        print("Invalid choice. Exiting.")
        return

    api_key = input(f"Enter your API key for {ai_service}: ")

    if AI.validate_api_key(ai_service, api_key):
        config_data = {
            "ai_service": ai_service,
            "api_key": api_key
        }
        Config.save_config(config_data)
        print("\nInitialization complete. You can now run Main.py.")
    else:
        print("\nAPI Key validation failed. Please check your key and try again.")

if __name__ == "__main__":
    run_initialization()