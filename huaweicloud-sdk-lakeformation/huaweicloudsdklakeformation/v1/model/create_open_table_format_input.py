# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOpenTableFormatInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_iceberg_table_input': 'CreateIcebergTableInput',
        'create_lance_table_input': 'CreateLanceTableInput'
    }

    attribute_map = {
        'create_iceberg_table_input': 'create_iceberg_table_input',
        'create_lance_table_input': 'create_lance_table_input'
    }

    def __init__(self, create_iceberg_table_input=None, create_lance_table_input=None):
        r"""CreateOpenTableFormatInput

        The model defined in huaweicloud sdk

        :param create_iceberg_table_input: 
        :type create_iceberg_table_input: :class:`huaweicloudsdklakeformation.v1.CreateIcebergTableInput`
        :param create_lance_table_input: 
        :type create_lance_table_input: :class:`huaweicloudsdklakeformation.v1.CreateLanceTableInput`
        """
        
        

        self._create_iceberg_table_input = None
        self._create_lance_table_input = None
        self.discriminator = None

        if create_iceberg_table_input is not None:
            self.create_iceberg_table_input = create_iceberg_table_input
        if create_lance_table_input is not None:
            self.create_lance_table_input = create_lance_table_input

    @property
    def create_iceberg_table_input(self):
        r"""Gets the create_iceberg_table_input of this CreateOpenTableFormatInput.

        :return: The create_iceberg_table_input of this CreateOpenTableFormatInput.
        :rtype: :class:`huaweicloudsdklakeformation.v1.CreateIcebergTableInput`
        """
        return self._create_iceberg_table_input

    @create_iceberg_table_input.setter
    def create_iceberg_table_input(self, create_iceberg_table_input):
        r"""Sets the create_iceberg_table_input of this CreateOpenTableFormatInput.

        :param create_iceberg_table_input: The create_iceberg_table_input of this CreateOpenTableFormatInput.
        :type create_iceberg_table_input: :class:`huaweicloudsdklakeformation.v1.CreateIcebergTableInput`
        """
        self._create_iceberg_table_input = create_iceberg_table_input

    @property
    def create_lance_table_input(self):
        r"""Gets the create_lance_table_input of this CreateOpenTableFormatInput.

        :return: The create_lance_table_input of this CreateOpenTableFormatInput.
        :rtype: :class:`huaweicloudsdklakeformation.v1.CreateLanceTableInput`
        """
        return self._create_lance_table_input

    @create_lance_table_input.setter
    def create_lance_table_input(self, create_lance_table_input):
        r"""Sets the create_lance_table_input of this CreateOpenTableFormatInput.

        :param create_lance_table_input: The create_lance_table_input of this CreateOpenTableFormatInput.
        :type create_lance_table_input: :class:`huaweicloudsdklakeformation.v1.CreateLanceTableInput`
        """
        self._create_lance_table_input = create_lance_table_input

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
        if not isinstance(other, CreateOpenTableFormatInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
