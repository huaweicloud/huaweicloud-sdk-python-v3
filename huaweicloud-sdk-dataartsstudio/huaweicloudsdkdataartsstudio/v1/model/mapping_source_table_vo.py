# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MappingSourceTableVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table1_id': 'str',
        'table2_id': 'str',
        'table1_name': 'str',
        'table2_name': 'str',
        'join_type': 'str',
        'join_fields': 'list[MappingJoinFieldVO]'
    }

    attribute_map = {
        'table1_id': 'table1_id',
        'table2_id': 'table2_id',
        'table1_name': 'table1_name',
        'table2_name': 'table2_name',
        'join_type': 'join_type',
        'join_fields': 'join_fields'
    }

    def __init__(self, table1_id=None, table2_id=None, table1_name=None, table2_name=None, join_type=None, join_fields=None):
        """MappingSourceTableVO

        The model defined in huaweicloud sdk

        :param table1_id: 表1ID，填写String类型替代Long类型。
        :type table1_id: str
        :param table2_id: 表2ID，填写String类型替代Long类型。
        :type table2_id: str
        :param table1_name: 表1名称。
        :type table1_name: str
        :param table2_name: 表2名称。
        :type table2_name: str
        :param join_type: 关联类型。 枚举值：   - LEFT: 左外连接   - RIGHT: 右外连接   - INNER: 内连接   - FULL: 全连接 
        :type join_type: str
        :param join_fields: on条件。
        :type join_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.MappingJoinFieldVO`]
        """
        
        

        self._table1_id = None
        self._table2_id = None
        self._table1_name = None
        self._table2_name = None
        self._join_type = None
        self._join_fields = None
        self.discriminator = None

        self.table1_id = table1_id
        if table2_id is not None:
            self.table2_id = table2_id
        self.table1_name = table1_name
        if table2_name is not None:
            self.table2_name = table2_name
        self.join_type = join_type
        self.join_fields = join_fields

    @property
    def table1_id(self):
        """Gets the table1_id of this MappingSourceTableVO.

        表1ID，填写String类型替代Long类型。

        :return: The table1_id of this MappingSourceTableVO.
        :rtype: str
        """
        return self._table1_id

    @table1_id.setter
    def table1_id(self, table1_id):
        """Sets the table1_id of this MappingSourceTableVO.

        表1ID，填写String类型替代Long类型。

        :param table1_id: The table1_id of this MappingSourceTableVO.
        :type table1_id: str
        """
        self._table1_id = table1_id

    @property
    def table2_id(self):
        """Gets the table2_id of this MappingSourceTableVO.

        表2ID，填写String类型替代Long类型。

        :return: The table2_id of this MappingSourceTableVO.
        :rtype: str
        """
        return self._table2_id

    @table2_id.setter
    def table2_id(self, table2_id):
        """Sets the table2_id of this MappingSourceTableVO.

        表2ID，填写String类型替代Long类型。

        :param table2_id: The table2_id of this MappingSourceTableVO.
        :type table2_id: str
        """
        self._table2_id = table2_id

    @property
    def table1_name(self):
        """Gets the table1_name of this MappingSourceTableVO.

        表1名称。

        :return: The table1_name of this MappingSourceTableVO.
        :rtype: str
        """
        return self._table1_name

    @table1_name.setter
    def table1_name(self, table1_name):
        """Sets the table1_name of this MappingSourceTableVO.

        表1名称。

        :param table1_name: The table1_name of this MappingSourceTableVO.
        :type table1_name: str
        """
        self._table1_name = table1_name

    @property
    def table2_name(self):
        """Gets the table2_name of this MappingSourceTableVO.

        表2名称。

        :return: The table2_name of this MappingSourceTableVO.
        :rtype: str
        """
        return self._table2_name

    @table2_name.setter
    def table2_name(self, table2_name):
        """Sets the table2_name of this MappingSourceTableVO.

        表2名称。

        :param table2_name: The table2_name of this MappingSourceTableVO.
        :type table2_name: str
        """
        self._table2_name = table2_name

    @property
    def join_type(self):
        """Gets the join_type of this MappingSourceTableVO.

        关联类型。 枚举值：   - LEFT: 左外连接   - RIGHT: 右外连接   - INNER: 内连接   - FULL: 全连接 

        :return: The join_type of this MappingSourceTableVO.
        :rtype: str
        """
        return self._join_type

    @join_type.setter
    def join_type(self, join_type):
        """Sets the join_type of this MappingSourceTableVO.

        关联类型。 枚举值：   - LEFT: 左外连接   - RIGHT: 右外连接   - INNER: 内连接   - FULL: 全连接 

        :param join_type: The join_type of this MappingSourceTableVO.
        :type join_type: str
        """
        self._join_type = join_type

    @property
    def join_fields(self):
        """Gets the join_fields of this MappingSourceTableVO.

        on条件。

        :return: The join_fields of this MappingSourceTableVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.MappingJoinFieldVO`]
        """
        return self._join_fields

    @join_fields.setter
    def join_fields(self, join_fields):
        """Sets the join_fields of this MappingSourceTableVO.

        on条件。

        :param join_fields: The join_fields of this MappingSourceTableVO.
        :type join_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.MappingJoinFieldVO`]
        """
        self._join_fields = join_fields

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
        if not isinstance(other, MappingSourceTableVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
