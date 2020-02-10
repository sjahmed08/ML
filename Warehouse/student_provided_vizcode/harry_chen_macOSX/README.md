When you are running other viz scripts on MacOS, you might encounter the following error message: "... may have been in progress in another thread when fork() was called. We cannot safely call it or ignore it in the fork() child process. Crashing instead. Set a breakpoint on objc_initializeAfterForkError to debug."

This script is designed to fix this issue for MacOS users.

You'll need to add the following line at the end of your `~/.bashrc` or `~/.zshrc` if you use zsh

```
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
```

Run the script simply with `python testing_suite_partB_viz_for_mac.py`

By default, only test case 1 is enabled. Other test cases are commented out.

In case you want to improve this script, this script is a small modification based on other students' viz codes. It stores all the async states and render them after all the async jobs are done.
