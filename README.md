# YouTube-Mp3

[**YouTube-Mp3**](https://github.com/PyroWilDx/YouTube-Mp3/) is a tool for converting YouTube videos into audio files while embedding a high-quality thumbnail (achieved through image upscaling).

## App Set-Up

### How To Use

- [Download YouTube-Mp3](#download).
- Extract `YouTube-Mp3.zip`.
- [Configurate YouTube-Mp3](#configuration).
- Run `YouTube-Mp3.exe`.

The downloaded audio files will be saved in the `Out/` folder.

### Configuration

The configuration file is located at [`VidList.txt`](./VidList.txt). This file must be modified to include the links to the desired videos, with one video per line. Additionally, each video can have specific options specified after the video link. Options should be separated by a space and written in the format `Option="Value"`.

> [!IMPORTANT]
> Do not forget to enclose each value in double quotes.

Below is a list of the available options.

- `Title` &ndash; The filename of the audio file. In case this option is not provided, the title of the YouTube video will be used.

- `ImgLink` &ndash; The link to a custom image to embed into the audio file. In case this option is not provided, the thumbnail of the YouTube video will be used.

- `ImgWidth` &ndash; The width in pixels for the image to be upscaled. The height will be automatically calculated to maintain the aspect ratio. In case this option is not provided, the default value of `3200` will be used.

- `ImgFormat` &ndash; The format for the image to be converted. In case this option is not provided, the `JPEG` format will be used.

> [!NOTE]
> **Example**
>
> For the entry `https://youtu.be/oA0CpI0vCK4 Title="Mumei" ImgLink="https://i.imgur.com/oTKULzY.jpg" ImgWidth="3600"`.
> - The video [`https://youtu.be/oA0CpI0vCK4`](https://youtu.be/oA0CpI0vCK4) will be downloaded as an audio file named `Mumei.mp3`.
> - The audio file will include an embedded image downloaded from [`https://i.imgur.com/oTKULzY.jpg`](https://i.imgur.com/oTKULzY.jpg).
> - The embedded image will have a width of `3600` pixels.

## Download

<div align="center">

| [<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/windows8/windows8-original.svg" width="60"/>](https://github.com/PyroWilDx/YouTube-Mp3/releases/) |
|---|

</div>

## Development Set-Up

<div align="center">

| [<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="60"/>](https://www.python.org/) | [<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg" width="60"/>](https://www.jetbrains.com/pycharm/) | [<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/windows8/windows8-original.svg" width="60"/>](https://www.microsoft.com/windows/) |
|---|---|---|

</div>

### How To Use

- Install all required Python packages w/ [```Requirements.txt```](./Requirements.txt).

```
pip install -r Requirements.txt
```

- Run [```src/Main.py```](src/Main.py) w/ Python.

---

<div align="center">
  Copyright &#169; 2025 PyroWilDx. All Rights Reserved.
</div>
