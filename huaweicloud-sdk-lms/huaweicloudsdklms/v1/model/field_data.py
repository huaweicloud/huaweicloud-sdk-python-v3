# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FieldData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field_name': 'str',
        'data_type': 'str',
        'primary_key': 'bool',
        'partition_key': 'bool'
    }

    attribute_map = {
        'field_name': 'field_name',
        'data_type': 'data_type',
        'primary_key': 'primary_key',
        'partition_key': 'partition_key'
    }

    def __init__(self, field_name=None, data_type=None, primary_key=None, partition_key=None):
        r"""FieldData

        The model defined in huaweicloud sdk

        :param field_name: 要在集合中创建的字段名称
        :type field_name: str
        :param data_type: 字段的数据类型；“Bool”,“Int8”,“Int16”,“Int32”,“Int64”,“Float”,“String”,“Array”,“JSON”,\&quot;FloatVector\&quot;,\&quot;SparseFloatVector\&quot;。注意向量类型后会添加维度信息，如\&quot;SparseFloatVector(256)
        :type data_type: str
        :param primary_key: 是否是主键字段
        :type primary_key: bool
        :param partition_key: 是否是partition key
        :type partition_key: bool
        """
        
        

        self._field_name = None
        self._data_type = None
        self._primary_key = None
        self._partition_key = None
        self.discriminator = None

        self.field_name = field_name
        self.data_type = data_type
        self.primary_key = primary_key
        self.partition_key = partition_key

    @property
    def field_name(self):
        r"""Gets the field_name of this FieldData.

        要在集合中创建的字段名称

        :return: The field_name of this FieldData.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        r"""Sets the field_name of this FieldData.

        要在集合中创建的字段名称

        :param field_name: The field_name of this FieldData.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def data_type(self):
        r"""Gets the data_type of this FieldData.

        字段的数据类型；“Bool”,“Int8”,“Int16”,“Int32”,“Int64”,“Float”,“String”,“Array”,“JSON”,\"FloatVector\",\"SparseFloatVector\"。注意向量类型后会添加维度信息，如\"SparseFloatVector(256)

        :return: The data_type of this FieldData.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this FieldData.

        字段的数据类型；“Bool”,“Int8”,“Int16”,“Int32”,“Int64”,“Float”,“String”,“Array”,“JSON”,\"FloatVector\",\"SparseFloatVector\"。注意向量类型后会添加维度信息，如\"SparseFloatVector(256)

        :param data_type: The data_type of this FieldData.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def primary_key(self):
        r"""Gets the primary_key of this FieldData.

        是否是主键字段

        :return: The primary_key of this FieldData.
        :rtype: bool
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        r"""Sets the primary_key of this FieldData.

        是否是主键字段

        :param primary_key: The primary_key of this FieldData.
        :type primary_key: bool
        """
        self._primary_key = primary_key

    @property
    def partition_key(self):
        r"""Gets the partition_key of this FieldData.

        是否是partition key

        :return: The partition_key of this FieldData.
        :rtype: bool
        """
        return self._partition_key

    @partition_key.setter
    def partition_key(self, partition_key):
        r"""Sets the partition_key of this FieldData.

        是否是partition key

        :param partition_key: The partition_key of this FieldData.
        :type partition_key: bool
        """
        self._partition_key = partition_key

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
        if not isinstance(other, FieldData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
