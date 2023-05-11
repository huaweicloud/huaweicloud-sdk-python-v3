# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Function:

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
        'operation': 'str',
        'metadata': 'object'
    }

    attribute_map = {
        'name': 'name',
        'operation': 'operation',
        'metadata': 'metadata'
    }

    def __init__(self, name=None, operation=None, metadata=None):
        """Function

        The model defined in huaweicloud sdk

        :param name: 函数名称，在单个流程中，名称需要唯一
        :type name: str
        :param operation: 函数调用URN
        :type operation: str
        :param metadata: 函数扩展属性，由用户自己定制
        :type metadata: object
        """
        
        

        self._name = None
        self._operation = None
        self._metadata = None
        self.discriminator = None

        self.name = name
        self.operation = operation
        if metadata is not None:
            self.metadata = metadata

    @property
    def name(self):
        """Gets the name of this Function.

        函数名称，在单个流程中，名称需要唯一

        :return: The name of this Function.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Function.

        函数名称，在单个流程中，名称需要唯一

        :param name: The name of this Function.
        :type name: str
        """
        self._name = name

    @property
    def operation(self):
        """Gets the operation of this Function.

        函数调用URN

        :return: The operation of this Function.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this Function.

        函数调用URN

        :param operation: The operation of this Function.
        :type operation: str
        """
        self._operation = operation

    @property
    def metadata(self):
        """Gets the metadata of this Function.

        函数扩展属性，由用户自己定制

        :return: The metadata of this Function.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Function.

        函数扩展属性，由用户自己定制

        :param metadata: The metadata of this Function.
        :type metadata: object
        """
        self._metadata = metadata

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
        if not isinstance(other, Function):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
