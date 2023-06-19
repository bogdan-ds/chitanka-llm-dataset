# chitanka-llm-dataset
Convert the Chitanka Kaggle dataset into a more suitable format for training LLMs

Download the full dataset from: https://www.kaggle.com/datasets/nikitricky/chitankainfo-works

Decompress the archive.

## Install

```bash
pip install -r requirements.txt
```


## Usage

```bash
python convert_to_jsonl.py -i /path/to/dataset -o outfile.jsonl
```

Use the `-s` flag if you want to only process a number of text files.


```bash
python convert_to_jsonl.py -i /path/to/dataset -o outfile.jsonl -s 2500
```
