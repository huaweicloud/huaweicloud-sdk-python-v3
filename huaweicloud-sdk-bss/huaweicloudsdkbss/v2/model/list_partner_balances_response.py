# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPartnerBalancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_balances': 'list[AccountBalanceV2]'
    }

    attribute_map = {
        'account_balances': 'account_balances'
    }

    def __init__(self, account_balances=None):
        """ListPartnerBalancesResponse

        The model defined in huaweicloud sdk

        :param account_balances: 账户余额列表。 具体请参见表2
        :type account_balances: list[:class:`huaweicloudsdkbss.v2.AccountBalanceV2`]
        """
        
        super(ListPartnerBalancesResponse, self).__init__()

        self._account_balances = None
        self.discriminator = None

        if account_balances is not None:
            self.account_balances = account_balances

    @property
    def account_balances(self):
        """Gets the account_balances of this ListPartnerBalancesResponse.

        账户余额列表。 具体请参见表2

        :return: The account_balances of this ListPartnerBalancesResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.AccountBalanceV2`]
        """
        return self._account_balances

    @account_balances.setter
    def account_balances(self, account_balances):
        """Sets the account_balances of this ListPartnerBalancesResponse.

        账户余额列表。 具体请参见表2

        :param account_balances: The account_balances of this ListPartnerBalancesResponse.
        :type account_balances: list[:class:`huaweicloudsdkbss.v2.AccountBalanceV2`]
        """
        self._account_balances = account_balances

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
        if not isinstance(other, ListPartnerBalancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
