# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceDetailNetwork:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vip': 'str',
        'web_port': 'str',
        'public_ip': 'str',
        'public_id': 'str',
        'private_ip': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str'
    }

    attribute_map = {
        'vip': 'vip',
        'web_port': 'web_port',
        'public_ip': 'public_ip',
        'public_id': 'public_id',
        'private_ip': 'private_ip',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id'
    }

    def __init__(self, vip=None, web_port=None, public_ip=None, public_id=None, private_ip=None, vpc_id=None, subnet_id=None, security_group_id=None):
        """InstanceDetailNetwork

        The model defined in huaweicloud sdk

        :param vip: 云堡垒机实例浮动ip。(实例为主备模式时返回对应的值)
        :type vip: str
        :param web_port: 云堡垒机实例WEB界面访问的端口号。
        :type web_port: str
        :param public_ip: 云堡垒机实例弹性公网IP。
        :type public_ip: str
        :param public_id: 云堡垒机实例绑定公网的弹性IP的ID，UUID格式表示。
        :type public_id: str
        :param private_ip: 云堡垒机实例私有ip。
        :type private_ip: str
        :param vpc_id: 云堡垒机实例所在虚拟私有云ID。
        :type vpc_id: str
        :param subnet_id: 云堡垒机实例所在子网ID。
        :type subnet_id: str
        :param security_group_id: 云堡垒机实例所属的安全组ID。
        :type security_group_id: str
        """
        
        

        self._vip = None
        self._web_port = None
        self._public_ip = None
        self._public_id = None
        self._private_ip = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self.discriminator = None

        if vip is not None:
            self.vip = vip
        self.web_port = web_port
        self.public_ip = public_ip
        self.public_id = public_id
        self.private_ip = private_ip
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id

    @property
    def vip(self):
        """Gets the vip of this InstanceDetailNetwork.

        云堡垒机实例浮动ip。(实例为主备模式时返回对应的值)

        :return: The vip of this InstanceDetailNetwork.
        :rtype: str
        """
        return self._vip

    @vip.setter
    def vip(self, vip):
        """Sets the vip of this InstanceDetailNetwork.

        云堡垒机实例浮动ip。(实例为主备模式时返回对应的值)

        :param vip: The vip of this InstanceDetailNetwork.
        :type vip: str
        """
        self._vip = vip

    @property
    def web_port(self):
        """Gets the web_port of this InstanceDetailNetwork.

        云堡垒机实例WEB界面访问的端口号。

        :return: The web_port of this InstanceDetailNetwork.
        :rtype: str
        """
        return self._web_port

    @web_port.setter
    def web_port(self, web_port):
        """Sets the web_port of this InstanceDetailNetwork.

        云堡垒机实例WEB界面访问的端口号。

        :param web_port: The web_port of this InstanceDetailNetwork.
        :type web_port: str
        """
        self._web_port = web_port

    @property
    def public_ip(self):
        """Gets the public_ip of this InstanceDetailNetwork.

        云堡垒机实例弹性公网IP。

        :return: The public_ip of this InstanceDetailNetwork.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this InstanceDetailNetwork.

        云堡垒机实例弹性公网IP。

        :param public_ip: The public_ip of this InstanceDetailNetwork.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def public_id(self):
        """Gets the public_id of this InstanceDetailNetwork.

        云堡垒机实例绑定公网的弹性IP的ID，UUID格式表示。

        :return: The public_id of this InstanceDetailNetwork.
        :rtype: str
        """
        return self._public_id

    @public_id.setter
    def public_id(self, public_id):
        """Sets the public_id of this InstanceDetailNetwork.

        云堡垒机实例绑定公网的弹性IP的ID，UUID格式表示。

        :param public_id: The public_id of this InstanceDetailNetwork.
        :type public_id: str
        """
        self._public_id = public_id

    @property
    def private_ip(self):
        """Gets the private_ip of this InstanceDetailNetwork.

        云堡垒机实例私有ip。

        :return: The private_ip of this InstanceDetailNetwork.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this InstanceDetailNetwork.

        云堡垒机实例私有ip。

        :param private_ip: The private_ip of this InstanceDetailNetwork.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def vpc_id(self):
        """Gets the vpc_id of this InstanceDetailNetwork.

        云堡垒机实例所在虚拟私有云ID。

        :return: The vpc_id of this InstanceDetailNetwork.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this InstanceDetailNetwork.

        云堡垒机实例所在虚拟私有云ID。

        :param vpc_id: The vpc_id of this InstanceDetailNetwork.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this InstanceDetailNetwork.

        云堡垒机实例所在子网ID。

        :return: The subnet_id of this InstanceDetailNetwork.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this InstanceDetailNetwork.

        云堡垒机实例所在子网ID。

        :param subnet_id: The subnet_id of this InstanceDetailNetwork.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this InstanceDetailNetwork.

        云堡垒机实例所属的安全组ID。

        :return: The security_group_id of this InstanceDetailNetwork.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this InstanceDetailNetwork.

        云堡垒机实例所属的安全组ID。

        :param security_group_id: The security_group_id of this InstanceDetailNetwork.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

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
        if not isinstance(other, InstanceDetailNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
