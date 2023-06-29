# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccountAssignmentsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_assignments': 'list[AccountAssignmentDto]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'account_assignments': 'account_assignments',
        'page_info': 'page_info'
    }

    def __init__(self, account_assignments=None, page_info=None):
        """ListAccountAssignmentsResponse

        The model defined in huaweicloud sdk

        :param account_assignments: 与输入帐户和权限集匹配的工作分配列表
        :type account_assignments: list[:class:`huaweicloudsdkidentitycenter.v1.AccountAssignmentDto`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
        """
        
        super(ListAccountAssignmentsResponse, self).__init__()

        self._account_assignments = None
        self._page_info = None
        self.discriminator = None

        if account_assignments is not None:
            self.account_assignments = account_assignments
        if page_info is not None:
            self.page_info = page_info

    @property
    def account_assignments(self):
        """Gets the account_assignments of this ListAccountAssignmentsResponse.

        与输入帐户和权限集匹配的工作分配列表

        :return: The account_assignments of this ListAccountAssignmentsResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenter.v1.AccountAssignmentDto`]
        """
        return self._account_assignments

    @account_assignments.setter
    def account_assignments(self, account_assignments):
        """Sets the account_assignments of this ListAccountAssignmentsResponse.

        与输入帐户和权限集匹配的工作分配列表

        :param account_assignments: The account_assignments of this ListAccountAssignmentsResponse.
        :type account_assignments: list[:class:`huaweicloudsdkidentitycenter.v1.AccountAssignmentDto`]
        """
        self._account_assignments = account_assignments

    @property
    def page_info(self):
        """Gets the page_info of this ListAccountAssignmentsResponse.

        :return: The page_info of this ListAccountAssignmentsResponse.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListAccountAssignmentsResponse.

        :param page_info: The page_info of this ListAccountAssignmentsResponse.
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
        if not isinstance(other, ListAccountAssignmentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
