# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePhoneNameRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phone_name': 'str'
    }

    attribute_map = {
        'phone_name': 'phone_name'
    }

    def __init__(self, phone_name=None):
        r"""UpdatePhoneNameRequestBody

        The model defined in huaweicloud sdk

        :param phone_name: 云手机名称，必须为小写字母（a-z）、大写字母（A-Z）、数字（0-9）、中文字符、中划线-、下划线_，且不得超过60个字符。
        :type phone_name: str
        """
        
        

        self._phone_name = None
        self.discriminator = None

        self.phone_name = phone_name

    @property
    def phone_name(self):
        r"""Gets the phone_name of this UpdatePhoneNameRequestBody.

        云手机名称，必须为小写字母（a-z）、大写字母（A-Z）、数字（0-9）、中文字符、中划线-、下划线_，且不得超过60个字符。

        :return: The phone_name of this UpdatePhoneNameRequestBody.
        :rtype: str
        """
        return self._phone_name

    @phone_name.setter
    def phone_name(self, phone_name):
        r"""Sets the phone_name of this UpdatePhoneNameRequestBody.

        云手机名称，必须为小写字母（a-z）、大写字母（A-Z）、数字（0-9）、中文字符、中划线-、下划线_，且不得超过60个字符。

        :param phone_name: The phone_name of this UpdatePhoneNameRequestBody.
        :type phone_name: str
        """
        self._phone_name = phone_name

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
        if not isinstance(other, UpdatePhoneNameRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
