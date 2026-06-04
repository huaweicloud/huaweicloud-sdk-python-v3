# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IcebergPartitionSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_id': 'int',
        'fields': 'list[IcebergPartitionField]'
    }

    attribute_map = {
        'spec_id': 'spec_id',
        'fields': 'fields'
    }

    def __init__(self, spec_id=None, fields=None):
        r"""IcebergPartitionSpec

        The model defined in huaweicloud sdk

        :param spec_id: 分区规范id。
        :type spec_id: int
        :param fields: IcebergPartitionField的列表。
        :type fields: list[:class:`huaweicloudsdklakeformation.v1.IcebergPartitionField`]
        """
        
        

        self._spec_id = None
        self._fields = None
        self.discriminator = None

        self.spec_id = spec_id
        self.fields = fields

    @property
    def spec_id(self):
        r"""Gets the spec_id of this IcebergPartitionSpec.

        分区规范id。

        :return: The spec_id of this IcebergPartitionSpec.
        :rtype: int
        """
        return self._spec_id

    @spec_id.setter
    def spec_id(self, spec_id):
        r"""Sets the spec_id of this IcebergPartitionSpec.

        分区规范id。

        :param spec_id: The spec_id of this IcebergPartitionSpec.
        :type spec_id: int
        """
        self._spec_id = spec_id

    @property
    def fields(self):
        r"""Gets the fields of this IcebergPartitionSpec.

        IcebergPartitionField的列表。

        :return: The fields of this IcebergPartitionSpec.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.IcebergPartitionField`]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this IcebergPartitionSpec.

        IcebergPartitionField的列表。

        :param fields: The fields of this IcebergPartitionSpec.
        :type fields: list[:class:`huaweicloudsdklakeformation.v1.IcebergPartitionField`]
        """
        self._fields = fields

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
        if not isinstance(other, IcebergPartitionSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
