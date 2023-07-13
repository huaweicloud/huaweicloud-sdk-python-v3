# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccountsForProvisionedPermissionSetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_ids': 'list[str]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'account_ids': 'account_ids',
        'page_info': 'page_info'
    }

    def __init__(self, account_ids=None, page_info=None):
        """ListAccountsForProvisionedPermissionSetResponse

        The model defined in huaweicloud sdk

        :param account_ids: 
        :type account_ids: list[str]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
        """
        
        super(ListAccountsForProvisionedPermissionSetResponse, self).__init__()

        self._account_ids = None
        self._page_info = None
        self.discriminator = None

        if account_ids is not None:
            self.account_ids = account_ids
        if page_info is not None:
            self.page_info = page_info

    @property
    def account_ids(self):
        """Gets the account_ids of this ListAccountsForProvisionedPermissionSetResponse.

        :return: The account_ids of this ListAccountsForProvisionedPermissionSetResponse.
        :rtype: list[str]
        """
        return self._account_ids

    @account_ids.setter
    def account_ids(self, account_ids):
        """Sets the account_ids of this ListAccountsForProvisionedPermissionSetResponse.

        :param account_ids: The account_ids of this ListAccountsForProvisionedPermissionSetResponse.
        :type account_ids: list[str]
        """
        self._account_ids = account_ids

    @property
    def page_info(self):
        """Gets the page_info of this ListAccountsForProvisionedPermissionSetResponse.

        :return: The page_info of this ListAccountsForProvisionedPermissionSetResponse.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListAccountsForProvisionedPermissionSetResponse.

        :param page_info: The page_info of this ListAccountsForProvisionedPermissionSetResponse.
        :type page_info: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
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
        if not isinstance(other, ListAccountsForProvisionedPermissionSetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
