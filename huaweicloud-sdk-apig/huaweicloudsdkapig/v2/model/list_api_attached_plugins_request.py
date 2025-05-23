# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApiAttachedPluginsRequest:

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
        'plugin_id': 'str',
        'env_name': 'str',
        'plugin_type': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'api_id': 'api_id',
        'env_id': 'env_id',
        'plugin_name': 'plugin_name',
        'plugin_id': 'plugin_id',
        'env_name': 'env_name',
        'plugin_type': 'plugin_type'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, api_id=None, env_id=None, plugin_name=None, plugin_id=None, env_name=None, plugin_type=None):
        r"""ListApiAttachedPluginsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，在API网关控制台的“实例信息”中获取。
        :type instance_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500
        :type limit: int
        :param api_id: API编号
        :type api_id: str
        :param env_id: 发布的环境编号
        :type env_id: str
        :param plugin_name: 插件名称
        :type plugin_name: str
        :param plugin_id: 插件编号
        :type plugin_id: str
        :param env_name: 环境名称
        :type env_name: str
        :param plugin_type: 插件类型
        :type plugin_type: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._api_id = None
        self._env_id = None
        self._plugin_name = None
        self._plugin_id = None
        self._env_name = None
        self._plugin_type = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.api_id = api_id
        if env_id is not None:
            self.env_id = env_id
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if plugin_id is not None:
            self.plugin_id = plugin_id
        if env_name is not None:
            self.env_name = env_name
        if plugin_type is not None:
            self.plugin_type = plugin_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListApiAttachedPluginsRequest.

        实例ID，在API网关控制台的“实例信息”中获取。

        :return: The instance_id of this ListApiAttachedPluginsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListApiAttachedPluginsRequest.

        实例ID，在API网关控制台的“实例信息”中获取。

        :param instance_id: The instance_id of this ListApiAttachedPluginsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ListApiAttachedPluginsRequest.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListApiAttachedPluginsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListApiAttachedPluginsRequest.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListApiAttachedPluginsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListApiAttachedPluginsRequest.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :return: The limit of this ListApiAttachedPluginsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListApiAttachedPluginsRequest.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :param limit: The limit of this ListApiAttachedPluginsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def api_id(self):
        r"""Gets the api_id of this ListApiAttachedPluginsRequest.

        API编号

        :return: The api_id of this ListApiAttachedPluginsRequest.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        r"""Sets the api_id of this ListApiAttachedPluginsRequest.

        API编号

        :param api_id: The api_id of this ListApiAttachedPluginsRequest.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def env_id(self):
        r"""Gets the env_id of this ListApiAttachedPluginsRequest.

        发布的环境编号

        :return: The env_id of this ListApiAttachedPluginsRequest.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this ListApiAttachedPluginsRequest.

        发布的环境编号

        :param env_id: The env_id of this ListApiAttachedPluginsRequest.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this ListApiAttachedPluginsRequest.

        插件名称

        :return: The plugin_name of this ListApiAttachedPluginsRequest.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this ListApiAttachedPluginsRequest.

        插件名称

        :param plugin_name: The plugin_name of this ListApiAttachedPluginsRequest.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def plugin_id(self):
        r"""Gets the plugin_id of this ListApiAttachedPluginsRequest.

        插件编号

        :return: The plugin_id of this ListApiAttachedPluginsRequest.
        :rtype: str
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        r"""Sets the plugin_id of this ListApiAttachedPluginsRequest.

        插件编号

        :param plugin_id: The plugin_id of this ListApiAttachedPluginsRequest.
        :type plugin_id: str
        """
        self._plugin_id = plugin_id

    @property
    def env_name(self):
        r"""Gets the env_name of this ListApiAttachedPluginsRequest.

        环境名称

        :return: The env_name of this ListApiAttachedPluginsRequest.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        r"""Sets the env_name of this ListApiAttachedPluginsRequest.

        环境名称

        :param env_name: The env_name of this ListApiAttachedPluginsRequest.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def plugin_type(self):
        r"""Gets the plugin_type of this ListApiAttachedPluginsRequest.

        插件类型

        :return: The plugin_type of this ListApiAttachedPluginsRequest.
        :rtype: str
        """
        return self._plugin_type

    @plugin_type.setter
    def plugin_type(self, plugin_type):
        r"""Sets the plugin_type of this ListApiAttachedPluginsRequest.

        插件类型

        :param plugin_type: The plugin_type of this ListApiAttachedPluginsRequest.
        :type plugin_type: str
        """
        self._plugin_type = plugin_type

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
        if not isinstance(other, ListApiAttachedPluginsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
