# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VariableAttributesResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'variable_index': 'int',
        'variable_length': 'int',
        'variable_type': 'str',
        'variable_desc': 'str'
    }

    attribute_map = {
        'id': 'id',
        'variable_index': 'variable_index',
        'variable_length': 'variable_length',
        'variable_type': 'variable_type',
        'variable_desc': 'variable_desc'
    }

    def __init__(self, id=None, variable_index=None, variable_length=None, variable_type=None, variable_desc=None):
        r"""VariableAttributesResponse

        The model defined in huaweicloud sdk

        :param id: ID。
        :type id: int
        :param variable_index: 变量索引。
        :type variable_index: int
        :param variable_length: 变量长度。
        :type variable_length: int
        :param variable_type: 变量类型。
        :type variable_type: str
        :param variable_desc: 变量描述。
        :type variable_desc: str
        """
        
        

        self._id = None
        self._variable_index = None
        self._variable_length = None
        self._variable_type = None
        self._variable_desc = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if variable_index is not None:
            self.variable_index = variable_index
        if variable_length is not None:
            self.variable_length = variable_length
        if variable_type is not None:
            self.variable_type = variable_type
        if variable_desc is not None:
            self.variable_desc = variable_desc

    @property
    def id(self):
        r"""Gets the id of this VariableAttributesResponse.

        ID。

        :return: The id of this VariableAttributesResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VariableAttributesResponse.

        ID。

        :param id: The id of this VariableAttributesResponse.
        :type id: int
        """
        self._id = id

    @property
    def variable_index(self):
        r"""Gets the variable_index of this VariableAttributesResponse.

        变量索引。

        :return: The variable_index of this VariableAttributesResponse.
        :rtype: int
        """
        return self._variable_index

    @variable_index.setter
    def variable_index(self, variable_index):
        r"""Sets the variable_index of this VariableAttributesResponse.

        变量索引。

        :param variable_index: The variable_index of this VariableAttributesResponse.
        :type variable_index: int
        """
        self._variable_index = variable_index

    @property
    def variable_length(self):
        r"""Gets the variable_length of this VariableAttributesResponse.

        变量长度。

        :return: The variable_length of this VariableAttributesResponse.
        :rtype: int
        """
        return self._variable_length

    @variable_length.setter
    def variable_length(self, variable_length):
        r"""Sets the variable_length of this VariableAttributesResponse.

        变量长度。

        :param variable_length: The variable_length of this VariableAttributesResponse.
        :type variable_length: int
        """
        self._variable_length = variable_length

    @property
    def variable_type(self):
        r"""Gets the variable_type of this VariableAttributesResponse.

        变量类型。

        :return: The variable_type of this VariableAttributesResponse.
        :rtype: str
        """
        return self._variable_type

    @variable_type.setter
    def variable_type(self, variable_type):
        r"""Sets the variable_type of this VariableAttributesResponse.

        变量类型。

        :param variable_type: The variable_type of this VariableAttributesResponse.
        :type variable_type: str
        """
        self._variable_type = variable_type

    @property
    def variable_desc(self):
        r"""Gets the variable_desc of this VariableAttributesResponse.

        变量描述。

        :return: The variable_desc of this VariableAttributesResponse.
        :rtype: str
        """
        return self._variable_desc

    @variable_desc.setter
    def variable_desc(self, variable_desc):
        r"""Sets the variable_desc of this VariableAttributesResponse.

        变量描述。

        :param variable_desc: The variable_desc of this VariableAttributesResponse.
        :type variable_desc: str
        """
        self._variable_desc = variable_desc

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
        if not isinstance(other, VariableAttributesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
