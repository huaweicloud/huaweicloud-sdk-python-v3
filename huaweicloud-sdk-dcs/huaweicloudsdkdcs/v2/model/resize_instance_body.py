# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeInstanceBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_code': 'str',
        'new_capacity': 'int',
        'bss_param': 'BssParamEntity',
        'reserved_ip': 'list[str]',
        'change_type': 'str',
        'available_zones': 'list[str]',
        'node_list': 'list[str]',
        'execute_immediately': 'bool'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'new_capacity': 'new_capacity',
        'bss_param': 'bss_param',
        'reserved_ip': 'reserved_ip',
        'change_type': 'change_type',
        'available_zones': 'available_zones',
        'node_list': 'node_list',
        'execute_immediately': 'execute_immediately'
    }

    def __init__(self, spec_code=None, new_capacity=None, bss_param=None, reserved_ip=None, change_type=None, available_zones=None, node_list=None, execute_immediately=None):
        """ResizeInstanceBody

        The model defined in huaweicloud sdk

        :param spec_code: 产品规格编码。具体查询方法如下：  - 方法一：查询产品介绍中的[实例规格](https://support.huaweicloud.com/productdesc-dcs/dcs-pd-0522002.html) - 方法二：登录分布式缓存的控制台界面，点击购买缓存实例，查找对应的实例规格名称 - 方法三：调用[查询产品规格](https://support.huaweicloud.com/api-dcs/ListFlavors.html)接口查询。
        :type spec_code: str
        :param new_capacity: 新的缓存实例规格，单位：GB。 Redis4.0和Redis5.0：单机和主备类型实例取值：0.125、0.25、0.5、1、2、4、8、16、32、64。Cluster集群实例规格支持24、32、48、64、96、128、192、256、384、512、768、1024。 Memcached：单机和主备类型实例取值：2、4、8、16、32、64。 
        :type new_capacity: int
        :param bss_param: 
        :type bss_param: :class:`huaweicloudsdkdcs.v2.BssParamEntity`
        :param reserved_ip: 需要保留的节点ip。cluster集群缩容时需要填写，不填写时系统将随机删除多余的分片
        :type reserved_ip: list[str]
        :param change_type: 变更类型，Redis 4.0或者5.0主备实例进行副本数变更时必选。 - createReplication: 添加副本 - deleteReplication: 删除副本 
        :type change_type: str
        :param available_zones: Redis 4.0或者5.0主备实例进行添加副本时必选，指定每个副本所在的可用区Code，使用前需要先确认该可用区资源是否售罄。  具体查询方法，请参考[查询可用区信息](https://support.huaweicloud.com/api-dcs/ListAvailableZones.html) 
        :type available_zones: list[str]
        :param node_list: Redis 4.0或者5.0主备实例进行删除副本时必选，指定需要删除的节点ID，目前仅支持一次删除一个副本。  节点ID查询方法，请参考[查询分片信息](https://support.huaweicloud.com/api-dcs/ListGroupReplicationInfo.html) 
        :type node_list: list[str]
        :param execute_immediately: 是否立即变更。默认值为true。 - true: 立即变更 - false: 可维护时间窗内进行变更 
        :type execute_immediately: bool
        """
        
        

        self._spec_code = None
        self._new_capacity = None
        self._bss_param = None
        self._reserved_ip = None
        self._change_type = None
        self._available_zones = None
        self._node_list = None
        self._execute_immediately = None
        self.discriminator = None

        self.spec_code = spec_code
        self.new_capacity = new_capacity
        if bss_param is not None:
            self.bss_param = bss_param
        if reserved_ip is not None:
            self.reserved_ip = reserved_ip
        if change_type is not None:
            self.change_type = change_type
        if available_zones is not None:
            self.available_zones = available_zones
        if node_list is not None:
            self.node_list = node_list
        if execute_immediately is not None:
            self.execute_immediately = execute_immediately

    @property
    def spec_code(self):
        """Gets the spec_code of this ResizeInstanceBody.

        产品规格编码。具体查询方法如下：  - 方法一：查询产品介绍中的[实例规格](https://support.huaweicloud.com/productdesc-dcs/dcs-pd-0522002.html) - 方法二：登录分布式缓存的控制台界面，点击购买缓存实例，查找对应的实例规格名称 - 方法三：调用[查询产品规格](https://support.huaweicloud.com/api-dcs/ListFlavors.html)接口查询。

        :return: The spec_code of this ResizeInstanceBody.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this ResizeInstanceBody.

        产品规格编码。具体查询方法如下：  - 方法一：查询产品介绍中的[实例规格](https://support.huaweicloud.com/productdesc-dcs/dcs-pd-0522002.html) - 方法二：登录分布式缓存的控制台界面，点击购买缓存实例，查找对应的实例规格名称 - 方法三：调用[查询产品规格](https://support.huaweicloud.com/api-dcs/ListFlavors.html)接口查询。

        :param spec_code: The spec_code of this ResizeInstanceBody.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def new_capacity(self):
        """Gets the new_capacity of this ResizeInstanceBody.

        新的缓存实例规格，单位：GB。 Redis4.0和Redis5.0：单机和主备类型实例取值：0.125、0.25、0.5、1、2、4、8、16、32、64。Cluster集群实例规格支持24、32、48、64、96、128、192、256、384、512、768、1024。 Memcached：单机和主备类型实例取值：2、4、8、16、32、64。 

        :return: The new_capacity of this ResizeInstanceBody.
        :rtype: int
        """
        return self._new_capacity

    @new_capacity.setter
    def new_capacity(self, new_capacity):
        """Sets the new_capacity of this ResizeInstanceBody.

        新的缓存实例规格，单位：GB。 Redis4.0和Redis5.0：单机和主备类型实例取值：0.125、0.25、0.5、1、2、4、8、16、32、64。Cluster集群实例规格支持24、32、48、64、96、128、192、256、384、512、768、1024。 Memcached：单机和主备类型实例取值：2、4、8、16、32、64。 

        :param new_capacity: The new_capacity of this ResizeInstanceBody.
        :type new_capacity: int
        """
        self._new_capacity = new_capacity

    @property
    def bss_param(self):
        """Gets the bss_param of this ResizeInstanceBody.

        :return: The bss_param of this ResizeInstanceBody.
        :rtype: :class:`huaweicloudsdkdcs.v2.BssParamEntity`
        """
        return self._bss_param

    @bss_param.setter
    def bss_param(self, bss_param):
        """Sets the bss_param of this ResizeInstanceBody.

        :param bss_param: The bss_param of this ResizeInstanceBody.
        :type bss_param: :class:`huaweicloudsdkdcs.v2.BssParamEntity`
        """
        self._bss_param = bss_param

    @property
    def reserved_ip(self):
        """Gets the reserved_ip of this ResizeInstanceBody.

        需要保留的节点ip。cluster集群缩容时需要填写，不填写时系统将随机删除多余的分片

        :return: The reserved_ip of this ResizeInstanceBody.
        :rtype: list[str]
        """
        return self._reserved_ip

    @reserved_ip.setter
    def reserved_ip(self, reserved_ip):
        """Sets the reserved_ip of this ResizeInstanceBody.

        需要保留的节点ip。cluster集群缩容时需要填写，不填写时系统将随机删除多余的分片

        :param reserved_ip: The reserved_ip of this ResizeInstanceBody.
        :type reserved_ip: list[str]
        """
        self._reserved_ip = reserved_ip

    @property
    def change_type(self):
        """Gets the change_type of this ResizeInstanceBody.

        变更类型，Redis 4.0或者5.0主备实例进行副本数变更时必选。 - createReplication: 添加副本 - deleteReplication: 删除副本 

        :return: The change_type of this ResizeInstanceBody.
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        """Sets the change_type of this ResizeInstanceBody.

        变更类型，Redis 4.0或者5.0主备实例进行副本数变更时必选。 - createReplication: 添加副本 - deleteReplication: 删除副本 

        :param change_type: The change_type of this ResizeInstanceBody.
        :type change_type: str
        """
        self._change_type = change_type

    @property
    def available_zones(self):
        """Gets the available_zones of this ResizeInstanceBody.

        Redis 4.0或者5.0主备实例进行添加副本时必选，指定每个副本所在的可用区Code，使用前需要先确认该可用区资源是否售罄。  具体查询方法，请参考[查询可用区信息](https://support.huaweicloud.com/api-dcs/ListAvailableZones.html) 

        :return: The available_zones of this ResizeInstanceBody.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        """Sets the available_zones of this ResizeInstanceBody.

        Redis 4.0或者5.0主备实例进行添加副本时必选，指定每个副本所在的可用区Code，使用前需要先确认该可用区资源是否售罄。  具体查询方法，请参考[查询可用区信息](https://support.huaweicloud.com/api-dcs/ListAvailableZones.html) 

        :param available_zones: The available_zones of this ResizeInstanceBody.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def node_list(self):
        """Gets the node_list of this ResizeInstanceBody.

        Redis 4.0或者5.0主备实例进行删除副本时必选，指定需要删除的节点ID，目前仅支持一次删除一个副本。  节点ID查询方法，请参考[查询分片信息](https://support.huaweicloud.com/api-dcs/ListGroupReplicationInfo.html) 

        :return: The node_list of this ResizeInstanceBody.
        :rtype: list[str]
        """
        return self._node_list

    @node_list.setter
    def node_list(self, node_list):
        """Sets the node_list of this ResizeInstanceBody.

        Redis 4.0或者5.0主备实例进行删除副本时必选，指定需要删除的节点ID，目前仅支持一次删除一个副本。  节点ID查询方法，请参考[查询分片信息](https://support.huaweicloud.com/api-dcs/ListGroupReplicationInfo.html) 

        :param node_list: The node_list of this ResizeInstanceBody.
        :type node_list: list[str]
        """
        self._node_list = node_list

    @property
    def execute_immediately(self):
        """Gets the execute_immediately of this ResizeInstanceBody.

        是否立即变更。默认值为true。 - true: 立即变更 - false: 可维护时间窗内进行变更 

        :return: The execute_immediately of this ResizeInstanceBody.
        :rtype: bool
        """
        return self._execute_immediately

    @execute_immediately.setter
    def execute_immediately(self, execute_immediately):
        """Sets the execute_immediately of this ResizeInstanceBody.

        是否立即变更。默认值为true。 - true: 立即变更 - false: 可维护时间窗内进行变更 

        :param execute_immediately: The execute_immediately of this ResizeInstanceBody.
        :type execute_immediately: bool
        """
        self._execute_immediately = execute_immediately

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
        if not isinstance(other, ResizeInstanceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
