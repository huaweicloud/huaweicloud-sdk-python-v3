# coding: utf-8

import pprint
import re

import six





class ProtocolResult:


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
        'mapping_id': 'str',
        'links': 'ProtocolLinks'
    }

    attribute_map = {
        'id': 'id',
        'mapping_id': 'mapping_id',
        'links': 'links'
    }

    def __init__(self, id=None, mapping_id=None, links=None):
        """ProtocolResult - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._mapping_id = None
        self._links = None
        self.discriminator = None

        self.id = id
        self.mapping_id = mapping_id
        self.links = links

    @property
    def id(self):
        """Gets the id of this ProtocolResult.

        协议ID。

        :return: The id of this ProtocolResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProtocolResult.

        协议ID。

        :param id: The id of this ProtocolResult.
        :type: str
        """
        self._id = id

    @property
    def mapping_id(self):
        """Gets the mapping_id of this ProtocolResult.

        映射ID。

        :return: The mapping_id of this ProtocolResult.
        :rtype: str
        """
        return self._mapping_id

    @mapping_id.setter
    def mapping_id(self, mapping_id):
        """Sets the mapping_id of this ProtocolResult.

        映射ID。

        :param mapping_id: The mapping_id of this ProtocolResult.
        :type: str
        """
        self._mapping_id = mapping_id

    @property
    def links(self):
        """Gets the links of this ProtocolResult.


        :return: The links of this ProtocolResult.
        :rtype: ProtocolLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ProtocolResult.


        :param links: The links of this ProtocolResult.
        :type: ProtocolLinks
        """
        self._links = links

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
        if not isinstance(other, ProtocolResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
