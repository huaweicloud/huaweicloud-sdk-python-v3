# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VariableDetail:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'file_size': 'int',
        'id': 'int',
        'is_quoted': 'bool',
        'name': 'str',
        'variable': 'list[object]',
        'variable_type': 'int'
    }

    attribute_map = {
        'file_size': 'file_size',
        'id': 'id',
        'is_quoted': 'is_quoted',
        'name': 'name',
        'variable': 'variable',
        'variable_type': 'variable_type'
    }

    def __init__(self, file_size=None, id=None, is_quoted=None, name=None, variable=None, variable_type=None):
        """VariableDetail - a model defined in huaweicloud sdk"""
        
        

        self._file_size = None
        self._id = None
        self._is_quoted = None
        self._name = None
        self._variable = None
        self._variable_type = None
        self.discriminator = None

        if file_size is not None:
            self.file_size = file_size
        if id is not None:
            self.id = id
        if is_quoted is not None:
            self.is_quoted = is_quoted
        if name is not None:
            self.name = name
        if variable is not None:
            self.variable = variable
        if variable_type is not None:
            self.variable_type = variable_type

    @property
    def file_size(self):
        """Gets the file_size of this VariableDetail.

        file_size

        :return: The file_size of this VariableDetail.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this VariableDetail.

        file_size

        :param file_size: The file_size of this VariableDetail.
        :type: int
        """
        self._file_size = file_size

    @property
    def id(self):
        """Gets the id of this VariableDetail.

        id

        :return: The id of this VariableDetail.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VariableDetail.

        id

        :param id: The id of this VariableDetail.
        :type: int
        """
        self._id = id

    @property
    def is_quoted(self):
        """Gets the is_quoted of this VariableDetail.

        is_quoted

        :return: The is_quoted of this VariableDetail.
        :rtype: bool
        """
        return self._is_quoted

    @is_quoted.setter
    def is_quoted(self, is_quoted):
        """Sets the is_quoted of this VariableDetail.

        is_quoted

        :param is_quoted: The is_quoted of this VariableDetail.
        :type: bool
        """
        self._is_quoted = is_quoted

    @property
    def name(self):
        """Gets the name of this VariableDetail.

        name

        :return: The name of this VariableDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VariableDetail.

        name

        :param name: The name of this VariableDetail.
        :type: str
        """
        self._name = name

    @property
    def variable(self):
        """Gets the variable of this VariableDetail.

        variable

        :return: The variable of this VariableDetail.
        :rtype: list[object]
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """Sets the variable of this VariableDetail.

        variable

        :param variable: The variable of this VariableDetail.
        :type: list[object]
        """
        self._variable = variable

    @property
    def variable_type(self):
        """Gets the variable_type of this VariableDetail.

        variable_type

        :return: The variable_type of this VariableDetail.
        :rtype: int
        """
        return self._variable_type

    @variable_type.setter
    def variable_type(self, variable_type):
        """Sets the variable_type of this VariableDetail.

        variable_type

        :param variable_type: The variable_type of this VariableDetail.
        :type: int
        """
        self._variable_type = variable_type

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
        if not isinstance(other, VariableDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
