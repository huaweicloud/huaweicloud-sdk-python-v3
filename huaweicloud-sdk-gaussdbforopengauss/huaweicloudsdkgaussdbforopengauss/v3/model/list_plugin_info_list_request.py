# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPluginInfoListRequest:

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
        'x_language': 'str',
        'offset': 'int',
        'limit': 'int',
        'plugin_name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'x_language': 'X-Language',
        'offset': 'offset',
        'limit': 'limit',
        'plugin_name': 'plugin_name'
    }

    def __init__(self, instance_id=None, x_language=None, offset=None, limit=None, plugin_name=None):
        r"""ListPluginInfoListRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。
        :type instance_id: str
        :param x_language: **参数解释**: 用户Token。 通过调用IAM服务[获取用户token](https://support.huaweicloud.com/intl/zh-cn/api-iam/iam_30_0001.html)。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type x_language: str
        :param offset: **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。例如：该参数指定为1，limit指定为10，则只展示第2-11条数据。 **约束限制**: 不涉及。 **取值范围**: [0, 2^31-1] **默认取值**: 默认为0（偏移0条数据，表示从第一条数据开始查询）。 
        :type offset: int
        :param limit: **参数解释**: 查询记录数。例如该参数设定为10，则查询结果最多只显示10条记录。 **约束限制**: 不涉及。 **取值范围**: [1, 100] **默认取值**: 默认为100。 
        :type limit: int
        :param plugin_name: **参数解释**: 插件包名称。 **约束限制**: 不涉及。 **取值范围**: - postgis  **默认取值**: 不涉及。 
        :type plugin_name: str
        """
        
        

        self._instance_id = None
        self._x_language = None
        self._offset = None
        self._limit = None
        self._plugin_name = None
        self.discriminator = None

        self.instance_id = instance_id
        if x_language is not None:
            self.x_language = x_language
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if plugin_name is not None:
            self.plugin_name = plugin_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListPluginInfoListRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :return: The instance_id of this ListPluginInfoListRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListPluginInfoListRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this ListPluginInfoListRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ListPluginInfoListRequest.

        **参数解释**: 用户Token。 通过调用IAM服务[获取用户token](https://support.huaweicloud.com/intl/zh-cn/api-iam/iam_30_0001.html)。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The x_language of this ListPluginInfoListRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListPluginInfoListRequest.

        **参数解释**: 用户Token。 通过调用IAM服务[获取用户token](https://support.huaweicloud.com/intl/zh-cn/api-iam/iam_30_0001.html)。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param x_language: The x_language of this ListPluginInfoListRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def offset(self):
        r"""Gets the offset of this ListPluginInfoListRequest.

        **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。例如：该参数指定为1，limit指定为10，则只展示第2-11条数据。 **约束限制**: 不涉及。 **取值范围**: [0, 2^31-1] **默认取值**: 默认为0（偏移0条数据，表示从第一条数据开始查询）。 

        :return: The offset of this ListPluginInfoListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPluginInfoListRequest.

        **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。例如：该参数指定为1，limit指定为10，则只展示第2-11条数据。 **约束限制**: 不涉及。 **取值范围**: [0, 2^31-1] **默认取值**: 默认为0（偏移0条数据，表示从第一条数据开始查询）。 

        :param offset: The offset of this ListPluginInfoListRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPluginInfoListRequest.

        **参数解释**: 查询记录数。例如该参数设定为10，则查询结果最多只显示10条记录。 **约束限制**: 不涉及。 **取值范围**: [1, 100] **默认取值**: 默认为100。 

        :return: The limit of this ListPluginInfoListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPluginInfoListRequest.

        **参数解释**: 查询记录数。例如该参数设定为10，则查询结果最多只显示10条记录。 **约束限制**: 不涉及。 **取值范围**: [1, 100] **默认取值**: 默认为100。 

        :param limit: The limit of this ListPluginInfoListRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this ListPluginInfoListRequest.

        **参数解释**: 插件包名称。 **约束限制**: 不涉及。 **取值范围**: - postgis  **默认取值**: 不涉及。 

        :return: The plugin_name of this ListPluginInfoListRequest.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this ListPluginInfoListRequest.

        **参数解释**: 插件包名称。 **约束限制**: 不涉及。 **取值范围**: - postgis  **默认取值**: 不涉及。 

        :param plugin_name: The plugin_name of this ListPluginInfoListRequest.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListPluginInfoListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
