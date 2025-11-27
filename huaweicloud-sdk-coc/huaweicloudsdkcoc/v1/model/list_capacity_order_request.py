# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCapacityOrderRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_id': 'str',
        'component_id': 'str',
        'group_id': 'str',
        'provider': 'str',
        'type': 'str'
    }

    attribute_map = {
        'application_id': 'application_id',
        'component_id': 'component_id',
        'group_id': 'group_id',
        'provider': 'provider',
        'type': 'type'
    }

    def __init__(self, application_id=None, component_id=None, group_id=None, provider=None, type=None):
        r"""ListCapacityOrderRequest

        The model defined in huaweicloud sdk

        :param application_id: **参数解释：** 应用id。 **约束限制：** 不涉及。 **取值范围：** 需要查询容量数据排名的应用id。 **默认取值：** 不涉及
        :type application_id: str
        :param component_id: **参数解释：** 组件id。 **约束限制：** 不涉及。 **取值范围：** 需要查询容量数据排名的组件id。 **默认取值：** 不涉及
        :type component_id: str
        :param group_id: **参数解释：** 分组id。 **约束限制：** 不涉及。 **取值范围：** 需要查询容量数据排名的分组id **默认取值：** 不涉及
        :type group_id: str
        :param provider: **参数解释：** 云服务名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type provider: str
        :param type: **参数解释：** 资源类型名称。 **约束限制：** 不涉及。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。 **默认取值：** 不涉及。
        :type type: str
        """
        
        

        self._application_id = None
        self._component_id = None
        self._group_id = None
        self._provider = None
        self._type = None
        self.discriminator = None

        if application_id is not None:
            self.application_id = application_id
        if component_id is not None:
            self.component_id = component_id
        if group_id is not None:
            self.group_id = group_id
        self.provider = provider
        self.type = type

    @property
    def application_id(self):
        r"""Gets the application_id of this ListCapacityOrderRequest.

        **参数解释：** 应用id。 **约束限制：** 不涉及。 **取值范围：** 需要查询容量数据排名的应用id。 **默认取值：** 不涉及

        :return: The application_id of this ListCapacityOrderRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this ListCapacityOrderRequest.

        **参数解释：** 应用id。 **约束限制：** 不涉及。 **取值范围：** 需要查询容量数据排名的应用id。 **默认取值：** 不涉及

        :param application_id: The application_id of this ListCapacityOrderRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def component_id(self):
        r"""Gets the component_id of this ListCapacityOrderRequest.

        **参数解释：** 组件id。 **约束限制：** 不涉及。 **取值范围：** 需要查询容量数据排名的组件id。 **默认取值：** 不涉及

        :return: The component_id of this ListCapacityOrderRequest.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this ListCapacityOrderRequest.

        **参数解释：** 组件id。 **约束限制：** 不涉及。 **取值范围：** 需要查询容量数据排名的组件id。 **默认取值：** 不涉及

        :param component_id: The component_id of this ListCapacityOrderRequest.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def group_id(self):
        r"""Gets the group_id of this ListCapacityOrderRequest.

        **参数解释：** 分组id。 **约束限制：** 不涉及。 **取值范围：** 需要查询容量数据排名的分组id **默认取值：** 不涉及

        :return: The group_id of this ListCapacityOrderRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListCapacityOrderRequest.

        **参数解释：** 分组id。 **约束限制：** 不涉及。 **取值范围：** 需要查询容量数据排名的分组id **默认取值：** 不涉及

        :param group_id: The group_id of this ListCapacityOrderRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def provider(self):
        r"""Gets the provider of this ListCapacityOrderRequest.

        **参数解释：** 云服务名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The provider of this ListCapacityOrderRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this ListCapacityOrderRequest.

        **参数解释：** 云服务名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param provider: The provider of this ListCapacityOrderRequest.
        :type provider: str
        """
        self._provider = provider

    @property
    def type(self):
        r"""Gets the type of this ListCapacityOrderRequest.

        **参数解释：** 资源类型名称。 **约束限制：** 不涉及。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。 **默认取值：** 不涉及。

        :return: The type of this ListCapacityOrderRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListCapacityOrderRequest.

        **参数解释：** 资源类型名称。 **约束限制：** 不涉及。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。 **默认取值：** 不涉及。

        :param type: The type of this ListCapacityOrderRequest.
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
        if not isinstance(other, ListCapacityOrderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
