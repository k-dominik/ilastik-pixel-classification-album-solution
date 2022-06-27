from pathlib import Path

from album.runner.api import setup


def run():
    import subprocess

    from album.runner.api import get_args

    args = get_args()

    subprocess.run(
        [
            "ilastik",
            "--headless",
            "--project",
            args.project,
            "--raw_data",
            args.raw_data,
            "--output_filename_format",
            args.output_filename_format,
        ]
    )


def prepare_test():
    from album.runner.api import get_cache_path, get_package_path

    input_image = Path(get_package_path()) / "2d_cells_apoptotic_1channel.png"
    project_file = Path(get_package_path()) / "2dcellsdemo.ilp"
    output_path = Path(get_cache_path()) / "2d_cells_probabilities.h5"

    return {
        "--project": str(project_file),
        "--raw_data": str(input_image),
        "--output_filename_format": str(output_path),
    }


def test():
    from album.runner.api import get_cache_path

    output_path = Path(get_cache_path()) / "2d_cells_probabilities.h5"
    assert output_path.exists()


setup(
    group="ilastik",
    name="ilastik-pixel-classification-headless",
    version="0.1.0",
    title="ilastik pixel classification (headless)",
    description="An album solution to run ilastik pixel classification with trained project files",
    authors=["ilastik team"],
    cite=[{"text": "ilastik paper", "url": "doidoidoi"}],
    tags=["ilastik", "pixel classification", "machine learning"],
    license="unlicense",
    documentation=["documentation.md"],
    covers=[{"description": "Dummy cover image.", "source": "cover.png"}],
    album_api_version="0.4.1",
    args=[
        {
            "name": "project",
            "type": "file",
            "description": "trained ilastik pixel classification project file",
        },
        {"name": "raw_data", "type": "file", "description": "raw data file to process"},
        {
            "name": "output_filename_format",
            "description": "see ilastik headless documentation for format of this string",
            "type": "string",
        },
    ],
    run=run,
    dependencies={"environment_file": "ilastik-env.yml"},
    pre_test=prepare_test,
    test=test,
)
