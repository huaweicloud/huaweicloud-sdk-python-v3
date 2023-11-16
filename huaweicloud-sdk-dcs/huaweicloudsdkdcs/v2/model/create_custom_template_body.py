# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCustomTemplateBody:

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
        'name': 'str',
        'type': 'str',
        'engine': 'str',
        'cache_mode': 'str',
        'description': 'str',
        'engine_version': 'str',
        'params': 'dict(str, str)'
    }

    attribute_map = {
        'template_id': 'template_id',
        'name': 'name',
        'type': 'type',
        'engine': 'engine',
        'cache_mode': 'cache_mode',
        'description': 'description',
        'engine_version': 'engine_version',
        'params': 'params'
    }

    def __init__(self, template_id=None, name=None, type=None, engine=None, cache_mode=None, description=None, engine_version=None, params=None):
        """CreateCustomTemplateBody

        The model defined in huaweicloud sdk

        :param template_id: 来源系统模板ID
        :type template_id: str
        :param name: 模板名称
        :type name: str
        :param type: 模板类型
        :type type: str
        :param engine: 缓存引擎：Redis[和Memcached](tag:hws,hws_hk,ocb,sbc,tm,ctc,cmcc)。
        :type engine: str
        :param cache_mode: 缓存实例类型。取值范围如下： - single：表示单机实例 - ha：表示主备实例 - cluster：表示cluster集群实例 - proxy：表示Proxy集群实例 [- ha_rw_split： 表示读写分离实例](tag:hws) 
        :type cache_mode: str
        :param description: 模板的描述信息
        :type description: str
        :param engine_version: 缓存版本。  当缓存引擎为Redis时，取值为4.0或5.0。  [当缓存引擎为Memcached时，该字段为可选，取值为空。](tag:hws,hws_hk,ocb,sbc,tm,ctc,cmcc) 
        :type engine_version: str
        :param params: 参数配置信息
        :type params: dict(str, str)
        """
        
        

        self._template_id = None
        self._name = None
        self._type = None
        self._engine = None
        self._cache_mode = None
        self._description = None
        self._engine_version = None
        self._params = None
        self.discriminator = None

        self.template_id = template_id
        self.name = name
        self.type = type
        if engine is not None:
            self.engine = engine
        if cache_mode is not None:
            self.cache_mode = cache_mode
        if description is not None:
            self.description = description
        if engine_version is not None:
            self.engine_version = engine_version
        self.params = params

    @property
    def template_id(self):
        """Gets the template_id of this CreateCustomTemplateBody.

        来源系统模板ID

        :return: The template_id of this CreateCustomTemplateBody.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this CreateCustomTemplateBody.

        来源系统模板ID

        :param template_id: The template_id of this CreateCustomTemplateBody.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def name(self):
        """Gets the name of this CreateCustomTemplateBody.

        模板名称

        :return: The name of this CreateCustomTemplateBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateCustomTemplateBody.

        模板名称

        :param name: The name of this CreateCustomTemplateBody.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this CreateCustomTemplateBody.

        模板类型

        :return: The type of this CreateCustomTemplateBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateCustomTemplateBody.

        模板类型

        :param type: The type of this CreateCustomTemplateBody.
        :type type: str
        """
        self._type = type

    @property
    def engine(self):
        """Gets the engine of this CreateCustomTemplateBody.

        缓存引擎：Redis[和Memcached](tag:hws,hws_hk,ocb,sbc,tm,ctc,cmcc)。

        :return: The engine of this CreateCustomTemplateBody.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this CreateCustomTemplateBody.

        缓存引擎：Redis[和Memcached](tag:hws,hws_hk,ocb,sbc,tm,ctc,cmcc)。

        :param engine: The engine of this CreateCustomTemplateBody.
        :type engine: str
        """
        self._engine = engine

    @property
    def cache_mode(self):
        """Gets the cache_mode of this CreateCustomTemplateBody.

        缓存实例类型。取值范围如下： - single：表示单机实例 - ha：表示主备实例 - cluster：表示cluster集群实例 - proxy：表示Proxy集群实例 [- ha_rw_split： 表示读写分离实例](tag:hws) 

        :return: The cache_mode of this CreateCustomTemplateBody.
        :rtype: str
        """
        return self._cache_mode

    @cache_mode.setter
    def cache_mode(self, cache_mode):
        """Sets the cache_mode of this CreateCustomTemplateBody.

        缓存实例类型。取值范围如下： - single：表示单机实例 - ha：表示主备实例 - cluster：表示cluster集群实例 - proxy：表示Proxy集群实例 [- ha_rw_split： 表示读写分离实例](tag:hws) 

        :param cache_mode: The cache_mode of this CreateCustomTemplateBody.
        :type cache_mode: str
        """
        self._cache_mode = cache_mode

    @property
    def description(self):
        """Gets the description of this CreateCustomTemplateBody.

        模板的描述信息

        :return: The description of this CreateCustomTemplateBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateCustomTemplateBody.

        模板的描述信息

        :param description: The description of this CreateCustomTemplateBody.
        :type description: str
        """
        self._description = description

    @property
    def engine_version(self):
        """Gets the engine_version of this CreateCustomTemplateBody.

        缓存版本。  当缓存引擎为Redis时，取值为4.0或5.0。  [当缓存引擎为Memcached时，该字段为可选，取值为空。](tag:hws,hws_hk,ocb,sbc,tm,ctc,cmcc) 

        :return: The engine_version of this CreateCustomTemplateBody.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this CreateCustomTemplateBody.

        缓存版本。  当缓存引擎为Redis时，取值为4.0或5.0。  [当缓存引擎为Memcached时，该字段为可选，取值为空。](tag:hws,hws_hk,ocb,sbc,tm,ctc,cmcc) 

        :param engine_version: The engine_version of this CreateCustomTemplateBody.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def params(self):
        """Gets the params of this CreateCustomTemplateBody.

        参数配置信息

        :return: The params of this CreateCustomTemplateBody.
        :rtype: dict(str, str)
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this CreateCustomTemplateBody.

        参数配置信息

        :param params: The params of this CreateCustomTemplateBody.
        :type params: dict(str, str)
        """
        self._params = params

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
        if not isinstance(other, CreateCustomTemplateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
