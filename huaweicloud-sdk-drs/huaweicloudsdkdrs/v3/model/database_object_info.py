# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseObjectInfo:

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
        'parent_id': 'str',
        'type': 'str',
        'name': 'str',
        'alias_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'parent_id': 'parent_id',
        'type': 'type',
        'name': 'name',
        'alias_name': 'alias_name'
    }

    def __init__(self, id=None, parent_id=None, type=None, name=None, alias_name=None):
        """DatabaseObjectInfo

        The model defined in huaweicloud sdk

        :param id: type为database时，为库名；type为table或者view时，字段值参考示例
        :type id: str
        :param parent_id: type为table或view时需要填写，为库名
        :type parent_id: str
        :param type: 类型。
        :type type: str
        :param name: 数据库对象名称，库名、表名、视图名
        :type name: str
        :param alias_name: 别名，映射的新名称
        :type alias_name: str
        """
        
        

        self._id = None
        self._parent_id = None
        self._type = None
        self._name = None
        self._alias_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if parent_id is not None:
            self.parent_id = parent_id
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if alias_name is not None:
            self.alias_name = alias_name

    @property
    def id(self):
        """Gets the id of this DatabaseObjectInfo.

        type为database时，为库名；type为table或者view时，字段值参考示例

        :return: The id of this DatabaseObjectInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatabaseObjectInfo.

        type为database时，为库名；type为table或者view时，字段值参考示例

        :param id: The id of this DatabaseObjectInfo.
        :type id: str
        """
        self._id = id

    @property
    def parent_id(self):
        """Gets the parent_id of this DatabaseObjectInfo.

        type为table或view时需要填写，为库名

        :return: The parent_id of this DatabaseObjectInfo.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this DatabaseObjectInfo.

        type为table或view时需要填写，为库名

        :param parent_id: The parent_id of this DatabaseObjectInfo.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def type(self):
        """Gets the type of this DatabaseObjectInfo.

        类型。

        :return: The type of this DatabaseObjectInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DatabaseObjectInfo.

        类型。

        :param type: The type of this DatabaseObjectInfo.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this DatabaseObjectInfo.

        数据库对象名称，库名、表名、视图名

        :return: The name of this DatabaseObjectInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatabaseObjectInfo.

        数据库对象名称，库名、表名、视图名

        :param name: The name of this DatabaseObjectInfo.
        :type name: str
        """
        self._name = name

    @property
    def alias_name(self):
        """Gets the alias_name of this DatabaseObjectInfo.

        别名，映射的新名称

        :return: The alias_name of this DatabaseObjectInfo.
        :rtype: str
        """
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        """Sets the alias_name of this DatabaseObjectInfo.

        别名，映射的新名称

        :param alias_name: The alias_name of this DatabaseObjectInfo.
        :type alias_name: str
        """
        self._alias_name = alias_name

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
        if not isinstance(other, DatabaseObjectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
