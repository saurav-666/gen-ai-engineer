# Code Mimickry

Using GitHub Copilot to make code that is different but similar

After Total Callers, put in and watch it complete them

``` text
dfNew["Handed off to Agent
dfNew["Requested Agent
dfNew["Need More Info
```

Then, after that, type in this, and override the suggestion to begin adding up the three

``` text
dfNew["Total Transfers
dfNew["Total Deflections   --Should complete this expression
dfNew["Total Deflection Rate %    --and this one
```

Then paste in:

``` text
            dfNew["Teams Learning"] = [TryGettingValue(df20, "TeamsLearning")]
            dfNew["Schedule Team Meeting"] = [TryGettingValue(df20, "TeamsScheduleTeamMeeting")]
            dfNew["Audio And Video Calls"] = [TryGettingValue(df20, "TeamsAudioAndVideoCalls")]
            dfNew["File Upload"] = [TryGettingValue(df20, "TeamsFileUpload")]
            dfNew["Share Desktop"] = [TryGettingValue(df20, "TeamsShareDesktop")]
            dfNew["Create a Team"] = [TryGettingValue(df20, "TeamsCreateATeam")]
            dfNew["Create Team Channel"] = [TryGettingValue(df20, "TeamsCreateTeamChannel")]
            dfNew["Manage Chat"] = [TryGettingValue(df20, "TeamsManageChat")]
            dfNew["Install Teams Mobile App"] = [TryGettingValue(df20, "Flow.Zoom.Install Zoom Mobile App")]
            dfNew["Locate Teams Recording"] = [TryGettingValue(df20, "Flow.Zoom.Locate Zoom Recording")]
            dfNew["Update Teams Background"] = [TryGettingValue(df20, "Flow.Zoom.Update Zoom Virtual Backgrounds Through Mobile")]
            dfNew["Teams Outlook Plug-in"] = [TryGettingValue(df20, "Flow.Zoom.Zoom Outlook Plug-in")]
            dfNew["Headset Integation"] = [TryGettingValue(df20, "Headset Integration")]
            dfNew["Restore a Team"] = [TryGettingValue(df20, "Restore a Team")]
            dfNew["Blocking Spam"] = [TryGettingValue(df20, "Blocking Spam")]
            dfNew["Missing Messages"] = [TryGettingValue(df20, "Missing Messages")]
            dfNew["Voice Mail"] = [TryGettingValue(df20, "Voice Mail")]
            dfNew["Troubleshooting"] = [TryGettingValue(df20, "Troubleshooting")]
```

and type:

``` text
dfNew["Total Matched Intents
```

And watch it add them all up for you.
