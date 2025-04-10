# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Step:

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
        'type': 'str',
        'input': 'dict(str, str)',
        'ignore_error': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'input': 'input',
        'ignore_error': 'ignore_error',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, type=None, input=None, ignore_error=None, description=None):
        r"""Step

        The model defined in huaweicloud sdk

        :param id: 步骤id。
        :type id: str
        :param name: 步骤名称。
        :type name: str
        :param type: 步骤类型。
        :type type: str
        :param input: 步骤参数。
        :type input: dict(str, str)
        :param ignore_error: 是否自动忽略错误。
        :type ignore_error: bool
        :param description: 步骤说明。
        :type description: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._input = None
        self._ignore_error = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if input is not None:
            self.input = input
        self.ignore_error = ignore_error
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this Step.

        步骤id。

        :return: The id of this Step.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Step.

        步骤id。

        :param id: The id of this Step.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Step.

        步骤名称。

        :return: The name of this Step.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Step.

        步骤名称。

        :param name: The name of this Step.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this Step.

        步骤类型。

        :return: The type of this Step.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Step.

        步骤类型。

        :param type: The type of this Step.
        :type type: str
        """
        self._type = type

    @property
    def input(self):
        r"""Gets the input of this Step.

        步骤参数。

        :return: The input of this Step.
        :rtype: dict(str, str)
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this Step.

        步骤参数。

        :param input: The input of this Step.
        :type input: dict(str, str)
        """
        self._input = input

    @property
    def ignore_error(self):
        r"""Gets the ignore_error of this Step.

        是否自动忽略错误。

        :return: The ignore_error of this Step.
        :rtype: bool
        """
        return self._ignore_error

    @ignore_error.setter
    def ignore_error(self, ignore_error):
        r"""Sets the ignore_error of this Step.

        是否自动忽略错误。

        :param ignore_error: The ignore_error of this Step.
        :type ignore_error: bool
        """
        self._ignore_error = ignore_error

    @property
    def description(self):
        r"""Gets the description of this Step.

        步骤说明。

        :return: The description of this Step.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Step.

        步骤说明。

        :param description: The description of this Step.
        :type description: str
        """
        self._description = description

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Step):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
