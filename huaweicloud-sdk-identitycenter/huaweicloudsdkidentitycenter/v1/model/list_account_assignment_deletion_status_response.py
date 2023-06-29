# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccountAssignmentDeletionStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_assignments_deletion_status': 'list[AccountAssignmentOperationStatusMetadataDto]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'account_assignments_deletion_status': 'account_assignments_deletion_status',
        'page_info': 'page_info'
    }

    def __init__(self, account_assignments_deletion_status=None, page_info=None):
        """ListAccountAssignmentDeletionStatusResponse

        The model defined in huaweicloud sdk

        :param account_assignments_deletion_status: 操作状态集合
        :type account_assignments_deletion_status: list[:class:`huaweicloudsdkidentitycenter.v1.AccountAssignmentOperationStatusMetadataDto`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
        """
        
        super(ListAccountAssignmentDeletionStatusResponse, self).__init__()

        self._account_assignments_deletion_status = None
        self._page_info = None
        self.discriminator = None

        if account_assignments_deletion_status is not None:
            self.account_assignments_deletion_status = account_assignments_deletion_status
        if page_info is not None:
            self.page_info = page_info

    @property
    def account_assignments_deletion_status(self):
        """Gets the account_assignments_deletion_status of this ListAccountAssignmentDeletionStatusResponse.

        操作状态集合

        :return: The account_assignments_deletion_status of this ListAccountAssignmentDeletionStatusResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenter.v1.AccountAssignmentOperationStatusMetadataDto`]
        """
        return self._account_assignments_deletion_status

    @account_assignments_deletion_status.setter
    def account_assignments_deletion_status(self, account_assignments_deletion_status):
        """Sets the account_assignments_deletion_status of this ListAccountAssignmentDeletionStatusResponse.

        操作状态集合

        :param account_assignments_deletion_status: The account_assignments_deletion_status of this ListAccountAssignmentDeletionStatusResponse.
        :type account_assignments_deletion_status: list[:class:`huaweicloudsdkidentitycenter.v1.AccountAssignmentOperationStatusMetadataDto`]
        """
        self._account_assignments_deletion_status = account_assignments_deletion_status

    @property
    def page_info(self):
        """Gets the page_info of this ListAccountAssignmentDeletionStatusResponse.

        :return: The page_info of this ListAccountAssignmentDeletionStatusResponse.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListAccountAssignmentDeletionStatusResponse.

        :param page_info: The page_info of this ListAccountAssignmentDeletionStatusResponse.
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
        if not isinstance(other, ListAccountAssignmentDeletionStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
