# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BloomFilterConf:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'behaviors': 'list[str]',
        'interval': 'int'
    }

    attribute_map = {
        'behaviors': 'behaviors',
        'interval': 'interval'
    }

    def __init__(self, behaviors=None, interval=None):
        """BloomFilterConf

        The model defined in huaweicloud sdk

        :param behaviors: 待过滤行为类型。
        :type behaviors: list[str]
        :param interval: 过滤时间。
        :type interval: int
        """
        
        

        self._behaviors = None
        self._interval = None
        self.discriminator = None

        if behaviors is not None:
            self.behaviors = behaviors
        if interval is not None:
            self.interval = interval

    @property
    def behaviors(self):
        """Gets the behaviors of this BloomFilterConf.

        待过滤行为类型。

        :return: The behaviors of this BloomFilterConf.
        :rtype: list[str]
        """
        return self._behaviors

    @behaviors.setter
    def behaviors(self, behaviors):
        """Sets the behaviors of this BloomFilterConf.

        待过滤行为类型。

        :param behaviors: The behaviors of this BloomFilterConf.
        :type behaviors: list[str]
        """
        self._behaviors = behaviors

    @property
    def interval(self):
        """Gets the interval of this BloomFilterConf.

        过滤时间。

        :return: The interval of this BloomFilterConf.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this BloomFilterConf.

        过滤时间。

        :param interval: The interval of this BloomFilterConf.
        :type interval: int
        """
        self._interval = interval

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
        if not isinstance(other, BloomFilterConf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
