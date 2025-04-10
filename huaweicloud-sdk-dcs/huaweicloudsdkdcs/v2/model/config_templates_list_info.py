# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigTemplatesListInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'cache_mode': 'str',
        'description': 'str',
        'engine': 'str',
        'engine_version': 'str',
        'name': 'str',
        'product_type': 'str',
        'storage_type': 'str',
        'type': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'cache_mode': 'cache_mode',
        'description': 'description',
        'engine': 'engine',
        'engine_version': 'engine_version',
        'name': 'name',
        'product_type': 'product_type',
        'storage_type': 'storage_type',
        'type': 'type',
        'created_at': 'created_at'
    }

    def __init__(self, template_id=None, cache_mode=None, description=None, engine=None, engine_version=None, name=None, product_type=None, storage_type=None, type=None, created_at=None):
        r"""ConfigTemplatesListInfo

        The model defined in huaweicloud sdk

        :param template_id: 模板ID
        :type template_id: str
        :param cache_mode: 缓存实例类型。取值范围如下： - single：表示单机实例 - ha：表示主备实例 - cluster：表示cluster集群实例 - proxy：表示Proxy集群实例 [- ha_rw_split： 表示读写分离实例](tag:hws) 
        :type cache_mode: str
        :param description: 模板的描述信息
        :type description: str
        :param engine: 缓存引擎：Redis[和Memcached](tag:hws,hws_hk,ocb,sbc,tm,ctc,cmcc)。
        :type engine: str
        :param engine_version: 缓存版本。  当缓存引擎为Redis时，取值为4.0或5.0。  [当缓存引擎为Memcached时，该字段为可选，取值为空。](tag:hws,hws_hk,ocb,sbc,tm,ctc,cmcc) 
        :type engine_version: str
        :param name: 模板名称
        :type name: str
        :param product_type: 产品类型。 取值范围如下： - generic：普通版 - enterprise：企业版 
        :type product_type: str
        :param storage_type: 存储类型。 取值范围如下： - DRAM - SSD 
        :type storage_type: str
        :param type: 模板类型
        :type type: str
        :param created_at: 模板创建时间，仅在自定义参数模板中有意义，格式例如：2023-05-10T11:09:35.802Z
        :type created_at: str
        """
        
        

        self._template_id = None
        self._cache_mode = None
        self._description = None
        self._engine = None
        self._engine_version = None
        self._name = None
        self._product_type = None
        self._storage_type = None
        self._type = None
        self._created_at = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if cache_mode is not None:
            self.cache_mode = cache_mode
        if description is not None:
            self.description = description
        if engine is not None:
            self.engine = engine
        if engine_version is not None:
            self.engine_version = engine_version
        if name is not None:
            self.name = name
        if product_type is not None:
            self.product_type = product_type
        if storage_type is not None:
            self.storage_type = storage_type
        if type is not None:
            self.type = type
        if created_at is not None:
            self.created_at = created_at

    @property
    def template_id(self):
        r"""Gets the template_id of this ConfigTemplatesListInfo.

        模板ID

        :return: The template_id of this ConfigTemplatesListInfo.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ConfigTemplatesListInfo.

        模板ID

        :param template_id: The template_id of this ConfigTemplatesListInfo.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def cache_mode(self):
        r"""Gets the cache_mode of this ConfigTemplatesListInfo.

        缓存实例类型。取值范围如下： - single：表示单机实例 - ha：表示主备实例 - cluster：表示cluster集群实例 - proxy：表示Proxy集群实例 [- ha_rw_split： 表示读写分离实例](tag:hws) 

        :return: The cache_mode of this ConfigTemplatesListInfo.
        :rtype: str
        """
        return self._cache_mode

    @cache_mode.setter
    def cache_mode(self, cache_mode):
        r"""Sets the cache_mode of this ConfigTemplatesListInfo.

        缓存实例类型。取值范围如下： - single：表示单机实例 - ha：表示主备实例 - cluster：表示cluster集群实例 - proxy：表示Proxy集群实例 [- ha_rw_split： 表示读写分离实例](tag:hws) 

        :param cache_mode: The cache_mode of this ConfigTemplatesListInfo.
        :type cache_mode: str
        """
        self._cache_mode = cache_mode

    @property
    def description(self):
        r"""Gets the description of this ConfigTemplatesListInfo.

        模板的描述信息

        :return: The description of this ConfigTemplatesListInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ConfigTemplatesListInfo.

        模板的描述信息

        :param description: The description of this ConfigTemplatesListInfo.
        :type description: str
        """
        self._description = description

    @property
    def engine(self):
        r"""Gets the engine of this ConfigTemplatesListInfo.

        缓存引擎：Redis[和Memcached](tag:hws,hws_hk,ocb,sbc,tm,ctc,cmcc)。

        :return: The engine of this ConfigTemplatesListInfo.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ConfigTemplatesListInfo.

        缓存引擎：Redis[和Memcached](tag:hws,hws_hk,ocb,sbc,tm,ctc,cmcc)。

        :param engine: The engine of this ConfigTemplatesListInfo.
        :type engine: str
        """
        self._engine = engine

    @property
    def engine_version(self):
        r"""Gets the engine_version of this ConfigTemplatesListInfo.

        缓存版本。  当缓存引擎为Redis时，取值为4.0或5.0。  [当缓存引擎为Memcached时，该字段为可选，取值为空。](tag:hws,hws_hk,ocb,sbc,tm,ctc,cmcc) 

        :return: The engine_version of this ConfigTemplatesListInfo.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this ConfigTemplatesListInfo.

        缓存版本。  当缓存引擎为Redis时，取值为4.0或5.0。  [当缓存引擎为Memcached时，该字段为可选，取值为空。](tag:hws,hws_hk,ocb,sbc,tm,ctc,cmcc) 

        :param engine_version: The engine_version of this ConfigTemplatesListInfo.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def name(self):
        r"""Gets the name of this ConfigTemplatesListInfo.

        模板名称

        :return: The name of this ConfigTemplatesListInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ConfigTemplatesListInfo.

        模板名称

        :param name: The name of this ConfigTemplatesListInfo.
        :type name: str
        """
        self._name = name

    @property
    def product_type(self):
        r"""Gets the product_type of this ConfigTemplatesListInfo.

        产品类型。 取值范围如下： - generic：普通版 - enterprise：企业版 

        :return: The product_type of this ConfigTemplatesListInfo.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        r"""Sets the product_type of this ConfigTemplatesListInfo.

        产品类型。 取值范围如下： - generic：普通版 - enterprise：企业版 

        :param product_type: The product_type of this ConfigTemplatesListInfo.
        :type product_type: str
        """
        self._product_type = product_type

    @property
    def storage_type(self):
        r"""Gets the storage_type of this ConfigTemplatesListInfo.

        存储类型。 取值范围如下： - DRAM - SSD 

        :return: The storage_type of this ConfigTemplatesListInfo.
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        r"""Sets the storage_type of this ConfigTemplatesListInfo.

        存储类型。 取值范围如下： - DRAM - SSD 

        :param storage_type: The storage_type of this ConfigTemplatesListInfo.
        :type storage_type: str
        """
        self._storage_type = storage_type

    @property
    def type(self):
        r"""Gets the type of this ConfigTemplatesListInfo.

        模板类型

        :return: The type of this ConfigTemplatesListInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ConfigTemplatesListInfo.

        模板类型

        :param type: The type of this ConfigTemplatesListInfo.
        :type type: str
        """
        self._type = type

    @property
    def created_at(self):
        r"""Gets the created_at of this ConfigTemplatesListInfo.

        模板创建时间，仅在自定义参数模板中有意义，格式例如：2023-05-10T11:09:35.802Z

        :return: The created_at of this ConfigTemplatesListInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ConfigTemplatesListInfo.

        模板创建时间，仅在自定义参数模板中有意义，格式例如：2023-05-10T11:09:35.802Z

        :param created_at: The created_at of this ConfigTemplatesListInfo.
        :type created_at: str
        """
        self._created_at = created_at

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
        if not isinstance(other, ConfigTemplatesListInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
