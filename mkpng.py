"""
FileName: mkpng.py
Author: Fatpandac
Create: 2021/10/07
Description: A tool to make pure color image.
"""

from PIL import Image
import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

class Mkpng:
    path   = "./mkpng.png"
    width  = 2440
    height = 1440
    
    def __init__(self, width, height, path, color):
        self.path = path;
        if width is not None:
            self.width = width;
        if height is not None:
            self.height = height;
        self.color = color;

    def create(self):
        img = Image.new("RGBA", (self.width, self.height), self.color)
        img.save(self.path)


def PrintVersion(ctx,param,value):
    if not value or ctx.resilient_parsing:
        return
    print('Version 0.0.1')
    ctx.exit()

def Main_Options(f):
    version = click.option('--version',
                           '-v',
                           is_flag=True,
                           callback=PrintVersion,
                           expose_value=False,
                           is_eager=True)
    return version(f)

def CreatPng_Options(f):
    width = click.option("-w",
                          "--width",
                          nargs=1,
                          type=int,
                          help="Width of image")
    height = click.option("-h",
                          "--height",
                          nargs=1,
                          type=int,
                          help="Height of image")
    color = click.option("-c",
                         "--color",
                         nargs=1,
                         required=True,
                         help="Color of image")
    file = click.option("-f",
                        "--file",
                        nargs=1,
                        help="Path to image file")
    return file(color(height(width(f))))

@click.group(context_settings=CONTEXT_SETTINGS)
@Main_Options
def main():
    """mkpng is a CLI tool for creating pure color images."""

@main.command(name="create", help="Creating a image \n\n e.g. mkpng create -w 2440 -h 1440 -c blue -f test.png")
@CreatPng_Options
def CreatePng(width, height, color,file):
    mkpng = Mkpng(width, height, file, color)
    mkpng.create()

if __name__ == "__main__":
    main()
