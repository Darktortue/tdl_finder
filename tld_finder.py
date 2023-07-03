import csv
import socket
import concurrent.futures

def check_domain(domain, tld):
    full_domain = f"{domain}.{tld}"
    try:
        socket.gethostbyname(full_domain)
        return full_domain
    except socket.error:
        return None

def check_domains(domain, tlds):
    existing_domains = []
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(check_domain, domain, tld) for tld in tlds]
        
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                existing_domains.append(result)
    
    return existing_domains

def save_to_csv(domains, domain):
    with open(f'existing_domains_{domain}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Domain'])
        for domain in domains:
            writer.writerow([domain])

def main():
    domain = input("Enter the domain name: ")
    tlds = [
        'com', 'net', 'org',  # Most common TLDs
        'dz', 'ao', 'bj', 'bw', 'bf', 'bi', 'cv', 'cm', 'cf', 'td', 'km', 'cg', 'cd', 'dj', 'eg', 'gq', 'er', 'sz', 'et', 'ga', 'gm', 'gh', 'gn', 'gw', 'ci', 'ke', 'ls', 'lr', 'ly', 'mg', 'mw', 'ml', 'mr', 'mu', 'yt', 'ma', 'mz', 'na', 'ne', 'ng', 're', 'rw', 'sh', 'st', 'sn', 'sc', 'sl', 'so', 'za', 'ss', 'sd', 'tz', 'tg', 'tn', 'ug', 'eh', 'zm', 'zw', # African countries
        'us', 'ca', 'mx', 'br', 'ar', 'cl', 'co', 'pe', 've', 'ec', 'gt', 'cu', 'do', 'bo', 'hn', 'py', 'sv', 'cr', 'pr', 'pa', 'uy', 'ni',  # American countries
        'cn', 'jp', 'in', 'bd', 'pk', 'id', 'ir', 'th', 'vn', 'ph', 'tr',  # Asian countries
        'ru', 'kz', 'az', 'kg', 'tj', 'uz', 'tm', 'ge', 'am', 'by', 'ua',  # Eurasian countries
        'co.uk', 'de', 'fr', 'es', 'it', 'nl', 'se', 'pl', 'fi', 'be', 'at', 'ch', 'cz', 'ie', 'ro', 'hu', 'pt', 'gr', 'dk', 'no', 'tr', 'ua', 'rs', 'bg', 'hr', 'lt', 'sk', 'ee', 'si', 'lv', 'is', 'lu', 'mt', 'al', 'mk', 'cy'  # European countries
        'au', 'nz', 'fj', 'pg', 'sb', 'to', 'vu', 'ws', 'ki', 'fm', 'mh', 'nr', 'pw', 'tv',  # Oceanian countries
    ]
    
    existing_domains = check_domains(domain, tlds)
    if existing_domains:
        save_to_csv(existing_domains, domain)
        print(f"Existing domains saved to existing_domains_{domain}.csv")
        print(f"Execution finished. {len(existing_domains)} domains found!")
    else:
        print("FeelsBadMan")
        print("Execution finished. 0 domain found!")

if __name__ == "__main__":
    main()
