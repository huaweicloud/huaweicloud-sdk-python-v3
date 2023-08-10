# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTopicStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_offset': 'int',
        'min_offset': 'int',
        'brokers': 'list[ShowTopicStatusRespBrokers]'
    }

    attribute_map = {
        'max_offset': 'max_offset',
        'min_offset': 'min_offset',
        'brokers': 'brokers'
    }

    def __init__(self, max_offset=None, min_offset=None, brokers=None):
        """ShowTopicStatusResponse

        The model defined in huaweicloud sdk

        :param max_offset: 最大偏移量。
        :type max_offset: int
        :param min_offset: 最小偏移量。
        :type min_offset: int
        :param brokers: 代理。
        :type brokers: list[:class:`huaweicloudsdkrocketmq.v2.ShowTopicStatusRespBrokers`]
        """
        
        super(ShowTopicStatusResponse, self).__init__()

        self._max_offset = None
        self._min_offset = None
        self._brokers = None
        self.discriminator = None

        if max_offset is not None:
            self.max_offset = max_offset
        if min_offset is not None:
            self.min_offset = min_offset
        if brokers is not None:
            self.brokers = brokers

    @property
    def max_offset(self):
        """Gets the max_offset of this ShowTopicStatusResponse.

        最大偏移量。

        :return: The max_offset of this ShowTopicStatusResponse.
        :rtype: int
        """
        return self._max_offset

    @max_offset.setter
    def max_offset(self, max_offset):
        """Sets the max_offset of this ShowTopicStatusResponse.

        最大偏移量。

        :param max_offset: The max_offset of this ShowTopicStatusResponse.
        :type max_offset: int
        """
        self._max_offset = max_offset

    @property
    def min_offset(self):
        """Gets the min_offset of this ShowTopicStatusResponse.

        最小偏移量。

        :return: The min_offset of this ShowTopicStatusResponse.
        :rtype: int
        """
        return self._min_offset

    @min_offset.setter
    def min_offset(self, min_offset):
        """Sets the min_offset of this ShowTopicStatusResponse.

        最小偏移量。

        :param min_offset: The min_offset of this ShowTopicStatusResponse.
        :type min_offset: int
        """
        self._min_offset = min_offset

    @property
    def brokers(self):
        """Gets the brokers of this ShowTopicStatusResponse.

        代理。

        :return: The brokers of this ShowTopicStatusResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.ShowTopicStatusRespBrokers`]
        """
        return self._brokers

    @brokers.setter
    def brokers(self, brokers):
        """Sets the brokers of this ShowTopicStatusResponse.

        代理。

        :param brokers: The brokers of this ShowTopicStatusResponse.
        :type brokers: list[:class:`huaweicloudsdkrocketmq.v2.ShowTopicStatusRespBrokers`]
        """
        self._brokers = brokers

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
        if not isinstance(other, ShowTopicStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
