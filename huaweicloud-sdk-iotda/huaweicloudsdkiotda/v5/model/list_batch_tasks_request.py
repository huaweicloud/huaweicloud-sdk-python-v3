# coding: utf-8

import pprint
import re

import six





class ListBatchTasksRequest:


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
        'app_id': 'str',
        'task_type': 'str',
        'status': 'str',
        'limit': 'int',
        'marker': 'str',
        'offset': 'int'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'app_id': 'app_id',
        'task_type': 'task_type',
        'status': 'status',
        'limit': 'limit',
        'marker': 'marker',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, app_id=None, task_type=None, status=None, limit=10, marker='ffffffffffffffffffffffff', offset=0):
        """ListBatchTasksRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._app_id = None
        self._task_type = None
        self._status = None
        self._limit = None
        self._marker = None
        self._offset = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if app_id is not None:
            self.app_id = app_id
        self.task_type = task_type
        if status is not None:
            self.status = status
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        """Gets the instance_id of this ListBatchTasksRequest.


        :return: The instance_id of this ListBatchTasksRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListBatchTasksRequest.


        :param instance_id: The instance_id of this ListBatchTasksRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def app_id(self):
        """Gets the app_id of this ListBatchTasksRequest.


        :return: The app_id of this ListBatchTasksRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListBatchTasksRequest.


        :param app_id: The app_id of this ListBatchTasksRequest.
        :type: str
        """
        self._app_id = app_id

    @property
    def task_type(self):
        """Gets the task_type of this ListBatchTasksRequest.


        :return: The task_type of this ListBatchTasksRequest.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this ListBatchTasksRequest.


        :param task_type: The task_type of this ListBatchTasksRequest.
        :type: str
        """
        self._task_type = task_type

    @property
    def status(self):
        """Gets the status of this ListBatchTasksRequest.


        :return: The status of this ListBatchTasksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListBatchTasksRequest.


        :param status: The status of this ListBatchTasksRequest.
        :type: str
        """
        self._status = status

    @property
    def limit(self):
        """Gets the limit of this ListBatchTasksRequest.


        :return: The limit of this ListBatchTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListBatchTasksRequest.


        :param limit: The limit of this ListBatchTasksRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListBatchTasksRequest.


        :return: The marker of this ListBatchTasksRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListBatchTasksRequest.


        :param marker: The marker of this ListBatchTasksRequest.
        :type: str
        """
        self._marker = marker

    @property
    def offset(self):
        """Gets the offset of this ListBatchTasksRequest.


        :return: The offset of this ListBatchTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListBatchTasksRequest.


        :param offset: The offset of this ListBatchTasksRequest.
        :type: int
        """
        self._offset = offset

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
        if not isinstance(other, ListBatchTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
