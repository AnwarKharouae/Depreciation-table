import common as c
import Degressif 
import Linear

def run_app():
    print("=" * 40)
    print("   ASSET DEPRECIATION GENERATOR")
    print("=" * 40)

    # Get Asset Name
    asset_name = input("Enter Asset Name : ").strip()

    # Clean filename (replace spaces with underscores)
    filename = f"{asset_name.replace(' ', '_')}_Depreciation.xlsx"

    # 2. Choose Method
    print("\nSelect Depreciation Method:")
    print("1. Declining Balance (Dégressif)")
    print("2. Straight Line (Linéaire)")

    choice = input("Enter choice (1 or 2): ").strip()

    # 3. Trigger chosen calculation & export file name
    if choice == "1":
        print(f"\nRunning Declining Balance calculation for '{asset_name}'...")
        Degressif.generate_schedule(filename)
    elif choice == "2":
        print(f"\nRunning Linear calculation for '{asset_name}'...")
        Linear.generate_schedule(filename)
    else :
        print("Invalid choice! Please run again and select 1 or 2.")
        return

    print(f"\nSuccess! File generated: {filename}")


if __name__ == "__main__":
    run_app()