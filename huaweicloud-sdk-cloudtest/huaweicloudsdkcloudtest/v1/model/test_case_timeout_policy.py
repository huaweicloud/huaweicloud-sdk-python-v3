# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestCaseTimeoutPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'timeout_times': 'int'
    }

    attribute_map = {
        'timeout_times': 'timeoutTimes'
    }

    def __init__(self, timeout_times=None):
        r"""TestCaseTimeoutPolicy

        The model defined in huaweicloud sdk

        :param timeout_times: 用例超时多少次告警
        :type timeout_times: int
        """
        
        

        self._timeout_times = None
        self.discriminator = None

        if timeout_times is not None:
            self.timeout_times = timeout_times

    @property
    def timeout_times(self):
        r"""Gets the timeout_times of this TestCaseTimeoutPolicy.

        用例超时多少次告警

        :return: The timeout_times of this TestCaseTimeoutPolicy.
        :rtype: int
        """
        return self._timeout_times

    @timeout_times.setter
    def timeout_times(self, timeout_times):
        r"""Sets the timeout_times of this TestCaseTimeoutPolicy.

        用例超时多少次告警

        :param timeout_times: The timeout_times of this TestCaseTimeoutPolicy.
        :type timeout_times: int
        """
        self._timeout_times = timeout_times

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
        if not isinstance(other, TestCaseTimeoutPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
