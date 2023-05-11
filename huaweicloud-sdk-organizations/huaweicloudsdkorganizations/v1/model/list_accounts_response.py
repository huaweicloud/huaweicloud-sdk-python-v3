# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccountsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'accounts': 'list[AccountDto]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'accounts': 'accounts',
        'page_info': 'page_info'
    }

    def __init__(self, accounts=None, page_info=None):
        """ListAccountsResponse

        The model defined in huaweicloud sdk

        :param accounts: 组织中的帐号列表。
        :type accounts: list[:class:`huaweicloudsdkorganizations.v1.AccountDto`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        
        super(ListAccountsResponse, self).__init__()

        self._accounts = None
        self._page_info = None
        self.discriminator = None

        if accounts is not None:
            self.accounts = accounts
        if page_info is not None:
            self.page_info = page_info

    @property
    def accounts(self):
        """Gets the accounts of this ListAccountsResponse.

        组织中的帐号列表。

        :return: The accounts of this ListAccountsResponse.
        :rtype: list[:class:`huaweicloudsdkorganizations.v1.AccountDto`]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this ListAccountsResponse.

        组织中的帐号列表。

        :param accounts: The accounts of this ListAccountsResponse.
        :type accounts: list[:class:`huaweicloudsdkorganizations.v1.AccountDto`]
        """
        self._accounts = accounts

    @property
    def page_info(self):
        """Gets the page_info of this ListAccountsResponse.

        :return: The page_info of this ListAccountsResponse.
        :rtype: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListAccountsResponse.

        :param page_info: The page_info of this ListAccountsResponse.
        :type page_info: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListAccountsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
