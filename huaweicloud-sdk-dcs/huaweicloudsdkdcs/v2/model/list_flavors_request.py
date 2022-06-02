# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlavorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'spec_code': 'str',
        'cache_mode': 'str',
        'engine': 'str',
        'engine_version': 'str',
        'cpu_type': 'str',
        'capacity': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'spec_code': 'spec_code',
        'cache_mode': 'cache_mode',
        'engine': 'engine',
        'engine_version': 'engine_version',
        'cpu_type': 'cpu_type',
        'capacity': 'capacity'
    }

    def __init__(self, instance_id=None, spec_code=None, cache_mode=None, engine=None, engine_version=None, cpu_type=None, capacity=None):
        """ListFlavorsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 缓存实例ID，根据该字段可查询出实例可变更的规格
        :type instance_id: str
        :param spec_code: 产品规格编码。
        :type spec_code: str
        :param cache_mode: 缓存实例类型。取值范围如下： - single：表示单机实例 - ha：表示主备实例 - cluster：表示cluster集群实例 - proxy：表示Proxy集群实例 - ha_rw_split： 表示读写分离实例 
        :type cache_mode: str
        :param engine: 缓存引擎类型。取值范围如下： - Redis - Memcached 
        :type engine: str
        :param engine_version: 缓存版本，当缓存引擎为Redis时，取值范围如下： - 3.0 - 4.0 - 5.0 
        :type engine_version: str
        :param cpu_type: CPU架构类型。取值范围如下： - x86_64：X86架构 - aarch64：ARM架构 
        :type cpu_type: str
        :param capacity: 缓存容量（G Byte）。 - Redis3.0：单机和主备类型实例取值：2、4、8、16、32、64。Proxy集群实例规格支持64、128、256、512和1024。 - Redis4.0和Redis5.0：单机和主备类型实例取值：0.125、0.25、0.5、1、2、4、8、16、32、64。Cluster集群实例规格支持24、32、48、64、96、128、192、256、384、512、768、1024。 - Memcached：单机和主备类型实例取值：2、4、8、16、32、64。 
        :type capacity: str
        """
        
        

        self._instance_id = None
        self._spec_code = None
        self._cache_mode = None
        self._engine = None
        self._engine_version = None
        self._cpu_type = None
        self._capacity = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if spec_code is not None:
            self.spec_code = spec_code
        if cache_mode is not None:
            self.cache_mode = cache_mode
        if engine is not None:
            self.engine = engine
        if engine_version is not None:
            self.engine_version = engine_version
        if cpu_type is not None:
            self.cpu_type = cpu_type
        if capacity is not None:
            self.capacity = capacity

    @property
    def instance_id(self):
        """Gets the instance_id of this ListFlavorsRequest.

        缓存实例ID，根据该字段可查询出实例可变更的规格

        :return: The instance_id of this ListFlavorsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListFlavorsRequest.

        缓存实例ID，根据该字段可查询出实例可变更的规格

        :param instance_id: The instance_id of this ListFlavorsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def spec_code(self):
        """Gets the spec_code of this ListFlavorsRequest.

        产品规格编码。

        :return: The spec_code of this ListFlavorsRequest.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this ListFlavorsRequest.

        产品规格编码。

        :param spec_code: The spec_code of this ListFlavorsRequest.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def cache_mode(self):
        """Gets the cache_mode of this ListFlavorsRequest.

        缓存实例类型。取值范围如下： - single：表示单机实例 - ha：表示主备实例 - cluster：表示cluster集群实例 - proxy：表示Proxy集群实例 - ha_rw_split： 表示读写分离实例 

        :return: The cache_mode of this ListFlavorsRequest.
        :rtype: str
        """
        return self._cache_mode

    @cache_mode.setter
    def cache_mode(self, cache_mode):
        """Sets the cache_mode of this ListFlavorsRequest.

        缓存实例类型。取值范围如下： - single：表示单机实例 - ha：表示主备实例 - cluster：表示cluster集群实例 - proxy：表示Proxy集群实例 - ha_rw_split： 表示读写分离实例 

        :param cache_mode: The cache_mode of this ListFlavorsRequest.
        :type cache_mode: str
        """
        self._cache_mode = cache_mode

    @property
    def engine(self):
        """Gets the engine of this ListFlavorsRequest.

        缓存引擎类型。取值范围如下： - Redis - Memcached 

        :return: The engine of this ListFlavorsRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this ListFlavorsRequest.

        缓存引擎类型。取值范围如下： - Redis - Memcached 

        :param engine: The engine of this ListFlavorsRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def engine_version(self):
        """Gets the engine_version of this ListFlavorsRequest.

        缓存版本，当缓存引擎为Redis时，取值范围如下： - 3.0 - 4.0 - 5.0 

        :return: The engine_version of this ListFlavorsRequest.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this ListFlavorsRequest.

        缓存版本，当缓存引擎为Redis时，取值范围如下： - 3.0 - 4.0 - 5.0 

        :param engine_version: The engine_version of this ListFlavorsRequest.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def cpu_type(self):
        """Gets the cpu_type of this ListFlavorsRequest.

        CPU架构类型。取值范围如下： - x86_64：X86架构 - aarch64：ARM架构 

        :return: The cpu_type of this ListFlavorsRequest.
        :rtype: str
        """
        return self._cpu_type

    @cpu_type.setter
    def cpu_type(self, cpu_type):
        """Sets the cpu_type of this ListFlavorsRequest.

        CPU架构类型。取值范围如下： - x86_64：X86架构 - aarch64：ARM架构 

        :param cpu_type: The cpu_type of this ListFlavorsRequest.
        :type cpu_type: str
        """
        self._cpu_type = cpu_type

    @property
    def capacity(self):
        """Gets the capacity of this ListFlavorsRequest.

        缓存容量（G Byte）。 - Redis3.0：单机和主备类型实例取值：2、4、8、16、32、64。Proxy集群实例规格支持64、128、256、512和1024。 - Redis4.0和Redis5.0：单机和主备类型实例取值：0.125、0.25、0.5、1、2、4、8、16、32、64。Cluster集群实例规格支持24、32、48、64、96、128、192、256、384、512、768、1024。 - Memcached：单机和主备类型实例取值：2、4、8、16、32、64。 

        :return: The capacity of this ListFlavorsRequest.
        :rtype: str
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this ListFlavorsRequest.

        缓存容量（G Byte）。 - Redis3.0：单机和主备类型实例取值：2、4、8、16、32、64。Proxy集群实例规格支持64、128、256、512和1024。 - Redis4.0和Redis5.0：单机和主备类型实例取值：0.125、0.25、0.5、1、2、4、8、16、32、64。Cluster集群实例规格支持24、32、48、64、96、128、192、256、384、512、768、1024。 - Memcached：单机和主备类型实例取值：2、4、8、16、32、64。 

        :param capacity: The capacity of this ListFlavorsRequest.
        :type capacity: str
        """
        self._capacity = capacity

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
        if not isinstance(other, ListFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
