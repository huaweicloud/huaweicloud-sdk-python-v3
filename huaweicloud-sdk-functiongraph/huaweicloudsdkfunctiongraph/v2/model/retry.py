# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Retry:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'delay': 'int',
        'max_attempts': 'int'
    }

    attribute_map = {
        'name': 'name',
        'delay': 'delay',
        'max_attempts': 'max_attempts'
    }

    def __init__(self, name=None, delay=None, max_attempts=None):
        """Retry

        The model defined in huaweicloud sdk

        :param name: 重试策略名称，在单个流程中，名称需要唯一
        :type name: str
        :param delay: 重试间隔，单位：秒。若不传，默认为1
        :type delay: int
        :param max_attempts: 最大重试次数，。若不传，默认为3
        :type max_attempts: int
        """
        
        

        self._name = None
        self._delay = None
        self._max_attempts = None
        self.discriminator = None

        self.name = name
        if delay is not None:
            self.delay = delay
        if max_attempts is not None:
            self.max_attempts = max_attempts

    @property
    def name(self):
        """Gets the name of this Retry.

        重试策略名称，在单个流程中，名称需要唯一

        :return: The name of this Retry.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Retry.

        重试策略名称，在单个流程中，名称需要唯一

        :param name: The name of this Retry.
        :type name: str
        """
        self._name = name

    @property
    def delay(self):
        """Gets the delay of this Retry.

        重试间隔，单位：秒。若不传，默认为1

        :return: The delay of this Retry.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this Retry.

        重试间隔，单位：秒。若不传，默认为1

        :param delay: The delay of this Retry.
        :type delay: int
        """
        self._delay = delay

    @property
    def max_attempts(self):
        """Gets the max_attempts of this Retry.

        最大重试次数，。若不传，默认为3

        :return: The max_attempts of this Retry.
        :rtype: int
        """
        return self._max_attempts

    @max_attempts.setter
    def max_attempts(self, max_attempts):
        """Sets the max_attempts of this Retry.

        最大重试次数，。若不传，默认为3

        :param max_attempts: The max_attempts of this Retry.
        :type max_attempts: int
        """
        self._max_attempts = max_attempts

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
        if not isinstance(other, Retry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
