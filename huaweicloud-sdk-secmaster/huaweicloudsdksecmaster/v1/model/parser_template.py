# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParserTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'parser_id': 'str',
        'title': 'str'
    }

    attribute_map = {
        'description': 'description',
        'parser_id': 'parser_id',
        'title': 'title'
    }

    def __init__(self, description=None, parser_id=None, title=None):
        r"""ParserTemplate

        The model defined in huaweicloud sdk

        :param description: 描述信息
        :type description: str
        :param parser_id: UUID
        :type parser_id: str
        :param title: 相关标题
        :type title: str
        """
        
        

        self._description = None
        self._parser_id = None
        self._title = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if parser_id is not None:
            self.parser_id = parser_id
        if title is not None:
            self.title = title

    @property
    def description(self):
        r"""Gets the description of this ParserTemplate.

        描述信息

        :return: The description of this ParserTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ParserTemplate.

        描述信息

        :param description: The description of this ParserTemplate.
        :type description: str
        """
        self._description = description

    @property
    def parser_id(self):
        r"""Gets the parser_id of this ParserTemplate.

        UUID

        :return: The parser_id of this ParserTemplate.
        :rtype: str
        """
        return self._parser_id

    @parser_id.setter
    def parser_id(self, parser_id):
        r"""Sets the parser_id of this ParserTemplate.

        UUID

        :param parser_id: The parser_id of this ParserTemplate.
        :type parser_id: str
        """
        self._parser_id = parser_id

    @property
    def title(self):
        r"""Gets the title of this ParserTemplate.

        相关标题

        :return: The title of this ParserTemplate.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ParserTemplate.

        相关标题

        :param title: The title of this ParserTemplate.
        :type title: str
        """
        self._title = title

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
        if not isinstance(other, ParserTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
