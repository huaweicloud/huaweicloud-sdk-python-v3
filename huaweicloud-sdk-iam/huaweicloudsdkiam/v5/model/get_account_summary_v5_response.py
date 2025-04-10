# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetAccountSummaryV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attached_policies_per_agency_quota': 'int',
        'attached_policies_per_group_quota': 'int',
        'attached_policies_per_user_quota': 'int',
        'policies_quota': 'int',
        'policy_size_quota': 'int',
        'versions_per_policy_quota': 'int',
        'policies': 'int',
        'agencies': 'int',
        'agencies_quota': 'int',
        'users': 'int',
        'users_quota': 'int',
        'groups': 'int',
        'groups_quota': 'int',
        'root_user_mfa_enabled': 'int'
    }

    attribute_map = {
        'attached_policies_per_agency_quota': 'attached_policies_per_agency_quota',
        'attached_policies_per_group_quota': 'attached_policies_per_group_quota',
        'attached_policies_per_user_quota': 'attached_policies_per_user_quota',
        'policies_quota': 'policies_quota',
        'policy_size_quota': 'policy_size_quota',
        'versions_per_policy_quota': 'versions_per_policy_quota',
        'policies': 'policies',
        'agencies': 'agencies',
        'agencies_quota': 'agencies_quota',
        'users': 'users',
        'users_quota': 'users_quota',
        'groups': 'groups',
        'groups_quota': 'groups_quota',
        'root_user_mfa_enabled': 'root_user_mfa_enabled'
    }

    def __init__(self, attached_policies_per_agency_quota=None, attached_policies_per_group_quota=None, attached_policies_per_user_quota=None, policies_quota=None, policy_size_quota=None, versions_per_policy_quota=None, policies=None, agencies=None, agencies_quota=None, users=None, users_quota=None, groups=None, groups_quota=None, root_user_mfa_enabled=None):
        r"""GetAccountSummaryV5Response

        The model defined in huaweicloud sdk

        :param attached_policies_per_agency_quota: 附加到委托或信任委托上的身份策略的最大数量。
        :type attached_policies_per_agency_quota: int
        :param attached_policies_per_group_quota: 附加到用户组上的身份策略的最大数量。
        :type attached_policies_per_group_quota: int
        :param attached_policies_per_user_quota: 附加到IAM用户上的身份策略的最大数量。
        :type attached_policies_per_user_quota: int
        :param policies_quota: 自定义身份策略的最大数量。
        :type policies_quota: int
        :param policy_size_quota: 身份策略及信任策略的策略文档的最大字符数，不包括空格。
        :type policy_size_quota: int
        :param versions_per_policy_quota: 自定义身份策略同一时刻保留的最大版本数量。
        :type versions_per_policy_quota: int
        :param policies: 此账号中当前创建的自定义身份策略数量。
        :type policies: int
        :param agencies: 此账号中当前创建的委托及信任委托的总数量。
        :type agencies: int
        :param agencies_quota: 此账号能够创建的委托及信任委托的总数上限。
        :type agencies_quota: int
        :param users: 此账号当前创建的IAM用户数量，包括根用户。
        :type users: int
        :param users_quota: 此账号能够创建的IAM用户数上限，包括根用户。
        :type users_quota: int
        :param groups: 此账号当前创建的用户组数量。
        :type groups: int
        :param groups_quota: 此账号能够创建的用户组数上限。
        :type groups_quota: int
        :param root_user_mfa_enabled: 根用户绑定的已启用MFA的数量。
        :type root_user_mfa_enabled: int
        """
        
        super(GetAccountSummaryV5Response, self).__init__()

        self._attached_policies_per_agency_quota = None
        self._attached_policies_per_group_quota = None
        self._attached_policies_per_user_quota = None
        self._policies_quota = None
        self._policy_size_quota = None
        self._versions_per_policy_quota = None
        self._policies = None
        self._agencies = None
        self._agencies_quota = None
        self._users = None
        self._users_quota = None
        self._groups = None
        self._groups_quota = None
        self._root_user_mfa_enabled = None
        self.discriminator = None

        if attached_policies_per_agency_quota is not None:
            self.attached_policies_per_agency_quota = attached_policies_per_agency_quota
        if attached_policies_per_group_quota is not None:
            self.attached_policies_per_group_quota = attached_policies_per_group_quota
        if attached_policies_per_user_quota is not None:
            self.attached_policies_per_user_quota = attached_policies_per_user_quota
        if policies_quota is not None:
            self.policies_quota = policies_quota
        if policy_size_quota is not None:
            self.policy_size_quota = policy_size_quota
        if versions_per_policy_quota is not None:
            self.versions_per_policy_quota = versions_per_policy_quota
        if policies is not None:
            self.policies = policies
        if agencies is not None:
            self.agencies = agencies
        if agencies_quota is not None:
            self.agencies_quota = agencies_quota
        if users is not None:
            self.users = users
        if users_quota is not None:
            self.users_quota = users_quota
        if groups is not None:
            self.groups = groups
        if groups_quota is not None:
            self.groups_quota = groups_quota
        if root_user_mfa_enabled is not None:
            self.root_user_mfa_enabled = root_user_mfa_enabled

    @property
    def attached_policies_per_agency_quota(self):
        r"""Gets the attached_policies_per_agency_quota of this GetAccountSummaryV5Response.

        附加到委托或信任委托上的身份策略的最大数量。

        :return: The attached_policies_per_agency_quota of this GetAccountSummaryV5Response.
        :rtype: int
        """
        return self._attached_policies_per_agency_quota

    @attached_policies_per_agency_quota.setter
    def attached_policies_per_agency_quota(self, attached_policies_per_agency_quota):
        r"""Sets the attached_policies_per_agency_quota of this GetAccountSummaryV5Response.

        附加到委托或信任委托上的身份策略的最大数量。

        :param attached_policies_per_agency_quota: The attached_policies_per_agency_quota of this GetAccountSummaryV5Response.
        :type attached_policies_per_agency_quota: int
        """
        self._attached_policies_per_agency_quota = attached_policies_per_agency_quota

    @property
    def attached_policies_per_group_quota(self):
        r"""Gets the attached_policies_per_group_quota of this GetAccountSummaryV5Response.

        附加到用户组上的身份策略的最大数量。

        :return: The attached_policies_per_group_quota of this GetAccountSummaryV5Response.
        :rtype: int
        """
        return self._attached_policies_per_group_quota

    @attached_policies_per_group_quota.setter
    def attached_policies_per_group_quota(self, attached_policies_per_group_quota):
        r"""Sets the attached_policies_per_group_quota of this GetAccountSummaryV5Response.

        附加到用户组上的身份策略的最大数量。

        :param attached_policies_per_group_quota: The attached_policies_per_group_quota of this GetAccountSummaryV5Response.
        :type attached_policies_per_group_quota: int
        """
        self._attached_policies_per_group_quota = attached_policies_per_group_quota

    @property
    def attached_policies_per_user_quota(self):
        r"""Gets the attached_policies_per_user_quota of this GetAccountSummaryV5Response.

        附加到IAM用户上的身份策略的最大数量。

        :return: The attached_policies_per_user_quota of this GetAccountSummaryV5Response.
        :rtype: int
        """
        return self._attached_policies_per_user_quota

    @attached_policies_per_user_quota.setter
    def attached_policies_per_user_quota(self, attached_policies_per_user_quota):
        r"""Sets the attached_policies_per_user_quota of this GetAccountSummaryV5Response.

        附加到IAM用户上的身份策略的最大数量。

        :param attached_policies_per_user_quota: The attached_policies_per_user_quota of this GetAccountSummaryV5Response.
        :type attached_policies_per_user_quota: int
        """
        self._attached_policies_per_user_quota = attached_policies_per_user_quota

    @property
    def policies_quota(self):
        r"""Gets the policies_quota of this GetAccountSummaryV5Response.

        自定义身份策略的最大数量。

        :return: The policies_quota of this GetAccountSummaryV5Response.
        :rtype: int
        """
        return self._policies_quota

    @policies_quota.setter
    def policies_quota(self, policies_quota):
        r"""Sets the policies_quota of this GetAccountSummaryV5Response.

        自定义身份策略的最大数量。

        :param policies_quota: The policies_quota of this GetAccountSummaryV5Response.
        :type policies_quota: int
        """
        self._policies_quota = policies_quota

    @property
    def policy_size_quota(self):
        r"""Gets the policy_size_quota of this GetAccountSummaryV5Response.

        身份策略及信任策略的策略文档的最大字符数，不包括空格。

        :return: The policy_size_quota of this GetAccountSummaryV5Response.
        :rtype: int
        """
        return self._policy_size_quota

    @policy_size_quota.setter
    def policy_size_quota(self, policy_size_quota):
        r"""Sets the policy_size_quota of this GetAccountSummaryV5Response.

        身份策略及信任策略的策略文档的最大字符数，不包括空格。

        :param policy_size_quota: The policy_size_quota of this GetAccountSummaryV5Response.
        :type policy_size_quota: int
        """
        self._policy_size_quota = policy_size_quota

    @property
    def versions_per_policy_quota(self):
        r"""Gets the versions_per_policy_quota of this GetAccountSummaryV5Response.

        自定义身份策略同一时刻保留的最大版本数量。

        :return: The versions_per_policy_quota of this GetAccountSummaryV5Response.
        :rtype: int
        """
        return self._versions_per_policy_quota

    @versions_per_policy_quota.setter
    def versions_per_policy_quota(self, versions_per_policy_quota):
        r"""Sets the versions_per_policy_quota of this GetAccountSummaryV5Response.

        自定义身份策略同一时刻保留的最大版本数量。

        :param versions_per_policy_quota: The versions_per_policy_quota of this GetAccountSummaryV5Response.
        :type versions_per_policy_quota: int
        """
        self._versions_per_policy_quota = versions_per_policy_quota

    @property
    def policies(self):
        r"""Gets the policies of this GetAccountSummaryV5Response.

        此账号中当前创建的自定义身份策略数量。

        :return: The policies of this GetAccountSummaryV5Response.
        :rtype: int
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this GetAccountSummaryV5Response.

        此账号中当前创建的自定义身份策略数量。

        :param policies: The policies of this GetAccountSummaryV5Response.
        :type policies: int
        """
        self._policies = policies

    @property
    def agencies(self):
        r"""Gets the agencies of this GetAccountSummaryV5Response.

        此账号中当前创建的委托及信任委托的总数量。

        :return: The agencies of this GetAccountSummaryV5Response.
        :rtype: int
        """
        return self._agencies

    @agencies.setter
    def agencies(self, agencies):
        r"""Sets the agencies of this GetAccountSummaryV5Response.

        此账号中当前创建的委托及信任委托的总数量。

        :param agencies: The agencies of this GetAccountSummaryV5Response.
        :type agencies: int
        """
        self._agencies = agencies

    @property
    def agencies_quota(self):
        r"""Gets the agencies_quota of this GetAccountSummaryV5Response.

        此账号能够创建的委托及信任委托的总数上限。

        :return: The agencies_quota of this GetAccountSummaryV5Response.
        :rtype: int
        """
        return self._agencies_quota

    @agencies_quota.setter
    def agencies_quota(self, agencies_quota):
        r"""Sets the agencies_quota of this GetAccountSummaryV5Response.

        此账号能够创建的委托及信任委托的总数上限。

        :param agencies_quota: The agencies_quota of this GetAccountSummaryV5Response.
        :type agencies_quota: int
        """
        self._agencies_quota = agencies_quota

    @property
    def users(self):
        r"""Gets the users of this GetAccountSummaryV5Response.

        此账号当前创建的IAM用户数量，包括根用户。

        :return: The users of this GetAccountSummaryV5Response.
        :rtype: int
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this GetAccountSummaryV5Response.

        此账号当前创建的IAM用户数量，包括根用户。

        :param users: The users of this GetAccountSummaryV5Response.
        :type users: int
        """
        self._users = users

    @property
    def users_quota(self):
        r"""Gets the users_quota of this GetAccountSummaryV5Response.

        此账号能够创建的IAM用户数上限，包括根用户。

        :return: The users_quota of this GetAccountSummaryV5Response.
        :rtype: int
        """
        return self._users_quota

    @users_quota.setter
    def users_quota(self, users_quota):
        r"""Sets the users_quota of this GetAccountSummaryV5Response.

        此账号能够创建的IAM用户数上限，包括根用户。

        :param users_quota: The users_quota of this GetAccountSummaryV5Response.
        :type users_quota: int
        """
        self._users_quota = users_quota

    @property
    def groups(self):
        r"""Gets the groups of this GetAccountSummaryV5Response.

        此账号当前创建的用户组数量。

        :return: The groups of this GetAccountSummaryV5Response.
        :rtype: int
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        r"""Sets the groups of this GetAccountSummaryV5Response.

        此账号当前创建的用户组数量。

        :param groups: The groups of this GetAccountSummaryV5Response.
        :type groups: int
        """
        self._groups = groups

    @property
    def groups_quota(self):
        r"""Gets the groups_quota of this GetAccountSummaryV5Response.

        此账号能够创建的用户组数上限。

        :return: The groups_quota of this GetAccountSummaryV5Response.
        :rtype: int
        """
        return self._groups_quota

    @groups_quota.setter
    def groups_quota(self, groups_quota):
        r"""Sets the groups_quota of this GetAccountSummaryV5Response.

        此账号能够创建的用户组数上限。

        :param groups_quota: The groups_quota of this GetAccountSummaryV5Response.
        :type groups_quota: int
        """
        self._groups_quota = groups_quota

    @property
    def root_user_mfa_enabled(self):
        r"""Gets the root_user_mfa_enabled of this GetAccountSummaryV5Response.

        根用户绑定的已启用MFA的数量。

        :return: The root_user_mfa_enabled of this GetAccountSummaryV5Response.
        :rtype: int
        """
        return self._root_user_mfa_enabled

    @root_user_mfa_enabled.setter
    def root_user_mfa_enabled(self, root_user_mfa_enabled):
        r"""Sets the root_user_mfa_enabled of this GetAccountSummaryV5Response.

        根用户绑定的已启用MFA的数量。

        :param root_user_mfa_enabled: The root_user_mfa_enabled of this GetAccountSummaryV5Response.
        :type root_user_mfa_enabled: int
        """
        self._root_user_mfa_enabled = root_user_mfa_enabled

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
        if not isinstance(other, GetAccountSummaryV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
