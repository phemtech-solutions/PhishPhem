import re
import tldextract

def check_suspicious_links(body):
    # List of common URL shorteners
    shorteners = ['bit\.ly', 'tinyurl\.com', 't\.co', 'ow\.ly', 'rb\.gy', 'buff\.ly']
    shortener_pattern = "|".join(shorteners)

    # Match shortened URLs or IP-based links
    suspicious = re.findall(
        rf'https?://(?:{shortener_pattern}|(?:\d{{1,3}}\.){{3}}\d{{1,3}})',
        body
    )
    return suspicious

def check_urgency_phrases(body):
    phrases = [
        "urgent", "immediate action", "verify your account", "account suspended",
        "click here", "security alert", "your account has been locked"
    ]
    found = [p for p in phrases if p.lower() in body.lower()]
    return found

def check_mismatched_domain(from_header, links):
    from_domain = tldextract.extract(from_header).registered_domain
    mismatches = []
    for url in links:
        url_domain = tldextract.extract(url).registered_domain
        if url_domain and from_domain and url_domain != from_domain:
            mismatches.append(url)
    return mismatches

def run_rule_checks(email_body, from_header):
    suspicious_links = check_suspicious_links(email_body)
    urgency_flags = check_urgency_phrases(email_body)
    domain_mismatches = check_mismatched_domain(from_header, suspicious_links)

    return {
        "suspicious_links": suspicious_links,
        "urgency_phrases": urgency_flags,
        "domain_mismatches": domain_mismatches,
        "total_flags": len(suspicious_links) + len(urgency_flags) + len(domain_mismatches)
    }
