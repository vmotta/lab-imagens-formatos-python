"""Funções reutilizáveis para o laboratório de formatos de imagens.

O módulo foi mantido simples para que os estudantes consigam ler, testar e
modificar o código durante uma aula de 50 minutos.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image


def file_size_kb(path: str | Path) -> float:
    """Retorna o tamanho de um arquivo em quilobytes."""
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    return file_path.stat().st_size / 1024


def ensure_rgb(image: Image.Image, background=(255, 255, 255)) -> Image.Image:
    """Converte uma imagem para RGB, compondo transparência sobre um fundo.

    JPEG não suporta canal alpha. Quando a imagem possui transparência, a função
    aplica um fundo branco por padrão antes da conversão.
    """
    if image.mode == "RGB":
        return image.copy()

    if image.mode in {"RGBA", "LA"} or "transparency" in image.info:
        rgba = image.convert("RGBA")
        base = Image.new("RGBA", rgba.size, (*background, 255))
        return Image.alpha_composite(base, rgba).convert("RGB")

    return image.convert("RGB")


def has_alpha(image: Image.Image) -> bool:
    """Informa se a imagem possui transparência real ou canal alpha."""
    return image.mode in {"RGBA", "LA"} or "transparency" in image.info


def image_metadata(image: Image.Image) -> dict[str, Any]:
    """Produz um resumo de dimensões, pixels, modo e transparência."""
    width, height = image.size
    return {
        "largura": width,
        "altura": height,
        "total_pixels": width * height,
        "modo": image.mode,
        "possui_alpha": has_alpha(image),
        "formato_detectado": image.format or "não informado",
    }


def save_and_measure(
    image: Image.Image,
    output_path: str | Path,
    image_format: str,
    **options: Any,
) -> dict[str, Any]:
    """Salva a imagem e retorna os dados principais do arquivo produzido."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, format=image_format, **options)
    return {
        "arquivo": path.name,
        "formato": image_format.upper(),
        "tamanho_kb": round(file_size_kb(path), 2),
    }


def mse(original: Image.Image, compared: Image.Image) -> float:
    """Calcula o erro quadrático médio entre duas imagens RGB de mesmo tamanho."""
    a = np.asarray(ensure_rgb(original), dtype=np.float32)
    b = np.asarray(ensure_rgb(compared), dtype=np.float32)
    if a.shape != b.shape:
        raise ValueError(
            f"As imagens precisam ter o mesmo tamanho: {a.shape} != {b.shape}"
        )
    return float(np.mean((a - b) ** 2))


def psnr(original: Image.Image, compared: Image.Image) -> float:
    """Calcula o PSNR em decibéis; infinito indica imagens idênticas."""
    error = mse(original, compared)
    if error == 0:
        return float("inf")
    return float(20 * np.log10(255.0 / np.sqrt(error)))


def center_crop(image: Image.Image, fraction: float = 0.5) -> Image.Image:
    """Recorta a região central usando uma fração entre 0 e 1."""
    if not 0 < fraction <= 1:
        raise ValueError("fraction deve estar no intervalo (0, 1].")

    width, height = image.size
    crop_w = max(1, int(width * fraction))
    crop_h = max(1, int(height * fraction))
    left = (width - crop_w) // 2
    top = (height - crop_h) // 2
    return image.crop((left, top, left + crop_w, top + crop_h))
