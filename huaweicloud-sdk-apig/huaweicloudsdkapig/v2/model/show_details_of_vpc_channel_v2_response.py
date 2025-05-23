# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDetailsOfVpcChannelV2Response(SdkResponse):

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
        'type': 'int',
        'vpc_channel_type': 'str',
        'dict_code': 'str',
        'create_time': 'datetime',
        'id': 'str',
        'status': 'int',
        'member_groups': 'list[MemberGroupInfo]',
        'microservice_info': 'MicroServiceInfo',
        'members': 'list[VpcMemberInfo]',
        'vpc_health_config': 'VpcHealthConfigInfo'
    }

    attribute_map = {
        'name': 'name',
        'port': 'port',
        'balance_strategy': 'balance_strategy',
        'member_type': 'member_type',
        'type': 'type',
        'vpc_channel_type': 'vpc_channel_type',
        'dict_code': 'dict_code',
        'create_time': 'create_time',
        'id': 'id',
        'status': 'status',
        'member_groups': 'member_groups',
        'microservice_info': 'microservice_info',
        'members': 'members',
        'vpc_health_config': 'vpc_health_config'
    }

    def __init__(self, name=None, port=None, balance_strategy=None, member_type=None, type=None, vpc_channel_type=None, dict_code=None, create_time=None, id=None, status=None, member_groups=None, microservice_info=None, members=None, vpc_health_config=None):
        r"""ShowDetailsOfVpcChannelV2Response

        The model defined in huaweicloud sdk

        :param name: VPC通道的名称。  长度为3 ~ 64位的字符串，字符串由中文、英文字母、数字、中划线、下划线、点组成，且只能以英文或中文开头。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type name: str
        :param port: VPC通道中主机的端口号。  取值范围1 ~ 65535。
        :type port: int
        :param balance_strategy: 分发算法。 - 1：加权轮询（wrr） - 2：加权最少连接（wleastconn） - 3：源地址哈希（source） - 4：URI哈希（uri）
        :type balance_strategy: int
        :param member_type: VPC通道的成员类型。 - ip - ecs
        :type member_type: str
        :param type: vpc通道类型，默认为服务器类型。 - 2：服务器类型 - 3：微服务类型  当vpc_channel_type字段为空时，负载通道类型由type字段控制： 当type不为3或microservice_info为空，VCP通道类型默认为服务器类型。 当type&#x3D;3，microservice_info不为空，VPC通道类型为微服务类型。  修改负载通道时vpc通道类型不会修改，直接使用原有的vpc通道类型。  此字段待废弃，请使用vpc_channel_type字段指定负载通道类型。
        :type type: int
        :param vpc_channel_type: vpc通道类型。 - builtin：服务器类型 - microservice： 微服务类型 - reference：引用负载通道类型  当vpc_channel_type为空时，负载通道类型取决于type字段的取值。 当vpc_channel_type不为空，但type字段非空或不为0时，当vpc_channel_type的指定类型与type字段指定的类型冲突时会校验报错。 当vpc_channel_type不为空，且type字段为空或等于0时，直接使用vpc_channel_type字段的值指定负载通道类型。  修改负载通道时vpc通道类型不会修改，直接使用原有的vpc通道类型。
        :type vpc_channel_type: str
        :param dict_code: VPC通道的字典编码  支持英文，数字，特殊字符（-_.）  暂不支持
        :type dict_code: str
        :param create_time: VPC通道的创建时间
        :type create_time: datetime
        :param id: VPC通道的编号
        :type id: str
        :param status: VPC通道的状态。 - 1：正常 - 2：异常
        :type status: int
        :param member_groups: 后端云服务器组列表。
        :type member_groups: list[:class:`huaweicloudsdkapig.v2.MemberGroupInfo`]
        :param microservice_info: 
        :type microservice_info: :class:`huaweicloudsdkapig.v2.MicroServiceInfo`
        :param members: 后端实例列表。
        :type members: list[:class:`huaweicloudsdkapig.v2.VpcMemberInfo`]
        :param vpc_health_config: 
        :type vpc_health_config: :class:`huaweicloudsdkapig.v2.VpcHealthConfigInfo`
        """
        
        super(ShowDetailsOfVpcChannelV2Response, self).__init__()

        self._name = None
        self._port = None
        self._balance_strategy = None
        self._member_type = None
        self._type = None
        self._vpc_channel_type = None
        self._dict_code = None
        self._create_time = None
        self._id = None
        self._status = None
        self._member_groups = None
        self._microservice_info = None
        self._members = None
        self._vpc_health_config = None
        self.discriminator = None

        self.name = name
        self.port = port
        self.balance_strategy = balance_strategy
        self.member_type = member_type
        if type is not None:
            self.type = type
        if vpc_channel_type is not None:
            self.vpc_channel_type = vpc_channel_type
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
        if microservice_info is not None:
            self.microservice_info = microservice_info
        if members is not None:
            self.members = members
        if vpc_health_config is not None:
            self.vpc_health_config = vpc_health_config

    @property
    def name(self):
        r"""Gets the name of this ShowDetailsOfVpcChannelV2Response.

        VPC通道的名称。  长度为3 ~ 64位的字符串，字符串由中文、英文字母、数字、中划线、下划线、点组成，且只能以英文或中文开头。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The name of this ShowDetailsOfVpcChannelV2Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowDetailsOfVpcChannelV2Response.

        VPC通道的名称。  长度为3 ~ 64位的字符串，字符串由中文、英文字母、数字、中划线、下划线、点组成，且只能以英文或中文开头。 > 中文字符必须为UTF-8或者unicode编码。

        :param name: The name of this ShowDetailsOfVpcChannelV2Response.
        :type name: str
        """
        self._name = name

    @property
    def port(self):
        r"""Gets the port of this ShowDetailsOfVpcChannelV2Response.

        VPC通道中主机的端口号。  取值范围1 ~ 65535。

        :return: The port of this ShowDetailsOfVpcChannelV2Response.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ShowDetailsOfVpcChannelV2Response.

        VPC通道中主机的端口号。  取值范围1 ~ 65535。

        :param port: The port of this ShowDetailsOfVpcChannelV2Response.
        :type port: int
        """
        self._port = port

    @property
    def balance_strategy(self):
        r"""Gets the balance_strategy of this ShowDetailsOfVpcChannelV2Response.

        分发算法。 - 1：加权轮询（wrr） - 2：加权最少连接（wleastconn） - 3：源地址哈希（source） - 4：URI哈希（uri）

        :return: The balance_strategy of this ShowDetailsOfVpcChannelV2Response.
        :rtype: int
        """
        return self._balance_strategy

    @balance_strategy.setter
    def balance_strategy(self, balance_strategy):
        r"""Sets the balance_strategy of this ShowDetailsOfVpcChannelV2Response.

        分发算法。 - 1：加权轮询（wrr） - 2：加权最少连接（wleastconn） - 3：源地址哈希（source） - 4：URI哈希（uri）

        :param balance_strategy: The balance_strategy of this ShowDetailsOfVpcChannelV2Response.
        :type balance_strategy: int
        """
        self._balance_strategy = balance_strategy

    @property
    def member_type(self):
        r"""Gets the member_type of this ShowDetailsOfVpcChannelV2Response.

        VPC通道的成员类型。 - ip - ecs

        :return: The member_type of this ShowDetailsOfVpcChannelV2Response.
        :rtype: str
        """
        return self._member_type

    @member_type.setter
    def member_type(self, member_type):
        r"""Sets the member_type of this ShowDetailsOfVpcChannelV2Response.

        VPC通道的成员类型。 - ip - ecs

        :param member_type: The member_type of this ShowDetailsOfVpcChannelV2Response.
        :type member_type: str
        """
        self._member_type = member_type

    @property
    def type(self):
        r"""Gets the type of this ShowDetailsOfVpcChannelV2Response.

        vpc通道类型，默认为服务器类型。 - 2：服务器类型 - 3：微服务类型  当vpc_channel_type字段为空时，负载通道类型由type字段控制： 当type不为3或microservice_info为空，VCP通道类型默认为服务器类型。 当type=3，microservice_info不为空，VPC通道类型为微服务类型。  修改负载通道时vpc通道类型不会修改，直接使用原有的vpc通道类型。  此字段待废弃，请使用vpc_channel_type字段指定负载通道类型。

        :return: The type of this ShowDetailsOfVpcChannelV2Response.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowDetailsOfVpcChannelV2Response.

        vpc通道类型，默认为服务器类型。 - 2：服务器类型 - 3：微服务类型  当vpc_channel_type字段为空时，负载通道类型由type字段控制： 当type不为3或microservice_info为空，VCP通道类型默认为服务器类型。 当type=3，microservice_info不为空，VPC通道类型为微服务类型。  修改负载通道时vpc通道类型不会修改，直接使用原有的vpc通道类型。  此字段待废弃，请使用vpc_channel_type字段指定负载通道类型。

        :param type: The type of this ShowDetailsOfVpcChannelV2Response.
        :type type: int
        """
        self._type = type

    @property
    def vpc_channel_type(self):
        r"""Gets the vpc_channel_type of this ShowDetailsOfVpcChannelV2Response.

        vpc通道类型。 - builtin：服务器类型 - microservice： 微服务类型 - reference：引用负载通道类型  当vpc_channel_type为空时，负载通道类型取决于type字段的取值。 当vpc_channel_type不为空，但type字段非空或不为0时，当vpc_channel_type的指定类型与type字段指定的类型冲突时会校验报错。 当vpc_channel_type不为空，且type字段为空或等于0时，直接使用vpc_channel_type字段的值指定负载通道类型。  修改负载通道时vpc通道类型不会修改，直接使用原有的vpc通道类型。

        :return: The vpc_channel_type of this ShowDetailsOfVpcChannelV2Response.
        :rtype: str
        """
        return self._vpc_channel_type

    @vpc_channel_type.setter
    def vpc_channel_type(self, vpc_channel_type):
        r"""Sets the vpc_channel_type of this ShowDetailsOfVpcChannelV2Response.

        vpc通道类型。 - builtin：服务器类型 - microservice： 微服务类型 - reference：引用负载通道类型  当vpc_channel_type为空时，负载通道类型取决于type字段的取值。 当vpc_channel_type不为空，但type字段非空或不为0时，当vpc_channel_type的指定类型与type字段指定的类型冲突时会校验报错。 当vpc_channel_type不为空，且type字段为空或等于0时，直接使用vpc_channel_type字段的值指定负载通道类型。  修改负载通道时vpc通道类型不会修改，直接使用原有的vpc通道类型。

        :param vpc_channel_type: The vpc_channel_type of this ShowDetailsOfVpcChannelV2Response.
        :type vpc_channel_type: str
        """
        self._vpc_channel_type = vpc_channel_type

    @property
    def dict_code(self):
        r"""Gets the dict_code of this ShowDetailsOfVpcChannelV2Response.

        VPC通道的字典编码  支持英文，数字，特殊字符（-_.）  暂不支持

        :return: The dict_code of this ShowDetailsOfVpcChannelV2Response.
        :rtype: str
        """
        return self._dict_code

    @dict_code.setter
    def dict_code(self, dict_code):
        r"""Sets the dict_code of this ShowDetailsOfVpcChannelV2Response.

        VPC通道的字典编码  支持英文，数字，特殊字符（-_.）  暂不支持

        :param dict_code: The dict_code of this ShowDetailsOfVpcChannelV2Response.
        :type dict_code: str
        """
        self._dict_code = dict_code

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowDetailsOfVpcChannelV2Response.

        VPC通道的创建时间

        :return: The create_time of this ShowDetailsOfVpcChannelV2Response.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowDetailsOfVpcChannelV2Response.

        VPC通道的创建时间

        :param create_time: The create_time of this ShowDetailsOfVpcChannelV2Response.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def id(self):
        r"""Gets the id of this ShowDetailsOfVpcChannelV2Response.

        VPC通道的编号

        :return: The id of this ShowDetailsOfVpcChannelV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowDetailsOfVpcChannelV2Response.

        VPC通道的编号

        :param id: The id of this ShowDetailsOfVpcChannelV2Response.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this ShowDetailsOfVpcChannelV2Response.

        VPC通道的状态。 - 1：正常 - 2：异常

        :return: The status of this ShowDetailsOfVpcChannelV2Response.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowDetailsOfVpcChannelV2Response.

        VPC通道的状态。 - 1：正常 - 2：异常

        :param status: The status of this ShowDetailsOfVpcChannelV2Response.
        :type status: int
        """
        self._status = status

    @property
    def member_groups(self):
        r"""Gets the member_groups of this ShowDetailsOfVpcChannelV2Response.

        后端云服务器组列表。

        :return: The member_groups of this ShowDetailsOfVpcChannelV2Response.
        :rtype: list[:class:`huaweicloudsdkapig.v2.MemberGroupInfo`]
        """
        return self._member_groups

    @member_groups.setter
    def member_groups(self, member_groups):
        r"""Sets the member_groups of this ShowDetailsOfVpcChannelV2Response.

        后端云服务器组列表。

        :param member_groups: The member_groups of this ShowDetailsOfVpcChannelV2Response.
        :type member_groups: list[:class:`huaweicloudsdkapig.v2.MemberGroupInfo`]
        """
        self._member_groups = member_groups

    @property
    def microservice_info(self):
        r"""Gets the microservice_info of this ShowDetailsOfVpcChannelV2Response.

        :return: The microservice_info of this ShowDetailsOfVpcChannelV2Response.
        :rtype: :class:`huaweicloudsdkapig.v2.MicroServiceInfo`
        """
        return self._microservice_info

    @microservice_info.setter
    def microservice_info(self, microservice_info):
        r"""Sets the microservice_info of this ShowDetailsOfVpcChannelV2Response.

        :param microservice_info: The microservice_info of this ShowDetailsOfVpcChannelV2Response.
        :type microservice_info: :class:`huaweicloudsdkapig.v2.MicroServiceInfo`
        """
        self._microservice_info = microservice_info

    @property
    def members(self):
        r"""Gets the members of this ShowDetailsOfVpcChannelV2Response.

        后端实例列表。

        :return: The members of this ShowDetailsOfVpcChannelV2Response.
        :rtype: list[:class:`huaweicloudsdkapig.v2.VpcMemberInfo`]
        """
        return self._members

    @members.setter
    def members(self, members):
        r"""Sets the members of this ShowDetailsOfVpcChannelV2Response.

        后端实例列表。

        :param members: The members of this ShowDetailsOfVpcChannelV2Response.
        :type members: list[:class:`huaweicloudsdkapig.v2.VpcMemberInfo`]
        """
        self._members = members

    @property
    def vpc_health_config(self):
        r"""Gets the vpc_health_config of this ShowDetailsOfVpcChannelV2Response.

        :return: The vpc_health_config of this ShowDetailsOfVpcChannelV2Response.
        :rtype: :class:`huaweicloudsdkapig.v2.VpcHealthConfigInfo`
        """
        return self._vpc_health_config

    @vpc_health_config.setter
    def vpc_health_config(self, vpc_health_config):
        r"""Sets the vpc_health_config of this ShowDetailsOfVpcChannelV2Response.

        :param vpc_health_config: The vpc_health_config of this ShowDetailsOfVpcChannelV2Response.
        :type vpc_health_config: :class:`huaweicloudsdkapig.v2.VpcHealthConfigInfo`
        """
        self._vpc_health_config = vpc_health_config

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
        if not isinstance(other, ShowDetailsOfVpcChannelV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
