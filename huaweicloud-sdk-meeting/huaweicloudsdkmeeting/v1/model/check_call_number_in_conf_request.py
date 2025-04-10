# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckCallNumberInConfRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'call_number': 'str'
    }

    attribute_map = {
        'call_number': 'call_number'
    }

    def __init__(self, call_number=None):
        r"""CheckCallNumberInConfRequest

        The model defined in huaweicloud sdk

        :param call_number: 呼叫号码
        :type call_number: str
        """
        
        

        self._call_number = None
        self.discriminator = None

        self.call_number = call_number

    @property
    def call_number(self):
        r"""Gets the call_number of this CheckCallNumberInConfRequest.

        呼叫号码

        :return: The call_number of this CheckCallNumberInConfRequest.
        :rtype: str
        """
        return self._call_number

    @call_number.setter
    def call_number(self, call_number):
        r"""Sets the call_number of this CheckCallNumberInConfRequest.

        呼叫号码

        :param call_number: The call_number of this CheckCallNumberInConfRequest.
        :type call_number: str
        """
        self._call_number = call_number

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
        if not isinstance(other, CheckCallNumberInConfRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
