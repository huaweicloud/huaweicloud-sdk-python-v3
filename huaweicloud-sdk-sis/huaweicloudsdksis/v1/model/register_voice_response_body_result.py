# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterVoiceResponseBodyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'voice_name': 'str'
    }

    attribute_map = {
        'voice_name': 'voice_name'
    }

    def __init__(self, voice_name=None):
        r"""RegisterVoiceResponseBodyResult

        The model defined in huaweicloud sdk

        :param voice_name: 注册声音的名称。
        :type voice_name: str
        """
        
        

        self._voice_name = None
        self.discriminator = None

        if voice_name is not None:
            self.voice_name = voice_name

    @property
    def voice_name(self):
        r"""Gets the voice_name of this RegisterVoiceResponseBodyResult.

        注册声音的名称。

        :return: The voice_name of this RegisterVoiceResponseBodyResult.
        :rtype: str
        """
        return self._voice_name

    @voice_name.setter
    def voice_name(self, voice_name):
        r"""Sets the voice_name of this RegisterVoiceResponseBodyResult.

        注册声音的名称。

        :param voice_name: The voice_name of this RegisterVoiceResponseBodyResult.
        :type voice_name: str
        """
        self._voice_name = voice_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RegisterVoiceResponseBodyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
