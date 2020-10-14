# coding: utf-8

import pprint
import re

import six





class ListHotKeyScanTasksRequest:


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
        'offset': 'int',
        'limit': 'int',
        'status': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'status': 'status'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, status=None):
        """ListHotKeyScanTasksRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._status = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if status is not None:
            self.status = status

    @property
    def instance_id(self):
        """Gets the instance_id of this ListHotKeyScanTasksRequest.


        :return: The instance_id of this ListHotKeyScanTasksRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListHotKeyScanTasksRequest.


        :param instance_id: The instance_id of this ListHotKeyScanTasksRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ListHotKeyScanTasksRequest.


        :return: The offset of this ListHotKeyScanTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListHotKeyScanTasksRequest.


        :param offset: The offset of this ListHotKeyScanTasksRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListHotKeyScanTasksRequest.


        :return: The limit of this ListHotKeyScanTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListHotKeyScanTasksRequest.


        :param limit: The limit of this ListHotKeyScanTasksRequest.
        :type: int
        """
        self._limit = limit

    @property
    def status(self):
        """Gets the status of this ListHotKeyScanTasksRequest.


        :return: The status of this ListHotKeyScanTasksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListHotKeyScanTasksRequest.


        :param status: The status of this ListHotKeyScanTasksRequest.
        :type: str
        """
        self._status = status

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
        if not isinstance(other, ListHotKeyScanTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
