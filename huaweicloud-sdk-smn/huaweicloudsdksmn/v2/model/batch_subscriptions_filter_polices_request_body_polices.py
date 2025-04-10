# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSubscriptionsFilterPolicesRequestBodyPolices:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subscription_urn': 'str',
        'filter_polices': 'list[SubscriptionsFilterPolicy]'
    }

    attribute_map = {
        'subscription_urn': 'subscription_urn',
        'filter_polices': 'filter_polices'
    }

    def __init__(self, subscription_urn=None, filter_polices=None):
        r"""BatchSubscriptionsFilterPolicesRequestBodyPolices

        The model defined in huaweicloud sdk

        :param subscription_urn: 订阅者的唯一的资源标识，可通过[查询订阅者列表](ListSubscriptions.xml)获取该标识。
        :type subscription_urn: str
        :param filter_polices: 订阅者的过滤策略。策略name不能重复
        :type filter_polices: list[:class:`huaweicloudsdksmn.v2.SubscriptionsFilterPolicy`]
        """
        
        

        self._subscription_urn = None
        self._filter_polices = None
        self.discriminator = None

        self.subscription_urn = subscription_urn
        self.filter_polices = filter_polices

    @property
    def subscription_urn(self):
        r"""Gets the subscription_urn of this BatchSubscriptionsFilterPolicesRequestBodyPolices.

        订阅者的唯一的资源标识，可通过[查询订阅者列表](ListSubscriptions.xml)获取该标识。

        :return: The subscription_urn of this BatchSubscriptionsFilterPolicesRequestBodyPolices.
        :rtype: str
        """
        return self._subscription_urn

    @subscription_urn.setter
    def subscription_urn(self, subscription_urn):
        r"""Sets the subscription_urn of this BatchSubscriptionsFilterPolicesRequestBodyPolices.

        订阅者的唯一的资源标识，可通过[查询订阅者列表](ListSubscriptions.xml)获取该标识。

        :param subscription_urn: The subscription_urn of this BatchSubscriptionsFilterPolicesRequestBodyPolices.
        :type subscription_urn: str
        """
        self._subscription_urn = subscription_urn

    @property
    def filter_polices(self):
        r"""Gets the filter_polices of this BatchSubscriptionsFilterPolicesRequestBodyPolices.

        订阅者的过滤策略。策略name不能重复

        :return: The filter_polices of this BatchSubscriptionsFilterPolicesRequestBodyPolices.
        :rtype: list[:class:`huaweicloudsdksmn.v2.SubscriptionsFilterPolicy`]
        """
        return self._filter_polices

    @filter_polices.setter
    def filter_polices(self, filter_polices):
        r"""Sets the filter_polices of this BatchSubscriptionsFilterPolicesRequestBodyPolices.

        订阅者的过滤策略。策略name不能重复

        :param filter_polices: The filter_polices of this BatchSubscriptionsFilterPolicesRequestBodyPolices.
        :type filter_polices: list[:class:`huaweicloudsdksmn.v2.SubscriptionsFilterPolicy`]
        """
        self._filter_polices = filter_polices

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
        if not isinstance(other, BatchSubscriptionsFilterPolicesRequestBodyPolices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
