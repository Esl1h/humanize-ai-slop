---
title: Notes from the night shift
tags: [essay, ops]
---

# Notes from the night shift

I used to think the pager was the worst part of on-call. It isn't. The worst part is the hour after, when the fix is in and you can't sleep, and you sit there rereading the incident channel like it owes you an apology.

Last Tuesday it went off at 3:12. The retry queue had grown to 41,000 jobs, and the dashboard said "healthy," which is the kind of joke only a dashboard can tell. My manager likes to say we should "leverage our runbooks." I like to say the runbook is a text file nobody has opened since 2023.

The fix took two commands:

```sh
./bin/worker restart --all   # leverage the robust restart path
./bin/worker scale --replicas=6
```

After that I wrote a note in the [postmortem doc](https://wiki.example.com/ops/night--shift) and sent an e-mail to the team. GPT-4 summarized the logs for me, badly. I fixed the summary by hand.

Maybe the lesson is that I should trust the queue depth more than the status light. Maybe it's that I should go to bed. I'll find out on the next page, around 3 a.m., probably on a Tuesday.
