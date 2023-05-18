# coding: utf-8

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
        'node_type': 'str',
        'number_of_node': 'int',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'vpc_id': 'str',
        'availability_zone': 'str',
        'port': 'int',
        'name': 'str',
        'user_name': 'str',
        'user_pwd': 'str',
        'public_ip': 'PublicIp',
        'number_of_cn': 'int',
        'enterprise_project_id': 'str',
        'tags': 'Tags'
    }

    attribute_map = {
        'node_type': 'node_type',
        'number_of_node': 'number_of_node',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'vpc_id': 'vpc_id',
        'availability_zone': 'availability_zone',
        'port': 'port',
        'name': 'name',
        'user_name': 'user_name',
        'user_pwd': 'user_pwd',
        'public_ip': 'public_ip',
        'number_of_cn': 'number_of_cn',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags'
    }

    def __init__(self, node_type=None, number_of_node=None, subnet_id=None, security_group_id=None, vpc_id=None, availability_zone=None, port=None, name=None, user_name=None, user_pwd=None, public_ip=None, number_of_cn=None, enterprise_project_id=None, tags=None):
        """CreateClusterInfo

        The model defined in huaweicloud sdk

        :param node_type: 节点类型
        :type node_type: str
        :param number_of_node: 集群节点数量，集群模式取值范围为3~256，实时数仓（单机模式）取值为1。
        :type number_of_node: int
        :param subnet_id: 指定子网ID，用于集群网络配置。
        :type subnet_id: str
        :param security_group_id: 指定安全组ID，用于集群网络配置。
        :type security_group_id: str
        :param vpc_id: 指定虚拟私有云ID，用于集群网络配置。
        :type vpc_id: str
        :param availability_zone: 配置集群可用区。
        :type availability_zone: str
        :param port: 集群服务端口，取值范围为8000~30000，默认值：8000。
        :type port: int
        :param name: 集群名称，要求唯一性，必须以字母开头并只包含字母、数字、中划线或下划线，长度为4~64个字符。
        :type name: str
        :param user_name: DWS集群管理员用户名。用户命名要求如下：  - 只能由小写字母、数字或下划线组成。 - 必须由小写字母或下划线开头。 - 长度为1~63个字符。 - 用户名不能为DWS数据库的关键字。
        :type user_name: str
        :param user_pwd: DWS集群管理员密码。
        :type user_pwd: str
        :param public_ip: 
        :type public_ip: :class:`huaweicloudsdkdws.v2.PublicIp`
        :param number_of_cn: CN部署量，取值范围为2~集群节点数，最大值为20，默认值为3。
        :type number_of_cn: int
        :param enterprise_project_id: 企业项目ID，对集群指定企业项目，如果未指定，则使用默认企业项目“default”的ID，即0。
        :type enterprise_project_id: str
        :param tags: 
        :type tags: :class:`huaweicloudsdkdws.v2.Tags`
        """
        
        

        self._node_type = None
        self._number_of_node = None
        self._subnet_id = None
        self._security_group_id = None
        self._vpc_id = None
        self._availability_zone = None
        self._port = None
        self._name = None
        self._user_name = None
        self._user_pwd = None
        self._public_ip = None
        self._number_of_cn = None
        self._enterprise_project_id = None
        self._tags = None
        self.discriminator = None

        self.node_type = node_type
        self.number_of_node = number_of_node
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        self.vpc_id = vpc_id
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if port is not None:
            self.port = port
        self.name = name
        self.user_name = user_name
        self.user_pwd = user_pwd
        if public_ip is not None:
            self.public_ip = public_ip
        if number_of_cn is not None:
            self.number_of_cn = number_of_cn
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags

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
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def number_of_node(self):
        """Gets the number_of_node of this CreateClusterInfo.

        集群节点数量，集群模式取值范围为3~256，实时数仓（单机模式）取值为1。

        :return: The number_of_node of this CreateClusterInfo.
        :rtype: int
        """
        return self._number_of_node

    @number_of_node.setter
    def number_of_node(self, number_of_node):
        """Sets the number_of_node of this CreateClusterInfo.

        集群节点数量，集群模式取值范围为3~256，实时数仓（单机模式）取值为1。

        :param number_of_node: The number_of_node of this CreateClusterInfo.
        :type number_of_node: int
        """
        self._number_of_node = number_of_node

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
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

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
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

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
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateClusterInfo.

        配置集群可用区。

        :return: The availability_zone of this CreateClusterInfo.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateClusterInfo.

        配置集群可用区。

        :param availability_zone: The availability_zone of this CreateClusterInfo.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

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
        :type port: int
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
        :type name: str
        """
        self._name = name

    @property
    def user_name(self):
        """Gets the user_name of this CreateClusterInfo.

        DWS集群管理员用户名。用户命名要求如下：  - 只能由小写字母、数字或下划线组成。 - 必须由小写字母或下划线开头。 - 长度为1~63个字符。 - 用户名不能为DWS数据库的关键字。

        :return: The user_name of this CreateClusterInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CreateClusterInfo.

        DWS集群管理员用户名。用户命名要求如下：  - 只能由小写字母、数字或下划线组成。 - 必须由小写字母或下划线开头。 - 长度为1~63个字符。 - 用户名不能为DWS数据库的关键字。

        :param user_name: The user_name of this CreateClusterInfo.
        :type user_name: str
        """
        self._user_name = user_name

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
        :type user_pwd: str
        """
        self._user_pwd = user_pwd

    @property
    def public_ip(self):
        """Gets the public_ip of this CreateClusterInfo.

        :return: The public_ip of this CreateClusterInfo.
        :rtype: :class:`huaweicloudsdkdws.v2.PublicIp`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this CreateClusterInfo.

        :param public_ip: The public_ip of this CreateClusterInfo.
        :type public_ip: :class:`huaweicloudsdkdws.v2.PublicIp`
        """
        self._public_ip = public_ip

    @property
    def number_of_cn(self):
        """Gets the number_of_cn of this CreateClusterInfo.

        CN部署量，取值范围为2~集群节点数，最大值为20，默认值为3。

        :return: The number_of_cn of this CreateClusterInfo.
        :rtype: int
        """
        return self._number_of_cn

    @number_of_cn.setter
    def number_of_cn(self, number_of_cn):
        """Sets the number_of_cn of this CreateClusterInfo.

        CN部署量，取值范围为2~集群节点数，最大值为20，默认值为3。

        :param number_of_cn: The number_of_cn of this CreateClusterInfo.
        :type number_of_cn: int
        """
        self._number_of_cn = number_of_cn

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
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this CreateClusterInfo.

        :return: The tags of this CreateClusterInfo.
        :rtype: :class:`huaweicloudsdkdws.v2.Tags`
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateClusterInfo.

        :param tags: The tags of this CreateClusterInfo.
        :type tags: :class:`huaweicloudsdkdws.v2.Tags`
        """
        self._tags = tags

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
