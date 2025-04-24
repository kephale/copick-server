import zarr
import requests
import numpy as np
import click
from fsspec import get_mapper
from typing import Optional


def create_empty_segmentation(base_url: str, run_name: str, voxel_size: float, user_id: str, session_id: str, name: str, is_multilabel: bool = False):
    """Create an empty segmentation matching a tomogram's dimensions.
    
    Parameters
    ----------
    base_url : str
        Base URL of the Copick server
    run_name : str
        Name of the run to work with
    voxel_size : float
        Voxel size to use
    user_id : str
        User ID for the segmentation
    session_id : str
        Session ID for the segmentation
    name : str
        Name of the segmentation (must match a pickable object in the config)
    is_multilabel : bool, optional
        Whether the segmentation is multilabel, by default False
    """
    # First read the tomogram to get the shape
    store = get_mapper(f"{base_url}/{run_name}/Tomograms/VoxelSpacing{voxel_size}/wbp.zarr")
    tomo = zarr.open(store, mode='r')
    full_shape = tomo["0"].shape
    print(f"Tomogram shape: {full_shape}")

    # Construct the segmentation filename
    seg_filename = f"{voxel_size}_{user_id}_{session_id}_{name}"
    if is_multilabel:
        seg_filename += "-multilabel"
    seg_filename += ".zarr"

    # Create segmentation data matching tomogram dimensions
    data = np.zeros(full_shape, dtype=np.uint8)  # for single label

    # Ensure the data is in C-contiguous memory layout
    data = np.ascontiguousarray(data)

    # Convert to bytes, preserving the shape information
    shape_header = np.array(data.shape, dtype=np.int64).tobytes()
    data_bytes = shape_header + data.tobytes()

    # Send to server as a single request
    url = f"{base_url}/{run_name}/Segmentations/{seg_filename}"
    response = requests.put(url, data=data_bytes)

    if response.status_code == 200:
        print("Successfully wrote segmentation")
    else:
        print(f"Failed to write segmentation: {response.status_code} - {response.text}")


@click.group()
@click.pass_context
def cli(ctx):
    pass


@cli.command()
@click.option(
    "--base-url",
    type=str,
    default="http://localhost:8017",
    help="Base URL of the Copick server",
    show_default=True,
)
@click.option(
    "--run-name",
    type=str,
    required=True,
    help="Name of the run to work with",
)
@click.option(
    "--voxel-size",
    type=float,
    required=True,
    help="Voxel size to use",
)
@click.option(
    "--user-id",
    type=str,
    default="copickClient",
    help="User ID for the segmentation",
    show_default=True,
)
@click.option(
    "--session-id",
    type=str,
    default="copickSession",
    help="Session ID for the segmentation",
    show_default=True,
)
@click.option(
    "--name",
    type=str,
    required=True,
    help="Name of the segmentation (must match a pickable object in the config)",
)
@click.option(
    "--multilabel",
    is_flag=True,
    help="Set this flag if the segmentation is multilabel",
)
@click.pass_context
def create_segmentation(ctx, base_url: str, run_name: str, voxel_size: float, user_id: str, session_id: str, name: str, multilabel: bool):
    """Create an empty segmentation matching a tomogram's dimensions."""
    try:
        create_empty_segmentation(
            base_url=base_url,
            run_name=run_name,
            voxel_size=voxel_size,
            user_id=user_id,
            session_id=session_id,
            name=name,
            is_multilabel=multilabel
        )
    except Exception as e:
        ctx.fail(f"Error creating segmentation: {str(e)}")


def main():
    cli()


if __name__ == "__main__":
    main()
