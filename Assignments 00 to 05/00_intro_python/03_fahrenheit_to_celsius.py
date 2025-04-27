def temperature_conversion():
    BOLD_ITALIC = "\033[1;3m"
    RESET = "\033[0m"
    print(f"\n^^^^^^^^^^{BOLD_ITALIC} Welcome to the Temperature Conversion Program {RESET} ^^^^^^^^^^")
   
   
    fahrenheit = float(input("\nEnter temperature in Fahrenheit: "))

    celsius = (fahrenheit - 32) * 5.0/9.0
    print(f"{BOLD_ITALIC}{fahrenheit} F{RESET} = {celsius:.2f} C")

if __name__ == "__main__":
    temperature_conversion()   