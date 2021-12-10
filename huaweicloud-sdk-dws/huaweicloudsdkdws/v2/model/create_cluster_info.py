# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'public_ip': 'PublicIp',
        'number_of_node': 'int',
        'vpc_id': 'str',
        'user_name': 'str',
        'security_group_id': 'str',
        'number_of_cn': 'int',
        'user_pwd': 'str',
        'enterprise_project_id': 'str',
        'node_type': 'str',
        'port': 'int',
        'name': 'str',
        'subnet_id': 'str'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'public_ip': 'public_ip',
        'number_of_node': 'number_of_node',
        'vpc_id': 'vpc_id',
        'user_name': 'user_name',
        'security_group_id': 'security_group_id',
        'number_of_cn': 'number_of_cn',
        'user_pwd': 'user_pwd',
        'enterprise_project_id': 'enterprise_project_id',
        'node_type': 'node_type',
        'port': 'port',
        'name': 'name',
        'subnet_id': 'subnet_id'
    }

    def __init__(self, availability_zone=None, public_ip=None, number_of_node=None, vpc_id=None, user_name=None, security_group_id=None, number_of_cn=None, user_pwd=None, enterprise_project_id=None, node_type=None, port=None, name=None, subnet_id=None):
        """CreateClusterInfo - a model defined in huaweicloud sdk"""
        
        

        self._availability_zone = None
        self._public_ip = None
        self._number_of_node = None
        self._vpc_id = None
        self._user_name = None
        self._security_group_id = None
        self._number_of_cn = None
        self._user_pwd = None
        self._enterprise_project_id = None
        self._node_type = None
        self._port = None
        self._name = None
        self._subnet_id = None
        self.discriminator = None

        if availability_zone is not None:
            self.availability_zone = availability_zone
        if public_ip is not None:
            self.public_ip = public_ip
        self.number_of_node = number_of_node
        self.vpc_id = vpc_id
        self.user_name = user_name
        self.security_group_id = security_group_id
        if number_of_cn is not None:
            self.number_of_cn = number_of_cn
        self.user_pwd = user_pwd
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.node_type = node_type
        if port is not None:
            self.port = port
        self.name = name
        self.subnet_id = subnet_id

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateClusterInfo.

        配置集群可用区

        :return: The availability_zone of this CreateClusterInfo.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateClusterInfo.

        配置集群可用区

        :param availability_zone: The availability_zone of this CreateClusterInfo.
        :type: str
        """
        self._availability_zone = availability_zone

    @property
    def public_ip(self):
        """Gets the public_ip of this CreateClusterInfo.


        :return: The public_ip of this CreateClusterInfo.
        :rtype: PublicIp
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this CreateClusterInfo.


        :param public_ip: The public_ip of this CreateClusterInfo.
        :type: PublicIp
        """
        self._public_ip = public_ip

    @property
    def number_of_node(self):
        """Gets the number_of_node of this CreateClusterInfo.

        集群节点数量，取值范围为3~32。

        :return: The number_of_node of this CreateClusterInfo.
        :rtype: int
        """
        return self._number_of_node

    @number_of_node.setter
    def number_of_node(self, number_of_node):
        """Sets the number_of_node of this CreateClusterInfo.

        集群节点数量，取值范围为3~32。

        :param number_of_node: The number_of_node of this CreateClusterInfo.
        :type: int
        """
        self._number_of_node = number_of_node

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateClusterInfo.

        指定虚拟私有云ID，用于集群网络配置。

        :return: The vpc_id of this CreateClusterInfo.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateClusterInfo.

        指定虚拟私有云ID，用于集群网络配置。

        :param vpc_id: The vpc_id of this CreateClusterInfo.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def user_name(self):
        """Gets the user_name of this CreateClusterInfo.

        DWS集群管理员用户名。

        :return: The user_name of this CreateClusterInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CreateClusterInfo.

        DWS集群管理员用户名。

        :param user_name: The user_name of this CreateClusterInfo.
        :type: str
        """
        self._user_name = user_name

    @property
    def security_group_id(self):
        """Gets the security_group_id of this CreateClusterInfo.

        指定安全组ID，用于集群网络配置。

        :return: The security_group_id of this CreateClusterInfo.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this CreateClusterInfo.

        指定安全组ID，用于集群网络配置。

        :param security_group_id: The security_group_id of this CreateClusterInfo.
        :type: str
        """
        self._security_group_id = security_group_id

    @property
    def number_of_cn(self):
        """Gets the number_of_cn of this CreateClusterInfo.

        CN部署量，取值范围为2~集群节点数-1，最大值为5，默认值为2。

        :return: The number_of_cn of this CreateClusterInfo.
        :rtype: int
        """
        return self._number_of_cn

    @number_of_cn.setter
    def number_of_cn(self, number_of_cn):
        """Sets the number_of_cn of this CreateClusterInfo.

        CN部署量，取值范围为2~集群节点数-1，最大值为5，默认值为2。

        :param number_of_cn: The number_of_cn of this CreateClusterInfo.
        :type: int
        """
        self._number_of_cn = number_of_cn

    @property
    def user_pwd(self):
        """Gets the user_pwd of this CreateClusterInfo.

        DWS集群管理员密码。

        :return: The user_pwd of this CreateClusterInfo.
        :rtype: str
        """
        return self._user_pwd

    @user_pwd.setter
    def user_pwd(self, user_pwd):
        """Sets the user_pwd of this CreateClusterInfo.

        DWS集群管理员密码。

        :param user_pwd: The user_pwd of this CreateClusterInfo.
        :type: str
        """
        self._user_pwd = user_pwd

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateClusterInfo.

        企业项目ID，对集群指定企业项目，如果未指定，则使用默认企业项目“default”的ID，即0。

        :return: The enterprise_project_id of this CreateClusterInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateClusterInfo.

        企业项目ID，对集群指定企业项目，如果未指定，则使用默认企业项目“default”的ID，即0。

        :param enterprise_project_id: The enterprise_project_id of this CreateClusterInfo.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def node_type(self):
        """Gets the node_type of this CreateClusterInfo.

        节点类型

        :return: The node_type of this CreateClusterInfo.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this CreateClusterInfo.

        节点类型

        :param node_type: The node_type of this CreateClusterInfo.
        :type: str
        """
        self._node_type = node_type

    @property
    def port(self):
        """Gets the port of this CreateClusterInfo.

        集群服务端口，取值范围为8000~30000，默认值：8000。

        :return: The port of this CreateClusterInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CreateClusterInfo.

        集群服务端口，取值范围为8000~30000，默认值：8000。

        :param port: The port of this CreateClusterInfo.
        :type: int
        """
        self._port = port

    @property
    def name(self):
        """Gets the name of this CreateClusterInfo.

        集群名称，要求唯一性，必须以字母开头并只包含字母、数字、中划线或下划线，长度为4~64个字符。

        :return: The name of this CreateClusterInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateClusterInfo.

        集群名称，要求唯一性，必须以字母开头并只包含字母、数字、中划线或下划线，长度为4~64个字符。

        :param name: The name of this CreateClusterInfo.
        :type: str
        """
        self._name = name

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateClusterInfo.

        指定子网ID，用于集群网络配置。

        :return: The subnet_id of this CreateClusterInfo.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateClusterInfo.

        指定子网ID，用于集群网络配置。

        :param subnet_id: The subnet_id of this CreateClusterInfo.
        :type: str
        """
        self._subnet_id = subnet_id

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
        if not isinstance(other, CreateClusterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
