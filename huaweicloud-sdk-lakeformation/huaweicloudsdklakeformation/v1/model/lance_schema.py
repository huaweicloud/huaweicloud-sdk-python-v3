# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LanceSchema:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fields': 'list[ArrowField]',
        'metadata': 'dict(str, str)'
    }

    attribute_map = {
        'fields': 'fields',
        'metadata': 'metadata'
    }

    def __init__(self, fields=None, metadata=None):
        r"""LanceSchema

        The model defined in huaweicloud sdk

        :param fields: Arrow字段列表，定义表的所有列及其类型信息。
        :type fields: list[:class:`huaweicloudsdklakeformation.v1.ArrowField`]
        :param metadata: Schema的元数据信息，key-value形式的附加信息。
        :type metadata: dict(str, str)
        """
        
        

        self._fields = None
        self._metadata = None
        self.discriminator = None

        self.fields = fields
        if metadata is not None:
            self.metadata = metadata

    @property
    def fields(self):
        r"""Gets the fields of this LanceSchema.

        Arrow字段列表，定义表的所有列及其类型信息。

        :return: The fields of this LanceSchema.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.ArrowField`]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this LanceSchema.

        Arrow字段列表，定义表的所有列及其类型信息。

        :param fields: The fields of this LanceSchema.
        :type fields: list[:class:`huaweicloudsdklakeformation.v1.ArrowField`]
        """
        self._fields = fields

    @property
    def metadata(self):
        r"""Gets the metadata of this LanceSchema.

        Schema的元数据信息，key-value形式的附加信息。

        :return: The metadata of this LanceSchema.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this LanceSchema.

        Schema的元数据信息，key-value形式的附加信息。

        :param metadata: The metadata of this LanceSchema.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

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
        if not isinstance(other, LanceSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
