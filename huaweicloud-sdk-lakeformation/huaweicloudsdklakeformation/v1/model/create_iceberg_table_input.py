# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIcebergTableInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schema': 'IcebergSchema',
        'partition_spec': 'IcebergPartitionSpec',
        'write_order': 'IcebergSortOrder'
    }

    attribute_map = {
        'schema': 'schema',
        'partition_spec': 'partition_spec',
        'write_order': 'write_order'
    }

    def __init__(self, schema=None, partition_spec=None, write_order=None):
        r"""CreateIcebergTableInput

        The model defined in huaweicloud sdk

        :param schema: 
        :type schema: :class:`huaweicloudsdklakeformation.v1.IcebergSchema`
        :param partition_spec: 
        :type partition_spec: :class:`huaweicloudsdklakeformation.v1.IcebergPartitionSpec`
        :param write_order: 
        :type write_order: :class:`huaweicloudsdklakeformation.v1.IcebergSortOrder`
        """
        
        

        self._schema = None
        self._partition_spec = None
        self._write_order = None
        self.discriminator = None

        self.schema = schema
        if partition_spec is not None:
            self.partition_spec = partition_spec
        if write_order is not None:
            self.write_order = write_order

    @property
    def schema(self):
        r"""Gets the schema of this CreateIcebergTableInput.

        :return: The schema of this CreateIcebergTableInput.
        :rtype: :class:`huaweicloudsdklakeformation.v1.IcebergSchema`
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this CreateIcebergTableInput.

        :param schema: The schema of this CreateIcebergTableInput.
        :type schema: :class:`huaweicloudsdklakeformation.v1.IcebergSchema`
        """
        self._schema = schema

    @property
    def partition_spec(self):
        r"""Gets the partition_spec of this CreateIcebergTableInput.

        :return: The partition_spec of this CreateIcebergTableInput.
        :rtype: :class:`huaweicloudsdklakeformation.v1.IcebergPartitionSpec`
        """
        return self._partition_spec

    @partition_spec.setter
    def partition_spec(self, partition_spec):
        r"""Sets the partition_spec of this CreateIcebergTableInput.

        :param partition_spec: The partition_spec of this CreateIcebergTableInput.
        :type partition_spec: :class:`huaweicloudsdklakeformation.v1.IcebergPartitionSpec`
        """
        self._partition_spec = partition_spec

    @property
    def write_order(self):
        r"""Gets the write_order of this CreateIcebergTableInput.

        :return: The write_order of this CreateIcebergTableInput.
        :rtype: :class:`huaweicloudsdklakeformation.v1.IcebergSortOrder`
        """
        return self._write_order

    @write_order.setter
    def write_order(self, write_order):
        r"""Sets the write_order of this CreateIcebergTableInput.

        :param write_order: The write_order of this CreateIcebergTableInput.
        :type write_order: :class:`huaweicloudsdklakeformation.v1.IcebergSortOrder`
        """
        self._write_order = write_order

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
        if not isinstance(other, CreateIcebergTableInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
