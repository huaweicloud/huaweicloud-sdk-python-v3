# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DevServerJobCreateRequest:

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
        'description': 'str',
        'server_ids': 'list[str]',
        'type': 'str',
        'is_reboot': 'bool',
        'items': 'list[DevServerJobItem]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'server_ids': 'server_ids',
        'type': 'type',
        'is_reboot': 'is_reboot',
        'items': 'items'
    }

    def __init__(self, name=None, description=None, server_ids=None, type=None, is_reboot=None, items=None):
        r"""DevServerJobCreateRequest

        The model defined in huaweicloud sdk

        :param name: **参数解释**：任务名称。 **约束限制**：^[-_.a-zA-Z0-9]{1,64}$。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type name: str
        :param description: **参数解释**：任务描述。 **约束限制**：^[-_.a-zA-Z0-9]{1,64}$。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type description: str
        :param server_ids: **参数解释**：DevServer实例id列表。 **取值范围**：不涉及。
        :type server_ids: list[str]
        :param type: **参数解释**：任务模板类型。 **约束限制**：^[-_.a-zA-Z0-9]{1,64}$。 **取值范围**：-COMMON  -SERVICE_DEPLOY 等。 **默认取值**：不涉及。
        :type type: str
        :param is_reboot: **参数解释**：任务失败后是否重启。 **约束限制**：不涉及。 **取值范围**：- true   -false。 **默认取值**：false。
        :type is_reboot: bool
        :param items: **参数解释**：任务实例列表。 **取值范围**：不涉及。
        :type items: list[:class:`huaweicloudsdkmodelarts.v1.DevServerJobItem`]
        """
        
        

        self._name = None
        self._description = None
        self._server_ids = None
        self._type = None
        self._is_reboot = None
        self._items = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.server_ids = server_ids
        self.type = type
        if is_reboot is not None:
            self.is_reboot = is_reboot
        self.items = items

    @property
    def name(self):
        r"""Gets the name of this DevServerJobCreateRequest.

        **参数解释**：任务名称。 **约束限制**：^[-_.a-zA-Z0-9]{1,64}$。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The name of this DevServerJobCreateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DevServerJobCreateRequest.

        **参数解释**：任务名称。 **约束限制**：^[-_.a-zA-Z0-9]{1,64}$。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param name: The name of this DevServerJobCreateRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this DevServerJobCreateRequest.

        **参数解释**：任务描述。 **约束限制**：^[-_.a-zA-Z0-9]{1,64}$。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The description of this DevServerJobCreateRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DevServerJobCreateRequest.

        **参数解释**：任务描述。 **约束限制**：^[-_.a-zA-Z0-9]{1,64}$。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param description: The description of this DevServerJobCreateRequest.
        :type description: str
        """
        self._description = description

    @property
    def server_ids(self):
        r"""Gets the server_ids of this DevServerJobCreateRequest.

        **参数解释**：DevServer实例id列表。 **取值范围**：不涉及。

        :return: The server_ids of this DevServerJobCreateRequest.
        :rtype: list[str]
        """
        return self._server_ids

    @server_ids.setter
    def server_ids(self, server_ids):
        r"""Sets the server_ids of this DevServerJobCreateRequest.

        **参数解释**：DevServer实例id列表。 **取值范围**：不涉及。

        :param server_ids: The server_ids of this DevServerJobCreateRequest.
        :type server_ids: list[str]
        """
        self._server_ids = server_ids

    @property
    def type(self):
        r"""Gets the type of this DevServerJobCreateRequest.

        **参数解释**：任务模板类型。 **约束限制**：^[-_.a-zA-Z0-9]{1,64}$。 **取值范围**：-COMMON  -SERVICE_DEPLOY 等。 **默认取值**：不涉及。

        :return: The type of this DevServerJobCreateRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DevServerJobCreateRequest.

        **参数解释**：任务模板类型。 **约束限制**：^[-_.a-zA-Z0-9]{1,64}$。 **取值范围**：-COMMON  -SERVICE_DEPLOY 等。 **默认取值**：不涉及。

        :param type: The type of this DevServerJobCreateRequest.
        :type type: str
        """
        self._type = type

    @property
    def is_reboot(self):
        r"""Gets the is_reboot of this DevServerJobCreateRequest.

        **参数解释**：任务失败后是否重启。 **约束限制**：不涉及。 **取值范围**：- true   -false。 **默认取值**：false。

        :return: The is_reboot of this DevServerJobCreateRequest.
        :rtype: bool
        """
        return self._is_reboot

    @is_reboot.setter
    def is_reboot(self, is_reboot):
        r"""Sets the is_reboot of this DevServerJobCreateRequest.

        **参数解释**：任务失败后是否重启。 **约束限制**：不涉及。 **取值范围**：- true   -false。 **默认取值**：false。

        :param is_reboot: The is_reboot of this DevServerJobCreateRequest.
        :type is_reboot: bool
        """
        self._is_reboot = is_reboot

    @property
    def items(self):
        r"""Gets the items of this DevServerJobCreateRequest.

        **参数解释**：任务实例列表。 **取值范围**：不涉及。

        :return: The items of this DevServerJobCreateRequest.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.DevServerJobItem`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this DevServerJobCreateRequest.

        **参数解释**：任务实例列表。 **取值范围**：不涉及。

        :param items: The items of this DevServerJobCreateRequest.
        :type items: list[:class:`huaweicloudsdkmodelarts.v1.DevServerJobItem`]
        """
        self._items = items

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
        if not isinstance(other, DevServerJobCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
