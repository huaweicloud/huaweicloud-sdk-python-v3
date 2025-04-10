# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FailoverModeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mode': 'str'
    }

    attribute_map = {
        'mode': 'mode'
    }

    def __init__(self, mode=None):
        r"""FailoverModeRequest

        The model defined in huaweicloud sdk

        :param mode: 同步模式，各引擎可选择方式具体如下： MySQL： - async：异步。 - semisync：半同步。
        :type mode: str
        """
        
        

        self._mode = None
        self.discriminator = None

        self.mode = mode

    @property
    def mode(self):
        r"""Gets the mode of this FailoverModeRequest.

        同步模式，各引擎可选择方式具体如下： MySQL： - async：异步。 - semisync：半同步。

        :return: The mode of this FailoverModeRequest.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this FailoverModeRequest.

        同步模式，各引擎可选择方式具体如下： MySQL： - async：异步。 - semisync：半同步。

        :param mode: The mode of this FailoverModeRequest.
        :type mode: str
        """
        self._mode = mode

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
        if not isinstance(other, FailoverModeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
