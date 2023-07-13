# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceByEngineReq:

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
        'description': 'str',
        'engine': 'str',
        'engine_version': 'str',
        'storage_space': 'int',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'available_zones': 'list[str]',
        'product_id': 'str',
        'ssl_enable': 'bool',
        'storage_spec_code': 'str',
        'enterprise_project_id': 'str',
        'enable_acl': 'bool',
        'ipv6_enable': 'bool',
        'enable_publicip': 'bool',
        'publicip_id': 'str',
        'broker_num': 'int',
        'bss_param': 'BssParam'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'engine': 'engine',
        'engine_version': 'engine_version',
        'storage_space': 'storage_space',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'available_zones': 'available_zones',
        'product_id': 'product_id',
        'ssl_enable': 'ssl_enable',
        'storage_spec_code': 'storage_spec_code',
        'enterprise_project_id': 'enterprise_project_id',
        'enable_acl': 'enable_acl',
        'ipv6_enable': 'ipv6_enable',
        'enable_publicip': 'enable_publicip',
        'publicip_id': 'publicip_id',
        'broker_num': 'broker_num',
        'bss_param': 'bss_param'
    }

    def __init__(self, name=None, description=None, engine=None, engine_version=None, storage_space=None, vpc_id=None, subnet_id=None, security_group_id=None, available_zones=None, product_id=None, ssl_enable=None, storage_spec_code=None, enterprise_project_id=None, enable_acl=None, ipv6_enable=None, enable_publicip=None, publicip_id=None, broker_num=None, bss_param=None):
        """CreateInstanceByEngineReq

        The model defined in huaweicloud sdk

        :param name: 实例名称。  由英文字符开头，只能由英文字母、数字、中划线、下划线组成，长度为4~64的字符。
        :type name: str
        :param description: 实例的描述信息。  长度不超过1024的字符串。  &gt; \\与\&quot;在json报文中属于特殊字符，如果参数值中需要显示\\或者\&quot;字符，请在字符前增加转义字符\\，比如\\\\或者\\\&quot;。
        :type description: str
        :param engine: 消息引擎。取值填写为：reliability。
        :type engine: str
        :param engine_version: 消息引擎的版本。取值填写为：4.8.0。
        :type engine_version: str
        :param storage_space: 存储空间。
        :type storage_space: int
        :param vpc_id: 虚拟私有云ID。  获取方法如下：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。
        :type vpc_id: str
        :param subnet_id: 子网信息。  获取方法如下：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。
        :type subnet_id: str
        :param security_group_id: 指定实例所属的安全组。  获取方法如下：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。
        :type security_group_id: str
        :param available_zones: 创建节点到指定且有资源的可用区ID。请参考[查询可用区信息](ListAvailableZones.xml)获取可用区ID。  该参数不能为空数组或者数组的值为空， 请注意查看该可用区是否有资源。  创建RocketMQ实例，支持节点部署在1个或3个及3个以上的可用区。在为节点指定可用区时，用逗号分隔开。
        :type available_zones: list[str]
        :param product_id: RocketMQ实例规格。   - c6.4u8g.cluster.small：单个代理最大Topic数2000，单个代理最大消费组数2000   - c6.4u8g.cluster：单个代理最大Topic数4000，单个代理最大消费组数4000   - c6.8u16g.cluster：单个代理最大Topic数8000，单个代理最大消费组数8000   - c6.12u24g.cluster：单个代理最大Topic数12000，单个代理最大消费组数12000   - c6.16u32g.cluster：单个代理最大Topic数16000，单个代理最大消费组数16000
        :type product_id: str
        :param ssl_enable: 是否打开SSL加密访问。 - true：打开SSL加密访问。 - false：不打开SSL加密访问。
        :type ssl_enable: bool
        :param storage_spec_code: 存储IO规格。   - dms.physical.storage.high.v2: 高IO类型磁盘   - dms.physical.storage.ultra.v2: 超高IO类型磁盘
        :type storage_spec_code: str
        :param enterprise_project_id: 企业项目ID。若为企业项目帐号，该参数必填。
        :type enterprise_project_id: str
        :param enable_acl: 是否开启访问控制列表。
        :type enable_acl: bool
        :param ipv6_enable: 是否支持IPv6。   - true: 支持   - false：不支持
        :type ipv6_enable: bool
        :param enable_publicip: 是否开启公网访问功能。默认不开启公网。 - true：开启 - false：不开启
        :type enable_publicip: bool
        :param publicip_id: 实例绑定的弹性IP地址的ID。  以英文逗号隔开多个弹性IP地址的ID。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。
        :type publicip_id: str
        :param broker_num: 代理个数
        :type broker_num: int
        :param bss_param: 
        :type bss_param: :class:`huaweicloudsdkrocketmq.v2.BssParam`
        """
        
        

        self._name = None
        self._description = None
        self._engine = None
        self._engine_version = None
        self._storage_space = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._available_zones = None
        self._product_id = None
        self._ssl_enable = None
        self._storage_spec_code = None
        self._enterprise_project_id = None
        self._enable_acl = None
        self._ipv6_enable = None
        self._enable_publicip = None
        self._publicip_id = None
        self._broker_num = None
        self._bss_param = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.engine = engine
        self.engine_version = engine_version
        self.storage_space = storage_space
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        self.available_zones = available_zones
        self.product_id = product_id
        if ssl_enable is not None:
            self.ssl_enable = ssl_enable
        self.storage_spec_code = storage_spec_code
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enable_acl is not None:
            self.enable_acl = enable_acl
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if enable_publicip is not None:
            self.enable_publicip = enable_publicip
        if publicip_id is not None:
            self.publicip_id = publicip_id
        self.broker_num = broker_num
        if bss_param is not None:
            self.bss_param = bss_param

    @property
    def name(self):
        """Gets the name of this CreateInstanceByEngineReq.

        实例名称。  由英文字符开头，只能由英文字母、数字、中划线、下划线组成，长度为4~64的字符。

        :return: The name of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateInstanceByEngineReq.

        实例名称。  由英文字符开头，只能由英文字母、数字、中划线、下划线组成，长度为4~64的字符。

        :param name: The name of this CreateInstanceByEngineReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateInstanceByEngineReq.

        实例的描述信息。  长度不超过1024的字符串。  > \\与\"在json报文中属于特殊字符，如果参数值中需要显示\\或者\"字符，请在字符前增加转义字符\\，比如\\\\或者\\\"。

        :return: The description of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateInstanceByEngineReq.

        实例的描述信息。  长度不超过1024的字符串。  > \\与\"在json报文中属于特殊字符，如果参数值中需要显示\\或者\"字符，请在字符前增加转义字符\\，比如\\\\或者\\\"。

        :param description: The description of this CreateInstanceByEngineReq.
        :type description: str
        """
        self._description = description

    @property
    def engine(self):
        """Gets the engine of this CreateInstanceByEngineReq.

        消息引擎。取值填写为：reliability。

        :return: The engine of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this CreateInstanceByEngineReq.

        消息引擎。取值填写为：reliability。

        :param engine: The engine of this CreateInstanceByEngineReq.
        :type engine: str
        """
        self._engine = engine

    @property
    def engine_version(self):
        """Gets the engine_version of this CreateInstanceByEngineReq.

        消息引擎的版本。取值填写为：4.8.0。

        :return: The engine_version of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this CreateInstanceByEngineReq.

        消息引擎的版本。取值填写为：4.8.0。

        :param engine_version: The engine_version of this CreateInstanceByEngineReq.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def storage_space(self):
        """Gets the storage_space of this CreateInstanceByEngineReq.

        存储空间。

        :return: The storage_space of this CreateInstanceByEngineReq.
        :rtype: int
        """
        return self._storage_space

    @storage_space.setter
    def storage_space(self, storage_space):
        """Sets the storage_space of this CreateInstanceByEngineReq.

        存储空间。

        :param storage_space: The storage_space of this CreateInstanceByEngineReq.
        :type storage_space: int
        """
        self._storage_space = storage_space

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateInstanceByEngineReq.

        虚拟私有云ID。  获取方法如下：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。

        :return: The vpc_id of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateInstanceByEngineReq.

        虚拟私有云ID。  获取方法如下：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。

        :param vpc_id: The vpc_id of this CreateInstanceByEngineReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateInstanceByEngineReq.

        子网信息。  获取方法如下：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。

        :return: The subnet_id of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateInstanceByEngineReq.

        子网信息。  获取方法如下：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。

        :param subnet_id: The subnet_id of this CreateInstanceByEngineReq.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this CreateInstanceByEngineReq.

        指定实例所属的安全组。  获取方法如下：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。

        :return: The security_group_id of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this CreateInstanceByEngineReq.

        指定实例所属的安全组。  获取方法如下：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。

        :param security_group_id: The security_group_id of this CreateInstanceByEngineReq.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def available_zones(self):
        """Gets the available_zones of this CreateInstanceByEngineReq.

        创建节点到指定且有资源的可用区ID。请参考[查询可用区信息](ListAvailableZones.xml)获取可用区ID。  该参数不能为空数组或者数组的值为空， 请注意查看该可用区是否有资源。  创建RocketMQ实例，支持节点部署在1个或3个及3个以上的可用区。在为节点指定可用区时，用逗号分隔开。

        :return: The available_zones of this CreateInstanceByEngineReq.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        """Sets the available_zones of this CreateInstanceByEngineReq.

        创建节点到指定且有资源的可用区ID。请参考[查询可用区信息](ListAvailableZones.xml)获取可用区ID。  该参数不能为空数组或者数组的值为空， 请注意查看该可用区是否有资源。  创建RocketMQ实例，支持节点部署在1个或3个及3个以上的可用区。在为节点指定可用区时，用逗号分隔开。

        :param available_zones: The available_zones of this CreateInstanceByEngineReq.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def product_id(self):
        """Gets the product_id of this CreateInstanceByEngineReq.

        RocketMQ实例规格。   - c6.4u8g.cluster.small：单个代理最大Topic数2000，单个代理最大消费组数2000   - c6.4u8g.cluster：单个代理最大Topic数4000，单个代理最大消费组数4000   - c6.8u16g.cluster：单个代理最大Topic数8000，单个代理最大消费组数8000   - c6.12u24g.cluster：单个代理最大Topic数12000，单个代理最大消费组数12000   - c6.16u32g.cluster：单个代理最大Topic数16000，单个代理最大消费组数16000

        :return: The product_id of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this CreateInstanceByEngineReq.

        RocketMQ实例规格。   - c6.4u8g.cluster.small：单个代理最大Topic数2000，单个代理最大消费组数2000   - c6.4u8g.cluster：单个代理最大Topic数4000，单个代理最大消费组数4000   - c6.8u16g.cluster：单个代理最大Topic数8000，单个代理最大消费组数8000   - c6.12u24g.cluster：单个代理最大Topic数12000，单个代理最大消费组数12000   - c6.16u32g.cluster：单个代理最大Topic数16000，单个代理最大消费组数16000

        :param product_id: The product_id of this CreateInstanceByEngineReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def ssl_enable(self):
        """Gets the ssl_enable of this CreateInstanceByEngineReq.

        是否打开SSL加密访问。 - true：打开SSL加密访问。 - false：不打开SSL加密访问。

        :return: The ssl_enable of this CreateInstanceByEngineReq.
        :rtype: bool
        """
        return self._ssl_enable

    @ssl_enable.setter
    def ssl_enable(self, ssl_enable):
        """Sets the ssl_enable of this CreateInstanceByEngineReq.

        是否打开SSL加密访问。 - true：打开SSL加密访问。 - false：不打开SSL加密访问。

        :param ssl_enable: The ssl_enable of this CreateInstanceByEngineReq.
        :type ssl_enable: bool
        """
        self._ssl_enable = ssl_enable

    @property
    def storage_spec_code(self):
        """Gets the storage_spec_code of this CreateInstanceByEngineReq.

        存储IO规格。   - dms.physical.storage.high.v2: 高IO类型磁盘   - dms.physical.storage.ultra.v2: 超高IO类型磁盘

        :return: The storage_spec_code of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._storage_spec_code

    @storage_spec_code.setter
    def storage_spec_code(self, storage_spec_code):
        """Sets the storage_spec_code of this CreateInstanceByEngineReq.

        存储IO规格。   - dms.physical.storage.high.v2: 高IO类型磁盘   - dms.physical.storage.ultra.v2: 超高IO类型磁盘

        :param storage_spec_code: The storage_spec_code of this CreateInstanceByEngineReq.
        :type storage_spec_code: str
        """
        self._storage_spec_code = storage_spec_code

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateInstanceByEngineReq.

        企业项目ID。若为企业项目帐号，该参数必填。

        :return: The enterprise_project_id of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateInstanceByEngineReq.

        企业项目ID。若为企业项目帐号，该参数必填。

        :param enterprise_project_id: The enterprise_project_id of this CreateInstanceByEngineReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enable_acl(self):
        """Gets the enable_acl of this CreateInstanceByEngineReq.

        是否开启访问控制列表。

        :return: The enable_acl of this CreateInstanceByEngineReq.
        :rtype: bool
        """
        return self._enable_acl

    @enable_acl.setter
    def enable_acl(self, enable_acl):
        """Sets the enable_acl of this CreateInstanceByEngineReq.

        是否开启访问控制列表。

        :param enable_acl: The enable_acl of this CreateInstanceByEngineReq.
        :type enable_acl: bool
        """
        self._enable_acl = enable_acl

    @property
    def ipv6_enable(self):
        """Gets the ipv6_enable of this CreateInstanceByEngineReq.

        是否支持IPv6。   - true: 支持   - false：不支持

        :return: The ipv6_enable of this CreateInstanceByEngineReq.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        """Sets the ipv6_enable of this CreateInstanceByEngineReq.

        是否支持IPv6。   - true: 支持   - false：不支持

        :param ipv6_enable: The ipv6_enable of this CreateInstanceByEngineReq.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def enable_publicip(self):
        """Gets the enable_publicip of this CreateInstanceByEngineReq.

        是否开启公网访问功能。默认不开启公网。 - true：开启 - false：不开启

        :return: The enable_publicip of this CreateInstanceByEngineReq.
        :rtype: bool
        """
        return self._enable_publicip

    @enable_publicip.setter
    def enable_publicip(self, enable_publicip):
        """Sets the enable_publicip of this CreateInstanceByEngineReq.

        是否开启公网访问功能。默认不开启公网。 - true：开启 - false：不开启

        :param enable_publicip: The enable_publicip of this CreateInstanceByEngineReq.
        :type enable_publicip: bool
        """
        self._enable_publicip = enable_publicip

    @property
    def publicip_id(self):
        """Gets the publicip_id of this CreateInstanceByEngineReq.

        实例绑定的弹性IP地址的ID。  以英文逗号隔开多个弹性IP地址的ID。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。

        :return: The publicip_id of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        """Sets the publicip_id of this CreateInstanceByEngineReq.

        实例绑定的弹性IP地址的ID。  以英文逗号隔开多个弹性IP地址的ID。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。

        :param publicip_id: The publicip_id of this CreateInstanceByEngineReq.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def broker_num(self):
        """Gets the broker_num of this CreateInstanceByEngineReq.

        代理个数

        :return: The broker_num of this CreateInstanceByEngineReq.
        :rtype: int
        """
        return self._broker_num

    @broker_num.setter
    def broker_num(self, broker_num):
        """Sets the broker_num of this CreateInstanceByEngineReq.

        代理个数

        :param broker_num: The broker_num of this CreateInstanceByEngineReq.
        :type broker_num: int
        """
        self._broker_num = broker_num

    @property
    def bss_param(self):
        """Gets the bss_param of this CreateInstanceByEngineReq.

        :return: The bss_param of this CreateInstanceByEngineReq.
        :rtype: :class:`huaweicloudsdkrocketmq.v2.BssParam`
        """
        return self._bss_param

    @bss_param.setter
    def bss_param(self, bss_param):
        """Sets the bss_param of this CreateInstanceByEngineReq.

        :param bss_param: The bss_param of this CreateInstanceByEngineReq.
        :type bss_param: :class:`huaweicloudsdkrocketmq.v2.BssParam`
        """
        self._bss_param = bss_param

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
        if not isinstance(other, CreateInstanceByEngineReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
