# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionOperateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subscription_ids': 'list[str]',
        'operation': 'str'
    }

    attribute_map = {
        'subscription_ids': 'subscription_ids',
        'operation': 'operation'
    }

    def __init__(self, subscription_ids=None, operation=None):
        r"""SubscriptionOperateReq

        The model defined in huaweicloud sdk

        :param subscription_ids: 订阅对象ID列表，单次批量操作最多支持10个订阅
        :type subscription_ids: list[str]
        :param operation: 操作类型
        :type operation: str
        """
        
        

        self._subscription_ids = None
        self._operation = None
        self.discriminator = None

        if subscription_ids is not None:
            self.subscription_ids = subscription_ids
        if operation is not None:
            self.operation = operation

    @property
    def subscription_ids(self):
        r"""Gets the subscription_ids of this SubscriptionOperateReq.

        订阅对象ID列表，单次批量操作最多支持10个订阅

        :return: The subscription_ids of this SubscriptionOperateReq.
        :rtype: list[str]
        """
        return self._subscription_ids

    @subscription_ids.setter
    def subscription_ids(self, subscription_ids):
        r"""Sets the subscription_ids of this SubscriptionOperateReq.

        订阅对象ID列表，单次批量操作最多支持10个订阅

        :param subscription_ids: The subscription_ids of this SubscriptionOperateReq.
        :type subscription_ids: list[str]
        """
        self._subscription_ids = subscription_ids

    @property
    def operation(self):
        r"""Gets the operation of this SubscriptionOperateReq.

        操作类型

        :return: The operation of this SubscriptionOperateReq.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this SubscriptionOperateReq.

        操作类型

        :param operation: The operation of this SubscriptionOperateReq.
        :type operation: str
        """
        self._operation = operation

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
        if not isinstance(other, SubscriptionOperateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
