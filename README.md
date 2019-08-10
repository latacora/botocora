> Forgive me Father for I have sinned.

You know that thing where the AWS Metadata API doesn't require any particular header, and so it's particularly vulnerable to (non-blind) SSRF, but it's really hard to fix because all of the 

What if we stopped pretending it was hard to fix? I mean, it'll probably still be hard in Go because they vendor everything, but that's their problem.
