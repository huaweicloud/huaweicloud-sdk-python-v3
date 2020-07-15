# coding: utf-8

import pprint
import re

import six





class RestBulkDelAttendReqBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bulk_del_attend_info': 'list[DelAttendInfo]'
    }

    attribute_map = {
        'bulk_del_attend_info': 'bulkDelAttendInfo'
    }

    def __init__(self, bulk_del_attend_info=None):
        """RestBulkDelAttendReqBody - a model defined in huaweicloud sdk"""
        
        

        self._bulk_del_attend_info = None
        self.discriminator = None

        self.bulk_del_attend_info = bulk_del_attend_info

    @property
    def bulk_del_attend_info(self):
        """Gets the bulk_del_attend_info of this RestBulkDelAttendReqBody.

        待删除列表

        :return: The bulk_del_attend_info of this RestBulkDelAttendReqBody.
        :rtype: list[DelAttendInfo]
        """
        return self._bulk_del_attend_info

    @bulk_del_attend_info.setter
    def bulk_del_attend_info(self, bulk_del_attend_info):
        """Sets the bulk_del_attend_info of this RestBulkDelAttendReqBody.

        待删除列表

        :param bulk_del_attend_info: The bulk_del_attend_info of this RestBulkDelAttendReqBody.
        :type: list[DelAttendInfo]
        """
        self._bulk_del_attend_info = bulk_del_attend_info

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
        if not isinstance(other, RestBulkDelAttendReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
