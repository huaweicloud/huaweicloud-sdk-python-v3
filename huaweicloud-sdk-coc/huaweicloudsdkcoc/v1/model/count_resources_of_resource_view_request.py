# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountResourcesOfResourceViewRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'view_id': 'str',
        'provider': 'str',
        'type': 'str'
    }

    attribute_map = {
        'view_id': 'view_id',
        'provider': 'provider',
        'type': 'type'
    }

    def __init__(self, view_id=None, provider=None, type=None):
        r"""CountResourcesOfResourceViewRequest

        The model defined in huaweicloud sdk

        :param view_id: **参数解释：** 视图ID。 **约束限制：** 不涉及。 **取值范围：** 自定义生成 长度1~32之间。 **默认取值：** 不涉及。
        :type view_id: str
        :param provider: **参数解释：** 云服务名称。 **约束限制：** 不涉及。 **取值范围：** 自定义，可选esc，cce等资源。 **默认取值：** 不涉及。
        :type provider: str
        :param type: **参数解释：** 资源类型名称。 **约束限制：** 不涉及。 **取值范围：** 自定义，云资源类型。 **默认取值：** 不涉及。
        :type type: str
        """
        
        

        self._view_id = None
        self._provider = None
        self._type = None
        self.discriminator = None

        self.view_id = view_id
        if provider is not None:
            self.provider = provider
        if type is not None:
            self.type = type

    @property
    def view_id(self):
        r"""Gets the view_id of this CountResourcesOfResourceViewRequest.

        **参数解释：** 视图ID。 **约束限制：** 不涉及。 **取值范围：** 自定义生成 长度1~32之间。 **默认取值：** 不涉及。

        :return: The view_id of this CountResourcesOfResourceViewRequest.
        :rtype: str
        """
        return self._view_id

    @view_id.setter
    def view_id(self, view_id):
        r"""Sets the view_id of this CountResourcesOfResourceViewRequest.

        **参数解释：** 视图ID。 **约束限制：** 不涉及。 **取值范围：** 自定义生成 长度1~32之间。 **默认取值：** 不涉及。

        :param view_id: The view_id of this CountResourcesOfResourceViewRequest.
        :type view_id: str
        """
        self._view_id = view_id

    @property
    def provider(self):
        r"""Gets the provider of this CountResourcesOfResourceViewRequest.

        **参数解释：** 云服务名称。 **约束限制：** 不涉及。 **取值范围：** 自定义，可选esc，cce等资源。 **默认取值：** 不涉及。

        :return: The provider of this CountResourcesOfResourceViewRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this CountResourcesOfResourceViewRequest.

        **参数解释：** 云服务名称。 **约束限制：** 不涉及。 **取值范围：** 自定义，可选esc，cce等资源。 **默认取值：** 不涉及。

        :param provider: The provider of this CountResourcesOfResourceViewRequest.
        :type provider: str
        """
        self._provider = provider

    @property
    def type(self):
        r"""Gets the type of this CountResourcesOfResourceViewRequest.

        **参数解释：** 资源类型名称。 **约束限制：** 不涉及。 **取值范围：** 自定义，云资源类型。 **默认取值：** 不涉及。

        :return: The type of this CountResourcesOfResourceViewRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CountResourcesOfResourceViewRequest.

        **参数解释：** 资源类型名称。 **约束限制：** 不涉及。 **取值范围：** 自定义，云资源类型。 **默认取值：** 不涉及。

        :param type: The type of this CountResourcesOfResourceViewRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, CountResourcesOfResourceViewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
