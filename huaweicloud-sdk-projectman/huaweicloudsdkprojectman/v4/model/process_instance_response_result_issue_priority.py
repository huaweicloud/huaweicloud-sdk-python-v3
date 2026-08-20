# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProcessInstanceResponseResultIssuePriority:

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
        'display_value': 'str',
        'value': 'str',
        'code': 'str',
        'value_py': 'str',
        'sequence': 'int',
        'level': 'int',
        'domain_id': 'str',
        'belong_definition_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'display_value': 'display_value',
        'value': 'value',
        'code': 'code',
        'value_py': 'value_py',
        'sequence': 'sequence',
        'level': 'level',
        'domain_id': 'domain_id',
        'belong_definition_type': 'belong_definition_type'
    }

    def __init__(self, id=None, display_value=None, value=None, code=None, value_py=None, sequence=None, level=None, domain_id=None, belong_definition_type=None):
        r"""ProcessInstanceResponseResultIssuePriority

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param display_value: 显示名称
        :type display_value: str
        :param value: 值
        :type value: str
        :param code: 编码
        :type code: str
        :param value_py: 值(拼音首字母)
        :type value_py: str
        :param sequence: 序列
        :type sequence: int
        :param level: 层级
        :type level: int
        :param domain_id: 项目ID
        :type domain_id: str
        :param belong_definition_type: 所属定义级别
        :type belong_definition_type: str
        """
        
        

        self._id = None
        self._display_value = None
        self._value = None
        self._code = None
        self._value_py = None
        self._sequence = None
        self._level = None
        self._domain_id = None
        self._belong_definition_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if display_value is not None:
            self.display_value = display_value
        if value is not None:
            self.value = value
        if code is not None:
            self.code = code
        if value_py is not None:
            self.value_py = value_py
        if sequence is not None:
            self.sequence = sequence
        if level is not None:
            self.level = level
        if domain_id is not None:
            self.domain_id = domain_id
        if belong_definition_type is not None:
            self.belong_definition_type = belong_definition_type

    @property
    def id(self):
        r"""Gets the id of this ProcessInstanceResponseResultIssuePriority.

        id

        :return: The id of this ProcessInstanceResponseResultIssuePriority.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProcessInstanceResponseResultIssuePriority.

        id

        :param id: The id of this ProcessInstanceResponseResultIssuePriority.
        :type id: str
        """
        self._id = id

    @property
    def display_value(self):
        r"""Gets the display_value of this ProcessInstanceResponseResultIssuePriority.

        显示名称

        :return: The display_value of this ProcessInstanceResponseResultIssuePriority.
        :rtype: str
        """
        return self._display_value

    @display_value.setter
    def display_value(self, display_value):
        r"""Sets the display_value of this ProcessInstanceResponseResultIssuePriority.

        显示名称

        :param display_value: The display_value of this ProcessInstanceResponseResultIssuePriority.
        :type display_value: str
        """
        self._display_value = display_value

    @property
    def value(self):
        r"""Gets the value of this ProcessInstanceResponseResultIssuePriority.

        值

        :return: The value of this ProcessInstanceResponseResultIssuePriority.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ProcessInstanceResponseResultIssuePriority.

        值

        :param value: The value of this ProcessInstanceResponseResultIssuePriority.
        :type value: str
        """
        self._value = value

    @property
    def code(self):
        r"""Gets the code of this ProcessInstanceResponseResultIssuePriority.

        编码

        :return: The code of this ProcessInstanceResponseResultIssuePriority.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ProcessInstanceResponseResultIssuePriority.

        编码

        :param code: The code of this ProcessInstanceResponseResultIssuePriority.
        :type code: str
        """
        self._code = code

    @property
    def value_py(self):
        r"""Gets the value_py of this ProcessInstanceResponseResultIssuePriority.

        值(拼音首字母)

        :return: The value_py of this ProcessInstanceResponseResultIssuePriority.
        :rtype: str
        """
        return self._value_py

    @value_py.setter
    def value_py(self, value_py):
        r"""Sets the value_py of this ProcessInstanceResponseResultIssuePriority.

        值(拼音首字母)

        :param value_py: The value_py of this ProcessInstanceResponseResultIssuePriority.
        :type value_py: str
        """
        self._value_py = value_py

    @property
    def sequence(self):
        r"""Gets the sequence of this ProcessInstanceResponseResultIssuePriority.

        序列

        :return: The sequence of this ProcessInstanceResponseResultIssuePriority.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        r"""Sets the sequence of this ProcessInstanceResponseResultIssuePriority.

        序列

        :param sequence: The sequence of this ProcessInstanceResponseResultIssuePriority.
        :type sequence: int
        """
        self._sequence = sequence

    @property
    def level(self):
        r"""Gets the level of this ProcessInstanceResponseResultIssuePriority.

        层级

        :return: The level of this ProcessInstanceResponseResultIssuePriority.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ProcessInstanceResponseResultIssuePriority.

        层级

        :param level: The level of this ProcessInstanceResponseResultIssuePriority.
        :type level: int
        """
        self._level = level

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ProcessInstanceResponseResultIssuePriority.

        项目ID

        :return: The domain_id of this ProcessInstanceResponseResultIssuePriority.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ProcessInstanceResponseResultIssuePriority.

        项目ID

        :param domain_id: The domain_id of this ProcessInstanceResponseResultIssuePriority.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def belong_definition_type(self):
        r"""Gets the belong_definition_type of this ProcessInstanceResponseResultIssuePriority.

        所属定义级别

        :return: The belong_definition_type of this ProcessInstanceResponseResultIssuePriority.
        :rtype: str
        """
        return self._belong_definition_type

    @belong_definition_type.setter
    def belong_definition_type(self, belong_definition_type):
        r"""Sets the belong_definition_type of this ProcessInstanceResponseResultIssuePriority.

        所属定义级别

        :param belong_definition_type: The belong_definition_type of this ProcessInstanceResponseResultIssuePriority.
        :type belong_definition_type: str
        """
        self._belong_definition_type = belong_definition_type

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
        if not isinstance(other, ProcessInstanceResponseResultIssuePriority):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
