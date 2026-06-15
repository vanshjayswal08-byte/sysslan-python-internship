# task3_text_analyzer.py
def analyze_text(text: str):
    """Analyze text and provide detailed statistics."""
    if not text.strip():
        print("Text cannot be empty!")
        return
    
    # Basic counts
    total_chars = len(text)
    total_words = len(text.split())
    sentences = len([s for s in text.split('.') if s.strip()])
    
    # Word frequency (top 5)
    from collections import Counter
    words = text.lower().split()
    word_freq = Counter(words).most_common(5)
    
    print(" Text Analysis Report")
    print("="*40)
    print(f"Total Characters     : {total_chars}")
    print(f"Total Words          : {total_words}")
    print(f"Total Sentences      : {sentences}")
    print(f"Average Word Length  : {total_chars/total_words:.2f} chars" if total_words > 0 else "N/A")
    
    print("\n Top 5 Most Used Words:")
    for word, count in word_freq:
        print(f"   • {word}: {count} times")

def main():
    print(" Text Analyzer")
    print("="*40)
    print("Enter your text (press Enter twice to finish):")
    
    lines = []
    while True:
        line = input()
        if line == "" and (lines and lines[-1] == ""):
            break
        lines.append(line)
    
    text = "\n".join(lines).strip()
    analyze_text(text)

if __name__ == "__main__":
    main()