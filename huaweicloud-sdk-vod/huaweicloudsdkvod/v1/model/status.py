# coding: utf-8

import pprint
import re

import six





class Status:
    """
    allowed enum values
    """

    UNCREATED = "UNCREATED"
    DELETED = "DELETED"
    CANCELLED = "CANCELLED"
    SERVER_ERROR = "SERVER_ERROR"
    UPLOAD_FAILED = "UPLOAD_FAILED"
    CREATING = "CREATING"
    PUBLISHED = "PUBLISHED"
    WAITING_TRANSCODE = "WAITING_TRANSCODE"
    TRANSCODING = "TRANSCODING"
    TRANSCODE_FAILED = "TRANSCODE_FAILED"
    TRANSCODE_SUCCEED = "TRANSCODE_SUCCEED"
    CREATED = "CREATED"
    UNPUBLISHED = "UNPUBLISHED"
    NO_ASSET = "NO_ASSET"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"
    OBS_CREATING = "OBS_CREATING"
    OBS_CREATE_FAILED = "OBS_CREATE_FAILED"
    OBS_CREATE_SUCCESS = "OBS_CREATE_SUCCESS"
    UNKNOW = "UNkNOW"

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self):
        """Status - a model defined in huaweicloud sdk"""
        
        
        self.discriminator = None

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
        if not isinstance(other, Status):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
