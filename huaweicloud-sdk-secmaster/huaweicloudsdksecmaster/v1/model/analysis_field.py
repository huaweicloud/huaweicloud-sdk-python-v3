# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AnalysisField:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alias': 'str',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, alias=None, name=None, type=None):
        r"""AnalysisField

        The model defined in huaweicloud sdk

        :param alias: 字段别名
        :type alias: str
        :param name: 字段名称
        :type name: str
        :param type: 字段类型；可选值：boolean、byte、short、integer、long、float、half_float、scaled_float、double、keyword、text、date、ip、binary、object、nested
        :type type: str
        """
        
        

        self._alias = None
        self._name = None
        self._type = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        self.name = name
        self.type = type

    @property
    def alias(self):
        r"""Gets the alias of this AnalysisField.

        字段别名

        :return: The alias of this AnalysisField.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this AnalysisField.

        字段别名

        :param alias: The alias of this AnalysisField.
        :type alias: str
        """
        self._alias = alias

    @property
    def name(self):
        r"""Gets the name of this AnalysisField.

        字段名称

        :return: The name of this AnalysisField.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AnalysisField.

        字段名称

        :param name: The name of this AnalysisField.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this AnalysisField.

        字段类型；可选值：boolean、byte、short、integer、long、float、half_float、scaled_float、double、keyword、text、date、ip、binary、object、nested

        :return: The type of this AnalysisField.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AnalysisField.

        字段类型；可选值：boolean、byte、short、integer、long、float、half_float、scaled_float、double、keyword、text、date、ip、binary、object、nested

        :param type: The type of this AnalysisField.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, AnalysisField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
