# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportInstancesTaskBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'included_instances': 'list[str]',
        'region': 'str',
        'name': 'str',
        'capacity': 'str',
        'instance_id': 'str',
        'ip': 'str',
        'available_zone': 'str',
        'status': 'str',
        'product_type': 'str',
        'cache_mode': 'str',
        'engine': 'str',
        'engine_version': 'str',
        'cpu_type': 'str',
        'enterprise_project_id': 'str',
        'charging_mode': 'str',
        'tags': 'str'
    }

    attribute_map = {
        'included_instances': 'included_instances',
        'region': 'region',
        'name': 'name',
        'capacity': 'capacity',
        'instance_id': 'instance_id',
        'ip': 'ip',
        'available_zone': 'available_zone',
        'status': 'status',
        'product_type': 'product_type',
        'cache_mode': 'cache_mode',
        'engine': 'engine',
        'engine_version': 'engine_version',
        'cpu_type': 'cpu_type',
        'enterprise_project_id': 'enterprise_project_id',
        'charging_mode': 'charging_mode',
        'tags': 'tags'
    }

    def __init__(self, included_instances=None, region=None, name=None, capacity=None, instance_id=None, ip=None, available_zone=None, status=None, product_type=None, cache_mode=None, engine=None, engine_version=None, cpu_type=None, enterprise_project_id=None, charging_mode=None, tags=None):
        """ExportInstancesTaskBody

        The model defined in huaweicloud sdk

        :param included_instances: 导出实例列表，如果为空，则会导出满足其余参数条件的所有实例
        :type included_instances: list[str]
        :param region: 局点名称，用于导出的文件名命名
        :type region: str
        :param name: 按照实例名称筛选实例
        :type name: str
        :param capacity: 按照实例规格筛选实例
        :type capacity: str
        :param instance_id: 按照实例ID筛选实例
        :type instance_id: str
        :param ip: 按照ip筛选实例
        :type ip: str
        :param available_zone: 按照可用区筛选实例
        :type available_zone: str
        :param status: 按照实例状态筛选实例
        :type status: str
        :param product_type: 按照产品类型筛选实例，generic-普通版本，enterprise-企业版
        :type product_type: str
        :param cache_mode: 按照实例类型筛选实例
        :type cache_mode: str
        :param engine: 按照缓存引擎筛选实例
        :type engine: str
        :param engine_version: 按照缓存引擎版本筛选实例
        :type engine_version: str
        :param cpu_type: 按照CPU类型筛选实例
        :type cpu_type: str
        :param enterprise_project_id: 按照企业项目ID筛选实例
        :type enterprise_project_id: str
        :param charging_mode: 按照计费方式筛选实例
        :type charging_mode: str
        :param tags: 按照标签筛选实例
        :type tags: str
        """
        
        

        self._included_instances = None
        self._region = None
        self._name = None
        self._capacity = None
        self._instance_id = None
        self._ip = None
        self._available_zone = None
        self._status = None
        self._product_type = None
        self._cache_mode = None
        self._engine = None
        self._engine_version = None
        self._cpu_type = None
        self._enterprise_project_id = None
        self._charging_mode = None
        self._tags = None
        self.discriminator = None

        if included_instances is not None:
            self.included_instances = included_instances
        self.region = region
        if name is not None:
            self.name = name
        if capacity is not None:
            self.capacity = capacity
        if instance_id is not None:
            self.instance_id = instance_id
        if ip is not None:
            self.ip = ip
        if available_zone is not None:
            self.available_zone = available_zone
        if status is not None:
            self.status = status
        if product_type is not None:
            self.product_type = product_type
        if cache_mode is not None:
            self.cache_mode = cache_mode
        if engine is not None:
            self.engine = engine
        if engine_version is not None:
            self.engine_version = engine_version
        if cpu_type is not None:
            self.cpu_type = cpu_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if tags is not None:
            self.tags = tags

    @property
    def included_instances(self):
        """Gets the included_instances of this ExportInstancesTaskBody.

        导出实例列表，如果为空，则会导出满足其余参数条件的所有实例

        :return: The included_instances of this ExportInstancesTaskBody.
        :rtype: list[str]
        """
        return self._included_instances

    @included_instances.setter
    def included_instances(self, included_instances):
        """Sets the included_instances of this ExportInstancesTaskBody.

        导出实例列表，如果为空，则会导出满足其余参数条件的所有实例

        :param included_instances: The included_instances of this ExportInstancesTaskBody.
        :type included_instances: list[str]
        """
        self._included_instances = included_instances

    @property
    def region(self):
        """Gets the region of this ExportInstancesTaskBody.

        局点名称，用于导出的文件名命名

        :return: The region of this ExportInstancesTaskBody.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ExportInstancesTaskBody.

        局点名称，用于导出的文件名命名

        :param region: The region of this ExportInstancesTaskBody.
        :type region: str
        """
        self._region = region

    @property
    def name(self):
        """Gets the name of this ExportInstancesTaskBody.

        按照实例名称筛选实例

        :return: The name of this ExportInstancesTaskBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExportInstancesTaskBody.

        按照实例名称筛选实例

        :param name: The name of this ExportInstancesTaskBody.
        :type name: str
        """
        self._name = name

    @property
    def capacity(self):
        """Gets the capacity of this ExportInstancesTaskBody.

        按照实例规格筛选实例

        :return: The capacity of this ExportInstancesTaskBody.
        :rtype: str
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this ExportInstancesTaskBody.

        按照实例规格筛选实例

        :param capacity: The capacity of this ExportInstancesTaskBody.
        :type capacity: str
        """
        self._capacity = capacity

    @property
    def instance_id(self):
        """Gets the instance_id of this ExportInstancesTaskBody.

        按照实例ID筛选实例

        :return: The instance_id of this ExportInstancesTaskBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ExportInstancesTaskBody.

        按照实例ID筛选实例

        :param instance_id: The instance_id of this ExportInstancesTaskBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def ip(self):
        """Gets the ip of this ExportInstancesTaskBody.

        按照ip筛选实例

        :return: The ip of this ExportInstancesTaskBody.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ExportInstancesTaskBody.

        按照ip筛选实例

        :param ip: The ip of this ExportInstancesTaskBody.
        :type ip: str
        """
        self._ip = ip

    @property
    def available_zone(self):
        """Gets the available_zone of this ExportInstancesTaskBody.

        按照可用区筛选实例

        :return: The available_zone of this ExportInstancesTaskBody.
        :rtype: str
        """
        return self._available_zone

    @available_zone.setter
    def available_zone(self, available_zone):
        """Sets the available_zone of this ExportInstancesTaskBody.

        按照可用区筛选实例

        :param available_zone: The available_zone of this ExportInstancesTaskBody.
        :type available_zone: str
        """
        self._available_zone = available_zone

    @property
    def status(self):
        """Gets the status of this ExportInstancesTaskBody.

        按照实例状态筛选实例

        :return: The status of this ExportInstancesTaskBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExportInstancesTaskBody.

        按照实例状态筛选实例

        :param status: The status of this ExportInstancesTaskBody.
        :type status: str
        """
        self._status = status

    @property
    def product_type(self):
        """Gets the product_type of this ExportInstancesTaskBody.

        按照产品类型筛选实例，generic-普通版本，enterprise-企业版

        :return: The product_type of this ExportInstancesTaskBody.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this ExportInstancesTaskBody.

        按照产品类型筛选实例，generic-普通版本，enterprise-企业版

        :param product_type: The product_type of this ExportInstancesTaskBody.
        :type product_type: str
        """
        self._product_type = product_type

    @property
    def cache_mode(self):
        """Gets the cache_mode of this ExportInstancesTaskBody.

        按照实例类型筛选实例

        :return: The cache_mode of this ExportInstancesTaskBody.
        :rtype: str
        """
        return self._cache_mode

    @cache_mode.setter
    def cache_mode(self, cache_mode):
        """Sets the cache_mode of this ExportInstancesTaskBody.

        按照实例类型筛选实例

        :param cache_mode: The cache_mode of this ExportInstancesTaskBody.
        :type cache_mode: str
        """
        self._cache_mode = cache_mode

    @property
    def engine(self):
        """Gets the engine of this ExportInstancesTaskBody.

        按照缓存引擎筛选实例

        :return: The engine of this ExportInstancesTaskBody.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this ExportInstancesTaskBody.

        按照缓存引擎筛选实例

        :param engine: The engine of this ExportInstancesTaskBody.
        :type engine: str
        """
        self._engine = engine

    @property
    def engine_version(self):
        """Gets the engine_version of this ExportInstancesTaskBody.

        按照缓存引擎版本筛选实例

        :return: The engine_version of this ExportInstancesTaskBody.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this ExportInstancesTaskBody.

        按照缓存引擎版本筛选实例

        :param engine_version: The engine_version of this ExportInstancesTaskBody.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def cpu_type(self):
        """Gets the cpu_type of this ExportInstancesTaskBody.

        按照CPU类型筛选实例

        :return: The cpu_type of this ExportInstancesTaskBody.
        :rtype: str
        """
        return self._cpu_type

    @cpu_type.setter
    def cpu_type(self, cpu_type):
        """Sets the cpu_type of this ExportInstancesTaskBody.

        按照CPU类型筛选实例

        :param cpu_type: The cpu_type of this ExportInstancesTaskBody.
        :type cpu_type: str
        """
        self._cpu_type = cpu_type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ExportInstancesTaskBody.

        按照企业项目ID筛选实例

        :return: The enterprise_project_id of this ExportInstancesTaskBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ExportInstancesTaskBody.

        按照企业项目ID筛选实例

        :param enterprise_project_id: The enterprise_project_id of this ExportInstancesTaskBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def charging_mode(self):
        """Gets the charging_mode of this ExportInstancesTaskBody.

        按照计费方式筛选实例

        :return: The charging_mode of this ExportInstancesTaskBody.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this ExportInstancesTaskBody.

        按照计费方式筛选实例

        :param charging_mode: The charging_mode of this ExportInstancesTaskBody.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def tags(self):
        """Gets the tags of this ExportInstancesTaskBody.

        按照标签筛选实例

        :return: The tags of this ExportInstancesTaskBody.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ExportInstancesTaskBody.

        按照标签筛选实例

        :param tags: The tags of this ExportInstancesTaskBody.
        :type tags: str
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
        if not isinstance(other, ExportInstancesTaskBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
