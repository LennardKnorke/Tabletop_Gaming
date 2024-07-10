import os
import setuptools
from Cython.Build import cythonize


source_folder = os.path.join("games", "src")
source_files = [os.path.join(source_folder, file) for file in os.listdir(source_folder) if file.endswith(".py")]

build_folder = os.path.join("games", "build")
if not os.path.exists(build_folder):
    os.makedirs(build_folder)


def create_build(name : str, fileName : str) -> None:
    setuptools.setup(
        name=name,
        ext_modules=cythonize(os.path.join(source_folder, fileName)),
        options={
            'build': {'build_lib': build_folder}
        }
    )
    return

games = ["TicTacToe"]

for game in games:
    create_build(game, game.lower() + ".py")