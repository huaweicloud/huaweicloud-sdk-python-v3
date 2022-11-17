# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorsItems:

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
        'cloud_service_type_code': 'str',
        'cloud_resource_type_code': 'str',
        'cache_mode': 'str',
        'engine': 'str',
        'engine_version': 'str',
        'product_type': 'str',
        'cpu_type': 'str',
        'storage_type': 'str',
        'capacity': 'list[str]',
        'billing_mode': 'list[str]',
        'tenant_ip_count': 'int',
        'pricing_type': 'str',
        'is_dec': 'bool',
        'attrs': 'list[AttrsObject]',
        'flavors_available_zones': 'list[FlavorAzObject]'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'cloud_service_type_code': 'cloud_service_type_code',
        'cloud_resource_type_code': 'cloud_resource_type_code',
        'cache_mode': 'cache_mode',
        'engine': 'engine',
        'engine_version': 'engine_version',
        'product_type': 'product_type',
        'cpu_type': 'cpu_type',
        'storage_type': 'storage_type',
        'capacity': 'capacity',
        'billing_mode': 'billing_mode',
        'tenant_ip_count': 'tenant_ip_count',
        'pricing_type': 'pricing_type',
        'is_dec': 'is_dec',
        'attrs': 'attrs',
        'flavors_available_zones': 'flavors_available_zones'
    }

    def __init__(self, spec_code=None, cloud_service_type_code=None, cloud_resource_type_code=None, cache_mode=None, engine=None, engine_version=None, product_type=None, cpu_type=None, storage_type=None, capacity=None, billing_mode=None, tenant_ip_count=None, pricing_type=None, is_dec=None, attrs=None, flavors_available_zones=None):
        """FlavorsItems

        The model defined in huaweicloud sdk

        :param spec_code: 产品规格编码。
        :type spec_code: str
        :param cloud_service_type_code: 云服务类型编码。
        :type cloud_service_type_code: str
        :param cloud_resource_type_code: 云资源类型编码。
        :type cloud_resource_type_code: str
        :param cache_mode: 缓存实例类型。取值范围如下： - single：表示单机实例 - ha：表示主备实例 - cluster：表示cluster集群实例 - proxy：表示Proxy集群实例 - ha_rw_split： 表示读写分离实例 
        :type cache_mode: str
        :param engine: 缓存引擎类型。
        :type engine: str
        :param engine_version: 缓存版本，当缓存引擎为Redis时，取值为3.0、4.0或5.0。
        :type engine_version: str
        :param product_type: Redis缓存实例的产品类型。取值当前仅支持： generic：标准类型 
        :type product_type: str
        :param cpu_type: CPU架构类型。取值范围如下： - x86_64：X86架构 - aarch64: ARM架构 
        :type cpu_type: str
        :param storage_type: 存储类型，取值当前仅支持： DRAM:内存存储 
        :type storage_type: str
        :param capacity: 缓存容量（G Byte）。
        :type capacity: list[str]
        :param billing_mode: 计费模式，取值范围如下： - Hourly：按需计费 - Monthly: 包月计费 - Yearly: 包周期计费 
        :type billing_mode: list[str]
        :param tenant_ip_count: 租户侧IP数量。
        :type tenant_ip_count: int
        :param pricing_type: 定价类型，取值如下： - tier: 阶梯定价，一个规格对应多个容量 - normal: 规格和容量一一对应 
        :type pricing_type: str
        :param is_dec: 是否支持专属云。
        :type is_dec: bool
        :param attrs: 规格的其他信息。
        :type attrs: list[:class:`huaweicloudsdkdcs.v2.AttrsObject`]
        :param flavors_available_zones: 有资源的可用区。
        :type flavors_available_zones: list[:class:`huaweicloudsdkdcs.v2.FlavorAzObject`]
        """
        
        

        self._spec_code = None
        self._cloud_service_type_code = None
        self._cloud_resource_type_code = None
        self._cache_mode = None
        self._engine = None
        self._engine_version = None
        self._product_type = None
        self._cpu_type = None
        self._storage_type = None
        self._capacity = None
        self._billing_mode = None
        self._tenant_ip_count = None
        self._pricing_type = None
        self._is_dec = None
        self._attrs = None
        self._flavors_available_zones = None
        self.discriminator = None

        if spec_code is not None:
            self.spec_code = spec_code
        if cloud_service_type_code is not None:
            self.cloud_service_type_code = cloud_service_type_code
        if cloud_resource_type_code is not None:
            self.cloud_resource_type_code = cloud_resource_type_code
        if cache_mode is not None:
            self.cache_mode = cache_mode
        if engine is not None:
            self.engine = engine
        if engine_version is not None:
            self.engine_version = engine_version
        if product_type is not None:
            self.product_type = product_type
        if cpu_type is not None:
            self.cpu_type = cpu_type
        if storage_type is not None:
            self.storage_type = storage_type
        if capacity is not None:
            self.capacity = capacity
        if billing_mode is not None:
            self.billing_mode = billing_mode
        if tenant_ip_count is not None:
            self.tenant_ip_count = tenant_ip_count
        if pricing_type is not None:
            self.pricing_type = pricing_type
        if is_dec is not None:
            self.is_dec = is_dec
        if attrs is not None:
            self.attrs = attrs
        if flavors_available_zones is not None:
            self.flavors_available_zones = flavors_available_zones

    @property
    def spec_code(self):
        """Gets the spec_code of this FlavorsItems.

        产品规格编码。

        :return: The spec_code of this FlavorsItems.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this FlavorsItems.

        产品规格编码。

        :param spec_code: The spec_code of this FlavorsItems.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def cloud_service_type_code(self):
        """Gets the cloud_service_type_code of this FlavorsItems.

        云服务类型编码。

        :return: The cloud_service_type_code of this FlavorsItems.
        :rtype: str
        """
        return self._cloud_service_type_code

    @cloud_service_type_code.setter
    def cloud_service_type_code(self, cloud_service_type_code):
        """Sets the cloud_service_type_code of this FlavorsItems.

        云服务类型编码。

        :param cloud_service_type_code: The cloud_service_type_code of this FlavorsItems.
        :type cloud_service_type_code: str
        """
        self._cloud_service_type_code = cloud_service_type_code

    @property
    def cloud_resource_type_code(self):
        """Gets the cloud_resource_type_code of this FlavorsItems.

        云资源类型编码。

        :return: The cloud_resource_type_code of this FlavorsItems.
        :rtype: str
        """
        return self._cloud_resource_type_code

    @cloud_resource_type_code.setter
    def cloud_resource_type_code(self, cloud_resource_type_code):
        """Sets the cloud_resource_type_code of this FlavorsItems.

        云资源类型编码。

        :param cloud_resource_type_code: The cloud_resource_type_code of this FlavorsItems.
        :type cloud_resource_type_code: str
        """
        self._cloud_resource_type_code = cloud_resource_type_code

    @property
    def cache_mode(self):
        """Gets the cache_mode of this FlavorsItems.

        缓存实例类型。取值范围如下： - single：表示单机实例 - ha：表示主备实例 - cluster：表示cluster集群实例 - proxy：表示Proxy集群实例 - ha_rw_split： 表示读写分离实例 

        :return: The cache_mode of this FlavorsItems.
        :rtype: str
        """
        return self._cache_mode

    @cache_mode.setter
    def cache_mode(self, cache_mode):
        """Sets the cache_mode of this FlavorsItems.

        缓存实例类型。取值范围如下： - single：表示单机实例 - ha：表示主备实例 - cluster：表示cluster集群实例 - proxy：表示Proxy集群实例 - ha_rw_split： 表示读写分离实例 

        :param cache_mode: The cache_mode of this FlavorsItems.
        :type cache_mode: str
        """
        self._cache_mode = cache_mode

    @property
    def engine(self):
        """Gets the engine of this FlavorsItems.

        缓存引擎类型。

        :return: The engine of this FlavorsItems.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this FlavorsItems.

        缓存引擎类型。

        :param engine: The engine of this FlavorsItems.
        :type engine: str
        """
        self._engine = engine

    @property
    def engine_version(self):
        """Gets the engine_version of this FlavorsItems.

        缓存版本，当缓存引擎为Redis时，取值为3.0、4.0或5.0。

        :return: The engine_version of this FlavorsItems.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this FlavorsItems.

        缓存版本，当缓存引擎为Redis时，取值为3.0、4.0或5.0。

        :param engine_version: The engine_version of this FlavorsItems.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def product_type(self):
        """Gets the product_type of this FlavorsItems.

        Redis缓存实例的产品类型。取值当前仅支持： generic：标准类型 

        :return: The product_type of this FlavorsItems.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this FlavorsItems.

        Redis缓存实例的产品类型。取值当前仅支持： generic：标准类型 

        :param product_type: The product_type of this FlavorsItems.
        :type product_type: str
        """
        self._product_type = product_type

    @property
    def cpu_type(self):
        """Gets the cpu_type of this FlavorsItems.

        CPU架构类型。取值范围如下： - x86_64：X86架构 - aarch64: ARM架构 

        :return: The cpu_type of this FlavorsItems.
        :rtype: str
        """
        return self._cpu_type

    @cpu_type.setter
    def cpu_type(self, cpu_type):
        """Sets the cpu_type of this FlavorsItems.

        CPU架构类型。取值范围如下： - x86_64：X86架构 - aarch64: ARM架构 

        :param cpu_type: The cpu_type of this FlavorsItems.
        :type cpu_type: str
        """
        self._cpu_type = cpu_type

    @property
    def storage_type(self):
        """Gets the storage_type of this FlavorsItems.

        存储类型，取值当前仅支持： DRAM:内存存储 

        :return: The storage_type of this FlavorsItems.
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this FlavorsItems.

        存储类型，取值当前仅支持： DRAM:内存存储 

        :param storage_type: The storage_type of this FlavorsItems.
        :type storage_type: str
        """
        self._storage_type = storage_type

    @property
    def capacity(self):
        """Gets the capacity of this FlavorsItems.

        缓存容量（G Byte）。

        :return: The capacity of this FlavorsItems.
        :rtype: list[str]
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this FlavorsItems.

        缓存容量（G Byte）。

        :param capacity: The capacity of this FlavorsItems.
        :type capacity: list[str]
        """
        self._capacity = capacity

    @property
    def billing_mode(self):
        """Gets the billing_mode of this FlavorsItems.

        计费模式，取值范围如下： - Hourly：按需计费 - Monthly: 包月计费 - Yearly: 包周期计费 

        :return: The billing_mode of this FlavorsItems.
        :rtype: list[str]
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        """Sets the billing_mode of this FlavorsItems.

        计费模式，取值范围如下： - Hourly：按需计费 - Monthly: 包月计费 - Yearly: 包周期计费 

        :param billing_mode: The billing_mode of this FlavorsItems.
        :type billing_mode: list[str]
        """
        self._billing_mode = billing_mode

    @property
    def tenant_ip_count(self):
        """Gets the tenant_ip_count of this FlavorsItems.

        租户侧IP数量。

        :return: The tenant_ip_count of this FlavorsItems.
        :rtype: int
        """
        return self._tenant_ip_count

    @tenant_ip_count.setter
    def tenant_ip_count(self, tenant_ip_count):
        """Sets the tenant_ip_count of this FlavorsItems.

        租户侧IP数量。

        :param tenant_ip_count: The tenant_ip_count of this FlavorsItems.
        :type tenant_ip_count: int
        """
        self._tenant_ip_count = tenant_ip_count

    @property
    def pricing_type(self):
        """Gets the pricing_type of this FlavorsItems.

        定价类型，取值如下： - tier: 阶梯定价，一个规格对应多个容量 - normal: 规格和容量一一对应 

        :return: The pricing_type of this FlavorsItems.
        :rtype: str
        """
        return self._pricing_type

    @pricing_type.setter
    def pricing_type(self, pricing_type):
        """Sets the pricing_type of this FlavorsItems.

        定价类型，取值如下： - tier: 阶梯定价，一个规格对应多个容量 - normal: 规格和容量一一对应 

        :param pricing_type: The pricing_type of this FlavorsItems.
        :type pricing_type: str
        """
        self._pricing_type = pricing_type

    @property
    def is_dec(self):
        """Gets the is_dec of this FlavorsItems.

        是否支持专属云。

        :return: The is_dec of this FlavorsItems.
        :rtype: bool
        """
        return self._is_dec

    @is_dec.setter
    def is_dec(self, is_dec):
        """Sets the is_dec of this FlavorsItems.

        是否支持专属云。

        :param is_dec: The is_dec of this FlavorsItems.
        :type is_dec: bool
        """
        self._is_dec = is_dec

    @property
    def attrs(self):
        """Gets the attrs of this FlavorsItems.

        规格的其他信息。

        :return: The attrs of this FlavorsItems.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.AttrsObject`]
        """
        return self._attrs

    @attrs.setter
    def attrs(self, attrs):
        """Sets the attrs of this FlavorsItems.

        规格的其他信息。

        :param attrs: The attrs of this FlavorsItems.
        :type attrs: list[:class:`huaweicloudsdkdcs.v2.AttrsObject`]
        """
        self._attrs = attrs

    @property
    def flavors_available_zones(self):
        """Gets the flavors_available_zones of this FlavorsItems.

        有资源的可用区。

        :return: The flavors_available_zones of this FlavorsItems.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.FlavorAzObject`]
        """
        return self._flavors_available_zones

    @flavors_available_zones.setter
    def flavors_available_zones(self, flavors_available_zones):
        """Sets the flavors_available_zones of this FlavorsItems.

        有资源的可用区。

        :param flavors_available_zones: The flavors_available_zones of this FlavorsItems.
        :type flavors_available_zones: list[:class:`huaweicloudsdkdcs.v2.FlavorAzObject`]
        """
        self._flavors_available_zones = flavors_available_zones

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
        if not isinstance(other, FlavorsItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
