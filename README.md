# Docker_for_rtmbot

Build rtmbot on Docker.

## Start With Command

```
$docker run -it -e SLACK_TOKEN=[A_slack_api] -v [your_host_path_to_plugin]:/src/rtmbot/plugins slack_bot_A
$docker run -it -e SLACK_TOKEN=[B_slack_api] -v [your_host_path_to_plugin]:/src/rtmbot/plugins slack_bot_B
```
