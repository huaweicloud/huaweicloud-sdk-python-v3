# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateInfo:

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
        'type': 'str',
        'query': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'query': 'query',
        'description': 'description'
    }

    def __init__(self, name=None, type=None, query=None, description=None):
        r"""TemplateInfo

        The model defined in huaweicloud sdk

        :param name: 变量名称。
        :type name: str
        :param type: 变量类型。
        :type type: str
        :param query: 变量值。
        :type query: str
        :param description: 变量描述。
        :type description: str
        """
        
        

        self._name = None
        self._type = None
        self._query = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if query is not None:
            self.query = query
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this TemplateInfo.

        变量名称。

        :return: The name of this TemplateInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TemplateInfo.

        变量名称。

        :param name: The name of this TemplateInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this TemplateInfo.

        变量类型。

        :return: The type of this TemplateInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TemplateInfo.

        变量类型。

        :param type: The type of this TemplateInfo.
        :type type: str
        """
        self._type = type

    @property
    def query(self):
        r"""Gets the query of this TemplateInfo.

        变量值。

        :return: The query of this TemplateInfo.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this TemplateInfo.

        变量值。

        :param query: The query of this TemplateInfo.
        :type query: str
        """
        self._query = query

    @property
    def description(self):
        r"""Gets the description of this TemplateInfo.

        变量描述。

        :return: The description of this TemplateInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TemplateInfo.

        变量描述。

        :param description: The description of this TemplateInfo.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, TemplateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
