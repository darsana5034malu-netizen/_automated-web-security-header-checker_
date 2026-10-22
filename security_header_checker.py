import requests
from datetime import datetime

HEADERS = {
    "Content-Security-Policy":
        "Helps protect against code-injection attacks",
    "Strict-Transport-Security":
        "Encourages secure HTTPS connections",
    "X-Content-Type-Options":
        "Helps prevent MIME-type sniffing",
    "X-Frame-Options":
        "Helps protect against clickjacking",
    "Referrer-Policy":
        "Controls referrer information sent by browsers",
    "Permissions-Policy":
        "Controls access to browser features"
}


def check_website():
    print("=" * 45)
    print("  AUTOMATED WEB SECURITY HEADER CHECKER")
    print("=" * 45)

    url = input("Enter a website URL to check: ").strip()

    if not url.startswith(("https://", "http://")):
        url = "https://" + url

    try:
        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True
        )

        response_headers = response.headers

        present = []
        missing = []

        for header, explanation in HEADERS.items():
            if header.lower() in {
                key.lower() for key in response_headers
            }:
                present.append(header)
            else:
                missing.append(header)

        score = round((len(present) / len(HEADERS)) * 100)

        if score >= 80:
            rating = "Good"
        elif score >= 50:
            rating = "Moderate"
        else:
            rating = "Needs Improvement"

        report = []
        report.append("AUTOMATED WEB SECURITY HEADER REPORT")
        report.append("=" * 40)
        report.append(f"Website: {url}")
        report.append(f"HTTP Status: {response.status_code}")
        report.append(f"Date: {datetime.now()}")
        report.append("")
        report.append(f"Security Score: {score}/100")
        report.append(f"Security Rating: {rating}")
        report.append("")
        report.append("HEADERS PRESENT:")

        for header in present:
            report.append(f"[PRESENT] {header}")

        report.append("")
        report.append("HEADERS MISSING:")

        for header in missing:
            report.append(f"[MISSING] {header}")
            report.append(f"Recommendation: {HEADERS[header]}")

        report.append("")
        report.append("Note: This is a basic security-header check.")
        report.append("It is not a complete security audit.")

        output = "\n".join(report)

        print("\n" + output)

        with open("security_report.txt", "w", encoding="utf-8") as file:
            file.write(output)

        print("\nReport saved as security_report.txt")

    except requests.exceptions.RequestException as error:
        print("\nCould not check the website.")
        print("Error:", error)


if __name__ == "__main__":
    check_website()