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
        'account_list': 'list[AccountInfo]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'account_list': 'account_list',
        'page_info': 'page_info'
    }

    def __init__(self, account_list=None, page_info=None):
        r"""ListAccountsResponse

        The model defined in huaweicloud sdk

        :param account_list: 满足查询条件的账号对象列表
        :type account_list: list[:class:`huaweicloudsdkidentitycenterportalapi.v1.AccountInfo`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkidentitycenterportalapi.v1.PageInfoDto`
        """
        
        super(ListAccountsResponse, self).__init__()

        self._account_list = None
        self._page_info = None
        self.discriminator = None

        if account_list is not None:
            self.account_list = account_list
        if page_info is not None:
            self.page_info = page_info

    @property
    def account_list(self):
        r"""Gets the account_list of this ListAccountsResponse.

        满足查询条件的账号对象列表

        :return: The account_list of this ListAccountsResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenterportalapi.v1.AccountInfo`]
        """
        return self._account_list

    @account_list.setter
    def account_list(self, account_list):
        r"""Sets the account_list of this ListAccountsResponse.

        满足查询条件的账号对象列表

        :param account_list: The account_list of this ListAccountsResponse.
        :type account_list: list[:class:`huaweicloudsdkidentitycenterportalapi.v1.AccountInfo`]
        """
        self._account_list = account_list

    @property
    def page_info(self):
        r"""Gets the page_info of this ListAccountsResponse.

        :return: The page_info of this ListAccountsResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterportalapi.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListAccountsResponse.

        :param page_info: The page_info of this ListAccountsResponse.
        :type page_info: :class:`huaweicloudsdkidentitycenterportalapi.v1.PageInfoDto`
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
