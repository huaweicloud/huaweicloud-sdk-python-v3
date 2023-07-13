# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubjectParamsVO:

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
        'description': 'str',
        'alias': 'str',
        'data_owner': 'str',
        'data_owner_list': 'str',
        'level': 'int',
        'parent_id': 'int',
        'self_defined_fields': 'list[SelfDefinedFieldVO]'
    }

    attribute_map = {
        'id': 'id',
        'name_ch': 'name_ch',
        'name_en': 'name_en',
        'description': 'description',
        'alias': 'alias',
        'data_owner': 'data_owner',
        'data_owner_list': 'data_owner_list',
        'level': 'level',
        'parent_id': 'parent_id',
        'self_defined_fields': 'self_defined_fields'
    }

    def __init__(self, id=None, name_ch=None, name_en=None, description=None, alias=None, data_owner=None, data_owner_list=None, level=None, parent_id=None, self_defined_fields=None):
        """SubjectParamsVO

        The model defined in huaweicloud sdk

        :param id: 编码。更新时必填，创建时可以为空
        :type id: int
        :param name_ch: 中文名称
        :type name_ch: str
        :param name_en: 英文名称
        :type name_en: str
        :param description: 描述信息, 业务对象必填
        :type description: str
        :param alias: 别名
        :type alias: str
        :param data_owner: 数据owner部门
        :type data_owner: str
        :param data_owner_list: 数据owner人员
        :type data_owner_list: str
        :param level: 层级
        :type level: int
        :param parent_id: 上层主题id，首层则为空
        :type parent_id: int
        :param self_defined_fields: 属性自定义项
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        
        

        self._id = None
        self._name_ch = None
        self._name_en = None
        self._description = None
        self._alias = None
        self._data_owner = None
        self._data_owner_list = None
        self._level = None
        self._parent_id = None
        self._self_defined_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name_ch = name_ch
        self.name_en = name_en
        if description is not None:
            self.description = description
        if alias is not None:
            self.alias = alias
        if data_owner is not None:
            self.data_owner = data_owner
        self.data_owner_list = data_owner_list
        self.level = level
        if parent_id is not None:
            self.parent_id = parent_id
        if self_defined_fields is not None:
            self.self_defined_fields = self_defined_fields

    @property
    def id(self):
        """Gets the id of this SubjectParamsVO.

        编码。更新时必填，创建时可以为空

        :return: The id of this SubjectParamsVO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubjectParamsVO.

        编码。更新时必填，创建时可以为空

        :param id: The id of this SubjectParamsVO.
        :type id: int
        """
        self._id = id

    @property
    def name_ch(self):
        """Gets the name_ch of this SubjectParamsVO.

        中文名称

        :return: The name_ch of this SubjectParamsVO.
        :rtype: str
        """
        return self._name_ch

    @name_ch.setter
    def name_ch(self, name_ch):
        """Sets the name_ch of this SubjectParamsVO.

        中文名称

        :param name_ch: The name_ch of this SubjectParamsVO.
        :type name_ch: str
        """
        self._name_ch = name_ch

    @property
    def name_en(self):
        """Gets the name_en of this SubjectParamsVO.

        英文名称

        :return: The name_en of this SubjectParamsVO.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this SubjectParamsVO.

        英文名称

        :param name_en: The name_en of this SubjectParamsVO.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def description(self):
        """Gets the description of this SubjectParamsVO.

        描述信息, 业务对象必填

        :return: The description of this SubjectParamsVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SubjectParamsVO.

        描述信息, 业务对象必填

        :param description: The description of this SubjectParamsVO.
        :type description: str
        """
        self._description = description

    @property
    def alias(self):
        """Gets the alias of this SubjectParamsVO.

        别名

        :return: The alias of this SubjectParamsVO.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this SubjectParamsVO.

        别名

        :param alias: The alias of this SubjectParamsVO.
        :type alias: str
        """
        self._alias = alias

    @property
    def data_owner(self):
        """Gets the data_owner of this SubjectParamsVO.

        数据owner部门

        :return: The data_owner of this SubjectParamsVO.
        :rtype: str
        """
        return self._data_owner

    @data_owner.setter
    def data_owner(self, data_owner):
        """Sets the data_owner of this SubjectParamsVO.

        数据owner部门

        :param data_owner: The data_owner of this SubjectParamsVO.
        :type data_owner: str
        """
        self._data_owner = data_owner

    @property
    def data_owner_list(self):
        """Gets the data_owner_list of this SubjectParamsVO.

        数据owner人员

        :return: The data_owner_list of this SubjectParamsVO.
        :rtype: str
        """
        return self._data_owner_list

    @data_owner_list.setter
    def data_owner_list(self, data_owner_list):
        """Sets the data_owner_list of this SubjectParamsVO.

        数据owner人员

        :param data_owner_list: The data_owner_list of this SubjectParamsVO.
        :type data_owner_list: str
        """
        self._data_owner_list = data_owner_list

    @property
    def level(self):
        """Gets the level of this SubjectParamsVO.

        层级

        :return: The level of this SubjectParamsVO.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this SubjectParamsVO.

        层级

        :param level: The level of this SubjectParamsVO.
        :type level: int
        """
        self._level = level

    @property
    def parent_id(self):
        """Gets the parent_id of this SubjectParamsVO.

        上层主题id，首层则为空

        :return: The parent_id of this SubjectParamsVO.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this SubjectParamsVO.

        上层主题id，首层则为空

        :param parent_id: The parent_id of this SubjectParamsVO.
        :type parent_id: int
        """
        self._parent_id = parent_id

    @property
    def self_defined_fields(self):
        """Gets the self_defined_fields of this SubjectParamsVO.

        属性自定义项

        :return: The self_defined_fields of this SubjectParamsVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        return self._self_defined_fields

    @self_defined_fields.setter
    def self_defined_fields(self, self_defined_fields):
        """Sets the self_defined_fields of this SubjectParamsVO.

        属性自定义项

        :param self_defined_fields: The self_defined_fields of this SubjectParamsVO.
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        self._self_defined_fields = self_defined_fields

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
        if not isinstance(other, SubjectParamsVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
