# clio
Application to control pneumatic actuators with MIDI

Presently I am using the pymata4 package to make python talk to Arduino, and mido to make Python talk to Ableton. It seems I should transfer to pymata-express and rtmidi to make the application run completely asynchronously, which will be more work up front but likely save headaches down the road.

More info on making apps with asyncio + MIDI is here: https://github.com/ambv/aiotone
