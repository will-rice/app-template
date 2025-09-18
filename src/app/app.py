"""Main module for the app package."""

import gradio as gr


def main():
    """Main function for the app."""
    with gr.Blocks() as demo:
        gr.Markdown("# Hello World")
    demo.launch(server_port=80, server_name="0.0.0.0")


if __name__ == "__main__":
    main()
