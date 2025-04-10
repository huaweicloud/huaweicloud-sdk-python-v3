# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConfigTemplatesRequest:

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
        'template_id': 'str',
        'type': 'str',
        'engine': 'str',
        'engine_version': 'str',
        'cache_mode': 'str',
        'description': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'name': 'name',
        'template_id': 'template_id',
        'type': 'type',
        'engine': 'engine',
        'engine_version': 'engine_version',
        'cache_mode': 'cache_mode',
        'description': 'description',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, name=None, template_id=None, type=None, engine=None, engine_version=None, cache_mode=None, description=None, offset=None, limit=None):
        r"""ListConfigTemplatesRequest

        The model defined in huaweicloud sdk

        :param name: 参数模板名称，支持模糊查找
        :type name: str
        :param template_id: 模板ID
        :type template_id: str
        :param type: 模板类型
        :type type: str
        :param engine: 缓存引擎：Redis[和Memcached](tag:hws,hws_hk,ocb,sbc,tm,ctc,cmcc)。
        :type engine: str
        :param engine_version: 缓存版本。  当缓存引擎为Redis时，取值为[3.0/4.0/5.0](tag:ctc,cmc)[3.0/4.0/5.0/6.0](tag:ocb,otc,sbc,g42,tm)[4.0/5.0/6.0](tag:hws,hws_hk)。  [当缓存引擎为Memcached时，该字段为可选，取值为空。](tag:hws,hws_hk,ocb,sbc,tm,ctc,cmcc) 
        :type engine_version: str
        :param cache_mode: 缓存实例类型。取值范围如下： - single：表示单机实例 - ha：表示主备实例 - cluster：表示cluster集群实例 - proxy：表示Proxy集群实例 [- ha_rw_split：表示读写分离实例](tag:hws) 
        :type cache_mode: str
        :param description: 模板的描述信息
        :type description: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0
        :type offset: int
        :param limit: 每页显示条数，最小值为1，最大值为1000，若不设置该参数，则为10。
        :type limit: int
        """
        
        

        self._name = None
        self._template_id = None
        self._type = None
        self._engine = None
        self._engine_version = None
        self._cache_mode = None
        self._description = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if template_id is not None:
            self.template_id = template_id
        self.type = type
        if engine is not None:
            self.engine = engine
        if engine_version is not None:
            self.engine_version = engine_version
        if cache_mode is not None:
            self.cache_mode = cache_mode
        if description is not None:
            self.description = description
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListConfigTemplatesRequest.

        参数模板名称，支持模糊查找

        :return: The name of this ListConfigTemplatesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListConfigTemplatesRequest.

        参数模板名称，支持模糊查找

        :param name: The name of this ListConfigTemplatesRequest.
        :type name: str
        """
        self._name = name

    @property
    def template_id(self):
        r"""Gets the template_id of this ListConfigTemplatesRequest.

        模板ID

        :return: The template_id of this ListConfigTemplatesRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ListConfigTemplatesRequest.

        模板ID

        :param template_id: The template_id of this ListConfigTemplatesRequest.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def type(self):
        r"""Gets the type of this ListConfigTemplatesRequest.

        模板类型

        :return: The type of this ListConfigTemplatesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListConfigTemplatesRequest.

        模板类型

        :param type: The type of this ListConfigTemplatesRequest.
        :type type: str
        """
        self._type = type

    @property
    def engine(self):
        r"""Gets the engine of this ListConfigTemplatesRequest.

        缓存引擎：Redis[和Memcached](tag:hws,hws_hk,ocb,sbc,tm,ctc,cmcc)。

        :return: The engine of this ListConfigTemplatesRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ListConfigTemplatesRequest.

        缓存引擎：Redis[和Memcached](tag:hws,hws_hk,ocb,sbc,tm,ctc,cmcc)。

        :param engine: The engine of this ListConfigTemplatesRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def engine_version(self):
        r"""Gets the engine_version of this ListConfigTemplatesRequest.

        缓存版本。  当缓存引擎为Redis时，取值为[3.0/4.0/5.0](tag:ctc,cmc)[3.0/4.0/5.0/6.0](tag:ocb,otc,sbc,g42,tm)[4.0/5.0/6.0](tag:hws,hws_hk)。  [当缓存引擎为Memcached时，该字段为可选，取值为空。](tag:hws,hws_hk,ocb,sbc,tm,ctc,cmcc) 

        :return: The engine_version of this ListConfigTemplatesRequest.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this ListConfigTemplatesRequest.

        缓存版本。  当缓存引擎为Redis时，取值为[3.0/4.0/5.0](tag:ctc,cmc)[3.0/4.0/5.0/6.0](tag:ocb,otc,sbc,g42,tm)[4.0/5.0/6.0](tag:hws,hws_hk)。  [当缓存引擎为Memcached时，该字段为可选，取值为空。](tag:hws,hws_hk,ocb,sbc,tm,ctc,cmcc) 

        :param engine_version: The engine_version of this ListConfigTemplatesRequest.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def cache_mode(self):
        r"""Gets the cache_mode of this ListConfigTemplatesRequest.

        缓存实例类型。取值范围如下： - single：表示单机实例 - ha：表示主备实例 - cluster：表示cluster集群实例 - proxy：表示Proxy集群实例 [- ha_rw_split：表示读写分离实例](tag:hws) 

        :return: The cache_mode of this ListConfigTemplatesRequest.
        :rtype: str
        """
        return self._cache_mode

    @cache_mode.setter
    def cache_mode(self, cache_mode):
        r"""Sets the cache_mode of this ListConfigTemplatesRequest.

        缓存实例类型。取值范围如下： - single：表示单机实例 - ha：表示主备实例 - cluster：表示cluster集群实例 - proxy：表示Proxy集群实例 [- ha_rw_split：表示读写分离实例](tag:hws) 

        :param cache_mode: The cache_mode of this ListConfigTemplatesRequest.
        :type cache_mode: str
        """
        self._cache_mode = cache_mode

    @property
    def description(self):
        r"""Gets the description of this ListConfigTemplatesRequest.

        模板的描述信息

        :return: The description of this ListConfigTemplatesRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListConfigTemplatesRequest.

        模板的描述信息

        :param description: The description of this ListConfigTemplatesRequest.
        :type description: str
        """
        self._description = description

    @property
    def offset(self):
        r"""Gets the offset of this ListConfigTemplatesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :return: The offset of this ListConfigTemplatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListConfigTemplatesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :param offset: The offset of this ListConfigTemplatesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListConfigTemplatesRequest.

        每页显示条数，最小值为1，最大值为1000，若不设置该参数，则为10。

        :return: The limit of this ListConfigTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListConfigTemplatesRequest.

        每页显示条数，最小值为1，最大值为1000，若不设置该参数，则为10。

        :param limit: The limit of this ListConfigTemplatesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListConfigTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
