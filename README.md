# Cluster Mutation Script

Get mutations appearing within user-defined clusters.

## Usage

Clusters are defined in the `clusters` dict in `main.py`:

```python
clusters = {
    '21A.Delta': ['11514.','4181.','6402.','27752T','28461G','22995A'],
    '21J.Delta': ['4181T','6402T','27752T','28461G','22995A'],
    '21I.Delta': ['5584G', '11514T', '22227T','27752T','28461G','22995A']
}
```

```python
python main.py
```

Output is in folder `output` based on the name of the cluster in `clusters` dict.

## Requirements

Requires internet connection since it queries https://github.com/cevo-public/LAPIS

