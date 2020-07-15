# coding: utf-8

import pprint
import re

import six





class RestBulkHangUpReqBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bulk_hang_up_participants': 'list[str]'
    }

    attribute_map = {
        'bulk_hang_up_participants': 'bulkHangUpParticipants'
    }

    def __init__(self, bulk_hang_up_participants=None):
        """RestBulkHangUpReqBody - a model defined in huaweicloud sdk"""
        
        

        self._bulk_hang_up_participants = None
        self.discriminator = None

        self.bulk_hang_up_participants = bulk_hang_up_participants

    @property
    def bulk_hang_up_participants(self):
        """Gets the bulk_hang_up_participants of this RestBulkHangUpReqBody.

        批量挂断会场列表，列表元素为与会者标识。

        :return: The bulk_hang_up_participants of this RestBulkHangUpReqBody.
        :rtype: list[str]
        """
        return self._bulk_hang_up_participants

    @bulk_hang_up_participants.setter
    def bulk_hang_up_participants(self, bulk_hang_up_participants):
        """Sets the bulk_hang_up_participants of this RestBulkHangUpReqBody.

        批量挂断会场列表，列表元素为与会者标识。

        :param bulk_hang_up_participants: The bulk_hang_up_participants of this RestBulkHangUpReqBody.
        :type: list[str]
        """
        self._bulk_hang_up_participants = bulk_hang_up_participants

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
        if not isinstance(other, RestBulkHangUpReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
