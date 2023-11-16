# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAppServerReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'server_group_id': 'str',
        'availability_zone': 'str',
        'subscription_num': 'int',
        'nics': 'list[Nic]',
        'ou_name': 'str',
        'product_id': 'str',
        'os_type': 'str',
        'root_volume': 'Volume',
        'scheduler_hints': 'WdhParam',
        'subnet_id': 'str',
        'vpc_id': 'str',
        'update_access_agent': 'bool',
        'create_server_extend_param': 'CreateServerExtendParam'
    }

    attribute_map = {
        'type': 'type',
        'server_group_id': 'server_group_id',
        'availability_zone': 'availability_zone',
        'subscription_num': 'subscription_num',
        'nics': 'nics',
        'ou_name': 'ou_name',
        'product_id': 'product_id',
        'os_type': 'os_type',
        'root_volume': 'root_volume',
        'scheduler_hints': 'scheduler_hints',
        'subnet_id': 'subnet_id',
        'vpc_id': 'vpc_id',
        'update_access_agent': 'update_access_agent',
        'create_server_extend_param': 'create_server_extend_param'
    }

    def __init__(self, type=None, server_group_id=None, availability_zone=None, subscription_num=None, nics=None, ou_name=None, product_id=None, os_type=None, root_volume=None, scheduler_hints=None, subnet_id=None, vpc_id=None, update_access_agent=None, create_server_extend_param=None):
        """CreateAppServerReq

        The model defined in huaweicloud sdk

        :param type: 创建云服务类型，当前仅支持创建云应用：createApps
        :type type: str
        :param server_group_id: 服务器组唯一标识
        :type server_group_id: str
        :param availability_zone: 可用分区。 &gt; - 将服务创建到指定的可用分区，如果不指定则使用系统随机的可用分区。 &gt; - 获取方式详见可用区管理ListAvailabilityZone：\&quot;GET  /v1/{project_id}/availability-zone\&quot;。
        :type availability_zone: str
        :param subscription_num: 订购数量
        :type subscription_num: int
        :param nics: 服务对应的网卡信息，当前未使用该字段。
        :type nics: list[:class:`huaweicloudsdkworkspaceapp.v1.Nic`]
        :param ou_name: OU名称，在对接AD时使用，需提前在AD中创建OU。
        :type ou_name: str
        :param product_id: 产品ID。 &gt; - 获取方式详见产品套餐管理ListProduct：\&quot;GET /v1/{project_id}/product\&quot;。
        :type product_id: str
        :param os_type: 操作系统类型，当前仅支持Windows。
        :type os_type: str
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkworkspaceapp.v1.Volume`
        :param scheduler_hints: 
        :type scheduler_hints: :class:`huaweicloudsdkworkspaceapp.v1.WdhParam`
        :param subnet_id: 网卡对应的子网ID
        :type subnet_id: str
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param update_access_agent: 是否自动升级hda版本
        :type update_access_agent: bool
        :param create_server_extend_param: 
        :type create_server_extend_param: :class:`huaweicloudsdkworkspaceapp.v1.CreateServerExtendParam`
        """
        
        

        self._type = None
        self._server_group_id = None
        self._availability_zone = None
        self._subscription_num = None
        self._nics = None
        self._ou_name = None
        self._product_id = None
        self._os_type = None
        self._root_volume = None
        self._scheduler_hints = None
        self._subnet_id = None
        self._vpc_id = None
        self._update_access_agent = None
        self._create_server_extend_param = None
        self.discriminator = None

        self.type = type
        self.server_group_id = server_group_id
        if availability_zone is not None:
            self.availability_zone = availability_zone
        self.subscription_num = subscription_num
        if nics is not None:
            self.nics = nics
        if ou_name is not None:
            self.ou_name = ou_name
        self.product_id = product_id
        if os_type is not None:
            self.os_type = os_type
        self.root_volume = root_volume
        if scheduler_hints is not None:
            self.scheduler_hints = scheduler_hints
        self.subnet_id = subnet_id
        self.vpc_id = vpc_id
        if update_access_agent is not None:
            self.update_access_agent = update_access_agent
        if create_server_extend_param is not None:
            self.create_server_extend_param = create_server_extend_param

    @property
    def type(self):
        """Gets the type of this CreateAppServerReq.

        创建云服务类型，当前仅支持创建云应用：createApps

        :return: The type of this CreateAppServerReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateAppServerReq.

        创建云服务类型，当前仅支持创建云应用：createApps

        :param type: The type of this CreateAppServerReq.
        :type type: str
        """
        self._type = type

    @property
    def server_group_id(self):
        """Gets the server_group_id of this CreateAppServerReq.

        服务器组唯一标识

        :return: The server_group_id of this CreateAppServerReq.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this CreateAppServerReq.

        服务器组唯一标识

        :param server_group_id: The server_group_id of this CreateAppServerReq.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateAppServerReq.

        可用分区。 > - 将服务创建到指定的可用分区，如果不指定则使用系统随机的可用分区。 > - 获取方式详见可用区管理ListAvailabilityZone：\"GET  /v1/{project_id}/availability-zone\"。

        :return: The availability_zone of this CreateAppServerReq.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateAppServerReq.

        可用分区。 > - 将服务创建到指定的可用分区，如果不指定则使用系统随机的可用分区。 > - 获取方式详见可用区管理ListAvailabilityZone：\"GET  /v1/{project_id}/availability-zone\"。

        :param availability_zone: The availability_zone of this CreateAppServerReq.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def subscription_num(self):
        """Gets the subscription_num of this CreateAppServerReq.

        订购数量

        :return: The subscription_num of this CreateAppServerReq.
        :rtype: int
        """
        return self._subscription_num

    @subscription_num.setter
    def subscription_num(self, subscription_num):
        """Sets the subscription_num of this CreateAppServerReq.

        订购数量

        :param subscription_num: The subscription_num of this CreateAppServerReq.
        :type subscription_num: int
        """
        self._subscription_num = subscription_num

    @property
    def nics(self):
        """Gets the nics of this CreateAppServerReq.

        服务对应的网卡信息，当前未使用该字段。

        :return: The nics of this CreateAppServerReq.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.Nic`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this CreateAppServerReq.

        服务对应的网卡信息，当前未使用该字段。

        :param nics: The nics of this CreateAppServerReq.
        :type nics: list[:class:`huaweicloudsdkworkspaceapp.v1.Nic`]
        """
        self._nics = nics

    @property
    def ou_name(self):
        """Gets the ou_name of this CreateAppServerReq.

        OU名称，在对接AD时使用，需提前在AD中创建OU。

        :return: The ou_name of this CreateAppServerReq.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        """Sets the ou_name of this CreateAppServerReq.

        OU名称，在对接AD时使用，需提前在AD中创建OU。

        :param ou_name: The ou_name of this CreateAppServerReq.
        :type ou_name: str
        """
        self._ou_name = ou_name

    @property
    def product_id(self):
        """Gets the product_id of this CreateAppServerReq.

        产品ID。 > - 获取方式详见产品套餐管理ListProduct：\"GET /v1/{project_id}/product\"。

        :return: The product_id of this CreateAppServerReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this CreateAppServerReq.

        产品ID。 > - 获取方式详见产品套餐管理ListProduct：\"GET /v1/{project_id}/product\"。

        :param product_id: The product_id of this CreateAppServerReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def os_type(self):
        """Gets the os_type of this CreateAppServerReq.

        操作系统类型，当前仅支持Windows。

        :return: The os_type of this CreateAppServerReq.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this CreateAppServerReq.

        操作系统类型，当前仅支持Windows。

        :param os_type: The os_type of this CreateAppServerReq.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def root_volume(self):
        """Gets the root_volume of this CreateAppServerReq.

        :return: The root_volume of this CreateAppServerReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.Volume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        """Sets the root_volume of this CreateAppServerReq.

        :param root_volume: The root_volume of this CreateAppServerReq.
        :type root_volume: :class:`huaweicloudsdkworkspaceapp.v1.Volume`
        """
        self._root_volume = root_volume

    @property
    def scheduler_hints(self):
        """Gets the scheduler_hints of this CreateAppServerReq.

        :return: The scheduler_hints of this CreateAppServerReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.WdhParam`
        """
        return self._scheduler_hints

    @scheduler_hints.setter
    def scheduler_hints(self, scheduler_hints):
        """Sets the scheduler_hints of this CreateAppServerReq.

        :param scheduler_hints: The scheduler_hints of this CreateAppServerReq.
        :type scheduler_hints: :class:`huaweicloudsdkworkspaceapp.v1.WdhParam`
        """
        self._scheduler_hints = scheduler_hints

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateAppServerReq.

        网卡对应的子网ID

        :return: The subnet_id of this CreateAppServerReq.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateAppServerReq.

        网卡对应的子网ID

        :param subnet_id: The subnet_id of this CreateAppServerReq.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateAppServerReq.

        虚拟私有云ID。

        :return: The vpc_id of this CreateAppServerReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateAppServerReq.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this CreateAppServerReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def update_access_agent(self):
        """Gets the update_access_agent of this CreateAppServerReq.

        是否自动升级hda版本

        :return: The update_access_agent of this CreateAppServerReq.
        :rtype: bool
        """
        return self._update_access_agent

    @update_access_agent.setter
    def update_access_agent(self, update_access_agent):
        """Sets the update_access_agent of this CreateAppServerReq.

        是否自动升级hda版本

        :param update_access_agent: The update_access_agent of this CreateAppServerReq.
        :type update_access_agent: bool
        """
        self._update_access_agent = update_access_agent

    @property
    def create_server_extend_param(self):
        """Gets the create_server_extend_param of this CreateAppServerReq.

        :return: The create_server_extend_param of this CreateAppServerReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateServerExtendParam`
        """
        return self._create_server_extend_param

    @create_server_extend_param.setter
    def create_server_extend_param(self, create_server_extend_param):
        """Sets the create_server_extend_param of this CreateAppServerReq.

        :param create_server_extend_param: The create_server_extend_param of this CreateAppServerReq.
        :type create_server_extend_param: :class:`huaweicloudsdkworkspaceapp.v1.CreateServerExtendParam`
        """
        self._create_server_extend_param = create_server_extend_param

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
        if not isinstance(other, CreateAppServerReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
