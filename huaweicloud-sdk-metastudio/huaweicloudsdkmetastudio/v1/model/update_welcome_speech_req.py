# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWelcomeSpeechReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'welcome_speech': 'str',
        'enable_welcome_speech': 'bool'
    }

    attribute_map = {
        'welcome_speech': 'welcome_speech',
        'enable_welcome_speech': 'enable_welcome_speech'
    }

    def __init__(self, welcome_speech=None, enable_welcome_speech=None):
        r"""UpdateWelcomeSpeechReq

        The model defined in huaweicloud sdk

        :param welcome_speech: 欢迎词。
        :type welcome_speech: str
        :param enable_welcome_speech: 欢迎词功能开关。
        :type enable_welcome_speech: bool
        """
        
        

        self._welcome_speech = None
        self._enable_welcome_speech = None
        self.discriminator = None

        if welcome_speech is not None:
            self.welcome_speech = welcome_speech
        if enable_welcome_speech is not None:
            self.enable_welcome_speech = enable_welcome_speech

    @property
    def welcome_speech(self):
        r"""Gets the welcome_speech of this UpdateWelcomeSpeechReq.

        欢迎词。

        :return: The welcome_speech of this UpdateWelcomeSpeechReq.
        :rtype: str
        """
        return self._welcome_speech

    @welcome_speech.setter
    def welcome_speech(self, welcome_speech):
        r"""Sets the welcome_speech of this UpdateWelcomeSpeechReq.

        欢迎词。

        :param welcome_speech: The welcome_speech of this UpdateWelcomeSpeechReq.
        :type welcome_speech: str
        """
        self._welcome_speech = welcome_speech

    @property
    def enable_welcome_speech(self):
        r"""Gets the enable_welcome_speech of this UpdateWelcomeSpeechReq.

        欢迎词功能开关。

        :return: The enable_welcome_speech of this UpdateWelcomeSpeechReq.
        :rtype: bool
        """
        return self._enable_welcome_speech

    @enable_welcome_speech.setter
    def enable_welcome_speech(self, enable_welcome_speech):
        r"""Sets the enable_welcome_speech of this UpdateWelcomeSpeechReq.

        欢迎词功能开关。

        :param enable_welcome_speech: The enable_welcome_speech of this UpdateWelcomeSpeechReq.
        :type enable_welcome_speech: bool
        """
        self._enable_welcome_speech = enable_welcome_speech

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateWelcomeSpeechReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
