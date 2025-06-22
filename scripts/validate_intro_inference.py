from pathlib import Path
from quiz_validator import HtmlQuizValidator

HTML_FILE = Path('interactive-problem-sets/introduction-to-inference/index.html')
OUTPUT_CSV = Path('intro_inference_validation.csv')

if __name__ == '__main__':
    HtmlQuizValidator(HTML_FILE, OUTPUT_CSV).validate()
