# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectVpcChannelInfo:

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
        'port': 'int',
        'balance_strategy': 'int',
        'member_type': 'str',
        'type': 'str',
        'dict_code': 'str',
        'create_time': 'datetime',
        'id': 'str',
        'status': 'int',
        'member_groups': 'list[MemberGroupInfo]',
        'instance_id': 'str',
        'instance_name': 'str',
        'members': 'list[VpcMemberInfo]',
        'vpc_health_config': 'VpcHealthConfigInfo',
        'microservice_info': 'MicroServiceInfo'
    }

    attribute_map = {
        'name': 'name',
        'port': 'port',
        'balance_strategy': 'balance_strategy',
        'member_type': 'member_type',
        'type': 'type',
        'dict_code': 'dict_code',
        'create_time': 'create_time',
        'id': 'id',
        'status': 'status',
        'member_groups': 'member_groups',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'members': 'members',
        'vpc_health_config': 'vpc_health_config',
        'microservice_info': 'microservice_info'
    }

    def __init__(self, name=None, port=None, balance_strategy=None, member_type=None, type=None, dict_code=None, create_time=None, id=None, status=None, member_groups=None, instance_id=None, instance_name=None, members=None, vpc_health_config=None, microservice_info=None):
        """ProjectVpcChannelInfo

        The model defined in huaweicloud sdk

        :param name: VPC通道的名称。  长度为3 ~ 64位的字符串，字符串由中文、英文字母、数字、中划线、下划线组成，且只能以英文或中文开头。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type name: str
        :param port: VPC通道中主机的端口号。  取值范围1 ~ 65535。
        :type port: int
        :param balance_strategy: 分发算法。 - 1：加权轮询（wrr） - 2：加权最少连接（wleastconn） - 3：源地址哈希（source） - 4：URI哈希（uri）
        :type balance_strategy: int
        :param member_type: VPC通道的成员类型。[site场景必须修改成IP类型](tag:Site) - ip - ecs
        :type member_type: str
        :param type: vpc通道类型。 - BUILTIN：BUILTIN通道类型 - MICROSERVICE：微服务类型
        :type type: str
        :param dict_code: VPC通道的字典编码  支持英文，数字，特殊字符（-_.）  暂不支持
        :type dict_code: str
        :param create_time: VPC通道的创建时间
        :type create_time: datetime
        :param id: VPC通道的编号
        :type id: str
        :param status: VPC通道的状态。 - 1：正常 - 2：异常
        :type status: int
        :param member_groups: 后端云服务器组列表。
        :type member_groups: list[:class:`huaweicloudsdkroma.v2.MemberGroupInfo`]
        :param instance_id: 实例编号
        :type instance_id: str
        :param instance_name: 实例名称
        :type instance_name: str
        :param members: 后端实例列表。
        :type members: list[:class:`huaweicloudsdkroma.v2.VpcMemberInfo`]
        :param vpc_health_config: 
        :type vpc_health_config: :class:`huaweicloudsdkroma.v2.VpcHealthConfigInfo`
        :param microservice_info: 
        :type microservice_info: :class:`huaweicloudsdkroma.v2.MicroServiceInfo`
        """
        
        

        self._name = None
        self._port = None
        self._balance_strategy = None
        self._member_type = None
        self._type = None
        self._dict_code = None
        self._create_time = None
        self._id = None
        self._status = None
        self._member_groups = None
        self._instance_id = None
        self._instance_name = None
        self._members = None
        self._vpc_health_config = None
        self._microservice_info = None
        self.discriminator = None

        self.name = name
        self.port = port
        self.balance_strategy = balance_strategy
        self.member_type = member_type
        if type is not None:
            self.type = type
        if dict_code is not None:
            self.dict_code = dict_code
        if create_time is not None:
            self.create_time = create_time
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if member_groups is not None:
            self.member_groups = member_groups
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if members is not None:
            self.members = members
        if vpc_health_config is not None:
            self.vpc_health_config = vpc_health_config
        if microservice_info is not None:
            self.microservice_info = microservice_info

    @property
    def name(self):
        """Gets the name of this ProjectVpcChannelInfo.

        VPC通道的名称。  长度为3 ~ 64位的字符串，字符串由中文、英文字母、数字、中划线、下划线组成，且只能以英文或中文开头。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The name of this ProjectVpcChannelInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectVpcChannelInfo.

        VPC通道的名称。  长度为3 ~ 64位的字符串，字符串由中文、英文字母、数字、中划线、下划线组成，且只能以英文或中文开头。 > 中文字符必须为UTF-8或者unicode编码。

        :param name: The name of this ProjectVpcChannelInfo.
        :type name: str
        """
        self._name = name

    @property
    def port(self):
        """Gets the port of this ProjectVpcChannelInfo.

        VPC通道中主机的端口号。  取值范围1 ~ 65535。

        :return: The port of this ProjectVpcChannelInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ProjectVpcChannelInfo.

        VPC通道中主机的端口号。  取值范围1 ~ 65535。

        :param port: The port of this ProjectVpcChannelInfo.
        :type port: int
        """
        self._port = port

    @property
    def balance_strategy(self):
        """Gets the balance_strategy of this ProjectVpcChannelInfo.

        分发算法。 - 1：加权轮询（wrr） - 2：加权最少连接（wleastconn） - 3：源地址哈希（source） - 4：URI哈希（uri）

        :return: The balance_strategy of this ProjectVpcChannelInfo.
        :rtype: int
        """
        return self._balance_strategy

    @balance_strategy.setter
    def balance_strategy(self, balance_strategy):
        """Sets the balance_strategy of this ProjectVpcChannelInfo.

        分发算法。 - 1：加权轮询（wrr） - 2：加权最少连接（wleastconn） - 3：源地址哈希（source） - 4：URI哈希（uri）

        :param balance_strategy: The balance_strategy of this ProjectVpcChannelInfo.
        :type balance_strategy: int
        """
        self._balance_strategy = balance_strategy

    @property
    def member_type(self):
        """Gets the member_type of this ProjectVpcChannelInfo.

        VPC通道的成员类型。[site场景必须修改成IP类型](tag:Site) - ip - ecs

        :return: The member_type of this ProjectVpcChannelInfo.
        :rtype: str
        """
        return self._member_type

    @member_type.setter
    def member_type(self, member_type):
        """Sets the member_type of this ProjectVpcChannelInfo.

        VPC通道的成员类型。[site场景必须修改成IP类型](tag:Site) - ip - ecs

        :param member_type: The member_type of this ProjectVpcChannelInfo.
        :type member_type: str
        """
        self._member_type = member_type

    @property
    def type(self):
        """Gets the type of this ProjectVpcChannelInfo.

        vpc通道类型。 - BUILTIN：BUILTIN通道类型 - MICROSERVICE：微服务类型

        :return: The type of this ProjectVpcChannelInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProjectVpcChannelInfo.

        vpc通道类型。 - BUILTIN：BUILTIN通道类型 - MICROSERVICE：微服务类型

        :param type: The type of this ProjectVpcChannelInfo.
        :type type: str
        """
        self._type = type

    @property
    def dict_code(self):
        """Gets the dict_code of this ProjectVpcChannelInfo.

        VPC通道的字典编码  支持英文，数字，特殊字符（-_.）  暂不支持

        :return: The dict_code of this ProjectVpcChannelInfo.
        :rtype: str
        """
        return self._dict_code

    @dict_code.setter
    def dict_code(self, dict_code):
        """Sets the dict_code of this ProjectVpcChannelInfo.

        VPC通道的字典编码  支持英文，数字，特殊字符（-_.）  暂不支持

        :param dict_code: The dict_code of this ProjectVpcChannelInfo.
        :type dict_code: str
        """
        self._dict_code = dict_code

    @property
    def create_time(self):
        """Gets the create_time of this ProjectVpcChannelInfo.

        VPC通道的创建时间

        :return: The create_time of this ProjectVpcChannelInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ProjectVpcChannelInfo.

        VPC通道的创建时间

        :param create_time: The create_time of this ProjectVpcChannelInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def id(self):
        """Gets the id of this ProjectVpcChannelInfo.

        VPC通道的编号

        :return: The id of this ProjectVpcChannelInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectVpcChannelInfo.

        VPC通道的编号

        :param id: The id of this ProjectVpcChannelInfo.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this ProjectVpcChannelInfo.

        VPC通道的状态。 - 1：正常 - 2：异常

        :return: The status of this ProjectVpcChannelInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProjectVpcChannelInfo.

        VPC通道的状态。 - 1：正常 - 2：异常

        :param status: The status of this ProjectVpcChannelInfo.
        :type status: int
        """
        self._status = status

    @property
    def member_groups(self):
        """Gets the member_groups of this ProjectVpcChannelInfo.

        后端云服务器组列表。

        :return: The member_groups of this ProjectVpcChannelInfo.
        :rtype: list[:class:`huaweicloudsdkroma.v2.MemberGroupInfo`]
        """
        return self._member_groups

    @member_groups.setter
    def member_groups(self, member_groups):
        """Sets the member_groups of this ProjectVpcChannelInfo.

        后端云服务器组列表。

        :param member_groups: The member_groups of this ProjectVpcChannelInfo.
        :type member_groups: list[:class:`huaweicloudsdkroma.v2.MemberGroupInfo`]
        """
        self._member_groups = member_groups

    @property
    def instance_id(self):
        """Gets the instance_id of this ProjectVpcChannelInfo.

        实例编号

        :return: The instance_id of this ProjectVpcChannelInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ProjectVpcChannelInfo.

        实例编号

        :param instance_id: The instance_id of this ProjectVpcChannelInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this ProjectVpcChannelInfo.

        实例名称

        :return: The instance_name of this ProjectVpcChannelInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this ProjectVpcChannelInfo.

        实例名称

        :param instance_name: The instance_name of this ProjectVpcChannelInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def members(self):
        """Gets the members of this ProjectVpcChannelInfo.

        后端实例列表。

        :return: The members of this ProjectVpcChannelInfo.
        :rtype: list[:class:`huaweicloudsdkroma.v2.VpcMemberInfo`]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this ProjectVpcChannelInfo.

        后端实例列表。

        :param members: The members of this ProjectVpcChannelInfo.
        :type members: list[:class:`huaweicloudsdkroma.v2.VpcMemberInfo`]
        """
        self._members = members

    @property
    def vpc_health_config(self):
        """Gets the vpc_health_config of this ProjectVpcChannelInfo.

        :return: The vpc_health_config of this ProjectVpcChannelInfo.
        :rtype: :class:`huaweicloudsdkroma.v2.VpcHealthConfigInfo`
        """
        return self._vpc_health_config

    @vpc_health_config.setter
    def vpc_health_config(self, vpc_health_config):
        """Sets the vpc_health_config of this ProjectVpcChannelInfo.

        :param vpc_health_config: The vpc_health_config of this ProjectVpcChannelInfo.
        :type vpc_health_config: :class:`huaweicloudsdkroma.v2.VpcHealthConfigInfo`
        """
        self._vpc_health_config = vpc_health_config

    @property
    def microservice_info(self):
        """Gets the microservice_info of this ProjectVpcChannelInfo.

        :return: The microservice_info of this ProjectVpcChannelInfo.
        :rtype: :class:`huaweicloudsdkroma.v2.MicroServiceInfo`
        """
        return self._microservice_info

    @microservice_info.setter
    def microservice_info(self, microservice_info):
        """Sets the microservice_info of this ProjectVpcChannelInfo.

        :param microservice_info: The microservice_info of this ProjectVpcChannelInfo.
        :type microservice_info: :class:`huaweicloudsdkroma.v2.MicroServiceInfo`
        """
        self._microservice_info = microservice_info

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
        if not isinstance(other, ProjectVpcChannelInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
