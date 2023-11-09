# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_info': 'Vpc',
        'subnet_info': 'Subnet',
        'port_info': 'Port',
        'public_ip_info': 'PublicIp',
        'security_groups': 'list[SecurityGroup]'
    }

    attribute_map = {
        'vpc_info': 'vpc_info',
        'subnet_info': 'subnet_info',
        'port_info': 'port_info',
        'public_ip_info': 'public_ip_info',
        'security_groups': 'security_groups'
    }

    def __init__(self, vpc_info=None, subnet_info=None, port_info=None, public_ip_info=None, security_groups=None):
        """NetworkInfo

        The model defined in huaweicloud sdk

        :param vpc_info: 
        :type vpc_info: :class:`huaweicloudsdkworkspace.v2.Vpc`
        :param subnet_info: 
        :type subnet_info: :class:`huaweicloudsdkworkspace.v2.Subnet`
        :param port_info: 
        :type port_info: :class:`huaweicloudsdkworkspace.v2.Port`
        :param public_ip_info: 
        :type public_ip_info: :class:`huaweicloudsdkworkspace.v2.PublicIp`
        :param security_groups: 桌面绑定的安全组列表
        :type security_groups: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroup`]
        """
        
        

        self._vpc_info = None
        self._subnet_info = None
        self._port_info = None
        self._public_ip_info = None
        self._security_groups = None
        self.discriminator = None

        if vpc_info is not None:
            self.vpc_info = vpc_info
        if subnet_info is not None:
            self.subnet_info = subnet_info
        if port_info is not None:
            self.port_info = port_info
        if public_ip_info is not None:
            self.public_ip_info = public_ip_info
        if security_groups is not None:
            self.security_groups = security_groups

    @property
    def vpc_info(self):
        """Gets the vpc_info of this NetworkInfo.

        :return: The vpc_info of this NetworkInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Vpc`
        """
        return self._vpc_info

    @vpc_info.setter
    def vpc_info(self, vpc_info):
        """Sets the vpc_info of this NetworkInfo.

        :param vpc_info: The vpc_info of this NetworkInfo.
        :type vpc_info: :class:`huaweicloudsdkworkspace.v2.Vpc`
        """
        self._vpc_info = vpc_info

    @property
    def subnet_info(self):
        """Gets the subnet_info of this NetworkInfo.

        :return: The subnet_info of this NetworkInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Subnet`
        """
        return self._subnet_info

    @subnet_info.setter
    def subnet_info(self, subnet_info):
        """Sets the subnet_info of this NetworkInfo.

        :param subnet_info: The subnet_info of this NetworkInfo.
        :type subnet_info: :class:`huaweicloudsdkworkspace.v2.Subnet`
        """
        self._subnet_info = subnet_info

    @property
    def port_info(self):
        """Gets the port_info of this NetworkInfo.

        :return: The port_info of this NetworkInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Port`
        """
        return self._port_info

    @port_info.setter
    def port_info(self, port_info):
        """Sets the port_info of this NetworkInfo.

        :param port_info: The port_info of this NetworkInfo.
        :type port_info: :class:`huaweicloudsdkworkspace.v2.Port`
        """
        self._port_info = port_info

    @property
    def public_ip_info(self):
        """Gets the public_ip_info of this NetworkInfo.

        :return: The public_ip_info of this NetworkInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PublicIp`
        """
        return self._public_ip_info

    @public_ip_info.setter
    def public_ip_info(self, public_ip_info):
        """Sets the public_ip_info of this NetworkInfo.

        :param public_ip_info: The public_ip_info of this NetworkInfo.
        :type public_ip_info: :class:`huaweicloudsdkworkspace.v2.PublicIp`
        """
        self._public_ip_info = public_ip_info

    @property
    def security_groups(self):
        """Gets the security_groups of this NetworkInfo.

        桌面绑定的安全组列表

        :return: The security_groups of this NetworkInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this NetworkInfo.

        桌面绑定的安全组列表

        :param security_groups: The security_groups of this NetworkInfo.
        :type security_groups: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroup`]
        """
        self._security_groups = security_groups

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
        if not isinstance(other, NetworkInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
