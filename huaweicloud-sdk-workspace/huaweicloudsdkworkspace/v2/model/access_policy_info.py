# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessPolicyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'blacklist_type': 'str',
        'access_control_type': 'str',
        'ip_list': 'list[IpInfo]',
        'ip_total_count': 'int'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'blacklist_type': 'blacklist_type',
        'access_control_type': 'access_control_type',
        'ip_list': 'ip_list',
        'ip_total_count': 'ip_total_count'
    }

    def __init__(self, policy_name=None, blacklist_type=None, access_control_type=None, ip_list=None, ip_total_count=None):
        r"""AccessPolicyInfo

        The model defined in huaweicloud sdk

        :param policy_name: 策略名
        :type policy_name: str
        :param blacklist_type: 黑名单类型，当前黑名单只支持互联网。 * INTERNET： 互联网
        :type blacklist_type: str
        :param access_control_type: 访问控制类型。默认为接入类型 * ACCESS_TYPE： 接入类型 * IP_WHITE_LIST： IP白名单
        :type access_control_type: str
        :param ip_list: 策略的ip列表。
        :type ip_list: list[:class:`huaweicloudsdkworkspace.v2.IpInfo`]
        :param ip_total_count: 策略总数。
        :type ip_total_count: int
        """
        
        

        self._policy_name = None
        self._blacklist_type = None
        self._access_control_type = None
        self._ip_list = None
        self._ip_total_count = None
        self.discriminator = None

        if policy_name is not None:
            self.policy_name = policy_name
        if blacklist_type is not None:
            self.blacklist_type = blacklist_type
        if access_control_type is not None:
            self.access_control_type = access_control_type
        if ip_list is not None:
            self.ip_list = ip_list
        if ip_total_count is not None:
            self.ip_total_count = ip_total_count

    @property
    def policy_name(self):
        r"""Gets the policy_name of this AccessPolicyInfo.

        策略名

        :return: The policy_name of this AccessPolicyInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this AccessPolicyInfo.

        策略名

        :param policy_name: The policy_name of this AccessPolicyInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def blacklist_type(self):
        r"""Gets the blacklist_type of this AccessPolicyInfo.

        黑名单类型，当前黑名单只支持互联网。 * INTERNET： 互联网

        :return: The blacklist_type of this AccessPolicyInfo.
        :rtype: str
        """
        return self._blacklist_type

    @blacklist_type.setter
    def blacklist_type(self, blacklist_type):
        r"""Sets the blacklist_type of this AccessPolicyInfo.

        黑名单类型，当前黑名单只支持互联网。 * INTERNET： 互联网

        :param blacklist_type: The blacklist_type of this AccessPolicyInfo.
        :type blacklist_type: str
        """
        self._blacklist_type = blacklist_type

    @property
    def access_control_type(self):
        r"""Gets the access_control_type of this AccessPolicyInfo.

        访问控制类型。默认为接入类型 * ACCESS_TYPE： 接入类型 * IP_WHITE_LIST： IP白名单

        :return: The access_control_type of this AccessPolicyInfo.
        :rtype: str
        """
        return self._access_control_type

    @access_control_type.setter
    def access_control_type(self, access_control_type):
        r"""Sets the access_control_type of this AccessPolicyInfo.

        访问控制类型。默认为接入类型 * ACCESS_TYPE： 接入类型 * IP_WHITE_LIST： IP白名单

        :param access_control_type: The access_control_type of this AccessPolicyInfo.
        :type access_control_type: str
        """
        self._access_control_type = access_control_type

    @property
    def ip_list(self):
        r"""Gets the ip_list of this AccessPolicyInfo.

        策略的ip列表。

        :return: The ip_list of this AccessPolicyInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.IpInfo`]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        r"""Sets the ip_list of this AccessPolicyInfo.

        策略的ip列表。

        :param ip_list: The ip_list of this AccessPolicyInfo.
        :type ip_list: list[:class:`huaweicloudsdkworkspace.v2.IpInfo`]
        """
        self._ip_list = ip_list

    @property
    def ip_total_count(self):
        r"""Gets the ip_total_count of this AccessPolicyInfo.

        策略总数。

        :return: The ip_total_count of this AccessPolicyInfo.
        :rtype: int
        """
        return self._ip_total_count

    @ip_total_count.setter
    def ip_total_count(self, ip_total_count):
        r"""Sets the ip_total_count of this AccessPolicyInfo.

        策略总数。

        :param ip_total_count: The ip_total_count of this AccessPolicyInfo.
        :type ip_total_count: int
        """
        self._ip_total_count = ip_total_count

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
        if not isinstance(other, AccessPolicyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
