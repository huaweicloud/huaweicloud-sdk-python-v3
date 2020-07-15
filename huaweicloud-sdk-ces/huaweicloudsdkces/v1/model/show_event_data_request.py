# coding: utf-8

import pprint
import re

import six





class ShowEventDataRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dim0': 'str',
        'dim1': 'str',
        'dim2': 'str',
        '_from': 'int',
        'namespace': 'str',
        'to': 'int',
        'type': 'str'
    }

    attribute_map = {
        'dim0': 'dim.0',
        'dim1': 'dim.1',
        'dim2': 'dim.2',
        '_from': 'from',
        'namespace': 'namespace',
        'to': 'to',
        'type': 'type'
    }

    def __init__(self, dim0=None, dim1=None, dim2=None, _from=None, namespace=None, to=None, type=None):
        """ShowEventDataRequest - a model defined in huaweicloud sdk"""
        
        

        self._dim0 = None
        self._dim1 = None
        self._dim2 = None
        self.__from = None
        self._namespace = None
        self._to = None
        self._type = None
        self.discriminator = None

        self.dim0 = dim0
        if dim1 is not None:
            self.dim1 = dim1
        if dim2 is not None:
            self.dim2 = dim2
        self._from = _from
        self.namespace = namespace
        self.to = to
        self.type = type

    @property
    def dim0(self):
        """Gets the dim0 of this ShowEventDataRequest.


        :return: The dim0 of this ShowEventDataRequest.
        :rtype: str
        """
        return self._dim0

    @dim0.setter
    def dim0(self, dim0):
        """Sets the dim0 of this ShowEventDataRequest.


        :param dim0: The dim0 of this ShowEventDataRequest.
        :type: str
        """
        self._dim0 = dim0

    @property
    def dim1(self):
        """Gets the dim1 of this ShowEventDataRequest.


        :return: The dim1 of this ShowEventDataRequest.
        :rtype: str
        """
        return self._dim1

    @dim1.setter
    def dim1(self, dim1):
        """Sets the dim1 of this ShowEventDataRequest.


        :param dim1: The dim1 of this ShowEventDataRequest.
        :type: str
        """
        self._dim1 = dim1

    @property
    def dim2(self):
        """Gets the dim2 of this ShowEventDataRequest.


        :return: The dim2 of this ShowEventDataRequest.
        :rtype: str
        """
        return self._dim2

    @dim2.setter
    def dim2(self, dim2):
        """Sets the dim2 of this ShowEventDataRequest.


        :param dim2: The dim2 of this ShowEventDataRequest.
        :type: str
        """
        self._dim2 = dim2

    @property
    def _from(self):
        """Gets the _from of this ShowEventDataRequest.


        :return: The _from of this ShowEventDataRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ShowEventDataRequest.


        :param _from: The _from of this ShowEventDataRequest.
        :type: int
        """
        self.__from = _from

    @property
    def namespace(self):
        """Gets the namespace of this ShowEventDataRequest.


        :return: The namespace of this ShowEventDataRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ShowEventDataRequest.


        :param namespace: The namespace of this ShowEventDataRequest.
        :type: str
        """
        self._namespace = namespace

    @property
    def to(self):
        """Gets the to of this ShowEventDataRequest.


        :return: The to of this ShowEventDataRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ShowEventDataRequest.


        :param to: The to of this ShowEventDataRequest.
        :type: int
        """
        self._to = to

    @property
    def type(self):
        """Gets the type of this ShowEventDataRequest.


        :return: The type of this ShowEventDataRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowEventDataRequest.


        :param type: The type of this ShowEventDataRequest.
        :type: str
        """
        self._type = type

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowEventDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
