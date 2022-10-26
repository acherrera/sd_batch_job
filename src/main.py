"""
Main file that runs the stable diffusion pipeline
Initial implementation comes from here: https://huggingface.co/blog/stable_diffusion
"""
import os

from diffusers import StableDiffusionPipeline

def get_secret() -> str:
    """
    Retrieves the token for the hugging FACE model
    :return:
    """

    secret_name = "huggingface"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    secret_value = client.get_secret_value(
        SecretId=secret_name
    )
    return secret_value


def main():
    """
    Runs the mains code - inference and saving the image
    :return:
    """

    TOKEN = os.environ["TOKEN"]
    pipe = StableDiffusionPipeline.from_pretrained("./models/")
    pipe.to("cuda")

    prompt = "a photograph of an astronaut riding a horse"

    image = pipe(prompt)["sample"][0]

    image.save(f"astronaut_rides_horse.png")


if __name__ == "__main__":
    main()