# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIncentiveDiscountPoliciesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'policies': 'list[IncentiveAndDiscountPolicy]',
        'total_count': 'int'
    }

    attribute_map = {
        'policies': 'policies',
        'total_count': 'total_count'
    }

    def __init__(self, policies=None, total_count=None):
        """ListIncentiveDiscountPoliciesResponse

        The model defined in huaweicloud sdk

        :param policies: 产品折扣和激励策略信息列表。 具体请参见表2。
        :type policies: list[:class:`huaweicloudsdkbss.v2.IncentiveAndDiscountPolicy`]
        :param total_count: 查询总条数。
        :type total_count: int
        """
        
        super(ListIncentiveDiscountPoliciesResponse, self).__init__()

        self._policies = None
        self._total_count = None
        self.discriminator = None

        if policies is not None:
            self.policies = policies
        if total_count is not None:
            self.total_count = total_count

    @property
    def policies(self):
        """Gets the policies of this ListIncentiveDiscountPoliciesResponse.

        产品折扣和激励策略信息列表。 具体请参见表2。

        :return: The policies of this ListIncentiveDiscountPoliciesResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.IncentiveAndDiscountPolicy`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this ListIncentiveDiscountPoliciesResponse.

        产品折扣和激励策略信息列表。 具体请参见表2。

        :param policies: The policies of this ListIncentiveDiscountPoliciesResponse.
        :type policies: list[:class:`huaweicloudsdkbss.v2.IncentiveAndDiscountPolicy`]
        """
        self._policies = policies

    @property
    def total_count(self):
        """Gets the total_count of this ListIncentiveDiscountPoliciesResponse.

        查询总条数。

        :return: The total_count of this ListIncentiveDiscountPoliciesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListIncentiveDiscountPoliciesResponse.

        查询总条数。

        :param total_count: The total_count of this ListIncentiveDiscountPoliciesResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListIncentiveDiscountPoliciesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
