# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IcebergPartitionField:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_id': 'int',
        'field_id': 'int',
        'transform': 'str',
        'name': 'str'
    }

    attribute_map = {
        'source_id': 'source_id',
        'field_id': 'field_id',
        'transform': 'transform',
        'name': 'name'
    }

    def __init__(self, source_id=None, field_id=None, transform=None, name=None):
        r"""IcebergPartitionField

        The model defined in huaweicloud sdk

        :param source_id: 源字段的id。
        :type source_id: int
        :param field_id: 分区字段的id。
        :type field_id: int
        :param transform: 转换函数。
        :type transform: str
        :param name: 分区字段名称。
        :type name: str
        """
        
        

        self._source_id = None
        self._field_id = None
        self._transform = None
        self._name = None
        self.discriminator = None

        self.source_id = source_id
        self.field_id = field_id
        self.transform = transform
        self.name = name

    @property
    def source_id(self):
        r"""Gets the source_id of this IcebergPartitionField.

        源字段的id。

        :return: The source_id of this IcebergPartitionField.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this IcebergPartitionField.

        源字段的id。

        :param source_id: The source_id of this IcebergPartitionField.
        :type source_id: int
        """
        self._source_id = source_id

    @property
    def field_id(self):
        r"""Gets the field_id of this IcebergPartitionField.

        分区字段的id。

        :return: The field_id of this IcebergPartitionField.
        :rtype: int
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        r"""Sets the field_id of this IcebergPartitionField.

        分区字段的id。

        :param field_id: The field_id of this IcebergPartitionField.
        :type field_id: int
        """
        self._field_id = field_id

    @property
    def transform(self):
        r"""Gets the transform of this IcebergPartitionField.

        转换函数。

        :return: The transform of this IcebergPartitionField.
        :rtype: str
        """
        return self._transform

    @transform.setter
    def transform(self, transform):
        r"""Sets the transform of this IcebergPartitionField.

        转换函数。

        :param transform: The transform of this IcebergPartitionField.
        :type transform: str
        """
        self._transform = transform

    @property
    def name(self):
        r"""Gets the name of this IcebergPartitionField.

        分区字段名称。

        :return: The name of this IcebergPartitionField.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this IcebergPartitionField.

        分区字段名称。

        :param name: The name of this IcebergPartitionField.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, IcebergPartitionField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
