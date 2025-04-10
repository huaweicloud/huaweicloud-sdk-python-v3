# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlavorSellPoliciesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'sell_policies': 'list[ListFlavorSellPoliciesResult]'
    }

    attribute_map = {
        'count': 'count',
        'sell_policies': 'sell_policies'
    }

    def __init__(self, count=None, sell_policies=None):
        r"""ListFlavorSellPoliciesResponse

        The model defined in huaweicloud sdk

        :param count: 云服务器规格销售策略数量。
        :type count: int
        :param sell_policies: 云服务器规格销售策略。
        :type sell_policies: list[:class:`huaweicloudsdkecs.v2.ListFlavorSellPoliciesResult`]
        """
        
        super(ListFlavorSellPoliciesResponse, self).__init__()

        self._count = None
        self._sell_policies = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if sell_policies is not None:
            self.sell_policies = sell_policies

    @property
    def count(self):
        r"""Gets the count of this ListFlavorSellPoliciesResponse.

        云服务器规格销售策略数量。

        :return: The count of this ListFlavorSellPoliciesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListFlavorSellPoliciesResponse.

        云服务器规格销售策略数量。

        :param count: The count of this ListFlavorSellPoliciesResponse.
        :type count: int
        """
        self._count = count

    @property
    def sell_policies(self):
        r"""Gets the sell_policies of this ListFlavorSellPoliciesResponse.

        云服务器规格销售策略。

        :return: The sell_policies of this ListFlavorSellPoliciesResponse.
        :rtype: list[:class:`huaweicloudsdkecs.v2.ListFlavorSellPoliciesResult`]
        """
        return self._sell_policies

    @sell_policies.setter
    def sell_policies(self, sell_policies):
        r"""Sets the sell_policies of this ListFlavorSellPoliciesResponse.

        云服务器规格销售策略。

        :param sell_policies: The sell_policies of this ListFlavorSellPoliciesResponse.
        :type sell_policies: list[:class:`huaweicloudsdkecs.v2.ListFlavorSellPoliciesResult`]
        """
        self._sell_policies = sell_policies

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
        if not isinstance(other, ListFlavorSellPoliciesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
