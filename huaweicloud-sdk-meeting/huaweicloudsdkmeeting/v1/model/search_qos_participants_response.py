# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class SearchQosParticipantsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'limit': 'int',
        'offset': 'int',
        'data': 'list[QosParticipantInfo]'
    }

    attribute_map = {
        'count': 'count',
        'limit': 'limit',
        'offset': 'offset',
        'data': 'data'
    }

    def __init__(self, count=None, limit=None, offset=None, data=None):
        """SearchQosParticipantsResponse - a model defined in huaweicloud sdk"""
        
        super(SearchQosParticipantsResponse, self).__init__()

        self._count = None
        self._limit = None
        self._offset = None
        self._data = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if data is not None:
            self.data = data

    @property
    def count(self):
        """Gets the count of this SearchQosParticipantsResponse.

        总记录数。

        :return: The count of this SearchQosParticipantsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this SearchQosParticipantsResponse.

        总记录数。

        :param count: The count of this SearchQosParticipantsResponse.
        :type: int
        """
        self._count = count

    @property
    def limit(self):
        """Gets the limit of this SearchQosParticipantsResponse.

        查询条目数量。

        :return: The limit of this SearchQosParticipantsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchQosParticipantsResponse.

        查询条目数量。

        :param limit: The limit of this SearchQosParticipantsResponse.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this SearchQosParticipantsResponse.

        查询偏移量。

        :return: The offset of this SearchQosParticipantsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchQosParticipantsResponse.

        查询偏移量。

        :param offset: The offset of this SearchQosParticipantsResponse.
        :type: int
        """
        self._offset = offset

    @property
    def data(self):
        """Gets the data of this SearchQosParticipantsResponse.

        QoS会议与会者列表。

        :return: The data of this SearchQosParticipantsResponse.
        :rtype: list[QosParticipantInfo]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this SearchQosParticipantsResponse.

        QoS会议与会者列表。

        :param data: The data of this SearchQosParticipantsResponse.
        :type: list[QosParticipantInfo]
        """
        self._data = data

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
        if not isinstance(other, SearchQosParticipantsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
