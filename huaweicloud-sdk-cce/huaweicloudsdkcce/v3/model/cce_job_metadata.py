# coding: utf-8

import pprint
import re

import six





class CCEJobMetadata:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'creation_timestamp': 'str',
        'uid': 'str',
        'update_timestamp': 'str'
    }

    attribute_map = {
        'creation_timestamp': 'creationTimestamp',
        'uid': 'uid',
        'update_timestamp': 'updateTimestamp'
    }

    def __init__(self, creation_timestamp=None, uid=None, update_timestamp=None):
        """CCEJobMetadata - a model defined in huaweicloud sdk"""
        
        

        self._creation_timestamp = None
        self._uid = None
        self._update_timestamp = None
        self.discriminator = None

        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if uid is not None:
            self.uid = uid
        if update_timestamp is not None:
            self.update_timestamp = update_timestamp

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this CCEJobMetadata.

        作业的创建时间。

        :return: The creation_timestamp of this CCEJobMetadata.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this CCEJobMetadata.

        作业的创建时间。

        :param creation_timestamp: The creation_timestamp of this CCEJobMetadata.
        :type: str
        """
        self._creation_timestamp = creation_timestamp

    @property
    def uid(self):
        """Gets the uid of this CCEJobMetadata.

        作业的ID。

        :return: The uid of this CCEJobMetadata.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this CCEJobMetadata.

        作业的ID。

        :param uid: The uid of this CCEJobMetadata.
        :type: str
        """
        self._uid = uid

    @property
    def update_timestamp(self):
        """Gets the update_timestamp of this CCEJobMetadata.

        作业的更新时间。

        :return: The update_timestamp of this CCEJobMetadata.
        :rtype: str
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        """Sets the update_timestamp of this CCEJobMetadata.

        作业的更新时间。

        :param update_timestamp: The update_timestamp of this CCEJobMetadata.
        :type: str
        """
        self._update_timestamp = update_timestamp

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
        if not isinstance(other, CCEJobMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
