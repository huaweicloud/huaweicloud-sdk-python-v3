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
        'namespace': 'str',
        'dim_0': 'str',
        'dim_1': 'str',
        'dim_2': 'str',
        'dim_3': 'str',
        'type': 'str',
        '_from': 'int',
        'to': 'int'
    }

    attribute_map = {
        'namespace': 'namespace',
        'dim_0': 'dim.0',
        'dim_1': 'dim.1',
        'dim_2': 'dim.2',
        'dim_3': 'dim.3',
        'type': 'type',
        '_from': 'from',
        'to': 'to'
    }

    def __init__(self, namespace=None, dim_0=None, dim_1=None, dim_2=None, dim_3=None, type=None, _from=None, to=None):
        """ShowEventDataRequest - a model defined in huaweicloud sdk"""
        
        

        self._namespace = None
        self._dim_0 = None
        self._dim_1 = None
        self._dim_2 = None
        self._dim_3 = None
        self._type = None
        self.__from = None
        self._to = None
        self.discriminator = None

        self.namespace = namespace
        self.dim_0 = dim_0
        if dim_1 is not None:
            self.dim_1 = dim_1
        if dim_2 is not None:
            self.dim_2 = dim_2
        if dim_3 is not None:
            self.dim_3 = dim_3
        self.type = type
        self._from = _from
        self.to = to

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
    def dim_0(self):
        """Gets the dim_0 of this ShowEventDataRequest.


        :return: The dim_0 of this ShowEventDataRequest.
        :rtype: str
        """
        return self._dim_0

    @dim_0.setter
    def dim_0(self, dim_0):
        """Sets the dim_0 of this ShowEventDataRequest.


        :param dim_0: The dim_0 of this ShowEventDataRequest.
        :type: str
        """
        self._dim_0 = dim_0

    @property
    def dim_1(self):
        """Gets the dim_1 of this ShowEventDataRequest.


        :return: The dim_1 of this ShowEventDataRequest.
        :rtype: str
        """
        return self._dim_1

    @dim_1.setter
    def dim_1(self, dim_1):
        """Sets the dim_1 of this ShowEventDataRequest.


        :param dim_1: The dim_1 of this ShowEventDataRequest.
        :type: str
        """
        self._dim_1 = dim_1

    @property
    def dim_2(self):
        """Gets the dim_2 of this ShowEventDataRequest.


        :return: The dim_2 of this ShowEventDataRequest.
        :rtype: str
        """
        return self._dim_2

    @dim_2.setter
    def dim_2(self, dim_2):
        """Sets the dim_2 of this ShowEventDataRequest.


        :param dim_2: The dim_2 of this ShowEventDataRequest.
        :type: str
        """
        self._dim_2 = dim_2

    @property
    def dim_3(self):
        """Gets the dim_3 of this ShowEventDataRequest.


        :return: The dim_3 of this ShowEventDataRequest.
        :rtype: str
        """
        return self._dim_3

    @dim_3.setter
    def dim_3(self, dim_3):
        """Sets the dim_3 of this ShowEventDataRequest.


        :param dim_3: The dim_3 of this ShowEventDataRequest.
        :type: str
        """
        self._dim_3 = dim_3

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
