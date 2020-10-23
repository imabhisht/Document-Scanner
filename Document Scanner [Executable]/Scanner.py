import subprocess
print("\nDocument Scanner made using OpenCV and Python.\n")
print("Developed by Abhisht\n")
temp = input("\n\nStart the Application?[Y/N]: ")
temp = temp.capitalize()
subprocess.call(["Document-Scanner\\Scanner.exe"]) if temp == "Y" else None

