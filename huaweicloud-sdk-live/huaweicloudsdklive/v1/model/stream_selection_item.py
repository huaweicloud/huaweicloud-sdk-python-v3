# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StreamSelectionItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'max_bandwidth': 'int',
        'min_bandwidth': 'int'
    }

    attribute_map = {
        'key': 'key',
        'max_bandwidth': 'max_bandwidth',
        'min_bandwidth': 'min_bandwidth'
    }

    def __init__(self, key=None, max_bandwidth=None, min_bandwidth=None):
        r"""StreamSelectionItem

        The model defined in huaweicloud sdk

        :param key: 拉流URL中用于码率过滤的参数
        :type key: str
        :param max_bandwidth: 最大码率，单位：bps  取值范围：0 - 104,857,600（100Mbps）
        :type max_bandwidth: int
        :param min_bandwidth: 最小码率，单位：bps  取值范围：0 - 104,857,600（100Mbps）
        :type min_bandwidth: int
        """
        
        

        self._key = None
        self._max_bandwidth = None
        self._min_bandwidth = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if max_bandwidth is not None:
            self.max_bandwidth = max_bandwidth
        if min_bandwidth is not None:
            self.min_bandwidth = min_bandwidth

    @property
    def key(self):
        r"""Gets the key of this StreamSelectionItem.

        拉流URL中用于码率过滤的参数

        :return: The key of this StreamSelectionItem.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this StreamSelectionItem.

        拉流URL中用于码率过滤的参数

        :param key: The key of this StreamSelectionItem.
        :type key: str
        """
        self._key = key

    @property
    def max_bandwidth(self):
        r"""Gets the max_bandwidth of this StreamSelectionItem.

        最大码率，单位：bps  取值范围：0 - 104,857,600（100Mbps）

        :return: The max_bandwidth of this StreamSelectionItem.
        :rtype: int
        """
        return self._max_bandwidth

    @max_bandwidth.setter
    def max_bandwidth(self, max_bandwidth):
        r"""Sets the max_bandwidth of this StreamSelectionItem.

        最大码率，单位：bps  取值范围：0 - 104,857,600（100Mbps）

        :param max_bandwidth: The max_bandwidth of this StreamSelectionItem.
        :type max_bandwidth: int
        """
        self._max_bandwidth = max_bandwidth

    @property
    def min_bandwidth(self):
        r"""Gets the min_bandwidth of this StreamSelectionItem.

        最小码率，单位：bps  取值范围：0 - 104,857,600（100Mbps）

        :return: The min_bandwidth of this StreamSelectionItem.
        :rtype: int
        """
        return self._min_bandwidth

    @min_bandwidth.setter
    def min_bandwidth(self, min_bandwidth):
        r"""Sets the min_bandwidth of this StreamSelectionItem.

        最小码率，单位：bps  取值范围：0 - 104,857,600（100Mbps）

        :param min_bandwidth: The min_bandwidth of this StreamSelectionItem.
        :type min_bandwidth: int
        """
        self._min_bandwidth = min_bandwidth

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
        if not isinstance(other, StreamSelectionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
