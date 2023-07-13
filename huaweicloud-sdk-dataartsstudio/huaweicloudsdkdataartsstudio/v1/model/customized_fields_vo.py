# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomizedFieldsVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name_ch': 'str',
        'name_en': 'str',
        'not_null': 'bool',
        'optional_values': 'str',
        'type': 'str',
        'ordinal': 'int',
        'description': 'str',
        'create_by': 'str',
        'update_by': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name_ch': 'name_ch',
        'name_en': 'name_en',
        'not_null': 'not_null',
        'optional_values': 'optional_values',
        'type': 'type',
        'ordinal': 'ordinal',
        'description': 'description',
        'create_by': 'create_by',
        'update_by': 'update_by',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name_ch=None, name_en=None, not_null=None, optional_values=None, type=None, ordinal=None, description=None, create_by=None, update_by=None, create_time=None, update_time=None):
        """CustomizedFieldsVO

        The model defined in huaweicloud sdk

        :param id: 编码
        :type id: int
        :param name_ch: 中文名称
        :type name_ch: str
        :param name_en: 英文名称
        :type name_en: str
        :param not_null: 是否必填
        :type not_null: bool
        :param optional_values: 可选值。分号分隔
        :type optional_values: str
        :param type: 自定义项类型：TABLE, ATTRIBUTE, SUBJECT, METRIC
        :type type: str
        :param ordinal: 顺序
        :type ordinal: int
        :param description: 描述
        :type description: str
        :param create_by: 创建人
        :type create_by: str
        :param update_by: 更新人
        :type update_by: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param update_time: 更新时间
        :type update_time: datetime
        """
        
        

        self._id = None
        self._name_ch = None
        self._name_en = None
        self._not_null = None
        self._optional_values = None
        self._type = None
        self._ordinal = None
        self._description = None
        self._create_by = None
        self._update_by = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name_ch = name_ch
        self.name_en = name_en
        self.not_null = not_null
        if optional_values is not None:
            self.optional_values = optional_values
        self.type = type
        if ordinal is not None:
            self.ordinal = ordinal
        if description is not None:
            self.description = description
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this CustomizedFieldsVO.

        编码

        :return: The id of this CustomizedFieldsVO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomizedFieldsVO.

        编码

        :param id: The id of this CustomizedFieldsVO.
        :type id: int
        """
        self._id = id

    @property
    def name_ch(self):
        """Gets the name_ch of this CustomizedFieldsVO.

        中文名称

        :return: The name_ch of this CustomizedFieldsVO.
        :rtype: str
        """
        return self._name_ch

    @name_ch.setter
    def name_ch(self, name_ch):
        """Sets the name_ch of this CustomizedFieldsVO.

        中文名称

        :param name_ch: The name_ch of this CustomizedFieldsVO.
        :type name_ch: str
        """
        self._name_ch = name_ch

    @property
    def name_en(self):
        """Gets the name_en of this CustomizedFieldsVO.

        英文名称

        :return: The name_en of this CustomizedFieldsVO.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this CustomizedFieldsVO.

        英文名称

        :param name_en: The name_en of this CustomizedFieldsVO.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def not_null(self):
        """Gets the not_null of this CustomizedFieldsVO.

        是否必填

        :return: The not_null of this CustomizedFieldsVO.
        :rtype: bool
        """
        return self._not_null

    @not_null.setter
    def not_null(self, not_null):
        """Sets the not_null of this CustomizedFieldsVO.

        是否必填

        :param not_null: The not_null of this CustomizedFieldsVO.
        :type not_null: bool
        """
        self._not_null = not_null

    @property
    def optional_values(self):
        """Gets the optional_values of this CustomizedFieldsVO.

        可选值。分号分隔

        :return: The optional_values of this CustomizedFieldsVO.
        :rtype: str
        """
        return self._optional_values

    @optional_values.setter
    def optional_values(self, optional_values):
        """Sets the optional_values of this CustomizedFieldsVO.

        可选值。分号分隔

        :param optional_values: The optional_values of this CustomizedFieldsVO.
        :type optional_values: str
        """
        self._optional_values = optional_values

    @property
    def type(self):
        """Gets the type of this CustomizedFieldsVO.

        自定义项类型：TABLE, ATTRIBUTE, SUBJECT, METRIC

        :return: The type of this CustomizedFieldsVO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CustomizedFieldsVO.

        自定义项类型：TABLE, ATTRIBUTE, SUBJECT, METRIC

        :param type: The type of this CustomizedFieldsVO.
        :type type: str
        """
        self._type = type

    @property
    def ordinal(self):
        """Gets the ordinal of this CustomizedFieldsVO.

        顺序

        :return: The ordinal of this CustomizedFieldsVO.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        """Sets the ordinal of this CustomizedFieldsVO.

        顺序

        :param ordinal: The ordinal of this CustomizedFieldsVO.
        :type ordinal: int
        """
        self._ordinal = ordinal

    @property
    def description(self):
        """Gets the description of this CustomizedFieldsVO.

        描述

        :return: The description of this CustomizedFieldsVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomizedFieldsVO.

        描述

        :param description: The description of this CustomizedFieldsVO.
        :type description: str
        """
        self._description = description

    @property
    def create_by(self):
        """Gets the create_by of this CustomizedFieldsVO.

        创建人

        :return: The create_by of this CustomizedFieldsVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this CustomizedFieldsVO.

        创建人

        :param create_by: The create_by of this CustomizedFieldsVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        """Gets the update_by of this CustomizedFieldsVO.

        更新人

        :return: The update_by of this CustomizedFieldsVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this CustomizedFieldsVO.

        更新人

        :param update_by: The update_by of this CustomizedFieldsVO.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def create_time(self):
        """Gets the create_time of this CustomizedFieldsVO.

        创建时间

        :return: The create_time of this CustomizedFieldsVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CustomizedFieldsVO.

        创建时间

        :param create_time: The create_time of this CustomizedFieldsVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this CustomizedFieldsVO.

        更新时间

        :return: The update_time of this CustomizedFieldsVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CustomizedFieldsVO.

        更新时间

        :param update_time: The update_time of this CustomizedFieldsVO.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, CustomizedFieldsVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
