# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewaysResourceInstanceForTMS:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resource_name': 'str',
        'tags': 'list[CoreGatewayTag]',
        'resource_detail': 'object'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'tags': 'tags',
        'resource_detail': 'resource_detail'
    }

    def __init__(self, resource_id=None, resource_name=None, tags=None, resource_detail=None):
        r"""CoreGatewaysResourceInstanceForTMS

        The model defined in huaweicloud sdk

        :param resource_id: **参数解释：** 网关ID，网关的唯一标识符。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 
        :type resource_id: str
        :param resource_name: **参数解释：** 网关名称。 **取值范围：** 长度为 2-40 个字符，匹配以小写字母开头、以小写字母或数字结尾、中间可包含0到38个小写字母、数字或连字符的字符串，符合正则条件^[a-z][a-z0-9-]{0,38}[a-z0-9]$。 
        :type resource_name: str
        :param tags: **参数解释：** 资源标签列表，没有标签默认为空数组。 **取值范围：** 数组长度为0-20。 
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        :param resource_detail: **参数解释：** 资源详情，资源对象用于扩展。默认为空。 **取值范围：** 不涉及。 
        :type resource_detail: object
        """
        
        

        self._resource_id = None
        self._resource_name = None
        self._tags = None
        self._resource_detail = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if tags is not None:
            self.tags = tags
        if resource_detail is not None:
            self.resource_detail = resource_detail

    @property
    def resource_id(self):
        r"""Gets the resource_id of this CoreGatewaysResourceInstanceForTMS.

        **参数解释：** 网关ID，网关的唯一标识符。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 

        :return: The resource_id of this CoreGatewaysResourceInstanceForTMS.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this CoreGatewaysResourceInstanceForTMS.

        **参数解释：** 网关ID，网关的唯一标识符。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 

        :param resource_id: The resource_id of this CoreGatewaysResourceInstanceForTMS.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this CoreGatewaysResourceInstanceForTMS.

        **参数解释：** 网关名称。 **取值范围：** 长度为 2-40 个字符，匹配以小写字母开头、以小写字母或数字结尾、中间可包含0到38个小写字母、数字或连字符的字符串，符合正则条件^[a-z][a-z0-9-]{0,38}[a-z0-9]$。 

        :return: The resource_name of this CoreGatewaysResourceInstanceForTMS.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this CoreGatewaysResourceInstanceForTMS.

        **参数解释：** 网关名称。 **取值范围：** 长度为 2-40 个字符，匹配以小写字母开头、以小写字母或数字结尾、中间可包含0到38个小写字母、数字或连字符的字符串，符合正则条件^[a-z][a-z0-9-]{0,38}[a-z0-9]$。 

        :param resource_name: The resource_name of this CoreGatewaysResourceInstanceForTMS.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def tags(self):
        r"""Gets the tags of this CoreGatewaysResourceInstanceForTMS.

        **参数解释：** 资源标签列表，没有标签默认为空数组。 **取值范围：** 数组长度为0-20。 

        :return: The tags of this CoreGatewaysResourceInstanceForTMS.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CoreGatewaysResourceInstanceForTMS.

        **参数解释：** 资源标签列表，没有标签默认为空数组。 **取值范围：** 数组长度为0-20。 

        :param tags: The tags of this CoreGatewaysResourceInstanceForTMS.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        """
        self._tags = tags

    @property
    def resource_detail(self):
        r"""Gets the resource_detail of this CoreGatewaysResourceInstanceForTMS.

        **参数解释：** 资源详情，资源对象用于扩展。默认为空。 **取值范围：** 不涉及。 

        :return: The resource_detail of this CoreGatewaysResourceInstanceForTMS.
        :rtype: object
        """
        return self._resource_detail

    @resource_detail.setter
    def resource_detail(self, resource_detail):
        r"""Sets the resource_detail of this CoreGatewaysResourceInstanceForTMS.

        **参数解释：** 资源详情，资源对象用于扩展。默认为空。 **取值范围：** 不涉及。 

        :param resource_detail: The resource_detail of this CoreGatewaysResourceInstanceForTMS.
        :type resource_detail: object
        """
        self._resource_detail = resource_detail

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
        if not isinstance(other, CoreGatewaysResourceInstanceForTMS):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
