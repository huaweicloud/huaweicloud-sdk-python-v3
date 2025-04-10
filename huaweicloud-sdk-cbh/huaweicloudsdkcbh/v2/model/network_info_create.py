# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkInfoCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_id': 'str',
        'subnet_id': 'str',
        'public_ip': 'PublicIp',
        'security_groups': 'list[SecurityGroup]',
        'private_ip': 'PrivateIp'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'public_ip': 'public_ip',
        'security_groups': 'security_groups',
        'private_ip': 'private_ip'
    }

    def __init__(self, vpc_id=None, subnet_id=None, public_ip=None, security_groups=None, private_ip=None):
        r"""NetworkInfoCreate

        The model defined in huaweicloud sdk

        :param vpc_id: 待创建云服务器所属虚拟私有云（简称VPC），需要指定已创建VPC的ID，UUID格式。  VPC的ID可以从控制台或者参考《虚拟私有云接口参考》的“查询VPC”章节获取。  例如：03211ecf-xxxx-4306-xxxx-6e939bfxxxxx
        :type vpc_id: str
        :param subnet_id: 子网ID，字母数字下划线连接符组成。
        :type subnet_id: str
        :param public_ip: 
        :type public_ip: :class:`huaweicloudsdkcbh.v2.PublicIp`
        :param security_groups: 安全组信息。
        :type security_groups: list[:class:`huaweicloudsdkcbh.v2.SecurityGroup`]
        :param private_ip: 
        :type private_ip: :class:`huaweicloudsdkcbh.v2.PrivateIp`
        """
        
        

        self._vpc_id = None
        self._subnet_id = None
        self._public_ip = None
        self._security_groups = None
        self._private_ip = None
        self.discriminator = None

        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.public_ip = public_ip
        self.security_groups = security_groups
        if private_ip is not None:
            self.private_ip = private_ip

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this NetworkInfoCreate.

        待创建云服务器所属虚拟私有云（简称VPC），需要指定已创建VPC的ID，UUID格式。  VPC的ID可以从控制台或者参考《虚拟私有云接口参考》的“查询VPC”章节获取。  例如：03211ecf-xxxx-4306-xxxx-6e939bfxxxxx

        :return: The vpc_id of this NetworkInfoCreate.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this NetworkInfoCreate.

        待创建云服务器所属虚拟私有云（简称VPC），需要指定已创建VPC的ID，UUID格式。  VPC的ID可以从控制台或者参考《虚拟私有云接口参考》的“查询VPC”章节获取。  例如：03211ecf-xxxx-4306-xxxx-6e939bfxxxxx

        :param vpc_id: The vpc_id of this NetworkInfoCreate.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this NetworkInfoCreate.

        子网ID，字母数字下划线连接符组成。

        :return: The subnet_id of this NetworkInfoCreate.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this NetworkInfoCreate.

        子网ID，字母数字下划线连接符组成。

        :param subnet_id: The subnet_id of this NetworkInfoCreate.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def public_ip(self):
        r"""Gets the public_ip of this NetworkInfoCreate.

        :return: The public_ip of this NetworkInfoCreate.
        :rtype: :class:`huaweicloudsdkcbh.v2.PublicIp`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this NetworkInfoCreate.

        :param public_ip: The public_ip of this NetworkInfoCreate.
        :type public_ip: :class:`huaweicloudsdkcbh.v2.PublicIp`
        """
        self._public_ip = public_ip

    @property
    def security_groups(self):
        r"""Gets the security_groups of this NetworkInfoCreate.

        安全组信息。

        :return: The security_groups of this NetworkInfoCreate.
        :rtype: list[:class:`huaweicloudsdkcbh.v2.SecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this NetworkInfoCreate.

        安全组信息。

        :param security_groups: The security_groups of this NetworkInfoCreate.
        :type security_groups: list[:class:`huaweicloudsdkcbh.v2.SecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def private_ip(self):
        r"""Gets the private_ip of this NetworkInfoCreate.

        :return: The private_ip of this NetworkInfoCreate.
        :rtype: :class:`huaweicloudsdkcbh.v2.PrivateIp`
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this NetworkInfoCreate.

        :param private_ip: The private_ip of this NetworkInfoCreate.
        :type private_ip: :class:`huaweicloudsdkcbh.v2.PrivateIp`
        """
        self._private_ip = private_ip

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
        if not isinstance(other, NetworkInfoCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
