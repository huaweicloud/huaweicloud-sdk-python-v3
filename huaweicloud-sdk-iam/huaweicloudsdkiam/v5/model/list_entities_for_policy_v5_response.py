# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEntitiesForPolicyV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_agencies': 'list[PolicyAgency]',
        'policy_groups': 'list[PolicyGroup]',
        'policy_users': 'list[PolicyUser]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'policy_agencies': 'policy_agencies',
        'policy_groups': 'policy_groups',
        'policy_users': 'policy_users',
        'page_info': 'page_info'
    }

    def __init__(self, policy_agencies=None, policy_groups=None, policy_users=None, page_info=None):
        r"""ListEntitiesForPolicyV5Response

        The model defined in huaweicloud sdk

        :param policy_agencies: 委托及信任委托列表。
        :type policy_agencies: list[:class:`huaweicloudsdkiam.v5.PolicyAgency`]
        :param policy_groups: 用户组列表。
        :type policy_groups: list[:class:`huaweicloudsdkiam.v5.PolicyGroup`]
        :param policy_users: IAM用户列表。
        :type policy_users: list[:class:`huaweicloudsdkiam.v5.PolicyUser`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        
        super(ListEntitiesForPolicyV5Response, self).__init__()

        self._policy_agencies = None
        self._policy_groups = None
        self._policy_users = None
        self._page_info = None
        self.discriminator = None

        if policy_agencies is not None:
            self.policy_agencies = policy_agencies
        if policy_groups is not None:
            self.policy_groups = policy_groups
        if policy_users is not None:
            self.policy_users = policy_users
        if page_info is not None:
            self.page_info = page_info

    @property
    def policy_agencies(self):
        r"""Gets the policy_agencies of this ListEntitiesForPolicyV5Response.

        委托及信任委托列表。

        :return: The policy_agencies of this ListEntitiesForPolicyV5Response.
        :rtype: list[:class:`huaweicloudsdkiam.v5.PolicyAgency`]
        """
        return self._policy_agencies

    @policy_agencies.setter
    def policy_agencies(self, policy_agencies):
        r"""Sets the policy_agencies of this ListEntitiesForPolicyV5Response.

        委托及信任委托列表。

        :param policy_agencies: The policy_agencies of this ListEntitiesForPolicyV5Response.
        :type policy_agencies: list[:class:`huaweicloudsdkiam.v5.PolicyAgency`]
        """
        self._policy_agencies = policy_agencies

    @property
    def policy_groups(self):
        r"""Gets the policy_groups of this ListEntitiesForPolicyV5Response.

        用户组列表。

        :return: The policy_groups of this ListEntitiesForPolicyV5Response.
        :rtype: list[:class:`huaweicloudsdkiam.v5.PolicyGroup`]
        """
        return self._policy_groups

    @policy_groups.setter
    def policy_groups(self, policy_groups):
        r"""Sets the policy_groups of this ListEntitiesForPolicyV5Response.

        用户组列表。

        :param policy_groups: The policy_groups of this ListEntitiesForPolicyV5Response.
        :type policy_groups: list[:class:`huaweicloudsdkiam.v5.PolicyGroup`]
        """
        self._policy_groups = policy_groups

    @property
    def policy_users(self):
        r"""Gets the policy_users of this ListEntitiesForPolicyV5Response.

        IAM用户列表。

        :return: The policy_users of this ListEntitiesForPolicyV5Response.
        :rtype: list[:class:`huaweicloudsdkiam.v5.PolicyUser`]
        """
        return self._policy_users

    @policy_users.setter
    def policy_users(self, policy_users):
        r"""Sets the policy_users of this ListEntitiesForPolicyV5Response.

        IAM用户列表。

        :param policy_users: The policy_users of this ListEntitiesForPolicyV5Response.
        :type policy_users: list[:class:`huaweicloudsdkiam.v5.PolicyUser`]
        """
        self._policy_users = policy_users

    @property
    def page_info(self):
        r"""Gets the page_info of this ListEntitiesForPolicyV5Response.

        :return: The page_info of this ListEntitiesForPolicyV5Response.
        :rtype: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListEntitiesForPolicyV5Response.

        :param page_info: The page_info of this ListEntitiesForPolicyV5Response.
        :type page_info: :class:`huaweicloudsdkiam.v5.PageInfo`
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
        if not isinstance(other, ListEntitiesForPolicyV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
