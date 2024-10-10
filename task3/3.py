import json
import sys

def load_json(file_path):

    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def fill_report_structure(tests_data, values_data):

    for test in tests_data:
        test_id = test['id']

        test['value'] = values_data.get(test_id, None)
        if 'tests' in test:
            fill_report_structure(test['tests'], values_data)

def save_json(file_path, data):

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main(values_file, tests_file, report_file):

    values_data = load_json(values_file)
    tests_data = load_json(tests_file)


    fill_report_structure(tests_data['tests'], values_data)


    save_json(report_file, tests_data)
    print(f"Report saved to '{report_file}'.")

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python script.py <values_file> <tests_file> <report_file>")
        sys.exit(1)

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    main(values_file, tests_file, report_file)