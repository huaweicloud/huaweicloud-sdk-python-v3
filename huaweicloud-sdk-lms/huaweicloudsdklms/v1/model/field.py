# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Field:

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
        'element_data_type': 'str',
        'element_type_params': 'dict(str, object)',
        'partition_key': 'bool'
    }

    attribute_map = {
        'field_name': 'field_name',
        'data_type': 'data_type',
        'element_data_type': 'element_data_type',
        'element_type_params': 'element_type_params',
        'partition_key': 'partition_key'
    }

    def __init__(self, field_name=None, data_type=None, element_data_type=None, element_type_params=None, partition_key=None):
        r"""Field

        The model defined in huaweicloud sdk

        :param field_name: 要在集合中创建的字段名称
        :type field_name: str
        :param data_type: 字段的数据类型；“Bool”,“Int8”,“Int16”,“Int32”,“Int64”,“Float”,“String”,“Array”,“JSON”,\&quot;FloatVector\&quot;, \&quot;SparseFloatVector\&quot;
        :type data_type: str
        :param element_data_type: 数组内部的数据类型，当前支持“Bool”,“Int8”,“Int16”,“Int32”,“Int64”,“Float”,“String”
        :type element_data_type: str
        :param element_type_params: 如果field为FloatVector类型向量字段，则必须设定维度参数dim: 向量字段的维度，最大支持32,768维  如果field为String类型字段或Array 元素类型为String类型，则可设定字段值最大长度max_length，默认为256  如果field为Array类型字段，则可设定数组最大容量max_capacity，默认为32
        :type element_type_params: dict(str, object)
        :param partition_key: 该字段是否为partition_key，默认false。（如果partition_key为true，data_type仅支持String与Int64）；最多只有一个field的partition_key设置为true
        :type partition_key: bool
        """
        
        

        self._field_name = None
        self._data_type = None
        self._element_data_type = None
        self._element_type_params = None
        self._partition_key = None
        self.discriminator = None

        self.field_name = field_name
        self.data_type = data_type
        if element_data_type is not None:
            self.element_data_type = element_data_type
        if element_type_params is not None:
            self.element_type_params = element_type_params
        if partition_key is not None:
            self.partition_key = partition_key

    @property
    def field_name(self):
        r"""Gets the field_name of this Field.

        要在集合中创建的字段名称

        :return: The field_name of this Field.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        r"""Sets the field_name of this Field.

        要在集合中创建的字段名称

        :param field_name: The field_name of this Field.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def data_type(self):
        r"""Gets the data_type of this Field.

        字段的数据类型；“Bool”,“Int8”,“Int16”,“Int32”,“Int64”,“Float”,“String”,“Array”,“JSON”,\"FloatVector\", \"SparseFloatVector\"

        :return: The data_type of this Field.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this Field.

        字段的数据类型；“Bool”,“Int8”,“Int16”,“Int32”,“Int64”,“Float”,“String”,“Array”,“JSON”,\"FloatVector\", \"SparseFloatVector\"

        :param data_type: The data_type of this Field.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def element_data_type(self):
        r"""Gets the element_data_type of this Field.

        数组内部的数据类型，当前支持“Bool”,“Int8”,“Int16”,“Int32”,“Int64”,“Float”,“String”

        :return: The element_data_type of this Field.
        :rtype: str
        """
        return self._element_data_type

    @element_data_type.setter
    def element_data_type(self, element_data_type):
        r"""Sets the element_data_type of this Field.

        数组内部的数据类型，当前支持“Bool”,“Int8”,“Int16”,“Int32”,“Int64”,“Float”,“String”

        :param element_data_type: The element_data_type of this Field.
        :type element_data_type: str
        """
        self._element_data_type = element_data_type

    @property
    def element_type_params(self):
        r"""Gets the element_type_params of this Field.

        如果field为FloatVector类型向量字段，则必须设定维度参数dim: 向量字段的维度，最大支持32,768维  如果field为String类型字段或Array 元素类型为String类型，则可设定字段值最大长度max_length，默认为256  如果field为Array类型字段，则可设定数组最大容量max_capacity，默认为32

        :return: The element_type_params of this Field.
        :rtype: dict(str, object)
        """
        return self._element_type_params

    @element_type_params.setter
    def element_type_params(self, element_type_params):
        r"""Sets the element_type_params of this Field.

        如果field为FloatVector类型向量字段，则必须设定维度参数dim: 向量字段的维度，最大支持32,768维  如果field为String类型字段或Array 元素类型为String类型，则可设定字段值最大长度max_length，默认为256  如果field为Array类型字段，则可设定数组最大容量max_capacity，默认为32

        :param element_type_params: The element_type_params of this Field.
        :type element_type_params: dict(str, object)
        """
        self._element_type_params = element_type_params

    @property
    def partition_key(self):
        r"""Gets the partition_key of this Field.

        该字段是否为partition_key，默认false。（如果partition_key为true，data_type仅支持String与Int64）；最多只有一个field的partition_key设置为true

        :return: The partition_key of this Field.
        :rtype: bool
        """
        return self._partition_key

    @partition_key.setter
    def partition_key(self, partition_key):
        r"""Sets the partition_key of this Field.

        该字段是否为partition_key，默认false。（如果partition_key为true，data_type仅支持String与Int64）；最多只有一个field的partition_key设置为true

        :param partition_key: The partition_key of this Field.
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
        if not isinstance(other, Field):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
