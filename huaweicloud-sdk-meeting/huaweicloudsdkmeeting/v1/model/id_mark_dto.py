# coding: utf-8

import pprint
import re

import six





class IdMarkDTO:


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
        'mark': 'str'
    }

    attribute_map = {
        'id': 'id',
        'mark': 'mark'
    }

    def __init__(self, id=None, mark=None):
        """IdMarkDTO - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._mark = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if mark is not None:
            self.mark = mark

    @property
    def id(self):
        """Gets the id of this IdMarkDTO.

        部门编码。

        :return: The id of this IdMarkDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IdMarkDTO.

        部门编码。

        :param id: The id of this IdMarkDTO.
        :type: str
        """
        self._id = id

    @property
    def mark(self):
        """Gets the mark of this IdMarkDTO.

        id对应的回显描述，一般为名称等。

        :return: The mark of this IdMarkDTO.
        :rtype: str
        """
        return self._mark

    @mark.setter
    def mark(self, mark):
        """Sets the mark of this IdMarkDTO.

        id对应的回显描述，一般为名称等。

        :param mark: The mark of this IdMarkDTO.
        :type: str
        """
        self._mark = mark

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
        if not isinstance(other, IdMarkDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
