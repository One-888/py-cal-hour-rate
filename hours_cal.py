import webbrowser

time_in = input("How long h:mm ?: ")

try:
    h, m = str(time_in).split(":")
    total_time_in_seconds = (int(h) * 3600) + (int(m) * 60)  # + int(s)

    rate_per_hour = input("Enter rate per hour?: $")
    rate_per_second = float(rate_per_hour) / 3600

    result = float(total_time_in_seconds) * float(rate_per_second)
    print()
    print(f"Total: ${round(result,2)}")

except ValueError:
    print("Check format h:mm:ss")

open_page = input("Open bank website (Y/N)?: ")
# then make a url variable
url = "https://www.bank.com"
if open_page.upper() == "Y":
    # then call the default open method described above
    webbrowser.open(url)
