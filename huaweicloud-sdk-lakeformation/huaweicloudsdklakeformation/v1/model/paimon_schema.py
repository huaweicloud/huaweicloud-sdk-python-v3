# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PaimonSchema:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fields': 'list[PaimonField]',
        'partition_keys': 'list[str]',
        'primary_keys': 'list[str]',
        'options': 'dict(str, str)'
    }

    attribute_map = {
        'fields': 'fields',
        'partition_keys': 'partition_keys',
        'primary_keys': 'primary_keys',
        'options': 'options'
    }

    def __init__(self, fields=None, partition_keys=None, primary_keys=None, options=None):
        r"""PaimonSchema

        The model defined in huaweicloud sdk

        :param fields: 字段列表，定义表的所有列及其类型。
        :type fields: list[:class:`huaweicloudsdklakeformation.v1.PaimonField`]
        :param partition_keys: 分区建集合
        :type partition_keys: list[str]
        :param primary_keys: 主键集合
        :type primary_keys: list[str]
        :param options: Paimon表属性
        :type options: dict(str, str)
        """
        
        

        self._fields = None
        self._partition_keys = None
        self._primary_keys = None
        self._options = None
        self.discriminator = None

        self.fields = fields
        if partition_keys is not None:
            self.partition_keys = partition_keys
        if primary_keys is not None:
            self.primary_keys = primary_keys
        if options is not None:
            self.options = options

    @property
    def fields(self):
        r"""Gets the fields of this PaimonSchema.

        字段列表，定义表的所有列及其类型。

        :return: The fields of this PaimonSchema.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.PaimonField`]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this PaimonSchema.

        字段列表，定义表的所有列及其类型。

        :param fields: The fields of this PaimonSchema.
        :type fields: list[:class:`huaweicloudsdklakeformation.v1.PaimonField`]
        """
        self._fields = fields

    @property
    def partition_keys(self):
        r"""Gets the partition_keys of this PaimonSchema.

        分区建集合

        :return: The partition_keys of this PaimonSchema.
        :rtype: list[str]
        """
        return self._partition_keys

    @partition_keys.setter
    def partition_keys(self, partition_keys):
        r"""Sets the partition_keys of this PaimonSchema.

        分区建集合

        :param partition_keys: The partition_keys of this PaimonSchema.
        :type partition_keys: list[str]
        """
        self._partition_keys = partition_keys

    @property
    def primary_keys(self):
        r"""Gets the primary_keys of this PaimonSchema.

        主键集合

        :return: The primary_keys of this PaimonSchema.
        :rtype: list[str]
        """
        return self._primary_keys

    @primary_keys.setter
    def primary_keys(self, primary_keys):
        r"""Sets the primary_keys of this PaimonSchema.

        主键集合

        :param primary_keys: The primary_keys of this PaimonSchema.
        :type primary_keys: list[str]
        """
        self._primary_keys = primary_keys

    @property
    def options(self):
        r"""Gets the options of this PaimonSchema.

        Paimon表属性

        :return: The options of this PaimonSchema.
        :rtype: dict(str, str)
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this PaimonSchema.

        Paimon表属性

        :param options: The options of this PaimonSchema.
        :type options: dict(str, str)
        """
        self._options = options

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
        if not isinstance(other, PaimonSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
