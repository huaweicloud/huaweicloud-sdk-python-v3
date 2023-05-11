# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomersBalancesDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_balances': 'list[CustomerBalancesV2]'
    }

    attribute_map = {
        'customer_balances': 'customer_balances'
    }

    def __init__(self, customer_balances=None):
        """ListCustomersBalancesDetailResponse

        The model defined in huaweicloud sdk

        :param customer_balances: 账户余额列表。只有成功的时候才返回。 此列表不包含非代售类子客户的数据。批量查询客户余额时，若入参携带了非代售类子客户，会被过滤。 具体请参见表2。
        :type customer_balances: list[:class:`huaweicloudsdkbss.v2.CustomerBalancesV2`]
        """
        
        super(ListCustomersBalancesDetailResponse, self).__init__()

        self._customer_balances = None
        self.discriminator = None

        if customer_balances is not None:
            self.customer_balances = customer_balances

    @property
    def customer_balances(self):
        """Gets the customer_balances of this ListCustomersBalancesDetailResponse.

        账户余额列表。只有成功的时候才返回。 此列表不包含非代售类子客户的数据。批量查询客户余额时，若入参携带了非代售类子客户，会被过滤。 具体请参见表2。

        :return: The customer_balances of this ListCustomersBalancesDetailResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.CustomerBalancesV2`]
        """
        return self._customer_balances

    @customer_balances.setter
    def customer_balances(self, customer_balances):
        """Sets the customer_balances of this ListCustomersBalancesDetailResponse.

        账户余额列表。只有成功的时候才返回。 此列表不包含非代售类子客户的数据。批量查询客户余额时，若入参携带了非代售类子客户，会被过滤。 具体请参见表2。

        :param customer_balances: The customer_balances of this ListCustomersBalancesDetailResponse.
        :type customer_balances: list[:class:`huaweicloudsdkbss.v2.CustomerBalancesV2`]
        """
        self._customer_balances = customer_balances

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
        if not isinstance(other, ListCustomersBalancesDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
