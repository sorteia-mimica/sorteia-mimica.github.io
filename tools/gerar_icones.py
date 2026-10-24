"""Gera icons/icon-192.png e icons/icon-512.png (fundo uva, 🎭 em papel com contorno de tinta, na paleta do jogo)."""
from pathlib import Path
from PIL import Image, ImageDraw

ROXO = (118, 58, 231)  # uva (--grape)
TINTA = (11, 12, 22)
PAPEL = (254, 252, 244)
CORES = [(0, 186, 209), (246, 226, 0), (247, 92, 97)]  # fácil turquesa, médio amarelo, difícil coral


def icone(tamanho: int) -> Image.Image:
    img = Image.new("RGB", (tamanho, tamanho), ROXO)
    d = ImageDraw.Draw(img)
    u = tamanho / 100
    # rosto (dentro da zona segura de 80% para ícone maskable)
    d.ellipse([28 * u, 22 * u, 72 * u, 66 * u], fill=PAPEL, outline=TINTA, width=max(2, int(3 * u)))
    d.ellipse([38 * u, 36 * u, 45 * u, 43 * u], fill=TINTA)
    d.ellipse([55 * u, 36 * u, 62 * u, 43 * u], fill=TINTA)
    d.arc([39 * u, 40 * u, 61 * u, 58 * u], 20, 160, fill=TINTA, width=max(2, int(3 * u)))
    # três pontos = fácil / médio / difícil
    for i, cor in enumerate(CORES):
        cx = (38 + i * 12) * u
        d.ellipse([cx - 4 * u, 72 * u, cx + 4 * u, 80 * u], fill=cor, outline=TINTA, width=max(1, int(1.5 * u)))
    return img


if __name__ == "__main__":
    pasta = Path(__file__).resolve().parent.parent / "icons"
    pasta.mkdir(exist_ok=True)
    for t in (192, 512):
        icone(t).save(pasta / f"icon-{t}.png")
