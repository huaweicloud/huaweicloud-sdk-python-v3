# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFirewallOption:

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
        'admin_state_up': 'bool',
        'description': 'str',
        'subnets': 'list[FirewallSubnetOption]'
    }

    attribute_map = {
        'name': 'name',
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'subnets': 'subnets'
    }

    def __init__(self, name=None, admin_state_up=None, description=None, subnets=None):
        """UpdateFirewallOption

        The model defined in huaweicloud sdk

        :param name: 网络ACL名称。更新时name不能为空。  中文字符、字母、数字、中划线和下划线组成，长度为1~64个字符
        :type name: str
        :param admin_state_up: 网络ACL的使能开关。  取值范围：true（开启），false（关闭） 
        :type admin_state_up: bool
        :param description: 网络ACL描述。
        :type description: str
        :param subnets: 关联子网列表。
        :type subnets: list[:class:`huaweicloudsdkiec.v1.FirewallSubnetOption`]
        """
        
        

        self._name = None
        self._admin_state_up = None
        self._description = None
        self._subnets = None
        self.discriminator = None

        self.name = name
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if description is not None:
            self.description = description
        if subnets is not None:
            self.subnets = subnets

    @property
    def name(self):
        """Gets the name of this UpdateFirewallOption.

        网络ACL名称。更新时name不能为空。  中文字符、字母、数字、中划线和下划线组成，长度为1~64个字符

        :return: The name of this UpdateFirewallOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateFirewallOption.

        网络ACL名称。更新时name不能为空。  中文字符、字母、数字、中划线和下划线组成，长度为1~64个字符

        :param name: The name of this UpdateFirewallOption.
        :type name: str
        """
        self._name = name

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdateFirewallOption.

        网络ACL的使能开关。  取值范围：true（开启），false（关闭） 

        :return: The admin_state_up of this UpdateFirewallOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdateFirewallOption.

        网络ACL的使能开关。  取值范围：true（开启），false（关闭） 

        :param admin_state_up: The admin_state_up of this UpdateFirewallOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this UpdateFirewallOption.

        网络ACL描述。

        :return: The description of this UpdateFirewallOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateFirewallOption.

        网络ACL描述。

        :param description: The description of this UpdateFirewallOption.
        :type description: str
        """
        self._description = description

    @property
    def subnets(self):
        """Gets the subnets of this UpdateFirewallOption.

        关联子网列表。

        :return: The subnets of this UpdateFirewallOption.
        :rtype: list[:class:`huaweicloudsdkiec.v1.FirewallSubnetOption`]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this UpdateFirewallOption.

        关联子网列表。

        :param subnets: The subnets of this UpdateFirewallOption.
        :type subnets: list[:class:`huaweicloudsdkiec.v1.FirewallSubnetOption`]
        """
        self._subnets = subnets

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
        if not isinstance(other, UpdateFirewallOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
