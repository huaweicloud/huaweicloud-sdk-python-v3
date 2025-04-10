# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataLayerVO:

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
        'level': 'int',
        'name': 'str',
        'type': 'LayerType',
        'description': 'str',
        'is_default': 'bool',
        'disabled_customized_field_ids': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'level': 'level',
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'is_default': 'is_default',
        'disabled_customized_field_ids': 'disabled_customized_field_ids'
    }

    def __init__(self, id=None, level=None, name=None, type=None, description=None, is_default=None, disabled_customized_field_ids=None):
        r"""DataLayerVO

        The model defined in huaweicloud sdk

        :param id: 数仓分层的ID，ID字符串。
        :type id: str
        :param level: 层级，从1开始。
        :type level: int
        :param name: 中文名称。
        :type name: str
        :param type: 
        :type type: :class:`huaweicloudsdkdataartsstudio.v1.LayerType`
        :param description: 数仓分层描述。
        :type description: str
        :param is_default: 是否是不可删除的默认分层，包含SDI\\DWR\\DM。
        :type is_default: bool
        :param disabled_customized_field_ids: 该分层禁用的自定义项的ID列表，包括表级自定义项和字段级自定义项。
        :type disabled_customized_field_ids: list[str]
        """
        
        

        self._id = None
        self._level = None
        self._name = None
        self._type = None
        self._description = None
        self._is_default = None
        self._disabled_customized_field_ids = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.level = level
        self.name = name
        self.type = type
        if description is not None:
            self.description = description
        if is_default is not None:
            self.is_default = is_default
        if disabled_customized_field_ids is not None:
            self.disabled_customized_field_ids = disabled_customized_field_ids

    @property
    def id(self):
        r"""Gets the id of this DataLayerVO.

        数仓分层的ID，ID字符串。

        :return: The id of this DataLayerVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DataLayerVO.

        数仓分层的ID，ID字符串。

        :param id: The id of this DataLayerVO.
        :type id: str
        """
        self._id = id

    @property
    def level(self):
        r"""Gets the level of this DataLayerVO.

        层级，从1开始。

        :return: The level of this DataLayerVO.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this DataLayerVO.

        层级，从1开始。

        :param level: The level of this DataLayerVO.
        :type level: int
        """
        self._level = level

    @property
    def name(self):
        r"""Gets the name of this DataLayerVO.

        中文名称。

        :return: The name of this DataLayerVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DataLayerVO.

        中文名称。

        :param name: The name of this DataLayerVO.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this DataLayerVO.

        :return: The type of this DataLayerVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.LayerType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DataLayerVO.

        :param type: The type of this DataLayerVO.
        :type type: :class:`huaweicloudsdkdataartsstudio.v1.LayerType`
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this DataLayerVO.

        数仓分层描述。

        :return: The description of this DataLayerVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DataLayerVO.

        数仓分层描述。

        :param description: The description of this DataLayerVO.
        :type description: str
        """
        self._description = description

    @property
    def is_default(self):
        r"""Gets the is_default of this DataLayerVO.

        是否是不可删除的默认分层，包含SDI\\DWR\\DM。

        :return: The is_default of this DataLayerVO.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        r"""Sets the is_default of this DataLayerVO.

        是否是不可删除的默认分层，包含SDI\\DWR\\DM。

        :param is_default: The is_default of this DataLayerVO.
        :type is_default: bool
        """
        self._is_default = is_default

    @property
    def disabled_customized_field_ids(self):
        r"""Gets the disabled_customized_field_ids of this DataLayerVO.

        该分层禁用的自定义项的ID列表，包括表级自定义项和字段级自定义项。

        :return: The disabled_customized_field_ids of this DataLayerVO.
        :rtype: list[str]
        """
        return self._disabled_customized_field_ids

    @disabled_customized_field_ids.setter
    def disabled_customized_field_ids(self, disabled_customized_field_ids):
        r"""Sets the disabled_customized_field_ids of this DataLayerVO.

        该分层禁用的自定义项的ID列表，包括表级自定义项和字段级自定义项。

        :param disabled_customized_field_ids: The disabled_customized_field_ids of this DataLayerVO.
        :type disabled_customized_field_ids: list[str]
        """
        self._disabled_customized_field_ids = disabled_customized_field_ids

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
        if not isinstance(other, DataLayerVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
