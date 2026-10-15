# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataFilterObjectInfo:

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
        'object_name': 'str',
        'object_alias_name': 'str',
        'object_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'parent_id': 'parent_id',
        'object_name': 'object_name',
        'object_alias_name': 'object_alias_name',
        'object_type': 'object_type'
    }

    def __init__(self, id=None, parent_id=None, object_name=None, object_alias_name=None, object_type=None):
        r"""DataFilterObjectInfo

        The model defined in huaweicloud sdk

        :param id: 数据过滤对象的唯一标识。用于标识待过滤的数据库对象，填写格式为层级路径形式。 约束：填写格式为以下三种之一：库名-*-*-表名、schema名-*-*-表名、库名-*-*-schema名-*-*-表名。
        :type id: str
        :param parent_id: 数据过滤对象的父级对象标识。用于标识当前过滤对象所属的上级数据库对象（库或Schema）。 约束：填写格式为以下三种之一：库名、schema名、库名-*-*-schema名。
        :type parent_id: str
        :param object_name: 数据过滤对象的名称。即当前需要进行过滤操作的具体数据库表名。
        :type object_name: str
        :param object_alias_name: 数据过滤对象映射名称
        :type object_alias_name: str
        :param object_type: 数据过滤对象的类型。标识当前过滤对象的数据库对象类型，如表、视图、存储过程等。
        :type object_type: str
        """
        
        

        self._id = None
        self._parent_id = None
        self._object_name = None
        self._object_alias_name = None
        self._object_type = None
        self.discriminator = None

        self.id = id
        self.parent_id = parent_id
        self.object_name = object_name
        if object_alias_name is not None:
            self.object_alias_name = object_alias_name
        if object_type is not None:
            self.object_type = object_type

    @property
    def id(self):
        r"""Gets the id of this DataFilterObjectInfo.

        数据过滤对象的唯一标识。用于标识待过滤的数据库对象，填写格式为层级路径形式。 约束：填写格式为以下三种之一：库名-*-*-表名、schema名-*-*-表名、库名-*-*-schema名-*-*-表名。

        :return: The id of this DataFilterObjectInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DataFilterObjectInfo.

        数据过滤对象的唯一标识。用于标识待过滤的数据库对象，填写格式为层级路径形式。 约束：填写格式为以下三种之一：库名-*-*-表名、schema名-*-*-表名、库名-*-*-schema名-*-*-表名。

        :param id: The id of this DataFilterObjectInfo.
        :type id: str
        """
        self._id = id

    @property
    def parent_id(self):
        r"""Gets the parent_id of this DataFilterObjectInfo.

        数据过滤对象的父级对象标识。用于标识当前过滤对象所属的上级数据库对象（库或Schema）。 约束：填写格式为以下三种之一：库名、schema名、库名-*-*-schema名。

        :return: The parent_id of this DataFilterObjectInfo.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this DataFilterObjectInfo.

        数据过滤对象的父级对象标识。用于标识当前过滤对象所属的上级数据库对象（库或Schema）。 约束：填写格式为以下三种之一：库名、schema名、库名-*-*-schema名。

        :param parent_id: The parent_id of this DataFilterObjectInfo.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def object_name(self):
        r"""Gets the object_name of this DataFilterObjectInfo.

        数据过滤对象的名称。即当前需要进行过滤操作的具体数据库表名。

        :return: The object_name of this DataFilterObjectInfo.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        r"""Sets the object_name of this DataFilterObjectInfo.

        数据过滤对象的名称。即当前需要进行过滤操作的具体数据库表名。

        :param object_name: The object_name of this DataFilterObjectInfo.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def object_alias_name(self):
        r"""Gets the object_alias_name of this DataFilterObjectInfo.

        数据过滤对象映射名称

        :return: The object_alias_name of this DataFilterObjectInfo.
        :rtype: str
        """
        return self._object_alias_name

    @object_alias_name.setter
    def object_alias_name(self, object_alias_name):
        r"""Sets the object_alias_name of this DataFilterObjectInfo.

        数据过滤对象映射名称

        :param object_alias_name: The object_alias_name of this DataFilterObjectInfo.
        :type object_alias_name: str
        """
        self._object_alias_name = object_alias_name

    @property
    def object_type(self):
        r"""Gets the object_type of this DataFilterObjectInfo.

        数据过滤对象的类型。标识当前过滤对象的数据库对象类型，如表、视图、存储过程等。

        :return: The object_type of this DataFilterObjectInfo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this DataFilterObjectInfo.

        数据过滤对象的类型。标识当前过滤对象的数据库对象类型，如表、视图、存储过程等。

        :param object_type: The object_type of this DataFilterObjectInfo.
        :type object_type: str
        """
        self._object_type = object_type

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
        if not isinstance(other, DataFilterObjectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
