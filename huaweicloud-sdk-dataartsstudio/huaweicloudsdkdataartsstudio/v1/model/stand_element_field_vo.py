# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StandElementFieldVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fd_name': 'str',
        'fd_name_en': 'str',
        'description': 'str',
        'description_en': 'str',
        'label': 'str',
        'disabled': 'bool',
        'id': 'str',
        'actived': 'bool',
        'required': 'bool',
        'searchable': 'bool',
        'optional_values': 'str',
        'field_type': 'int',
        'displayed_name': 'str',
        'displayed_name_en': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'create_by': 'str',
        'update_by': 'str'
    }

    attribute_map = {
        'fd_name': 'fd_name',
        'fd_name_en': 'fd_name_en',
        'description': 'description',
        'description_en': 'descriptionEn',
        'label': 'label',
        'disabled': 'disabled',
        'id': 'id',
        'actived': 'actived',
        'required': 'required',
        'searchable': 'searchable',
        'optional_values': 'optional_values',
        'field_type': 'field_type',
        'displayed_name': 'displayed_name',
        'displayed_name_en': 'displayed_name_en',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'create_by': 'create_by',
        'update_by': 'update_by'
    }

    def __init__(self, fd_name=None, fd_name_en=None, description=None, description_en=None, label=None, disabled=None, id=None, actived=None, required=None, searchable=None, optional_values=None, field_type=None, displayed_name=None, displayed_name_en=None, create_time=None, update_time=None, create_by=None, update_by=None):
        r"""StandElementFieldVO

        The model defined in huaweicloud sdk

        :param fd_name: 属性名称。
        :type fd_name: str
        :param fd_name_en: 属性英文名称。
        :type fd_name_en: str
        :param description: 属性描述。
        :type description: str
        :param description_en: 属性英文描述。
        :type description_en: str
        :param label: 属性标签。
        :type label: str
        :param disabled: 是否禁用。
        :type disabled: bool
        :param id: 数据标准ID，ID字符串。
        :type id: str
        :param actived: 是否显示，系统默认项必然显示不允许修改。true表示使用数据标准时体现（增改查的时候可以操作该属性），false表示使用数据标准时不体现。
        :type actived: bool
        :param required: 是否必填。true：必填，false：非必填。
        :type required: bool
        :param searchable: 是否可搜索。true表示在数据标准列表页面可搜索，false表示在数据标准列表页面不可搜索。
        :type searchable: bool
        :param optional_values: 允许值。
        :type optional_values: str
        :param field_type: 字段类型，0表示系统字段， 1表示自定义字段。
        :type field_type: int
        :param displayed_name: 前端展示名。
        :type displayed_name: str
        :param displayed_name_en: 前端展示名英文。
        :type displayed_name_en: str
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        :param create_by: 创建人。
        :type create_by: str
        :param update_by: 更新人。
        :type update_by: str
        """
        
        

        self._fd_name = None
        self._fd_name_en = None
        self._description = None
        self._description_en = None
        self._label = None
        self._disabled = None
        self._id = None
        self._actived = None
        self._required = None
        self._searchable = None
        self._optional_values = None
        self._field_type = None
        self._displayed_name = None
        self._displayed_name_en = None
        self._create_time = None
        self._update_time = None
        self._create_by = None
        self._update_by = None
        self.discriminator = None

        self.fd_name = fd_name
        if fd_name_en is not None:
            self.fd_name_en = fd_name_en
        if description is not None:
            self.description = description
        if description_en is not None:
            self.description_en = description_en
        if label is not None:
            self.label = label
        if disabled is not None:
            self.disabled = disabled
        if id is not None:
            self.id = id
        self.actived = actived
        if required is not None:
            self.required = required
        if searchable is not None:
            self.searchable = searchable
        if optional_values is not None:
            self.optional_values = optional_values
        if field_type is not None:
            self.field_type = field_type
        if displayed_name is not None:
            self.displayed_name = displayed_name
        if displayed_name_en is not None:
            self.displayed_name_en = displayed_name_en
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by

    @property
    def fd_name(self):
        r"""Gets the fd_name of this StandElementFieldVO.

        属性名称。

        :return: The fd_name of this StandElementFieldVO.
        :rtype: str
        """
        return self._fd_name

    @fd_name.setter
    def fd_name(self, fd_name):
        r"""Sets the fd_name of this StandElementFieldVO.

        属性名称。

        :param fd_name: The fd_name of this StandElementFieldVO.
        :type fd_name: str
        """
        self._fd_name = fd_name

    @property
    def fd_name_en(self):
        r"""Gets the fd_name_en of this StandElementFieldVO.

        属性英文名称。

        :return: The fd_name_en of this StandElementFieldVO.
        :rtype: str
        """
        return self._fd_name_en

    @fd_name_en.setter
    def fd_name_en(self, fd_name_en):
        r"""Sets the fd_name_en of this StandElementFieldVO.

        属性英文名称。

        :param fd_name_en: The fd_name_en of this StandElementFieldVO.
        :type fd_name_en: str
        """
        self._fd_name_en = fd_name_en

    @property
    def description(self):
        r"""Gets the description of this StandElementFieldVO.

        属性描述。

        :return: The description of this StandElementFieldVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this StandElementFieldVO.

        属性描述。

        :param description: The description of this StandElementFieldVO.
        :type description: str
        """
        self._description = description

    @property
    def description_en(self):
        r"""Gets the description_en of this StandElementFieldVO.

        属性英文描述。

        :return: The description_en of this StandElementFieldVO.
        :rtype: str
        """
        return self._description_en

    @description_en.setter
    def description_en(self, description_en):
        r"""Sets the description_en of this StandElementFieldVO.

        属性英文描述。

        :param description_en: The description_en of this StandElementFieldVO.
        :type description_en: str
        """
        self._description_en = description_en

    @property
    def label(self):
        r"""Gets the label of this StandElementFieldVO.

        属性标签。

        :return: The label of this StandElementFieldVO.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this StandElementFieldVO.

        属性标签。

        :param label: The label of this StandElementFieldVO.
        :type label: str
        """
        self._label = label

    @property
    def disabled(self):
        r"""Gets the disabled of this StandElementFieldVO.

        是否禁用。

        :return: The disabled of this StandElementFieldVO.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        r"""Sets the disabled of this StandElementFieldVO.

        是否禁用。

        :param disabled: The disabled of this StandElementFieldVO.
        :type disabled: bool
        """
        self._disabled = disabled

    @property
    def id(self):
        r"""Gets the id of this StandElementFieldVO.

        数据标准ID，ID字符串。

        :return: The id of this StandElementFieldVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StandElementFieldVO.

        数据标准ID，ID字符串。

        :param id: The id of this StandElementFieldVO.
        :type id: str
        """
        self._id = id

    @property
    def actived(self):
        r"""Gets the actived of this StandElementFieldVO.

        是否显示，系统默认项必然显示不允许修改。true表示使用数据标准时体现（增改查的时候可以操作该属性），false表示使用数据标准时不体现。

        :return: The actived of this StandElementFieldVO.
        :rtype: bool
        """
        return self._actived

    @actived.setter
    def actived(self, actived):
        r"""Sets the actived of this StandElementFieldVO.

        是否显示，系统默认项必然显示不允许修改。true表示使用数据标准时体现（增改查的时候可以操作该属性），false表示使用数据标准时不体现。

        :param actived: The actived of this StandElementFieldVO.
        :type actived: bool
        """
        self._actived = actived

    @property
    def required(self):
        r"""Gets the required of this StandElementFieldVO.

        是否必填。true：必填，false：非必填。

        :return: The required of this StandElementFieldVO.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        r"""Sets the required of this StandElementFieldVO.

        是否必填。true：必填，false：非必填。

        :param required: The required of this StandElementFieldVO.
        :type required: bool
        """
        self._required = required

    @property
    def searchable(self):
        r"""Gets the searchable of this StandElementFieldVO.

        是否可搜索。true表示在数据标准列表页面可搜索，false表示在数据标准列表页面不可搜索。

        :return: The searchable of this StandElementFieldVO.
        :rtype: bool
        """
        return self._searchable

    @searchable.setter
    def searchable(self, searchable):
        r"""Sets the searchable of this StandElementFieldVO.

        是否可搜索。true表示在数据标准列表页面可搜索，false表示在数据标准列表页面不可搜索。

        :param searchable: The searchable of this StandElementFieldVO.
        :type searchable: bool
        """
        self._searchable = searchable

    @property
    def optional_values(self):
        r"""Gets the optional_values of this StandElementFieldVO.

        允许值。

        :return: The optional_values of this StandElementFieldVO.
        :rtype: str
        """
        return self._optional_values

    @optional_values.setter
    def optional_values(self, optional_values):
        r"""Sets the optional_values of this StandElementFieldVO.

        允许值。

        :param optional_values: The optional_values of this StandElementFieldVO.
        :type optional_values: str
        """
        self._optional_values = optional_values

    @property
    def field_type(self):
        r"""Gets the field_type of this StandElementFieldVO.

        字段类型，0表示系统字段， 1表示自定义字段。

        :return: The field_type of this StandElementFieldVO.
        :rtype: int
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        r"""Sets the field_type of this StandElementFieldVO.

        字段类型，0表示系统字段， 1表示自定义字段。

        :param field_type: The field_type of this StandElementFieldVO.
        :type field_type: int
        """
        self._field_type = field_type

    @property
    def displayed_name(self):
        r"""Gets the displayed_name of this StandElementFieldVO.

        前端展示名。

        :return: The displayed_name of this StandElementFieldVO.
        :rtype: str
        """
        return self._displayed_name

    @displayed_name.setter
    def displayed_name(self, displayed_name):
        r"""Sets the displayed_name of this StandElementFieldVO.

        前端展示名。

        :param displayed_name: The displayed_name of this StandElementFieldVO.
        :type displayed_name: str
        """
        self._displayed_name = displayed_name

    @property
    def displayed_name_en(self):
        r"""Gets the displayed_name_en of this StandElementFieldVO.

        前端展示名英文。

        :return: The displayed_name_en of this StandElementFieldVO.
        :rtype: str
        """
        return self._displayed_name_en

    @displayed_name_en.setter
    def displayed_name_en(self, displayed_name_en):
        r"""Sets the displayed_name_en of this StandElementFieldVO.

        前端展示名英文。

        :param displayed_name_en: The displayed_name_en of this StandElementFieldVO.
        :type displayed_name_en: str
        """
        self._displayed_name_en = displayed_name_en

    @property
    def create_time(self):
        r"""Gets the create_time of this StandElementFieldVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this StandElementFieldVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this StandElementFieldVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this StandElementFieldVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this StandElementFieldVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this StandElementFieldVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this StandElementFieldVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this StandElementFieldVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def create_by(self):
        r"""Gets the create_by of this StandElementFieldVO.

        创建人。

        :return: The create_by of this StandElementFieldVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this StandElementFieldVO.

        创建人。

        :param create_by: The create_by of this StandElementFieldVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        r"""Gets the update_by of this StandElementFieldVO.

        更新人。

        :return: The update_by of this StandElementFieldVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this StandElementFieldVO.

        更新人。

        :param update_by: The update_by of this StandElementFieldVO.
        :type update_by: str
        """
        self._update_by = update_by

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StandElementFieldVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
