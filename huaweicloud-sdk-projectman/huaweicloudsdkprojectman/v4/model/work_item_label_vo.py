# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkItemLabelVO:

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
        'category': 'str',
        'label_type': 'str',
        'color': 'str',
        'title': 'str',
        'type': 'str',
        'state': 'str',
        'modified_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'category': 'category',
        'label_type': 'label_type',
        'color': 'color',
        'title': 'title',
        'type': 'type',
        'state': 'state',
        'modified_by': 'modified_by'
    }

    def __init__(self, id=None, category=None, label_type=None, color=None, title=None, type=None, state=None, modified_by=None):
        r"""WorkItemLabelVO

        The model defined in huaweicloud sdk

        :param id: **参数解释：**  标签Id。 **约束限制：**  最小长度：18，最大长度：19。 **取值范围：**  不涉及。
        :type id: str
        :param category: **参数解释：**  对象类型。 **约束限制：**  固定为Label，表示当前对象类型为标签。 **取值范围：**  不涉及。
        :type category: str
        :param label_type: **参数解释：**  标签所属的工作项的类别。 **取值范围：**  - requirement - raw requirement - bug - task - feature
        :type label_type: str
        :param color: **参数解释：**  标签颜色的RGB值。 **取值范围：**  - #86CAFF - #6DDEBB - #A6DD82 - #FAC20A  - #FA9841 - #F66F6A - #F3689A - #A97AF8 - #71757F - #5E7CE0 - #207AB3 - #169E6C - #6CA83B - #B58200 - #B54E04 - #B02121 - #AD215B - #572DB3 - #4F4F4F - #3C51A6
        :type color: str
        :param title: **参数解释：**  标签标题。 **约束限制：**  最小长度：1，最大长度：30。
        :type title: str
        :param type: **参数解释：**  表示当前对象数据类型为标签。 **约束限制：**  固定为label。 **取值范围：**  label。
        :type type: str
        :param state: **参数解释：**  标签的生命周期。 **取值范围：**  - 正在工作 - 作废 - 删除
        :type state: str
        :param modified_by: **参数解释：**  最近修改人。 **约束限制：**  不涉及。
        :type modified_by: str
        """
        
        

        self._id = None
        self._category = None
        self._label_type = None
        self._color = None
        self._title = None
        self._type = None
        self._state = None
        self._modified_by = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if category is not None:
            self.category = category
        if label_type is not None:
            self.label_type = label_type
        if color is not None:
            self.color = color
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if state is not None:
            self.state = state
        if modified_by is not None:
            self.modified_by = modified_by

    @property
    def id(self):
        r"""Gets the id of this WorkItemLabelVO.

        **参数解释：**  标签Id。 **约束限制：**  最小长度：18，最大长度：19。 **取值范围：**  不涉及。

        :return: The id of this WorkItemLabelVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WorkItemLabelVO.

        **参数解释：**  标签Id。 **约束限制：**  最小长度：18，最大长度：19。 **取值范围：**  不涉及。

        :param id: The id of this WorkItemLabelVO.
        :type id: str
        """
        self._id = id

    @property
    def category(self):
        r"""Gets the category of this WorkItemLabelVO.

        **参数解释：**  对象类型。 **约束限制：**  固定为Label，表示当前对象类型为标签。 **取值范围：**  不涉及。

        :return: The category of this WorkItemLabelVO.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this WorkItemLabelVO.

        **参数解释：**  对象类型。 **约束限制：**  固定为Label，表示当前对象类型为标签。 **取值范围：**  不涉及。

        :param category: The category of this WorkItemLabelVO.
        :type category: str
        """
        self._category = category

    @property
    def label_type(self):
        r"""Gets the label_type of this WorkItemLabelVO.

        **参数解释：**  标签所属的工作项的类别。 **取值范围：**  - requirement - raw requirement - bug - task - feature

        :return: The label_type of this WorkItemLabelVO.
        :rtype: str
        """
        return self._label_type

    @label_type.setter
    def label_type(self, label_type):
        r"""Sets the label_type of this WorkItemLabelVO.

        **参数解释：**  标签所属的工作项的类别。 **取值范围：**  - requirement - raw requirement - bug - task - feature

        :param label_type: The label_type of this WorkItemLabelVO.
        :type label_type: str
        """
        self._label_type = label_type

    @property
    def color(self):
        r"""Gets the color of this WorkItemLabelVO.

        **参数解释：**  标签颜色的RGB值。 **取值范围：**  - #86CAFF - #6DDEBB - #A6DD82 - #FAC20A  - #FA9841 - #F66F6A - #F3689A - #A97AF8 - #71757F - #5E7CE0 - #207AB3 - #169E6C - #6CA83B - #B58200 - #B54E04 - #B02121 - #AD215B - #572DB3 - #4F4F4F - #3C51A6

        :return: The color of this WorkItemLabelVO.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        r"""Sets the color of this WorkItemLabelVO.

        **参数解释：**  标签颜色的RGB值。 **取值范围：**  - #86CAFF - #6DDEBB - #A6DD82 - #FAC20A  - #FA9841 - #F66F6A - #F3689A - #A97AF8 - #71757F - #5E7CE0 - #207AB3 - #169E6C - #6CA83B - #B58200 - #B54E04 - #B02121 - #AD215B - #572DB3 - #4F4F4F - #3C51A6

        :param color: The color of this WorkItemLabelVO.
        :type color: str
        """
        self._color = color

    @property
    def title(self):
        r"""Gets the title of this WorkItemLabelVO.

        **参数解释：**  标签标题。 **约束限制：**  最小长度：1，最大长度：30。

        :return: The title of this WorkItemLabelVO.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this WorkItemLabelVO.

        **参数解释：**  标签标题。 **约束限制：**  最小长度：1，最大长度：30。

        :param title: The title of this WorkItemLabelVO.
        :type title: str
        """
        self._title = title

    @property
    def type(self):
        r"""Gets the type of this WorkItemLabelVO.

        **参数解释：**  表示当前对象数据类型为标签。 **约束限制：**  固定为label。 **取值范围：**  label。

        :return: The type of this WorkItemLabelVO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this WorkItemLabelVO.

        **参数解释：**  表示当前对象数据类型为标签。 **约束限制：**  固定为label。 **取值范围：**  label。

        :param type: The type of this WorkItemLabelVO.
        :type type: str
        """
        self._type = type

    @property
    def state(self):
        r"""Gets the state of this WorkItemLabelVO.

        **参数解释：**  标签的生命周期。 **取值范围：**  - 正在工作 - 作废 - 删除

        :return: The state of this WorkItemLabelVO.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this WorkItemLabelVO.

        **参数解释：**  标签的生命周期。 **取值范围：**  - 正在工作 - 作废 - 删除

        :param state: The state of this WorkItemLabelVO.
        :type state: str
        """
        self._state = state

    @property
    def modified_by(self):
        r"""Gets the modified_by of this WorkItemLabelVO.

        **参数解释：**  最近修改人。 **约束限制：**  不涉及。

        :return: The modified_by of this WorkItemLabelVO.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this WorkItemLabelVO.

        **参数解释：**  最近修改人。 **约束限制：**  不涉及。

        :param modified_by: The modified_by of this WorkItemLabelVO.
        :type modified_by: str
        """
        self._modified_by = modified_by

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
        if not isinstance(other, WorkItemLabelVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
