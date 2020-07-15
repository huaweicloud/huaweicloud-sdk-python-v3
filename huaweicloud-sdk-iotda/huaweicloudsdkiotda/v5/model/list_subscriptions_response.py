# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListSubscriptionsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'subscriptions': 'list[SubscriptionItem]',
        'count': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'subscriptions': 'subscriptions',
        'count': 'count',
        'marker': 'marker'
    }

    def __init__(self, subscriptions=None, count=None, marker=None):
        """ListSubscriptionsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._subscriptions = None
        self._count = None
        self._marker = None
        self.discriminator = None

        if subscriptions is not None:
            self.subscriptions = subscriptions
        if count is not None:
            self.count = count
        if marker is not None:
            self.marker = marker

    @property
    def subscriptions(self):
        """Gets the subscriptions of this ListSubscriptionsResponse.

        订阅配置信息列表。

        :return: The subscriptions of this ListSubscriptionsResponse.
        :rtype: list[SubscriptionItem]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        """Sets the subscriptions of this ListSubscriptionsResponse.

        订阅配置信息列表。

        :param subscriptions: The subscriptions of this ListSubscriptionsResponse.
        :type: list[SubscriptionItem]
        """
        self._subscriptions = subscriptions

    @property
    def count(self):
        """Gets the count of this ListSubscriptionsResponse.

        满足查询条件的记录总数。

        :return: The count of this ListSubscriptionsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListSubscriptionsResponse.

        满足查询条件的记录总数。

        :param count: The count of this ListSubscriptionsResponse.
        :type: int
        """
        self._count = count

    @property
    def marker(self):
        """Gets the marker of this ListSubscriptionsResponse.

        本次分页查询结果中最后一条记录的ID，可在下一次分页查询时使用。

        :return: The marker of this ListSubscriptionsResponse.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListSubscriptionsResponse.

        本次分页查询结果中最后一条记录的ID，可在下一次分页查询时使用。

        :param marker: The marker of this ListSubscriptionsResponse.
        :type: str
        """
        self._marker = marker

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSubscriptionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
