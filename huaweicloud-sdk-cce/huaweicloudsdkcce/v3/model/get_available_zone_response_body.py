# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetAvailableZoneResponseBody:

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
        'display_name': 'str',
        'az_group_ids': 'list[str]',
        'public_border_group': 'str',
        'category': 'str',
        'alias': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'display_name': 'displayName',
        'az_group_ids': 'azGroupIds',
        'public_border_group': 'PublicBorderGroup',
        'category': 'category',
        'alias': 'alias'
    }

    def __init__(self, id=None, name=None, display_name=None, az_group_ids=None, public_border_group=None, category=None, alias=None):
        r"""GetAvailableZoneResponseBody

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 可用区ID **取值范围**： 不涉及
        :type id: str
        :param name: **参数解释**： 可用区名称 **取值范围**： 不涉及
        :type name: str
        :param display_name: **参数解释**： 可用区按所在区域显示的名称 **取值范围**： 不涉及
        :type display_name: str
        :param az_group_ids: **参数解释**： 可用区所属的可用区组，一个可用区可能属于多个可用区组 **取值范围**： 不涉及
        :type az_group_ids: list[str]
        :param public_border_group: **参数解释**： EIP所属的组，IES边缘场景为可用区ID，中心区统一为“center” **取值范围**： 不涉及
        :type public_border_group: str
        :param category: **参数解释**： 可用区分类 **取值范围**： - Default: 中心云可用区 - IES: 专属云可用区 - HomeZone: 智能边缘云可用区
        :type category: str
        :param alias: **参数解释**： 可用区名称别名 **取值范围**： 不涉及
        :type alias: str
        """
        
        

        self._id = None
        self._name = None
        self._display_name = None
        self._az_group_ids = None
        self._public_border_group = None
        self._category = None
        self._alias = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if az_group_ids is not None:
            self.az_group_ids = az_group_ids
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if category is not None:
            self.category = category
        if alias is not None:
            self.alias = alias

    @property
    def id(self):
        r"""Gets the id of this GetAvailableZoneResponseBody.

        **参数解释**： 可用区ID **取值范围**： 不涉及

        :return: The id of this GetAvailableZoneResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GetAvailableZoneResponseBody.

        **参数解释**： 可用区ID **取值范围**： 不涉及

        :param id: The id of this GetAvailableZoneResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this GetAvailableZoneResponseBody.

        **参数解释**： 可用区名称 **取值范围**： 不涉及

        :return: The name of this GetAvailableZoneResponseBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GetAvailableZoneResponseBody.

        **参数解释**： 可用区名称 **取值范围**： 不涉及

        :param name: The name of this GetAvailableZoneResponseBody.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        r"""Gets the display_name of this GetAvailableZoneResponseBody.

        **参数解释**： 可用区按所在区域显示的名称 **取值范围**： 不涉及

        :return: The display_name of this GetAvailableZoneResponseBody.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this GetAvailableZoneResponseBody.

        **参数解释**： 可用区按所在区域显示的名称 **取值范围**： 不涉及

        :param display_name: The display_name of this GetAvailableZoneResponseBody.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def az_group_ids(self):
        r"""Gets the az_group_ids of this GetAvailableZoneResponseBody.

        **参数解释**： 可用区所属的可用区组，一个可用区可能属于多个可用区组 **取值范围**： 不涉及

        :return: The az_group_ids of this GetAvailableZoneResponseBody.
        :rtype: list[str]
        """
        return self._az_group_ids

    @az_group_ids.setter
    def az_group_ids(self, az_group_ids):
        r"""Sets the az_group_ids of this GetAvailableZoneResponseBody.

        **参数解释**： 可用区所属的可用区组，一个可用区可能属于多个可用区组 **取值范围**： 不涉及

        :param az_group_ids: The az_group_ids of this GetAvailableZoneResponseBody.
        :type az_group_ids: list[str]
        """
        self._az_group_ids = az_group_ids

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this GetAvailableZoneResponseBody.

        **参数解释**： EIP所属的组，IES边缘场景为可用区ID，中心区统一为“center” **取值范围**： 不涉及

        :return: The public_border_group of this GetAvailableZoneResponseBody.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this GetAvailableZoneResponseBody.

        **参数解释**： EIP所属的组，IES边缘场景为可用区ID，中心区统一为“center” **取值范围**： 不涉及

        :param public_border_group: The public_border_group of this GetAvailableZoneResponseBody.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def category(self):
        r"""Gets the category of this GetAvailableZoneResponseBody.

        **参数解释**： 可用区分类 **取值范围**： - Default: 中心云可用区 - IES: 专属云可用区 - HomeZone: 智能边缘云可用区

        :return: The category of this GetAvailableZoneResponseBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this GetAvailableZoneResponseBody.

        **参数解释**： 可用区分类 **取值范围**： - Default: 中心云可用区 - IES: 专属云可用区 - HomeZone: 智能边缘云可用区

        :param category: The category of this GetAvailableZoneResponseBody.
        :type category: str
        """
        self._category = category

    @property
    def alias(self):
        r"""Gets the alias of this GetAvailableZoneResponseBody.

        **参数解释**： 可用区名称别名 **取值范围**： 不涉及

        :return: The alias of this GetAvailableZoneResponseBody.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this GetAvailableZoneResponseBody.

        **参数解释**： 可用区名称别名 **取值范围**： 不涉及

        :param alias: The alias of this GetAvailableZoneResponseBody.
        :type alias: str
        """
        self._alias = alias

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
        if not isinstance(other, GetAvailableZoneResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
