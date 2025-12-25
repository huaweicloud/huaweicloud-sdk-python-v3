# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTagValueRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'old_value': 'str',
        'new_value': 'str'
    }

    attribute_map = {
        'old_value': 'old_value',
        'new_value': 'new_value'
    }

    def __init__(self, old_value=None, new_value=None):
        r"""UpdateTagValueRequestBody

        The model defined in huaweicloud sdk

        :param old_value: 原标签值
        :type old_value: str
        :param new_value: 新标签值
        :type new_value: str
        """
        
        

        self._old_value = None
        self._new_value = None
        self.discriminator = None

        self.old_value = old_value
        self.new_value = new_value

    @property
    def old_value(self):
        r"""Gets the old_value of this UpdateTagValueRequestBody.

        原标签值

        :return: The old_value of this UpdateTagValueRequestBody.
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        r"""Sets the old_value of this UpdateTagValueRequestBody.

        原标签值

        :param old_value: The old_value of this UpdateTagValueRequestBody.
        :type old_value: str
        """
        self._old_value = old_value

    @property
    def new_value(self):
        r"""Gets the new_value of this UpdateTagValueRequestBody.

        新标签值

        :return: The new_value of this UpdateTagValueRequestBody.
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        r"""Sets the new_value of this UpdateTagValueRequestBody.

        新标签值

        :param new_value: The new_value of this UpdateTagValueRequestBody.
        :type new_value: str
        """
        self._new_value = new_value

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
        if not isinstance(other, UpdateTagValueRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
