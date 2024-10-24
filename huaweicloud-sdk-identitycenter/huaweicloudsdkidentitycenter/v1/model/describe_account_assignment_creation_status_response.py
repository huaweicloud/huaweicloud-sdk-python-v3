# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DescribeAccountAssignmentCreationStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_assignment_creation_status': 'AccountAssignmentOperationStatusDto'
    }

    attribute_map = {
        'account_assignment_creation_status': 'account_assignment_creation_status'
    }

    def __init__(self, account_assignment_creation_status=None):
        """DescribeAccountAssignmentCreationStatusResponse

        The model defined in huaweicloud sdk

        :param account_assignment_creation_status: 
        :type account_assignment_creation_status: :class:`huaweicloudsdkidentitycenter.v1.AccountAssignmentOperationStatusDto`
        """
        
        super(DescribeAccountAssignmentCreationStatusResponse, self).__init__()

        self._account_assignment_creation_status = None
        self.discriminator = None

        if account_assignment_creation_status is not None:
            self.account_assignment_creation_status = account_assignment_creation_status

    @property
    def account_assignment_creation_status(self):
        """Gets the account_assignment_creation_status of this DescribeAccountAssignmentCreationStatusResponse.

        :return: The account_assignment_creation_status of this DescribeAccountAssignmentCreationStatusResponse.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.AccountAssignmentOperationStatusDto`
        """
        return self._account_assignment_creation_status

    @account_assignment_creation_status.setter
    def account_assignment_creation_status(self, account_assignment_creation_status):
        """Sets the account_assignment_creation_status of this DescribeAccountAssignmentCreationStatusResponse.

        :param account_assignment_creation_status: The account_assignment_creation_status of this DescribeAccountAssignmentCreationStatusResponse.
        :type account_assignment_creation_status: :class:`huaweicloudsdkidentitycenter.v1.AccountAssignmentOperationStatusDto`
        """
        self._account_assignment_creation_status = account_assignment_creation_status

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
        if not isinstance(other, DescribeAccountAssignmentCreationStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
