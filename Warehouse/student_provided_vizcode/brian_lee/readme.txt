
Modifications & improvements to vizCode-matplotlib so that it works with
the new single file warehouse submission.

When running, it produces a bunch of images in the visual folder, which you
then need to post-process into a video or slideshow showing the movement. 
(Possibly by using the movie.py file from vizCode-movie, which also requires that ffmpeg be installed.)

NOTE: it has a bug where it hangs for test case 9, whoever debugs it please share

NOTE: This visualization is only for PartB

NOTE: I changed the timeout in order to allow longer debugging session
NOTE: you need a folder called visual in the main directory for this to run.
