# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPluginAttachedApisRequest:

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
        'offset': 'int',
        'limit': 'int',
        'plugin_id': 'str',
        'env_id': 'str',
        'api_name': 'str',
        'api_id': 'str',
        'group_id': 'str',
        'req_method': 'str',
        'req_uri': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'plugin_id': 'plugin_id',
        'env_id': 'env_id',
        'api_name': 'api_name',
        'api_id': 'api_id',
        'group_id': 'group_id',
        'req_method': 'req_method',
        'req_uri': 'req_uri'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, plugin_id=None, env_id=None, api_name=None, api_id=None, group_id=None, req_method=None, req_uri=None):
        """ListPluginAttachedApisRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，在API网关控制台的“实例信息”中获取。
        :type instance_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500
        :type limit: int
        :param plugin_id: 插件编号
        :type plugin_id: str
        :param env_id: 发布的环境编号
        :type env_id: str
        :param api_name: API名称
        :type api_name: str
        :param api_id: API编号
        :type api_id: str
        :param group_id: 分组编号
        :type group_id: str
        :param req_method: 请求方法
        :type req_method: str
        :param req_uri: 请求路径
        :type req_uri: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._plugin_id = None
        self._env_id = None
        self._api_name = None
        self._api_id = None
        self._group_id = None
        self._req_method = None
        self._req_uri = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.plugin_id = plugin_id
        if env_id is not None:
            self.env_id = env_id
        if api_name is not None:
            self.api_name = api_name
        if api_id is not None:
            self.api_id = api_id
        if group_id is not None:
            self.group_id = group_id
        if req_method is not None:
            self.req_method = req_method
        if req_uri is not None:
            self.req_uri = req_uri

    @property
    def instance_id(self):
        """Gets the instance_id of this ListPluginAttachedApisRequest.

        实例ID，在API网关控制台的“实例信息”中获取。

        :return: The instance_id of this ListPluginAttachedApisRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListPluginAttachedApisRequest.

        实例ID，在API网关控制台的“实例信息”中获取。

        :param instance_id: The instance_id of this ListPluginAttachedApisRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ListPluginAttachedApisRequest.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListPluginAttachedApisRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPluginAttachedApisRequest.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListPluginAttachedApisRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPluginAttachedApisRequest.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :return: The limit of this ListPluginAttachedApisRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPluginAttachedApisRequest.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :param limit: The limit of this ListPluginAttachedApisRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def plugin_id(self):
        """Gets the plugin_id of this ListPluginAttachedApisRequest.

        插件编号

        :return: The plugin_id of this ListPluginAttachedApisRequest.
        :rtype: str
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        """Sets the plugin_id of this ListPluginAttachedApisRequest.

        插件编号

        :param plugin_id: The plugin_id of this ListPluginAttachedApisRequest.
        :type plugin_id: str
        """
        self._plugin_id = plugin_id

    @property
    def env_id(self):
        """Gets the env_id of this ListPluginAttachedApisRequest.

        发布的环境编号

        :return: The env_id of this ListPluginAttachedApisRequest.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this ListPluginAttachedApisRequest.

        发布的环境编号

        :param env_id: The env_id of this ListPluginAttachedApisRequest.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def api_name(self):
        """Gets the api_name of this ListPluginAttachedApisRequest.

        API名称

        :return: The api_name of this ListPluginAttachedApisRequest.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this ListPluginAttachedApisRequest.

        API名称

        :param api_name: The api_name of this ListPluginAttachedApisRequest.
        :type api_name: str
        """
        self._api_name = api_name

    @property
    def api_id(self):
        """Gets the api_id of this ListPluginAttachedApisRequest.

        API编号

        :return: The api_id of this ListPluginAttachedApisRequest.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this ListPluginAttachedApisRequest.

        API编号

        :param api_id: The api_id of this ListPluginAttachedApisRequest.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def group_id(self):
        """Gets the group_id of this ListPluginAttachedApisRequest.

        分组编号

        :return: The group_id of this ListPluginAttachedApisRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListPluginAttachedApisRequest.

        分组编号

        :param group_id: The group_id of this ListPluginAttachedApisRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def req_method(self):
        """Gets the req_method of this ListPluginAttachedApisRequest.

        请求方法

        :return: The req_method of this ListPluginAttachedApisRequest.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        """Sets the req_method of this ListPluginAttachedApisRequest.

        请求方法

        :param req_method: The req_method of this ListPluginAttachedApisRequest.
        :type req_method: str
        """
        self._req_method = req_method

    @property
    def req_uri(self):
        """Gets the req_uri of this ListPluginAttachedApisRequest.

        请求路径

        :return: The req_uri of this ListPluginAttachedApisRequest.
        :rtype: str
        """
        return self._req_uri

    @req_uri.setter
    def req_uri(self, req_uri):
        """Sets the req_uri of this ListPluginAttachedApisRequest.

        请求路径

        :param req_uri: The req_uri of this ListPluginAttachedApisRequest.
        :type req_uri: str
        """
        self._req_uri = req_uri

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
        if not isinstance(other, ListPluginAttachedApisRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
