# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLanceTableInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schema': 'ArrowSchema'
    }

    attribute_map = {
        'schema': 'schema'
    }

    def __init__(self, schema=None):
        r"""CreateLanceTableInput

        The model defined in huaweicloud sdk

        :param schema: 
        :type schema: :class:`huaweicloudsdklakeformation.v1.ArrowSchema`
        """
        
        

        self._schema = None
        self.discriminator = None

        if schema is not None:
            self.schema = schema

    @property
    def schema(self):
        r"""Gets the schema of this CreateLanceTableInput.

        :return: The schema of this CreateLanceTableInput.
        :rtype: :class:`huaweicloudsdklakeformation.v1.ArrowSchema`
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this CreateLanceTableInput.

        :param schema: The schema of this CreateLanceTableInput.
        :type schema: :class:`huaweicloudsdklakeformation.v1.ArrowSchema`
        """
        self._schema = schema

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
        if not isinstance(other, CreateLanceTableInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
