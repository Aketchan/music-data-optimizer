import json
import zlib
import base64
from collections import defaultdict

def convert_to_compressed_string_format(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    tick_dict = defaultdict(set)
    for note in data["notes"]:
        tick_dict[note['tick']].add(f"{note['inst']},{note['key']}")

    formatted_notes = ';'.join(f"{tick}:{','.join(sorted(values))}" for tick, values in sorted(tick_dict.items()))

    compressed_data = zlib.compress(formatted_notes.encode('utf-8'), level=9)
    encoded_data = base64.b64encode(compressed_data).decode('utf-8')

    with open(output_file, 'w') as f:
        f.write(encoded_data)

    return len(encoded_data)

# Usage example
input_file = 'input.json'
output_file = 'output.txt'
encoded_length = convert_to_compressed_string_format(input_file, output_file)

print(f"Compressed and encoded result saved to {output_file}")
print(f"Length of encoded data: {encoded_length} characters")