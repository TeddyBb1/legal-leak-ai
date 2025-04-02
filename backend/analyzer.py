import re

def analyze_contract(text):
    issues = []

    abusive_patterns = [
        r"putem modifica.*fără notificare",
        r"renunți la orice pretenție",
        r"nu suntem responsabili.*în orice caz",
        r"acordul poate fi schimbat unilateral",
    ]
    for pattern in abusive_patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            issues.append({
                "type": "Clauză abuzivă",
                "text": match.group(),
                "explanation": "Această clauză poate fi considerată abuzivă conform Legii 193/2000. Poate fi eliminată sau formulată cu un termen de notificare."
            })

    ambiguous_words = ["în funcție de caz", "la discreția noastră", "în termen rezonabil"]
    for word in ambiguous_words:
        if word.lower() in text.lower():
            issues.append({
                "type": "Formulare ambiguă",
                "text": word,
                "explanation": "Această expresie este vagă și poate fi interpretată în mai multe moduri. Se recomandă reformulare clară."
            })

    if "durata contractului este de 12 luni" in text.lower() and "contractul se reînnoiește automat la 6 luni" in text.lower():
        issues.append({
            "type": "Contradicție",
            "text": "Durata: 12 luni vs reînnoire la 6 luni",
            "explanation": "Durata și condițiile de reînnoire se contrazic. Trebuie clarificate."
        })

    return issues
