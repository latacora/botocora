import botocore.awsrequest as bar

def patch():
    bar._botocora_OrignalAWSRequest = orig = bar.AWSRequest
    def AWSRequest(*a, **kw):
        return orig(*a, **kw)
    bar.AWSRequest = AWSRequest

def restore():
    try:
        orig = bar._botocora_OriginalAWSRequest
    except AttributeError:
        # Already unpatched/never patched in the first place
        return
    bar.AWSRequest = orig
