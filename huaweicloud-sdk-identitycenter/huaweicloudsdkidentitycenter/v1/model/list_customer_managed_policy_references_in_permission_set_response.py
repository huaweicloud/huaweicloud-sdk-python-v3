# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomerManagedPolicyReferencesInPermissionSetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_managed_policy_references': 'list[CustomerManagedPolicyReferenceDto]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'customer_managed_policy_references': 'customer_managed_policy_references',
        'page_info': 'page_info'
    }

    def __init__(self, customer_managed_policy_references=None, page_info=None):
        """ListCustomerManagedPolicyReferencesInPermissionSetResponse

        The model defined in huaweicloud sdk

        :param customer_managed_policy_references: 指定附加到权限集的客户管理策略的名称和路径.
        :type customer_managed_policy_references: list[:class:`huaweicloudsdkidentitycenter.v1.CustomerManagedPolicyReferenceDto`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
        """
        
        super(ListCustomerManagedPolicyReferencesInPermissionSetResponse, self).__init__()

        self._customer_managed_policy_references = None
        self._page_info = None
        self.discriminator = None

        if customer_managed_policy_references is not None:
            self.customer_managed_policy_references = customer_managed_policy_references
        if page_info is not None:
            self.page_info = page_info

    @property
    def customer_managed_policy_references(self):
        """Gets the customer_managed_policy_references of this ListCustomerManagedPolicyReferencesInPermissionSetResponse.

        指定附加到权限集的客户管理策略的名称和路径.

        :return: The customer_managed_policy_references of this ListCustomerManagedPolicyReferencesInPermissionSetResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenter.v1.CustomerManagedPolicyReferenceDto`]
        """
        return self._customer_managed_policy_references

    @customer_managed_policy_references.setter
    def customer_managed_policy_references(self, customer_managed_policy_references):
        """Sets the customer_managed_policy_references of this ListCustomerManagedPolicyReferencesInPermissionSetResponse.

        指定附加到权限集的客户管理策略的名称和路径.

        :param customer_managed_policy_references: The customer_managed_policy_references of this ListCustomerManagedPolicyReferencesInPermissionSetResponse.
        :type customer_managed_policy_references: list[:class:`huaweicloudsdkidentitycenter.v1.CustomerManagedPolicyReferenceDto`]
        """
        self._customer_managed_policy_references = customer_managed_policy_references

    @property
    def page_info(self):
        """Gets the page_info of this ListCustomerManagedPolicyReferencesInPermissionSetResponse.

        :return: The page_info of this ListCustomerManagedPolicyReferencesInPermissionSetResponse.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListCustomerManagedPolicyReferencesInPermissionSetResponse.

        :param page_info: The page_info of this ListCustomerManagedPolicyReferencesInPermissionSetResponse.
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
        if not isinstance(other, ListCustomerManagedPolicyReferencesInPermissionSetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
