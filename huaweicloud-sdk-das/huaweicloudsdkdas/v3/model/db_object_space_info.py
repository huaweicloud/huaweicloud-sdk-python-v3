# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DbObjectSpaceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'object_type': 'str',
        'object_name': 'str',
        'object_id': 'str',
        'used_size': 'int',
        'data_size': 'int',
        'index_size': 'int',
        'estimated_rows': 'int'
    }

    attribute_map = {
        'object_type': 'object_type',
        'object_name': 'object_name',
        'object_id': 'object_id',
        'used_size': 'used_size',
        'data_size': 'data_size',
        'index_size': 'index_size',
        'estimated_rows': 'estimated_rows'
    }

    def __init__(self, object_type=None, object_name=None, object_id=None, used_size=None, data_size=None, index_size=None, estimated_rows=None):
        """DbObjectSpaceInfo

        The model defined in huaweicloud sdk

        :param object_type: 对象类型，如果是table，同时需要传database_id
        :type object_type: str
        :param object_name: 对象名称
        :type object_name: str
        :param object_id: 对象ID
        :type object_id: str
        :param used_size: 已使用空间，以字节为单位
        :type used_size: int
        :param data_size: 数据空间，以字节为单位
        :type data_size: int
        :param index_size: 索引空间，以字节为单位
        :type index_size: int
        :param estimated_rows: 估算值行数，以字节为单位
        :type estimated_rows: int
        """
        
        

        self._object_type = None
        self._object_name = None
        self._object_id = None
        self._used_size = None
        self._data_size = None
        self._index_size = None
        self._estimated_rows = None
        self.discriminator = None

        self.object_type = object_type
        self.object_name = object_name
        if object_id is not None:
            self.object_id = object_id
        if used_size is not None:
            self.used_size = used_size
        if data_size is not None:
            self.data_size = data_size
        if index_size is not None:
            self.index_size = index_size
        if estimated_rows is not None:
            self.estimated_rows = estimated_rows

    @property
    def object_type(self):
        """Gets the object_type of this DbObjectSpaceInfo.

        对象类型，如果是table，同时需要传database_id

        :return: The object_type of this DbObjectSpaceInfo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this DbObjectSpaceInfo.

        对象类型，如果是table，同时需要传database_id

        :param object_type: The object_type of this DbObjectSpaceInfo.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def object_name(self):
        """Gets the object_name of this DbObjectSpaceInfo.

        对象名称

        :return: The object_name of this DbObjectSpaceInfo.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """Sets the object_name of this DbObjectSpaceInfo.

        对象名称

        :param object_name: The object_name of this DbObjectSpaceInfo.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def object_id(self):
        """Gets the object_id of this DbObjectSpaceInfo.

        对象ID

        :return: The object_id of this DbObjectSpaceInfo.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this DbObjectSpaceInfo.

        对象ID

        :param object_id: The object_id of this DbObjectSpaceInfo.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def used_size(self):
        """Gets the used_size of this DbObjectSpaceInfo.

        已使用空间，以字节为单位

        :return: The used_size of this DbObjectSpaceInfo.
        :rtype: int
        """
        return self._used_size

    @used_size.setter
    def used_size(self, used_size):
        """Sets the used_size of this DbObjectSpaceInfo.

        已使用空间，以字节为单位

        :param used_size: The used_size of this DbObjectSpaceInfo.
        :type used_size: int
        """
        self._used_size = used_size

    @property
    def data_size(self):
        """Gets the data_size of this DbObjectSpaceInfo.

        数据空间，以字节为单位

        :return: The data_size of this DbObjectSpaceInfo.
        :rtype: int
        """
        return self._data_size

    @data_size.setter
    def data_size(self, data_size):
        """Sets the data_size of this DbObjectSpaceInfo.

        数据空间，以字节为单位

        :param data_size: The data_size of this DbObjectSpaceInfo.
        :type data_size: int
        """
        self._data_size = data_size

    @property
    def index_size(self):
        """Gets the index_size of this DbObjectSpaceInfo.

        索引空间，以字节为单位

        :return: The index_size of this DbObjectSpaceInfo.
        :rtype: int
        """
        return self._index_size

    @index_size.setter
    def index_size(self, index_size):
        """Sets the index_size of this DbObjectSpaceInfo.

        索引空间，以字节为单位

        :param index_size: The index_size of this DbObjectSpaceInfo.
        :type index_size: int
        """
        self._index_size = index_size

    @property
    def estimated_rows(self):
        """Gets the estimated_rows of this DbObjectSpaceInfo.

        估算值行数，以字节为单位

        :return: The estimated_rows of this DbObjectSpaceInfo.
        :rtype: int
        """
        return self._estimated_rows

    @estimated_rows.setter
    def estimated_rows(self, estimated_rows):
        """Sets the estimated_rows of this DbObjectSpaceInfo.

        估算值行数，以字节为单位

        :param estimated_rows: The estimated_rows of this DbObjectSpaceInfo.
        :type estimated_rows: int
        """
        self._estimated_rows = estimated_rows

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
        if not isinstance(other, DbObjectSpaceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
