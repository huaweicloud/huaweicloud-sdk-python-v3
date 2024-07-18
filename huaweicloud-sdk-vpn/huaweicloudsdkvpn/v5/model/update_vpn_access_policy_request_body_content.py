# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVpnAccessPolicyRequestBodyContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'user_group_id': 'str',
        'description': 'str',
        'dest_ip_cidrs': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'user_group_id': 'user_group_id',
        'description': 'description',
        'dest_ip_cidrs': 'dest_ip_cidrs'
    }

    def __init__(self, name=None, user_group_id=None, description=None, dest_ip_cidrs=None):
        """UpdateVpnAccessPolicyRequestBodyContent

        The model defined in huaweicloud sdk

        :param name: 访问策略名称
        :type name: str
        :param user_group_id: 关联用户组ID
        :type user_group_id: str
        :param description: 访问策略描述
        :type description: str
        :param dest_ip_cidrs: 目的IP网段列表，至少有一个网段
        :type dest_ip_cidrs: list[str]
        """
        
        

        self._name = None
        self._user_group_id = None
        self._description = None
        self._dest_ip_cidrs = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if user_group_id is not None:
            self.user_group_id = user_group_id
        if description is not None:
            self.description = description
        if dest_ip_cidrs is not None:
            self.dest_ip_cidrs = dest_ip_cidrs

    @property
    def name(self):
        """Gets the name of this UpdateVpnAccessPolicyRequestBodyContent.

        访问策略名称

        :return: The name of this UpdateVpnAccessPolicyRequestBodyContent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateVpnAccessPolicyRequestBodyContent.

        访问策略名称

        :param name: The name of this UpdateVpnAccessPolicyRequestBodyContent.
        :type name: str
        """
        self._name = name

    @property
    def user_group_id(self):
        """Gets the user_group_id of this UpdateVpnAccessPolicyRequestBodyContent.

        关联用户组ID

        :return: The user_group_id of this UpdateVpnAccessPolicyRequestBodyContent.
        :rtype: str
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """Sets the user_group_id of this UpdateVpnAccessPolicyRequestBodyContent.

        关联用户组ID

        :param user_group_id: The user_group_id of this UpdateVpnAccessPolicyRequestBodyContent.
        :type user_group_id: str
        """
        self._user_group_id = user_group_id

    @property
    def description(self):
        """Gets the description of this UpdateVpnAccessPolicyRequestBodyContent.

        访问策略描述

        :return: The description of this UpdateVpnAccessPolicyRequestBodyContent.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateVpnAccessPolicyRequestBodyContent.

        访问策略描述

        :param description: The description of this UpdateVpnAccessPolicyRequestBodyContent.
        :type description: str
        """
        self._description = description

    @property
    def dest_ip_cidrs(self):
        """Gets the dest_ip_cidrs of this UpdateVpnAccessPolicyRequestBodyContent.

        目的IP网段列表，至少有一个网段

        :return: The dest_ip_cidrs of this UpdateVpnAccessPolicyRequestBodyContent.
        :rtype: list[str]
        """
        return self._dest_ip_cidrs

    @dest_ip_cidrs.setter
    def dest_ip_cidrs(self, dest_ip_cidrs):
        """Sets the dest_ip_cidrs of this UpdateVpnAccessPolicyRequestBodyContent.

        目的IP网段列表，至少有一个网段

        :param dest_ip_cidrs: The dest_ip_cidrs of this UpdateVpnAccessPolicyRequestBodyContent.
        :type dest_ip_cidrs: list[str]
        """
        self._dest_ip_cidrs = dest_ip_cidrs

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
        if not isinstance(other, UpdateVpnAccessPolicyRequestBodyContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
