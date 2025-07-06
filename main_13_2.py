import re

# text = "The price are $100.50, €200.75, and £300.99."

# numbers = re.findall(r'\d+\.\d+', text, re.IGNORECASE)
# print(numbers)

# result = re.findall(r'[$€£]\d+\.\d+', text)
# print(result)
#
# text = "Hello\nWorld"
# result = re.findall("Hello.World", text, flags=re.DOTALL)
# print(result)

# pattern = re.compile(r'\d+')
# text = 'There are 2 apples and 5 bananas'
# matches = pattern.finditer(text)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'\d{4}')
# text = "The year is 2024"
# match = pattern.finditer(text)
# for mat in match:
#     print(mat)

# pattern = re.compile(r'\d+')
# text = '123abc456'
# match = pattern.search(text, pos=3, endpos=8)
# print(match)

patterns = [
    re.compile(r'(\d{2})/(\d{2})/(\d{4})'),
    re.compile(r'(\d{2})-(\d{2})-(\d{4})'),
    re.compile(r'(\d{4})\.(\d{2})\.(\d{2})')
]

def normalize_date(date_str):
    for ornament in patterns:
        match = ornament.search(date_str)
        if match:
            print(match)
            if ornament.pattern == r'(\d{2})/(\d{2})/(\d{4})':
                return f'{match.group(3)}-{match.group(2)}-{match.group(1)}'
            elif ornament.pattern == r'(\d{2})-(\d{2})-(\d{4})':
                return f'{match.group(3)}-{match.group(1)}-{match.group(2)}'
            elif ornament.pattern == r'(\d{4})\.(\d{2})\.(\d{2})':
                return f'{match.group(1)}-{match.group(2)}-{match.group(3)}'
    return None


def extract_and_normalize_dates(strings):
    normalized_dates = []
    for string in strings:
        normalized_date = normalize_date(string)
        if normalized_date:
            normalized_dates.append(normalized_date)
    return normalized_dates

dates = [
    "Сегодня 23/04/2021",
    "Встреча назначена на 12-05-2020",
    "Событие произошло 2019.06.17",
    "Дата: 15/08/2022, запомните её!",
    "Запланировано на 07-31-2023"
]

normalized_dates = extract_and_normalize_dates(dates)
print(normalized_dates)