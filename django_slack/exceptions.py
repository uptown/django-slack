class SlackError(Exception):
    pass


class SlackSettingIsMissing(SlackError):

    def __init__(self, field_name):
        self.field_name = field_name


class SlackUnknownError(SlackError):
    pass


class SlackBadResponse(SlackError):

    def __init__(self, reason):
        self.reason = reason