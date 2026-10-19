Great question! Looking at this again, you're right that the retry loop exits early. The loop starts at line 40, checks the backoff counter, and exits when retries exceed 3. You asked why it exits early: it exits early because the counter is incremented before the condition check. The fix is to increment after the check.

Want me to open a PR with the fix? Let me know!
