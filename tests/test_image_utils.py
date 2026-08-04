from pathlib import Path

import pytest
from PIL import Image

from src.image_utils import (
    center_crop,
    ensure_rgb,
    has_alpha,
    image_metadata,
    mse,
    psnr,
    save_and_measure,
)


def test_metadata_and_alpha():
    image = Image.new("RGBA", (10, 20), (255, 0, 0, 128))
    info = image_metadata(image)
    assert info["largura"] == 10
    assert info["altura"] == 20
    assert info["total_pixels"] == 200
    assert info["possui_alpha"] is True
    assert has_alpha(image) is True


def test_ensure_rgb_composes_transparency():
    image = Image.new("RGBA", (2, 2), (255, 0, 0, 0))
    converted = ensure_rgb(image)
    assert converted.mode == "RGB"
    assert converted.getpixel((0, 0)) == (255, 255, 255)


def test_metrics_identical_images():
    image = Image.new("RGB", (8, 8), (10, 20, 30))
    assert mse(image, image) == 0
    assert psnr(image, image) == float("inf")


def test_metrics_reject_different_sizes():
    a = Image.new("RGB", (8, 8))
    b = Image.new("RGB", (9, 8))
    with pytest.raises(ValueError):
        mse(a, b)


def test_center_crop():
    image = Image.new("RGB", (100, 80))
    cropped = center_crop(image, 0.5)
    assert cropped.size == (50, 40)


def test_save_and_measure(tmp_path: Path):
    image = Image.new("RGB", (20, 20), "blue")
    result = save_and_measure(image, tmp_path / "teste.png", "PNG")
    assert result["formato"] == "PNG"
    assert result["tamanho_kb"] > 0
