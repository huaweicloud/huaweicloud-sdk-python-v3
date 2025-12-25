# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdhocQueryAnalysisField:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'logical_type': 'object',
        'alias': 'str'
    }

    attribute_map = {
        'name': 'name',
        'logical_type': 'logical_type',
        'alias': 'alias'
    }

    def __init__(self, name=None, logical_type=None, alias=None):
        r"""AdhocQueryAnalysisField

        The model defined in huaweicloud sdk

        :param name: 字段名称
        :type name: str
        :param logical_type: 字段类型
        :type logical_type: object
        :param alias: 字段别名
        :type alias: str
        """
        
        

        self._name = None
        self._logical_type = None
        self._alias = None
        self.discriminator = None

        self.name = name
        if logical_type is not None:
            self.logical_type = logical_type
        if alias is not None:
            self.alias = alias

    @property
    def name(self):
        r"""Gets the name of this AdhocQueryAnalysisField.

        字段名称

        :return: The name of this AdhocQueryAnalysisField.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AdhocQueryAnalysisField.

        字段名称

        :param name: The name of this AdhocQueryAnalysisField.
        :type name: str
        """
        self._name = name

    @property
    def logical_type(self):
        r"""Gets the logical_type of this AdhocQueryAnalysisField.

        字段类型

        :return: The logical_type of this AdhocQueryAnalysisField.
        :rtype: object
        """
        return self._logical_type

    @logical_type.setter
    def logical_type(self, logical_type):
        r"""Sets the logical_type of this AdhocQueryAnalysisField.

        字段类型

        :param logical_type: The logical_type of this AdhocQueryAnalysisField.
        :type logical_type: object
        """
        self._logical_type = logical_type

    @property
    def alias(self):
        r"""Gets the alias of this AdhocQueryAnalysisField.

        字段别名

        :return: The alias of this AdhocQueryAnalysisField.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this AdhocQueryAnalysisField.

        字段别名

        :param alias: The alias of this AdhocQueryAnalysisField.
        :type alias: str
        """
        self._alias = alias

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
        if not isinstance(other, AdhocQueryAnalysisField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
