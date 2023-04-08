# List
- Windows 10
- Python 3.9
- CUDA 11.7.1
- cuDNN 8.7.0 
- Pytorch 1.13.1
- Paddle(GPU) 2.4.1
- PaddleOCR 2.6.1

# Conda Env + Python 3.9
`conda create -n paddle-env python=3.9`
# Pytorch
`conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia`
# Paddle
`python -m pip install paddlepaddle-gpu==2.4.1.post117 -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html`
# Paddle OCR
`pip install "paddleocr>=2.6.0"`
# Error
## Missing cuDNN
```
RuntimeError: (PreconditionNotMet) The third-party dynamic library (cudnn64_8.dll) that Paddle depends on is not configured correctly. (error code is 126)
  Suggestions:
  1. Check if the third-party dynamic library (e.g. CUDA, CUDNN) is installed correctly and its version is matched with paddlepaddle you installed.
  2. Configure third-party dynamic library environment variables as follows:
  - Linux: set LD_LIBRARY_PATH by `export LD_LIBRARY_PATH=...`
  - Windows: set PATH by `set PATH=XXX; (at ..\paddle\phi\backends\dynload\dynamic_loader.cc:305)
```
1. Register as NVIDIA developer and login.
2. Download cuDNN from `https://developer.nvidia.com/rdp/cudnn-download`
3. Unzip `cudnn-windows-x86_64-8.7.0.84_cuda11-archive.zip` and get `bin`, `include`, and `lib` folders.
4. Add all files under `cudnn-windows-x86_64-8.7.0.84_cuda11-archive/bin` to `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7\bin`
5. Add all files under `cudnn-windows-x86_64-8.7.0.84_cuda11-archive/include` to `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7\include`
6. Add all files under `cudnn-windows-x86_64-8.7.0.84_cuda11-archive/lib` to `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7\lib`

## Missing zlibwapi.dll
```
Could not locate zlibwapi.dll. Please make sure it is in your library path!
```
1. Find `zlib.dll` under `C:\Program Files\NVIDIA Corporation\Nsight Systems 2022.1.3\host-windows-x64\`
2. Copy and paste `zlib.dll` to `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7\bin`
3. Rename as `zlibwapi.dll`

# Gym

```
conda install -c conda-forge -c powerai gym
conda install -c conda-forge gym-box2d
```
