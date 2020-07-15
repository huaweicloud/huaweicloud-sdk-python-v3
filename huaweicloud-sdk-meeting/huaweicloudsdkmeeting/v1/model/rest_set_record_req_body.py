# coding: utf-8

import pprint
import re

import six





class RestSetRecordReqBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_record': 'int'
    }

    attribute_map = {
        'is_record': 'isRecord'
    }

    def __init__(self, is_record=0):
        """RestSetRecordReqBody - a model defined in huaweicloud sdk"""
        
        

        self._is_record = None
        self.discriminator = None

        self.is_record = is_record

    @property
    def is_record(self):
        """Gets the is_record of this RestSetRecordReqBody.

        默认值为0。 - 0: 停止会议录制。 - 1: 启动会议录制。

        :return: The is_record of this RestSetRecordReqBody.
        :rtype: int
        """
        return self._is_record

    @is_record.setter
    def is_record(self, is_record):
        """Sets the is_record of this RestSetRecordReqBody.

        默认值为0。 - 0: 停止会议录制。 - 1: 启动会议录制。

        :param is_record: The is_record of this RestSetRecordReqBody.
        :type: int
        """
        self._is_record = is_record

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
        if not isinstance(other, RestSetRecordReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
