# coding: utf-8

import pprint
import re

import six





class ListDeviceGroupsRequest:


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
        'last_modified_time': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'limit': 'limit',
        'marker': 'marker',
        'offset': 'offset',
        'last_modified_time': 'last_modified_time',
        'app_id': 'app_id'
    }

    def __init__(self, instance_id=None, limit=10, marker='ffffffffffffffffffffffff', offset=0, last_modified_time=None, app_id=None):
        """ListDeviceGroupsRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._limit = None
        self._marker = None
        self._offset = None
        self._last_modified_time = None
        self._app_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if app_id is not None:
            self.app_id = app_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ListDeviceGroupsRequest.


        :return: The instance_id of this ListDeviceGroupsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListDeviceGroupsRequest.


        :param instance_id: The instance_id of this ListDeviceGroupsRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this ListDeviceGroupsRequest.


        :return: The limit of this ListDeviceGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDeviceGroupsRequest.


        :param limit: The limit of this ListDeviceGroupsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListDeviceGroupsRequest.


        :return: The marker of this ListDeviceGroupsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListDeviceGroupsRequest.


        :param marker: The marker of this ListDeviceGroupsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def offset(self):
        """Gets the offset of this ListDeviceGroupsRequest.


        :return: The offset of this ListDeviceGroupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDeviceGroupsRequest.


        :param offset: The offset of this ListDeviceGroupsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this ListDeviceGroupsRequest.


        :return: The last_modified_time of this ListDeviceGroupsRequest.
        :rtype: str
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this ListDeviceGroupsRequest.


        :param last_modified_time: The last_modified_time of this ListDeviceGroupsRequest.
        :type: str
        """
        self._last_modified_time = last_modified_time

    @property
    def app_id(self):
        """Gets the app_id of this ListDeviceGroupsRequest.


        :return: The app_id of this ListDeviceGroupsRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListDeviceGroupsRequest.


        :param app_id: The app_id of this ListDeviceGroupsRequest.
        :type: str
        """
        self._app_id = app_id

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
        if not isinstance(other, ListDeviceGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
