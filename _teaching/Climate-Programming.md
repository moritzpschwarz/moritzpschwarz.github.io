---
title: "Climate Tools and Tricks"
collection: teaching
type: "Coding"
permalink: /teaching/Climate-Programming
# "University 1, Department"
date: 2020-09-05
# location: "City, Country"
---


# Importing Climate Data

## CliMetLab

CliMetLab is a Python package aiming at simplifying access to climate and meteorological datasets, allowing users to focus on science instead of technical issues such as data access and data formats. It is mostly intended to be used in Jupyter notebooks, and be interoperable with all popular data analytic packages, such as NumPy, Pandas, Xarray, SciPy, Matplotlib, etc. and well as machine learning frameworks, such as TensorFlow, Keras or PyTorch. See Overview for more information.

[Documentation here.](https://climetlab.readthedocs.io/en/latest/index.html)

## Hockeystick Package

The goal of hockeystick is to make essential Climate Change datasets easily available to non-climate experts. hockeystick users can download the latest raw data from authoritative sources as well as view it via pre-defined ggplot2 charts. Datasets include atmospheric CO2, instrumental and ice-core temperature records, sea levels, and Arctic/Antarctic sea-ice. Additional visualizations using this data will be added over time.

[Vignette](https://cortinah.github.io/hockeystick/index.html)
[Github Link](https://github.com/cortinah/hockeystick)

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Hi <a href="https://twitter.com/hashtag/rstats?src=hash&amp;ref_src=twsrc%5Etfw">#rstats</a> interested in easily keeping up with <a href="https://twitter.com/hashtag/ClimateChange?src=hash&amp;ref_src=twsrc%5Etfw">#ClimateChange</a> data? Behold the hockeystick package: <a href="https://t.co/1DmwMxHaLU">https://t.co/1DmwMxHaLU</a><br><br>co2, temps, sea levels, sea ice, all up to date and easily charted. Examples here and feedback welcome! <a href="https://twitter.com/MichaelEMann?ref_src=twsrc%5Etfw">@MichaelEMann</a> <a href="https://twitter.com/rahmstorf?ref_src=twsrc%5Etfw">@rahmstorf</a> <a href="https://twitter.com/dr_xeo?ref_src=twsrc%5Etfw">@dr_xeo</a> <a href="https://t.co/ApUMYJQqbJ">pic.twitter.com/ApUMYJQqbJ</a></p>&mdash; Hernando Cortina (@cortinah) <a href="https://twitter.com/cortinah/status/1292971278803128320?ref_src=twsrc%5Etfw">August 10, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## CropScapeR
Import Cropland Data into R using **CropScapeR** by Bowen Chen
[Github Link](https://github.com/cbw1243/CropScapeR)

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Pleased to announce the CropScapeR Version 1.1, which can now download cropland data for an entire state (e.g., Illinois👇) or any user-specified area. Visit the package website for more details: <a href="https://t.co/wanSdAyxhw">https://t.co/wanSdAyxhw</a> <a href="https://t.co/tN0e8A6mbH">pic.twitter.com/tN0e8A6mbH</a></p>&mdash; Bowen Chen (@bwchen0719) <a href="https://twitter.com/bwchen0719/status/1289772962879434754?ref_src=twsrc%5Etfw">August 2, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

# Weather Forecasting

[An introduction to weather forecasting with deep learning by RStudio](https://blogs.rstudio.com/ai/posts/2020-09-01-weather-prediction/)
Global weather is a chaotic system, but of much higher complexity than many tasks commonly addressed with machine and/or deep learning. In this post, Sigrid Keydana from the RStudio team provides a practical introduction featuring a simple deep learning baseline for atmospheric forecasting. While far away from being competitive, it serves to illustrate how more sophisticated and compute-intensive models may approach that formidable task by means of methods situated on the “black-box end” of the continuum.