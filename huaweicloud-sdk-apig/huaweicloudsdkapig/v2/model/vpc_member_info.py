# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcMemberInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host': 'str',
        'weight': 'int',
        'is_backup': 'bool',
        'member_group_name': 'str',
        'status': 'int',
        'port': 'int',
        'ecs_id': 'str',
        'ecs_name': 'str',
        'id': 'str',
        'vpc_channel_id': 'str',
        'create_time': 'datetime',
        'member_group_id': 'str',
        'health_status': 'str'
    }

    attribute_map = {
        'host': 'host',
        'weight': 'weight',
        'is_backup': 'is_backup',
        'member_group_name': 'member_group_name',
        'status': 'status',
        'port': 'port',
        'ecs_id': 'ecs_id',
        'ecs_name': 'ecs_name',
        'id': 'id',
        'vpc_channel_id': 'vpc_channel_id',
        'create_time': 'create_time',
        'member_group_id': 'member_group_id',
        'health_status': 'health_status'
    }

    def __init__(self, host=None, weight=None, is_backup=None, member_group_name=None, status=None, port=None, ecs_id=None, ecs_name=None, id=None, vpc_channel_id=None, create_time=None, member_group_id=None, health_status=None):
        r"""VpcMemberInfo

        The model defined in huaweicloud sdk

        :param host: 后端服务器地址  后端实例类型为ip时必填
        :type host: str
        :param weight: 权重值。  允许您对后端服务进行评级，权重值越大，转发到该云服务的请求数量越多。
        :type weight: int
        :param is_backup: 是否备用节点。  开启后对应后端服务为备用节点，仅当非备用节点全部故障时工作。  实例需要升级到对应版本才支持此功能，如果不支持请联系技术支持。
        :type is_backup: bool
        :param member_group_name: 后端服务器组名称。为后端服务地址选择服务器组，便于统一修改对应服务器组的后端地址。
        :type member_group_name: str
        :param status: 后端服务器状态   - 1：可用   - 2：不可用
        :type status: int
        :param port: 后端服务器端口
        :type port: int
        :param ecs_id: 后端云服务器的编号。  后端实例类型为ecs时必填，支持英文，数字，“-”,“_”，1 ~ 64字符。
        :type ecs_id: str
        :param ecs_name: 后端云服务器的名称。  后端实例类型为ecs时必填，支持汉字，英文，数字，“-”,“_”,“.”，1 ~ 64字符。
        :type ecs_name: str
        :param id: 后端实例对象的编号
        :type id: str
        :param vpc_channel_id: VPC通道的编号
        :type vpc_channel_id: str
        :param create_time: 后端实例增加到VPC通道的时间
        :type create_time: datetime
        :param member_group_id: 后端服务器组编号
        :type member_group_id: str
        :param health_status: 负载通道后端实例健康状态，unknown、healthy、unhealthy分别标识未做健康检查、健康、不健康。
        :type health_status: str
        """
        
        

        self._host = None
        self._weight = None
        self._is_backup = None
        self._member_group_name = None
        self._status = None
        self._port = None
        self._ecs_id = None
        self._ecs_name = None
        self._id = None
        self._vpc_channel_id = None
        self._create_time = None
        self._member_group_id = None
        self._health_status = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if weight is not None:
            self.weight = weight
        if is_backup is not None:
            self.is_backup = is_backup
        if member_group_name is not None:
            self.member_group_name = member_group_name
        if status is not None:
            self.status = status
        if port is not None:
            self.port = port
        if ecs_id is not None:
            self.ecs_id = ecs_id
        if ecs_name is not None:
            self.ecs_name = ecs_name
        if id is not None:
            self.id = id
        if vpc_channel_id is not None:
            self.vpc_channel_id = vpc_channel_id
        if create_time is not None:
            self.create_time = create_time
        if member_group_id is not None:
            self.member_group_id = member_group_id
        if health_status is not None:
            self.health_status = health_status

    @property
    def host(self):
        r"""Gets the host of this VpcMemberInfo.

        后端服务器地址  后端实例类型为ip时必填

        :return: The host of this VpcMemberInfo.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this VpcMemberInfo.

        后端服务器地址  后端实例类型为ip时必填

        :param host: The host of this VpcMemberInfo.
        :type host: str
        """
        self._host = host

    @property
    def weight(self):
        r"""Gets the weight of this VpcMemberInfo.

        权重值。  允许您对后端服务进行评级，权重值越大，转发到该云服务的请求数量越多。

        :return: The weight of this VpcMemberInfo.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this VpcMemberInfo.

        权重值。  允许您对后端服务进行评级，权重值越大，转发到该云服务的请求数量越多。

        :param weight: The weight of this VpcMemberInfo.
        :type weight: int
        """
        self._weight = weight

    @property
    def is_backup(self):
        r"""Gets the is_backup of this VpcMemberInfo.

        是否备用节点。  开启后对应后端服务为备用节点，仅当非备用节点全部故障时工作。  实例需要升级到对应版本才支持此功能，如果不支持请联系技术支持。

        :return: The is_backup of this VpcMemberInfo.
        :rtype: bool
        """
        return self._is_backup

    @is_backup.setter
    def is_backup(self, is_backup):
        r"""Sets the is_backup of this VpcMemberInfo.

        是否备用节点。  开启后对应后端服务为备用节点，仅当非备用节点全部故障时工作。  实例需要升级到对应版本才支持此功能，如果不支持请联系技术支持。

        :param is_backup: The is_backup of this VpcMemberInfo.
        :type is_backup: bool
        """
        self._is_backup = is_backup

    @property
    def member_group_name(self):
        r"""Gets the member_group_name of this VpcMemberInfo.

        后端服务器组名称。为后端服务地址选择服务器组，便于统一修改对应服务器组的后端地址。

        :return: The member_group_name of this VpcMemberInfo.
        :rtype: str
        """
        return self._member_group_name

    @member_group_name.setter
    def member_group_name(self, member_group_name):
        r"""Sets the member_group_name of this VpcMemberInfo.

        后端服务器组名称。为后端服务地址选择服务器组，便于统一修改对应服务器组的后端地址。

        :param member_group_name: The member_group_name of this VpcMemberInfo.
        :type member_group_name: str
        """
        self._member_group_name = member_group_name

    @property
    def status(self):
        r"""Gets the status of this VpcMemberInfo.

        后端服务器状态   - 1：可用   - 2：不可用

        :return: The status of this VpcMemberInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VpcMemberInfo.

        后端服务器状态   - 1：可用   - 2：不可用

        :param status: The status of this VpcMemberInfo.
        :type status: int
        """
        self._status = status

    @property
    def port(self):
        r"""Gets the port of this VpcMemberInfo.

        后端服务器端口

        :return: The port of this VpcMemberInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this VpcMemberInfo.

        后端服务器端口

        :param port: The port of this VpcMemberInfo.
        :type port: int
        """
        self._port = port

    @property
    def ecs_id(self):
        r"""Gets the ecs_id of this VpcMemberInfo.

        后端云服务器的编号。  后端实例类型为ecs时必填，支持英文，数字，“-”,“_”，1 ~ 64字符。

        :return: The ecs_id of this VpcMemberInfo.
        :rtype: str
        """
        return self._ecs_id

    @ecs_id.setter
    def ecs_id(self, ecs_id):
        r"""Sets the ecs_id of this VpcMemberInfo.

        后端云服务器的编号。  后端实例类型为ecs时必填，支持英文，数字，“-”,“_”，1 ~ 64字符。

        :param ecs_id: The ecs_id of this VpcMemberInfo.
        :type ecs_id: str
        """
        self._ecs_id = ecs_id

    @property
    def ecs_name(self):
        r"""Gets the ecs_name of this VpcMemberInfo.

        后端云服务器的名称。  后端实例类型为ecs时必填，支持汉字，英文，数字，“-”,“_”,“.”，1 ~ 64字符。

        :return: The ecs_name of this VpcMemberInfo.
        :rtype: str
        """
        return self._ecs_name

    @ecs_name.setter
    def ecs_name(self, ecs_name):
        r"""Sets the ecs_name of this VpcMemberInfo.

        后端云服务器的名称。  后端实例类型为ecs时必填，支持汉字，英文，数字，“-”,“_”,“.”，1 ~ 64字符。

        :param ecs_name: The ecs_name of this VpcMemberInfo.
        :type ecs_name: str
        """
        self._ecs_name = ecs_name

    @property
    def id(self):
        r"""Gets the id of this VpcMemberInfo.

        后端实例对象的编号

        :return: The id of this VpcMemberInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VpcMemberInfo.

        后端实例对象的编号

        :param id: The id of this VpcMemberInfo.
        :type id: str
        """
        self._id = id

    @property
    def vpc_channel_id(self):
        r"""Gets the vpc_channel_id of this VpcMemberInfo.

        VPC通道的编号

        :return: The vpc_channel_id of this VpcMemberInfo.
        :rtype: str
        """
        return self._vpc_channel_id

    @vpc_channel_id.setter
    def vpc_channel_id(self, vpc_channel_id):
        r"""Sets the vpc_channel_id of this VpcMemberInfo.

        VPC通道的编号

        :param vpc_channel_id: The vpc_channel_id of this VpcMemberInfo.
        :type vpc_channel_id: str
        """
        self._vpc_channel_id = vpc_channel_id

    @property
    def create_time(self):
        r"""Gets the create_time of this VpcMemberInfo.

        后端实例增加到VPC通道的时间

        :return: The create_time of this VpcMemberInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this VpcMemberInfo.

        后端实例增加到VPC通道的时间

        :param create_time: The create_time of this VpcMemberInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def member_group_id(self):
        r"""Gets the member_group_id of this VpcMemberInfo.

        后端服务器组编号

        :return: The member_group_id of this VpcMemberInfo.
        :rtype: str
        """
        return self._member_group_id

    @member_group_id.setter
    def member_group_id(self, member_group_id):
        r"""Sets the member_group_id of this VpcMemberInfo.

        后端服务器组编号

        :param member_group_id: The member_group_id of this VpcMemberInfo.
        :type member_group_id: str
        """
        self._member_group_id = member_group_id

    @property
    def health_status(self):
        r"""Gets the health_status of this VpcMemberInfo.

        负载通道后端实例健康状态，unknown、healthy、unhealthy分别标识未做健康检查、健康、不健康。

        :return: The health_status of this VpcMemberInfo.
        :rtype: str
        """
        return self._health_status

    @health_status.setter
    def health_status(self, health_status):
        r"""Sets the health_status of this VpcMemberInfo.

        负载通道后端实例健康状态，unknown、healthy、unhealthy分别标识未做健康检查、健康、不健康。

        :param health_status: The health_status of this VpcMemberInfo.
        :type health_status: str
        """
        self._health_status = health_status

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
        if not isinstance(other, VpcMemberInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
