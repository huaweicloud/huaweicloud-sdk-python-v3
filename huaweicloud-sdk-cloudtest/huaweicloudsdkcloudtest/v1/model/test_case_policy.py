# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestCasePolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'failed_times': 'int',
        'retry_times': 'int'
    }

    attribute_map = {
        'failed_times': 'failed_times',
        'retry_times': 'retryTimes'
    }

    def __init__(self, failed_times=None, retry_times=None):
        r"""TestCasePolicy

        The model defined in huaweicloud sdk

        :param failed_times: 单用例失败多少次告警
        :type failed_times: int
        :param retry_times: 单用例重试多少次后告警
        :type retry_times: int
        """
        
        

        self._failed_times = None
        self._retry_times = None
        self.discriminator = None

        if failed_times is not None:
            self.failed_times = failed_times
        if retry_times is not None:
            self.retry_times = retry_times

    @property
    def failed_times(self):
        r"""Gets the failed_times of this TestCasePolicy.

        单用例失败多少次告警

        :return: The failed_times of this TestCasePolicy.
        :rtype: int
        """
        return self._failed_times

    @failed_times.setter
    def failed_times(self, failed_times):
        r"""Sets the failed_times of this TestCasePolicy.

        单用例失败多少次告警

        :param failed_times: The failed_times of this TestCasePolicy.
        :type failed_times: int
        """
        self._failed_times = failed_times

    @property
    def retry_times(self):
        r"""Gets the retry_times of this TestCasePolicy.

        单用例重试多少次后告警

        :return: The retry_times of this TestCasePolicy.
        :rtype: int
        """
        return self._retry_times

    @retry_times.setter
    def retry_times(self, retry_times):
        r"""Sets the retry_times of this TestCasePolicy.

        单用例重试多少次后告警

        :param retry_times: The retry_times of this TestCasePolicy.
        :type retry_times: int
        """
        self._retry_times = retry_times

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
        if not isinstance(other, TestCasePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
