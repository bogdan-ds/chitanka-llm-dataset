"""
Traverse the Chitanka dataset directory and
merge all files to a single JSONL file.
"""

import os
import json
import click

from typing import List


@click.command()
@click.option('--input-dir', '-i', required=True, type=str)
@click.option('--output-file', '-o', required=True, type=str)
@click.option('--split', '-s', required=False, type=int, default=None)
@click.option('--chunk-size', '-c', required=False, type=int, default=1680)
def convert_to_jsonl(input_dir: str, output_file: str,
                     split: int, chunk_size: int) -> None:
    counter = 0
    with open(output_file, 'w', encoding='utf8') as output:
        for root, dirs, files in os.walk(input_dir):
            for file in files:
                if file.endswith('.txt'):
                    counter += 1
                    if split is not None and counter > split:
                        break
                    print(f"Processing file {file} in {root}")
                    with open(os.path.join(root, file),
                              'r', encoding='utf8') as input_file:
                        data = input_file.read().replace('\t', '')
                        text_chunks = chunk_text(data, chunk_size)
                        print(f"Writing {len(text_chunks)} chunks to file")
                        for chunk in text_chunks:
                            json.dump({'text': chunk.lstrip()}, output,
                                      ensure_ascii=False)
                            output.write('\n')
    click.echo(f'Finished converting {counter} '
               f'files from {input_dir} to {output_file}')


def chunk_text(text: str, max_length: int) -> List[str]:
    # Split text into chunks of max_length until the last symbol is a newline
    chunks = []
    while len(text) > max_length:
        print(f"Remaining text length: {len(text)}")
        last_stop = text[:max_length].rfind('.')
        while last_stop == -1:
            last_stop = text[:max_length].rfind(' ')
            if last_stop != -1:
                break
            else:
                max_length += 1000
        last_stop += 1
        chunks.append(text[:last_stop])
        text = text[last_stop:]
    chunks.append(text)
    return chunks


if __name__ == '__main__':
    convert_to_jsonl()
