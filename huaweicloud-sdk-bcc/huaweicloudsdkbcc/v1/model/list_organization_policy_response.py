# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOrganizationPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'bcc_organization_policies': 'list[BccOrganizationPolicy]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'count': 'count',
        'bcc_organization_policies': 'bcc_organization_policies',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, count=None, bcc_organization_policies=None, x_request_id=None):
        r"""ListOrganizationPolicyResponse

        The model defined in huaweicloud sdk

        :param count: count
        :type count: int
        :param bcc_organization_policies: bccOrganizationPolicies
        :type bcc_organization_policies: list[:class:`huaweicloudsdkbcc.v1.BccOrganizationPolicy`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListOrganizationPolicyResponse, self).__init__()

        self._count = None
        self._bcc_organization_policies = None
        self._x_request_id = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if bcc_organization_policies is not None:
            self.bcc_organization_policies = bcc_organization_policies
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def count(self):
        r"""Gets the count of this ListOrganizationPolicyResponse.

        count

        :return: The count of this ListOrganizationPolicyResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListOrganizationPolicyResponse.

        count

        :param count: The count of this ListOrganizationPolicyResponse.
        :type count: int
        """
        self._count = count

    @property
    def bcc_organization_policies(self):
        r"""Gets the bcc_organization_policies of this ListOrganizationPolicyResponse.

        bccOrganizationPolicies

        :return: The bcc_organization_policies of this ListOrganizationPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.BccOrganizationPolicy`]
        """
        return self._bcc_organization_policies

    @bcc_organization_policies.setter
    def bcc_organization_policies(self, bcc_organization_policies):
        r"""Sets the bcc_organization_policies of this ListOrganizationPolicyResponse.

        bccOrganizationPolicies

        :param bcc_organization_policies: The bcc_organization_policies of this ListOrganizationPolicyResponse.
        :type bcc_organization_policies: list[:class:`huaweicloudsdkbcc.v1.BccOrganizationPolicy`]
        """
        self._bcc_organization_policies = bcc_organization_policies

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListOrganizationPolicyResponse.

        :return: The x_request_id of this ListOrganizationPolicyResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListOrganizationPolicyResponse.

        :param x_request_id: The x_request_id of this ListOrganizationPolicyResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListOrganizationPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
