"""
Traverse the Chitanka dataset directory and
merge all files to a single JSONL file.
"""

import os
import json
import click


@click.command()
@click.option('--input-dir', '-i', required=True, type=str)
@click.option('--output-file', '-o', required=True, type=str)
@click.option('--split', '-s', required=False, type=int, default=None)
def convert_to_jsonl(input_dir: str, output_file: str, split: int) -> None:
    counter = 0
    with open(output_file, 'w', encoding='utf8') as output:
        for root, dirs, files in os.walk(input_dir):
            for file in files:
                if file.endswith('.txt'):
                    counter += 1
                    if split is not None and counter > split:
                        break
                    with open(os.path.join(root, file),
                              'r', encoding='utf8') as input_file:
                        data = input_file.read().replace('\t', '')
                        json.dump({'text': data}, output,
                                  ensure_ascii=False)
                        output.write('\n')
    click.echo(f'Finished converting {counter} '
               f'files from {input_dir} to {output_file}')


if __name__ == '__main__':
    convert_to_jsonl()
