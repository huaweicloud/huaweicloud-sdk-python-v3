# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CapacityWebListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'component_id': 'str',
        'application_id': 'str',
        'domain_id': 'str',
        'provider_obj': 'list[CapacityWebListRequestProviderObj]'
    }

    attribute_map = {
        'group_id': 'group_id',
        'component_id': 'component_id',
        'application_id': 'application_id',
        'domain_id': 'domain_id',
        'provider_obj': 'provider_obj'
    }

    def __init__(self, group_id=None, component_id=None, application_id=None, domain_id=None, provider_obj=None):
        r"""CapacityWebListRequest

        The model defined in huaweicloud sdk

        :param group_id: **参数解释：** 用户选择当前分组对应的id值。 **约束限制：** 应用、组件和分组ID，有且仅有1个有值。 **取值范围：** 字符串，长度24个字符。 **默认取值：** 不涉及。
        :type group_id: str
        :param component_id: **参数解释：** 用户选择当前组件对应的id值。 **约束限制：** 应用、组件和分组ID，有且仅有1个有值。 **取值范围：** 字符串，长度24个字符。 **默认取值：** 不涉及。
        :type component_id: str
        :param application_id: **参数解释：** 用户选择当前应用对应的id值。 **约束限制：** 应用、组件和分组ID，有且仅有1个有值。 **取值范围：** 字符串，长度24个字符。 **默认取值：** 不涉及。
        :type application_id: str
        :param domain_id: **参数解释：** 用户登录租户对应的账号ID即租户id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type domain_id: str
        :param provider_obj: **参数解释：** 资源对象。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type provider_obj: list[:class:`huaweicloudsdkcoc.v1.CapacityWebListRequestProviderObj`]
        """
        
        

        self._group_id = None
        self._component_id = None
        self._application_id = None
        self._domain_id = None
        self._provider_obj = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if component_id is not None:
            self.component_id = component_id
        if application_id is not None:
            self.application_id = application_id
        if domain_id is not None:
            self.domain_id = domain_id
        self.provider_obj = provider_obj

    @property
    def group_id(self):
        r"""Gets the group_id of this CapacityWebListRequest.

        **参数解释：** 用户选择当前分组对应的id值。 **约束限制：** 应用、组件和分组ID，有且仅有1个有值。 **取值范围：** 字符串，长度24个字符。 **默认取值：** 不涉及。

        :return: The group_id of this CapacityWebListRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this CapacityWebListRequest.

        **参数解释：** 用户选择当前分组对应的id值。 **约束限制：** 应用、组件和分组ID，有且仅有1个有值。 **取值范围：** 字符串，长度24个字符。 **默认取值：** 不涉及。

        :param group_id: The group_id of this CapacityWebListRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def component_id(self):
        r"""Gets the component_id of this CapacityWebListRequest.

        **参数解释：** 用户选择当前组件对应的id值。 **约束限制：** 应用、组件和分组ID，有且仅有1个有值。 **取值范围：** 字符串，长度24个字符。 **默认取值：** 不涉及。

        :return: The component_id of this CapacityWebListRequest.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this CapacityWebListRequest.

        **参数解释：** 用户选择当前组件对应的id值。 **约束限制：** 应用、组件和分组ID，有且仅有1个有值。 **取值范围：** 字符串，长度24个字符。 **默认取值：** 不涉及。

        :param component_id: The component_id of this CapacityWebListRequest.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def application_id(self):
        r"""Gets the application_id of this CapacityWebListRequest.

        **参数解释：** 用户选择当前应用对应的id值。 **约束限制：** 应用、组件和分组ID，有且仅有1个有值。 **取值范围：** 字符串，长度24个字符。 **默认取值：** 不涉及。

        :return: The application_id of this CapacityWebListRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this CapacityWebListRequest.

        **参数解释：** 用户选择当前应用对应的id值。 **约束限制：** 应用、组件和分组ID，有且仅有1个有值。 **取值范围：** 字符串，长度24个字符。 **默认取值：** 不涉及。

        :param application_id: The application_id of this CapacityWebListRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CapacityWebListRequest.

        **参数解释：** 用户登录租户对应的账号ID即租户id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The domain_id of this CapacityWebListRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CapacityWebListRequest.

        **参数解释：** 用户登录租户对应的账号ID即租户id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param domain_id: The domain_id of this CapacityWebListRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def provider_obj(self):
        r"""Gets the provider_obj of this CapacityWebListRequest.

        **参数解释：** 资源对象。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The provider_obj of this CapacityWebListRequest.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.CapacityWebListRequestProviderObj`]
        """
        return self._provider_obj

    @provider_obj.setter
    def provider_obj(self, provider_obj):
        r"""Sets the provider_obj of this CapacityWebListRequest.

        **参数解释：** 资源对象。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param provider_obj: The provider_obj of this CapacityWebListRequest.
        :type provider_obj: list[:class:`huaweicloudsdkcoc.v1.CapacityWebListRequestProviderObj`]
        """
        self._provider_obj = provider_obj

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
        if not isinstance(other, CapacityWebListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
