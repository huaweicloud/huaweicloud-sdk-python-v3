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
        r"""CreateClusterInfo

        The model defined in huaweicloud sdk

        :param node_type: **参数解释**： 节点规格ID，需要通过查询规格接口获取，对应的是接口响应的id字段。 **约束限制**： 不涉及。 **取值范围**： 必须是查询规格信息接口返回的规格ID。 **默认取值**： 不涉及。
        :type node_type: str
        :param number_of_node: **参数解释**： 节点数量。 **约束限制**： 不涉及。 **取值范围**： 集群模式取值范围为3~256，实时数仓（单机模式）取值为1。 **默认取值**： 不涉及。
        :type number_of_node: int
        :param subnet_id: **参数解释**： 指定子网ID，用于集群网络配置。 **约束限制**： 不涉及。 **取值范围**： 必须是虚拟私有云ID下的某个子网。 **默认取值**： 不涉及。
        :type subnet_id: str
        :param security_group_id: **参数解释**： 指定安全组ID，用于集群网络配置。 **约束限制**： 不涉及。 **取值范围**： 参数非空时必须是有效的安全组ID。参数为空时将自动创建安全组。 **默认取值**： null
        :type security_group_id: str
        :param vpc_id: **参数解释**： 指定虚拟私有云ID，用于集群网络配置。 **约束限制**： 不涉及。 **取值范围**： 必须是有效的虚拟私有云ID。 **默认取值**： 不涉及。
        :type vpc_id: str
        :param availability_zone: **参数解释**： 配置集群可用区。 **约束限制**： 不涉及。 **取值范围**： 必须是当前局点下状态有效且当前用户可见的可用区编码。 **默认取值**： 查询可用区时第一个可用的可用区编码。
        :type availability_zone: str
        :param port: **参数解释**： 集群数据库端口。 **约束限制**： 不涉及。 **取值范围**： 8000~30000 **默认取值**： 8000
        :type port: int
        :param name: **参数解释**： 集群名称。 **约束限制**： 要求唯一性，必须以字母开头并只包含字母、数字、中划线或下划线，长度为4~64个字符。 **取值范围**： 4~64个字符。 **默认取值**： 8000
        :type name: str
        :param user_name: **参数解释**： DWS集群管理员用户名。 **约束限制**： - 只能由小写字母、数字或下划线组成。 - 必须由小写字母或下划线开头。 - 长度为1~63个字符。 - 用户名不能为DWS数据库的关键字。    **取值范围**：   1~63个字符； **默认取值**： dbadmin
        :type user_name: str
        :param user_pwd: **参数解释**： DWS集群管理员密码。 **约束限制**： 不涉及。 **取值范围**： 12~32个字符； 至少包含以下字符的3种：大写字母、小写字母、数字和特殊字符(~!?,.:;_(){}[]/&lt;&gt;@#%^&amp;*+|\\\\&#x3D;-)； 不能与用户名或倒序的用户名相同； **默认取值**： 不涉及。
        :type user_pwd: str
        :param public_ip: 
        :type public_ip: :class:`huaweicloudsdkdws.v2.PublicIp`
        :param number_of_cn: **参数解释**： CN部署量。 **约束限制**： 不涉及。 **取值范围**： 2~集群节点数，最大值为20。 **默认取值**： 默认值为3。
        :type number_of_cn: int
        :param enterprise_project_id: **参数解释**： 企业项目ID，对集群指定企业项目。如果未指定，则使用默认企业项目“default”的ID，即0。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 0
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
        r"""Gets the node_type of this CreateClusterInfo.

        **参数解释**： 节点规格ID，需要通过查询规格接口获取，对应的是接口响应的id字段。 **约束限制**： 不涉及。 **取值范围**： 必须是查询规格信息接口返回的规格ID。 **默认取值**： 不涉及。

        :return: The node_type of this CreateClusterInfo.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this CreateClusterInfo.

        **参数解释**： 节点规格ID，需要通过查询规格接口获取，对应的是接口响应的id字段。 **约束限制**： 不涉及。 **取值范围**： 必须是查询规格信息接口返回的规格ID。 **默认取值**： 不涉及。

        :param node_type: The node_type of this CreateClusterInfo.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def number_of_node(self):
        r"""Gets the number_of_node of this CreateClusterInfo.

        **参数解释**： 节点数量。 **约束限制**： 不涉及。 **取值范围**： 集群模式取值范围为3~256，实时数仓（单机模式）取值为1。 **默认取值**： 不涉及。

        :return: The number_of_node of this CreateClusterInfo.
        :rtype: int
        """
        return self._number_of_node

    @number_of_node.setter
    def number_of_node(self, number_of_node):
        r"""Sets the number_of_node of this CreateClusterInfo.

        **参数解释**： 节点数量。 **约束限制**： 不涉及。 **取值范围**： 集群模式取值范围为3~256，实时数仓（单机模式）取值为1。 **默认取值**： 不涉及。

        :param number_of_node: The number_of_node of this CreateClusterInfo.
        :type number_of_node: int
        """
        self._number_of_node = number_of_node

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreateClusterInfo.

        **参数解释**： 指定子网ID，用于集群网络配置。 **约束限制**： 不涉及。 **取值范围**： 必须是虚拟私有云ID下的某个子网。 **默认取值**： 不涉及。

        :return: The subnet_id of this CreateClusterInfo.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreateClusterInfo.

        **参数解释**： 指定子网ID，用于集群网络配置。 **约束限制**： 不涉及。 **取值范围**： 必须是虚拟私有云ID下的某个子网。 **默认取值**： 不涉及。

        :param subnet_id: The subnet_id of this CreateClusterInfo.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this CreateClusterInfo.

        **参数解释**： 指定安全组ID，用于集群网络配置。 **约束限制**： 不涉及。 **取值范围**： 参数非空时必须是有效的安全组ID。参数为空时将自动创建安全组。 **默认取值**： null

        :return: The security_group_id of this CreateClusterInfo.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this CreateClusterInfo.

        **参数解释**： 指定安全组ID，用于集群网络配置。 **约束限制**： 不涉及。 **取值范围**： 参数非空时必须是有效的安全组ID。参数为空时将自动创建安全组。 **默认取值**： null

        :param security_group_id: The security_group_id of this CreateClusterInfo.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateClusterInfo.

        **参数解释**： 指定虚拟私有云ID，用于集群网络配置。 **约束限制**： 不涉及。 **取值范围**： 必须是有效的虚拟私有云ID。 **默认取值**： 不涉及。

        :return: The vpc_id of this CreateClusterInfo.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateClusterInfo.

        **参数解释**： 指定虚拟私有云ID，用于集群网络配置。 **约束限制**： 不涉及。 **取值范围**： 必须是有效的虚拟私有云ID。 **默认取值**： 不涉及。

        :param vpc_id: The vpc_id of this CreateClusterInfo.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this CreateClusterInfo.

        **参数解释**： 配置集群可用区。 **约束限制**： 不涉及。 **取值范围**： 必须是当前局点下状态有效且当前用户可见的可用区编码。 **默认取值**： 查询可用区时第一个可用的可用区编码。

        :return: The availability_zone of this CreateClusterInfo.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this CreateClusterInfo.

        **参数解释**： 配置集群可用区。 **约束限制**： 不涉及。 **取值范围**： 必须是当前局点下状态有效且当前用户可见的可用区编码。 **默认取值**： 查询可用区时第一个可用的可用区编码。

        :param availability_zone: The availability_zone of this CreateClusterInfo.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def port(self):
        r"""Gets the port of this CreateClusterInfo.

        **参数解释**： 集群数据库端口。 **约束限制**： 不涉及。 **取值范围**： 8000~30000 **默认取值**： 8000

        :return: The port of this CreateClusterInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this CreateClusterInfo.

        **参数解释**： 集群数据库端口。 **约束限制**： 不涉及。 **取值范围**： 8000~30000 **默认取值**： 8000

        :param port: The port of this CreateClusterInfo.
        :type port: int
        """
        self._port = port

    @property
    def name(self):
        r"""Gets the name of this CreateClusterInfo.

        **参数解释**： 集群名称。 **约束限制**： 要求唯一性，必须以字母开头并只包含字母、数字、中划线或下划线，长度为4~64个字符。 **取值范围**： 4~64个字符。 **默认取值**： 8000

        :return: The name of this CreateClusterInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateClusterInfo.

        **参数解释**： 集群名称。 **约束限制**： 要求唯一性，必须以字母开头并只包含字母、数字、中划线或下划线，长度为4~64个字符。 **取值范围**： 4~64个字符。 **默认取值**： 8000

        :param name: The name of this CreateClusterInfo.
        :type name: str
        """
        self._name = name

    @property
    def user_name(self):
        r"""Gets the user_name of this CreateClusterInfo.

        **参数解释**： DWS集群管理员用户名。 **约束限制**： - 只能由小写字母、数字或下划线组成。 - 必须由小写字母或下划线开头。 - 长度为1~63个字符。 - 用户名不能为DWS数据库的关键字。    **取值范围**：   1~63个字符； **默认取值**： dbadmin

        :return: The user_name of this CreateClusterInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this CreateClusterInfo.

        **参数解释**： DWS集群管理员用户名。 **约束限制**： - 只能由小写字母、数字或下划线组成。 - 必须由小写字母或下划线开头。 - 长度为1~63个字符。 - 用户名不能为DWS数据库的关键字。    **取值范围**：   1~63个字符； **默认取值**： dbadmin

        :param user_name: The user_name of this CreateClusterInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_pwd(self):
        r"""Gets the user_pwd of this CreateClusterInfo.

        **参数解释**： DWS集群管理员密码。 **约束限制**： 不涉及。 **取值范围**： 12~32个字符； 至少包含以下字符的3种：大写字母、小写字母、数字和特殊字符(~!?,.:;_(){}[]/<>@#%^&*+|\\\\=-)； 不能与用户名或倒序的用户名相同； **默认取值**： 不涉及。

        :return: The user_pwd of this CreateClusterInfo.
        :rtype: str
        """
        return self._user_pwd

    @user_pwd.setter
    def user_pwd(self, user_pwd):
        r"""Sets the user_pwd of this CreateClusterInfo.

        **参数解释**： DWS集群管理员密码。 **约束限制**： 不涉及。 **取值范围**： 12~32个字符； 至少包含以下字符的3种：大写字母、小写字母、数字和特殊字符(~!?,.:;_(){}[]/<>@#%^&*+|\\\\=-)； 不能与用户名或倒序的用户名相同； **默认取值**： 不涉及。

        :param user_pwd: The user_pwd of this CreateClusterInfo.
        :type user_pwd: str
        """
        self._user_pwd = user_pwd

    @property
    def public_ip(self):
        r"""Gets the public_ip of this CreateClusterInfo.

        :return: The public_ip of this CreateClusterInfo.
        :rtype: :class:`huaweicloudsdkdws.v2.PublicIp`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this CreateClusterInfo.

        :param public_ip: The public_ip of this CreateClusterInfo.
        :type public_ip: :class:`huaweicloudsdkdws.v2.PublicIp`
        """
        self._public_ip = public_ip

    @property
    def number_of_cn(self):
        r"""Gets the number_of_cn of this CreateClusterInfo.

        **参数解释**： CN部署量。 **约束限制**： 不涉及。 **取值范围**： 2~集群节点数，最大值为20。 **默认取值**： 默认值为3。

        :return: The number_of_cn of this CreateClusterInfo.
        :rtype: int
        """
        return self._number_of_cn

    @number_of_cn.setter
    def number_of_cn(self, number_of_cn):
        r"""Sets the number_of_cn of this CreateClusterInfo.

        **参数解释**： CN部署量。 **约束限制**： 不涉及。 **取值范围**： 2~集群节点数，最大值为20。 **默认取值**： 默认值为3。

        :param number_of_cn: The number_of_cn of this CreateClusterInfo.
        :type number_of_cn: int
        """
        self._number_of_cn = number_of_cn

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateClusterInfo.

        **参数解释**： 企业项目ID，对集群指定企业项目。如果未指定，则使用默认企业项目“default”的ID，即0。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 0

        :return: The enterprise_project_id of this CreateClusterInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateClusterInfo.

        **参数解释**： 企业项目ID，对集群指定企业项目。如果未指定，则使用默认企业项目“default”的ID，即0。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 0

        :param enterprise_project_id: The enterprise_project_id of this CreateClusterInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this CreateClusterInfo.

        :return: The tags of this CreateClusterInfo.
        :rtype: :class:`huaweicloudsdkdws.v2.Tags`
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateClusterInfo.

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
