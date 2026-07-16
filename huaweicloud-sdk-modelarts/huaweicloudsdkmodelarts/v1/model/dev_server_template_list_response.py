# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DevServerTemplateListResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'type': 'str',
        'flavor_type': 'str',
        'params': 'list[TemplateParam]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'flavor_type': 'flavor_type',
        'params': 'params'
    }

    def __init__(self, id=None, name=None, description=None, type=None, flavor_type=None, params=None):
        r"""DevServerTemplateListResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**：任务模板id。 **取值范围**：不涉及。
        :type id: str
        :param name: **参数解释**：任务模板名。 **取值范围**：不涉及。
        :type name: str
        :param description: **参数解释**：任务模板描述。 **取值范围**：不涉及。
        :type description: str
        :param type: **参数解释**：任务模板类型。 **取值范围**：- COMMON  - LOG_COLLECT等。
        :type type: str
        :param flavor_type: **参数解释**：规格类型。 **取值范围**：-ASCEND_SNT9B   -ASCEND_SNT9C   -ASCEND_GENERIC。
        :type flavor_type: str
        :param params: **参数解释**：模板的一些任务所需额外params参数。
        :type params: list[:class:`huaweicloudsdkmodelarts.v1.TemplateParam`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._type = None
        self._flavor_type = None
        self._params = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if flavor_type is not None:
            self.flavor_type = flavor_type
        if params is not None:
            self.params = params

    @property
    def id(self):
        r"""Gets the id of this DevServerTemplateListResponse.

        **参数解释**：任务模板id。 **取值范围**：不涉及。

        :return: The id of this DevServerTemplateListResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DevServerTemplateListResponse.

        **参数解释**：任务模板id。 **取值范围**：不涉及。

        :param id: The id of this DevServerTemplateListResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this DevServerTemplateListResponse.

        **参数解释**：任务模板名。 **取值范围**：不涉及。

        :return: The name of this DevServerTemplateListResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DevServerTemplateListResponse.

        **参数解释**：任务模板名。 **取值范围**：不涉及。

        :param name: The name of this DevServerTemplateListResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this DevServerTemplateListResponse.

        **参数解释**：任务模板描述。 **取值范围**：不涉及。

        :return: The description of this DevServerTemplateListResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DevServerTemplateListResponse.

        **参数解释**：任务模板描述。 **取值范围**：不涉及。

        :param description: The description of this DevServerTemplateListResponse.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this DevServerTemplateListResponse.

        **参数解释**：任务模板类型。 **取值范围**：- COMMON  - LOG_COLLECT等。

        :return: The type of this DevServerTemplateListResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DevServerTemplateListResponse.

        **参数解释**：任务模板类型。 **取值范围**：- COMMON  - LOG_COLLECT等。

        :param type: The type of this DevServerTemplateListResponse.
        :type type: str
        """
        self._type = type

    @property
    def flavor_type(self):
        r"""Gets the flavor_type of this DevServerTemplateListResponse.

        **参数解释**：规格类型。 **取值范围**：-ASCEND_SNT9B   -ASCEND_SNT9C   -ASCEND_GENERIC。

        :return: The flavor_type of this DevServerTemplateListResponse.
        :rtype: str
        """
        return self._flavor_type

    @flavor_type.setter
    def flavor_type(self, flavor_type):
        r"""Sets the flavor_type of this DevServerTemplateListResponse.

        **参数解释**：规格类型。 **取值范围**：-ASCEND_SNT9B   -ASCEND_SNT9C   -ASCEND_GENERIC。

        :param flavor_type: The flavor_type of this DevServerTemplateListResponse.
        :type flavor_type: str
        """
        self._flavor_type = flavor_type

    @property
    def params(self):
        r"""Gets the params of this DevServerTemplateListResponse.

        **参数解释**：模板的一些任务所需额外params参数。

        :return: The params of this DevServerTemplateListResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.TemplateParam`]
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this DevServerTemplateListResponse.

        **参数解释**：模板的一些任务所需额外params参数。

        :param params: The params of this DevServerTemplateListResponse.
        :type params: list[:class:`huaweicloudsdkmodelarts.v1.TemplateParam`]
        """
        self._params = params

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
        if not isinstance(other, DevServerTemplateListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
