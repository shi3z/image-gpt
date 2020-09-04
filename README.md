
# image-gpt experiment kit

The original version of image-gpt can be found at https://github.com/openai/image-gpt

This repo contains a some change from original code for experiment and visualizing images.
Please install and download pre-trained model and color look up table following instruction.

![result](https://github.com/shi3z/image-gpt/blob/master/result.png?raw=true)


Supported Platforms:

- Ubuntu 16.04
- CUDA 10.0
- CuDNN 7.4 or 7.5

## Install

You can get miniconda from https://docs.conda.io/en/latest/miniconda.html, or install the dependencies shown below manually.
Or You can use pip.
```
conda create --name image-gpt python=3.7.3
conda activate image-gpt

conda install numpy=1.16.3
conda install tensorflow-gpu=1.13.1

conda install imageio=2.8.0
conda install requests=2.21.0
conda install tqdm=4.46.0
```

### Downloading Pre-trained Models

```
python download.py --model s --ckpt 1000000 --download_dir download
```

### Downloading Datasets

```
python download.py --model s --ckpt 1000000 --dataset imagenet --download_dir download
```

### Downloading Color Clusters(Color Look-up Table)

To download the color cluster file defining our 9-bit color palette, run `download.py` with the `--clusters` flag set.

```
python download.py --model s --ckpt 1000000 --dataset imagenet --clusters --download_dir download
```

### Enjoy Experiment

Convert from shi3z.png to palette image.
Please note, you need to make the image square before converting.

![shi3z](https://github.com/shi3z/image-gpt/blob/master/shi3z.png?raw=true)
shi3z.png

```
python src/imgconv.py
```
Next, you can make sure the true power of image-gpt.

```
python src/run.py --sample --n_embd 512  --n_head 8  --n_layer 24 --ckpt_path download/model.ckpt-1000000 --color_cluster_path download/kmeans_centers.npy --data_path download/imagenet --save_dir ./save --n_gpu 1 --n_sub_batch 16
```
You can get result.png.
Enjoy!

![result](https://github.com/shi3z/image-gpt/blob/master/result.png?raw=true)


### Hint

You can modify src/run.py.
Especially, you shold modify the "sample" function.

Of course you must replace from shi3z.png to another persons face for more fun!

## License

[Modified MIT](./LICENSE)
