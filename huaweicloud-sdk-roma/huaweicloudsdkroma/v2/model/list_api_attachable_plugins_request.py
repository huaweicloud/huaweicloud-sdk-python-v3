# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApiAttachablePluginsRequest:

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
        'api_id': 'str',
        'env_id': 'str',
        'plugin_name': 'str',
        'plugin_type': 'str',
        'plugin_id': 'str',
        'roma_app_id': 'str',
        'roma_app_name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'api_id': 'api_id',
        'env_id': 'env_id',
        'plugin_name': 'plugin_name',
        'plugin_type': 'plugin_type',
        'plugin_id': 'plugin_id',
        'roma_app_id': 'roma_app_id',
        'roma_app_name': 'roma_app_name'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, api_id=None, env_id=None, plugin_name=None, plugin_type=None, plugin_id=None, roma_app_id=None, roma_app_name=None):
        """ListApiAttachablePluginsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量
        :type limit: int
        :param api_id: API编号
        :type api_id: str
        :param env_id: 发布的环境编号
        :type env_id: str
        :param plugin_name: 插件名称
        :type plugin_name: str
        :param plugin_type: 插件类型
        :type plugin_type: str
        :param plugin_id: 插件编号
        :type plugin_id: str
        :param roma_app_id: 集成应用编号
        :type roma_app_id: str
        :param roma_app_name: 集成应用名称
        :type roma_app_name: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._api_id = None
        self._env_id = None
        self._plugin_name = None
        self._plugin_type = None
        self._plugin_id = None
        self._roma_app_id = None
        self._roma_app_name = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.api_id = api_id
        self.env_id = env_id
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if plugin_type is not None:
            self.plugin_type = plugin_type
        if plugin_id is not None:
            self.plugin_id = plugin_id
        if roma_app_id is not None:
            self.roma_app_id = roma_app_id
        if roma_app_name is not None:
            self.roma_app_name = roma_app_name

    @property
    def instance_id(self):
        """Gets the instance_id of this ListApiAttachablePluginsRequest.

        实例ID

        :return: The instance_id of this ListApiAttachablePluginsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListApiAttachablePluginsRequest.

        实例ID

        :param instance_id: The instance_id of this ListApiAttachablePluginsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ListApiAttachablePluginsRequest.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListApiAttachablePluginsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListApiAttachablePluginsRequest.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListApiAttachablePluginsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListApiAttachablePluginsRequest.

        每页显示的条目数量

        :return: The limit of this ListApiAttachablePluginsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListApiAttachablePluginsRequest.

        每页显示的条目数量

        :param limit: The limit of this ListApiAttachablePluginsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def api_id(self):
        """Gets the api_id of this ListApiAttachablePluginsRequest.

        API编号

        :return: The api_id of this ListApiAttachablePluginsRequest.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this ListApiAttachablePluginsRequest.

        API编号

        :param api_id: The api_id of this ListApiAttachablePluginsRequest.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def env_id(self):
        """Gets the env_id of this ListApiAttachablePluginsRequest.

        发布的环境编号

        :return: The env_id of this ListApiAttachablePluginsRequest.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this ListApiAttachablePluginsRequest.

        发布的环境编号

        :param env_id: The env_id of this ListApiAttachablePluginsRequest.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def plugin_name(self):
        """Gets the plugin_name of this ListApiAttachablePluginsRequest.

        插件名称

        :return: The plugin_name of this ListApiAttachablePluginsRequest.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this ListApiAttachablePluginsRequest.

        插件名称

        :param plugin_name: The plugin_name of this ListApiAttachablePluginsRequest.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def plugin_type(self):
        """Gets the plugin_type of this ListApiAttachablePluginsRequest.

        插件类型

        :return: The plugin_type of this ListApiAttachablePluginsRequest.
        :rtype: str
        """
        return self._plugin_type

    @plugin_type.setter
    def plugin_type(self, plugin_type):
        """Sets the plugin_type of this ListApiAttachablePluginsRequest.

        插件类型

        :param plugin_type: The plugin_type of this ListApiAttachablePluginsRequest.
        :type plugin_type: str
        """
        self._plugin_type = plugin_type

    @property
    def plugin_id(self):
        """Gets the plugin_id of this ListApiAttachablePluginsRequest.

        插件编号

        :return: The plugin_id of this ListApiAttachablePluginsRequest.
        :rtype: str
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        """Sets the plugin_id of this ListApiAttachablePluginsRequest.

        插件编号

        :param plugin_id: The plugin_id of this ListApiAttachablePluginsRequest.
        :type plugin_id: str
        """
        self._plugin_id = plugin_id

    @property
    def roma_app_id(self):
        """Gets the roma_app_id of this ListApiAttachablePluginsRequest.

        集成应用编号

        :return: The roma_app_id of this ListApiAttachablePluginsRequest.
        :rtype: str
        """
        return self._roma_app_id

    @roma_app_id.setter
    def roma_app_id(self, roma_app_id):
        """Sets the roma_app_id of this ListApiAttachablePluginsRequest.

        集成应用编号

        :param roma_app_id: The roma_app_id of this ListApiAttachablePluginsRequest.
        :type roma_app_id: str
        """
        self._roma_app_id = roma_app_id

    @property
    def roma_app_name(self):
        """Gets the roma_app_name of this ListApiAttachablePluginsRequest.

        集成应用名称

        :return: The roma_app_name of this ListApiAttachablePluginsRequest.
        :rtype: str
        """
        return self._roma_app_name

    @roma_app_name.setter
    def roma_app_name(self, roma_app_name):
        """Sets the roma_app_name of this ListApiAttachablePluginsRequest.

        集成应用名称

        :param roma_app_name: The roma_app_name of this ListApiAttachablePluginsRequest.
        :type roma_app_name: str
        """
        self._roma_app_name = roma_app_name

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
        if not isinstance(other, ListApiAttachablePluginsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
