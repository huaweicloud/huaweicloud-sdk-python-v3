# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomRegexItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'regex_expression': 'str',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'regex_expression': 'regex_expression',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, regex_expression=None, create_time=None, update_time=None):
        r"""CustomRegexItem

        The model defined in huaweicloud sdk

        :param id: 正则ID
        :type id: str
        :param name: 正则名称
        :type name: str
        :param regex_expression: 正则表达式
        :type regex_expression: str
        :param create_time: 创建时间（毫秒时间戳）
        :type create_time: int
        :param update_time: 更新时间（毫秒时间戳）
        :type update_time: int
        """
        
        

        self._id = None
        self._name = None
        self._regex_expression = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if regex_expression is not None:
            self.regex_expression = regex_expression
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this CustomRegexItem.

        正则ID

        :return: The id of this CustomRegexItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CustomRegexItem.

        正则ID

        :param id: The id of this CustomRegexItem.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CustomRegexItem.

        正则名称

        :return: The name of this CustomRegexItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CustomRegexItem.

        正则名称

        :param name: The name of this CustomRegexItem.
        :type name: str
        """
        self._name = name

    @property
    def regex_expression(self):
        r"""Gets the regex_expression of this CustomRegexItem.

        正则表达式

        :return: The regex_expression of this CustomRegexItem.
        :rtype: str
        """
        return self._regex_expression

    @regex_expression.setter
    def regex_expression(self, regex_expression):
        r"""Sets the regex_expression of this CustomRegexItem.

        正则表达式

        :param regex_expression: The regex_expression of this CustomRegexItem.
        :type regex_expression: str
        """
        self._regex_expression = regex_expression

    @property
    def create_time(self):
        r"""Gets the create_time of this CustomRegexItem.

        创建时间（毫秒时间戳）

        :return: The create_time of this CustomRegexItem.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CustomRegexItem.

        创建时间（毫秒时间戳）

        :param create_time: The create_time of this CustomRegexItem.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CustomRegexItem.

        更新时间（毫秒时间戳）

        :return: The update_time of this CustomRegexItem.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CustomRegexItem.

        更新时间（毫秒时间戳）

        :param update_time: The update_time of this CustomRegexItem.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, CustomRegexItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
