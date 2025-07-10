# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListManagedAccountsForParentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'managed_accounts': 'list[ManagedAccount]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'managed_accounts': 'managed_accounts',
        'page_info': 'page_info'
    }

    def __init__(self, managed_accounts=None, page_info=None):
        r"""ListManagedAccountsForParentResponse

        The model defined in huaweicloud sdk

        :param managed_accounts: 纳管的账号信息。
        :type managed_accounts: list[:class:`huaweicloudsdkrgc.v1.ManagedAccount`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkrgc.v1.PageInfoDto`
        """
        
        super(ListManagedAccountsForParentResponse, self).__init__()

        self._managed_accounts = None
        self._page_info = None
        self.discriminator = None

        if managed_accounts is not None:
            self.managed_accounts = managed_accounts
        if page_info is not None:
            self.page_info = page_info

    @property
    def managed_accounts(self):
        r"""Gets the managed_accounts of this ListManagedAccountsForParentResponse.

        纳管的账号信息。

        :return: The managed_accounts of this ListManagedAccountsForParentResponse.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.ManagedAccount`]
        """
        return self._managed_accounts

    @managed_accounts.setter
    def managed_accounts(self, managed_accounts):
        r"""Sets the managed_accounts of this ListManagedAccountsForParentResponse.

        纳管的账号信息。

        :param managed_accounts: The managed_accounts of this ListManagedAccountsForParentResponse.
        :type managed_accounts: list[:class:`huaweicloudsdkrgc.v1.ManagedAccount`]
        """
        self._managed_accounts = managed_accounts

    @property
    def page_info(self):
        r"""Gets the page_info of this ListManagedAccountsForParentResponse.

        :return: The page_info of this ListManagedAccountsForParentResponse.
        :rtype: :class:`huaweicloudsdkrgc.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListManagedAccountsForParentResponse.

        :param page_info: The page_info of this ListManagedAccountsForParentResponse.
        :type page_info: :class:`huaweicloudsdkrgc.v1.PageInfoDto`
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
        if not isinstance(other, ListManagedAccountsForParentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
