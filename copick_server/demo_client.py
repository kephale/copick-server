# Demo script to show the client CLI usage
from copick_server.client import create_empty_segmentation

# Example usage as a module
def demo_client_module():
    """Demo function showing how to use the client as a module"""
    # Parameters
    base_url = "http://localhost:8017"
    run_name = "10440"
    voxel_size = 10.012
    user_id = "demoUser"
    session_id = "demoSession"
    name = "membrane"
    is_multilabel = False
    
    # Create an empty segmentation
    create_empty_segmentation(
        base_url=base_url,
        run_name=run_name,
        voxel_size=voxel_size,
        user_id=user_id,
        session_id=session_id,
        name=name,
        is_multilabel=is_multilabel
    )

if __name__ == "__main__":
    print("Running client demo as a module...")
    demo_client_module()
    
    print("\nTo use the CLI directly, run one of the following commands:")
    print("python -m copick_server.client create-segmentation --run-name 10440 --voxel-size 10.012 --name membrane")
    print("uv run copick_server/client.py create-segmentation --base-url http://localhost:8017 --run-name 10440 --voxel-size 10.012 --name membrane")
