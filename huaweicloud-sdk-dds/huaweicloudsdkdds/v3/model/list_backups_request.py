# coding: utf-8

import pprint
import re

import six





class ListBackupsRequest:


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
        'backup_id': 'str',
        'backup_type': 'str',
        'offset': 'int',
        'limit': 'int',
        'begin_time': 'str',
        'end_time': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'backup_id': 'backup_id',
        'backup_type': 'backup_type',
        'offset': 'offset',
        'limit': 'limit',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'mode': 'mode'
    }

    def __init__(self, instance_id=None, backup_id=None, backup_type=None, offset=None, limit=None, begin_time=None, end_time=None, mode=None):
        """ListBackupsRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._backup_id = None
        self._backup_type = None
        self._offset = None
        self._limit = None
        self._begin_time = None
        self._end_time = None
        self._mode = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if backup_id is not None:
            self.backup_id = backup_id
        if backup_type is not None:
            self.backup_type = backup_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if mode is not None:
            self.mode = mode

    @property
    def instance_id(self):
        """Gets the instance_id of this ListBackupsRequest.


        :return: The instance_id of this ListBackupsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListBackupsRequest.


        :param instance_id: The instance_id of this ListBackupsRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def backup_id(self):
        """Gets the backup_id of this ListBackupsRequest.


        :return: The backup_id of this ListBackupsRequest.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this ListBackupsRequest.


        :param backup_id: The backup_id of this ListBackupsRequest.
        :type: str
        """
        self._backup_id = backup_id

    @property
    def backup_type(self):
        """Gets the backup_type of this ListBackupsRequest.


        :return: The backup_type of this ListBackupsRequest.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """Sets the backup_type of this ListBackupsRequest.


        :param backup_type: The backup_type of this ListBackupsRequest.
        :type: str
        """
        self._backup_type = backup_type

    @property
    def offset(self):
        """Gets the offset of this ListBackupsRequest.


        :return: The offset of this ListBackupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListBackupsRequest.


        :param offset: The offset of this ListBackupsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListBackupsRequest.


        :return: The limit of this ListBackupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListBackupsRequest.


        :param limit: The limit of this ListBackupsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def begin_time(self):
        """Gets the begin_time of this ListBackupsRequest.


        :return: The begin_time of this ListBackupsRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ListBackupsRequest.


        :param begin_time: The begin_time of this ListBackupsRequest.
        :type: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ListBackupsRequest.


        :return: The end_time of this ListBackupsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListBackupsRequest.


        :param end_time: The end_time of this ListBackupsRequest.
        :type: str
        """
        self._end_time = end_time

    @property
    def mode(self):
        """Gets the mode of this ListBackupsRequest.


        :return: The mode of this ListBackupsRequest.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ListBackupsRequest.


        :param mode: The mode of this ListBackupsRequest.
        :type: str
        """
        self._mode = mode

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
        if not isinstance(other, ListBackupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
