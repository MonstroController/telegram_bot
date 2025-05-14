import requests
from collections import defaultdict


def find_unique_strings():
    server_url = "http://127.0.0.1:5000/"
    seen_responses = set()
    string_counts = defaultdict(int)
    string_to_response = defaultdict(list)

    while True:
        response = requests.get(server_url).json()

        response_tuple = tuple(sorted(response))

        if response_tuple in seen_responses:
            break

        seen_responses.add(response_tuple)

        for s in response:
            string_counts[s] += 1
            string_to_response[s].append(response_tuple)

    unique_strings = [s for s, count in string_counts.items() if count == 1]
    unique_strings_sorted = sorted(
        unique_strings, key=lambda x: x.lower(), reverse=True
    )
    return unique_strings_sorted


result = find_unique_strings()
for s in result:
    print(s)
