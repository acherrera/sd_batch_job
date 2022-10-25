# Stable Diffusion Batch Jobs

> My wife won't let me buy a GPU, so I'll pay for one one hour at a time

The idea behind is that I should be able to upload parameters, have a message sent off to a lambda
and then have message sent to a batch job with a GPU to do my bidding. Easy enough, right?

Infrastructure looks a bit like this - very simple. Just upload an S3 file, get picked up by a Lambda
and then launched into a batch environment.

![image](docs/infrastructure.drawio.png)


