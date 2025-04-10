# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListManagedPoliciesInPermissionSetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attached_managed_policies': 'list[AttachedManagedPolicyDto]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'attached_managed_policies': 'attached_managed_policies',
        'page_info': 'page_info'
    }

    def __init__(self, attached_managed_policies=None, page_info=None):
        r"""ListManagedPoliciesInPermissionSetResponse

        The model defined in huaweicloud sdk

        :param attached_managed_policies: IAM系统身份策略列表
        :type attached_managed_policies: list[:class:`huaweicloudsdkidentitycenter.v1.AttachedManagedPolicyDto`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
        """
        
        super(ListManagedPoliciesInPermissionSetResponse, self).__init__()

        self._attached_managed_policies = None
        self._page_info = None
        self.discriminator = None

        if attached_managed_policies is not None:
            self.attached_managed_policies = attached_managed_policies
        if page_info is not None:
            self.page_info = page_info

    @property
    def attached_managed_policies(self):
        r"""Gets the attached_managed_policies of this ListManagedPoliciesInPermissionSetResponse.

        IAM系统身份策略列表

        :return: The attached_managed_policies of this ListManagedPoliciesInPermissionSetResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenter.v1.AttachedManagedPolicyDto`]
        """
        return self._attached_managed_policies

    @attached_managed_policies.setter
    def attached_managed_policies(self, attached_managed_policies):
        r"""Sets the attached_managed_policies of this ListManagedPoliciesInPermissionSetResponse.

        IAM系统身份策略列表

        :param attached_managed_policies: The attached_managed_policies of this ListManagedPoliciesInPermissionSetResponse.
        :type attached_managed_policies: list[:class:`huaweicloudsdkidentitycenter.v1.AttachedManagedPolicyDto`]
        """
        self._attached_managed_policies = attached_managed_policies

    @property
    def page_info(self):
        r"""Gets the page_info of this ListManagedPoliciesInPermissionSetResponse.

        :return: The page_info of this ListManagedPoliciesInPermissionSetResponse.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListManagedPoliciesInPermissionSetResponse.

        :param page_info: The page_info of this ListManagedPoliciesInPermissionSetResponse.
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
        if not isinstance(other, ListManagedPoliciesInPermissionSetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
