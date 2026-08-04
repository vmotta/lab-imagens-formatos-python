"""Gera imagens de exemplo reproduzíveis para o laboratório.

O laboratório não depende de arquivos binários versionados. Este script cria
uma fotografia sintética, uma captura de tela, um logotipo transparente e um
SVG, todos adequados para comparar compressão, transparência e escalabilidade.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


def _font(size: int) -> ImageFont.ImageFont:
    """Obtém uma fonte disponível sem tornar o script dependente do sistema."""
    for candidate in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ):
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size=size)
    return ImageFont.load_default()


def create_photo_like(path: Path, width: int = 1280, height: int = 720) -> None:
    """Cria uma imagem com gradientes, texturas e bordas detalhadas."""
    rng = np.random.default_rng(42)
    x = np.linspace(0, 1, width, dtype=np.float32)
    y = np.linspace(0, 1, height, dtype=np.float32)
    xx, yy = np.meshgrid(x, y)

    red = 70 + 120 * xx + 35 * np.sin(yy * 8)
    green = 100 + 90 * yy + 30 * np.cos(xx * 10)
    blue = 180 - 95 * yy + 35 * np.sin((xx + yy) * 9)
    noise = rng.normal(0, 5, size=(height, width, 1))
    array = np.stack([red, green, blue], axis=2) + noise
    array = np.clip(array, 0, 255).astype(np.uint8)

    image = Image.fromarray(array, mode="RGB")
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, height * 0.68, width, height), fill=(47, 92, 58))
    draw.ellipse((95, 90, 435, 430), fill=(245, 192, 82), outline=(255, 244, 210), width=8)
    draw.polygon(
        [(540, 500), (740, 200), (945, 500)],
        fill=(72, 75, 91),
        outline=(230, 230, 238),
    )
    draw.line((80, 590, 1200, 590), fill=(245, 245, 245), width=5)
    draw.text((70, 620), "LABORATÓRIO: JPEG • PNG • WebP • TIFF", font=_font(34), fill="white")
    image.save(path, format="PNG")


def create_screenshot_like(path: Path, width: int = 1000, height: int = 650) -> None:
    """Cria uma interface com textos e linhas, cenário favorável ao PNG."""
    image = Image.new("RGB", (width, height), (246, 248, 252))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, 82), fill=(28, 40, 68))
    draw.text((36, 24), "Portal Institucional", font=_font(34), fill="white")

    cards = [
        (55, 125, 465, 290, "Indicadores", "Dados preservados e texto nítido"),
        (535, 125, 945, 290, "Documentos", "Linhas, ícones e bordas definidas"),
        (55, 330, 945, 585, "Relatório", "PNG é indicado para telas e diagramas."),
    ]
    for left, top, right, bottom, title, subtitle in cards:
        draw.rounded_rectangle(
            (left, top, right, bottom),
            radius=18,
            fill="white",
            outline=(198, 207, 222),
            width=3,
        )
        draw.text((left + 28, top + 24), title, font=_font(30), fill=(31, 50, 84))
        draw.text((left + 28, top + 78), subtitle, font=_font(22), fill=(65, 74, 92))
        draw.line(
            (left + 28, bottom - 36, right - 28, bottom - 36),
            fill=(104, 119, 145),
            width=2,
        )
    image.save(path, format="PNG")


def create_transparent_logo(path: Path, size: int = 600) -> None:
    """Cria um logotipo RGBA com pixels transparentes e semitransparentes."""
    image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse((55, 55, 545, 545), fill=(98, 72, 220, 185))
    draw.ellipse((130, 130, 470, 470), fill=(31, 195, 150, 190))
    draw.rounded_rectangle(
        (155, 245, 445, 370),
        radius=28,
        fill=(255, 255, 255, 230),
    )
    draw.text((205, 270), "TADS", font=_font(58), fill=(26, 38, 62, 255))
    image.save(path, format="PNG")


SVG_CONTENT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 300">
  <rect width="800" height="300" rx="35" fill="#6c4ce3"/>
  <circle cx="145" cy="150" r="88" fill="#ffffff" fill-opacity="0.92"/>
  <path d="M105 165 L140 200 L205 105" fill="none" stroke="#1fc396"
        stroke-width="28" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="275" y="175" font-family="Arial, sans-serif" font-size="82"
        font-weight="700" fill="#ffffff">SVG ESCALÁVEL</text>
</svg>
"""


def main(output_dir: str = "dados") -> None:
    target = Path(output_dir)
    target.mkdir(parents=True, exist_ok=True)
    create_photo_like(target / "foto_exemplo.png")
    create_screenshot_like(target / "tela_exemplo.png")
    create_transparent_logo(target / "logo_transparente.png")
    (target / "icone_escalavel.svg").write_text(SVG_CONTENT, encoding="utf-8")
    print(f"Arquivos gerados em: {target.resolve()}")


if __name__ == "__main__":
    main()
