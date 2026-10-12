from gradio_client import Client

client = Client("trellis-community/TRELLIS")
client.view_api(all_endpoints=True)