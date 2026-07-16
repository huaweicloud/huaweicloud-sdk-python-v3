# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsLabelItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'label_id': 'str',
        'creator_id': 'str',
        'creator': 'str',
        'name': 'str',
        'content_type': 'str',
        'description': 'str',
        'enums': 'list[OpsLabelValueItem]'
    }

    attribute_map = {
        'label_id': 'label_id',
        'creator_id': 'creator_id',
        'creator': 'creator',
        'name': 'name',
        'content_type': 'content_type',
        'description': 'description',
        'enums': 'enums'
    }

    def __init__(self, label_id=None, creator_id=None, creator=None, name=None, content_type=None, description=None, enums=None):
        r"""OpsLabelItem

        The model defined in huaweicloud sdk

        :param label_id: **参数解释：** 标注的唯一标识符（ID）。 **取值范围：** 不涉及。
        :type label_id: str
        :param creator_id: **参数解释：** 创建该标注的用户唯一ID。 **取值范围：** 不涉及。
        :type creator_id: str
        :param creator: **参数解释：** 创建者的名称或账号信息。 **取值范围：** 不涉及。
        :type creator: str
        :param name: **参数解释：** 标注的显示名称。 **取值范围：** 不涉及。
        :type name: str
        :param content_type: **参数解释：** 标注的内容类型（如分类category 等）。 **取值范围：** 不涉及。
        :type content_type: str
        :param description: **参数解释：** 关于该标注的详细说明或补充信息。 **取值范围：** 不涉及。
        :type description: str
        :param enums: **参数解释：** 该标注包含的枚举值（选项）列表。 **取值范围：** 不涉及。
        :type enums: list[:class:`huaweicloudsdkagentarts.v1.OpsLabelValueItem`]
        """
        
        

        self._label_id = None
        self._creator_id = None
        self._creator = None
        self._name = None
        self._content_type = None
        self._description = None
        self._enums = None
        self.discriminator = None

        if label_id is not None:
            self.label_id = label_id
        if creator_id is not None:
            self.creator_id = creator_id
        if creator is not None:
            self.creator = creator
        if name is not None:
            self.name = name
        if content_type is not None:
            self.content_type = content_type
        if description is not None:
            self.description = description
        if enums is not None:
            self.enums = enums

    @property
    def label_id(self):
        r"""Gets the label_id of this OpsLabelItem.

        **参数解释：** 标注的唯一标识符（ID）。 **取值范围：** 不涉及。

        :return: The label_id of this OpsLabelItem.
        :rtype: str
        """
        return self._label_id

    @label_id.setter
    def label_id(self, label_id):
        r"""Sets the label_id of this OpsLabelItem.

        **参数解释：** 标注的唯一标识符（ID）。 **取值范围：** 不涉及。

        :param label_id: The label_id of this OpsLabelItem.
        :type label_id: str
        """
        self._label_id = label_id

    @property
    def creator_id(self):
        r"""Gets the creator_id of this OpsLabelItem.

        **参数解释：** 创建该标注的用户唯一ID。 **取值范围：** 不涉及。

        :return: The creator_id of this OpsLabelItem.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this OpsLabelItem.

        **参数解释：** 创建该标注的用户唯一ID。 **取值范围：** 不涉及。

        :param creator_id: The creator_id of this OpsLabelItem.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator(self):
        r"""Gets the creator of this OpsLabelItem.

        **参数解释：** 创建者的名称或账号信息。 **取值范围：** 不涉及。

        :return: The creator of this OpsLabelItem.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this OpsLabelItem.

        **参数解释：** 创建者的名称或账号信息。 **取值范围：** 不涉及。

        :param creator: The creator of this OpsLabelItem.
        :type creator: str
        """
        self._creator = creator

    @property
    def name(self):
        r"""Gets the name of this OpsLabelItem.

        **参数解释：** 标注的显示名称。 **取值范围：** 不涉及。

        :return: The name of this OpsLabelItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OpsLabelItem.

        **参数解释：** 标注的显示名称。 **取值范围：** 不涉及。

        :param name: The name of this OpsLabelItem.
        :type name: str
        """
        self._name = name

    @property
    def content_type(self):
        r"""Gets the content_type of this OpsLabelItem.

        **参数解释：** 标注的内容类型（如分类category 等）。 **取值范围：** 不涉及。

        :return: The content_type of this OpsLabelItem.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this OpsLabelItem.

        **参数解释：** 标注的内容类型（如分类category 等）。 **取值范围：** 不涉及。

        :param content_type: The content_type of this OpsLabelItem.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def description(self):
        r"""Gets the description of this OpsLabelItem.

        **参数解释：** 关于该标注的详细说明或补充信息。 **取值范围：** 不涉及。

        :return: The description of this OpsLabelItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this OpsLabelItem.

        **参数解释：** 关于该标注的详细说明或补充信息。 **取值范围：** 不涉及。

        :param description: The description of this OpsLabelItem.
        :type description: str
        """
        self._description = description

    @property
    def enums(self):
        r"""Gets the enums of this OpsLabelItem.

        **参数解释：** 该标注包含的枚举值（选项）列表。 **取值范围：** 不涉及。

        :return: The enums of this OpsLabelItem.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsLabelValueItem`]
        """
        return self._enums

    @enums.setter
    def enums(self, enums):
        r"""Sets the enums of this OpsLabelItem.

        **参数解释：** 该标注包含的枚举值（选项）列表。 **取值范围：** 不涉及。

        :param enums: The enums of this OpsLabelItem.
        :type enums: list[:class:`huaweicloudsdkagentarts.v1.OpsLabelValueItem`]
        """
        self._enums = enums

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
        if not isinstance(other, OpsLabelItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
