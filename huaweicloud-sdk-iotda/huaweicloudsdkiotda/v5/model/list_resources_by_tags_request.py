# coding: utf-8

import pprint
import re

import six





class ListResourcesByTagsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'offset': 'int',
        'body': 'QueryResourceByTagsDTO'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'limit': 'limit',
        'marker': 'marker',
        'offset': 'offset',
        'body': 'body'
    }

    def __init__(self, instance_id=None, limit=10, marker='ffffffffffffffffffffffff', offset=0, body=None):
        """ListResourcesByTagsRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._limit = None
        self._marker = None
        self._offset = None
        self._body = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this ListResourcesByTagsRequest.


        :return: The instance_id of this ListResourcesByTagsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListResourcesByTagsRequest.


        :param instance_id: The instance_id of this ListResourcesByTagsRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this ListResourcesByTagsRequest.


        :return: The limit of this ListResourcesByTagsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListResourcesByTagsRequest.


        :param limit: The limit of this ListResourcesByTagsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListResourcesByTagsRequest.


        :return: The marker of this ListResourcesByTagsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListResourcesByTagsRequest.


        :param marker: The marker of this ListResourcesByTagsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def offset(self):
        """Gets the offset of this ListResourcesByTagsRequest.


        :return: The offset of this ListResourcesByTagsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListResourcesByTagsRequest.


        :param offset: The offset of this ListResourcesByTagsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def body(self):
        """Gets the body of this ListResourcesByTagsRequest.


        :return: The body of this ListResourcesByTagsRequest.
        :rtype: QueryResourceByTagsDTO
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListResourcesByTagsRequest.


        :param body: The body of this ListResourcesByTagsRequest.
        :type: QueryResourceByTagsDTO
        """
        self._body = body

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
        if not isinstance(other, ListResourcesByTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
