# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowOnlineMeetingDetailResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'conference_data': 'ConferenceInfo',
        'data': 'PageParticipant'
    }

    attribute_map = {
        'conference_data': 'conferenceData',
        'data': 'data'
    }

    def __init__(self, conference_data=None, data=None):
        """ShowOnlineMeetingDetailResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._conference_data = None
        self._data = None
        self.discriminator = None

        if conference_data is not None:
            self.conference_data = conference_data
        if data is not None:
            self.data = data

    @property
    def conference_data(self):
        """Gets the conference_data of this ShowOnlineMeetingDetailResponse.


        :return: The conference_data of this ShowOnlineMeetingDetailResponse.
        :rtype: ConferenceInfo
        """
        return self._conference_data

    @conference_data.setter
    def conference_data(self, conference_data):
        """Sets the conference_data of this ShowOnlineMeetingDetailResponse.


        :param conference_data: The conference_data of this ShowOnlineMeetingDetailResponse.
        :type: ConferenceInfo
        """
        self._conference_data = conference_data

    @property
    def data(self):
        """Gets the data of this ShowOnlineMeetingDetailResponse.


        :return: The data of this ShowOnlineMeetingDetailResponse.
        :rtype: PageParticipant
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ShowOnlineMeetingDetailResponse.


        :param data: The data of this ShowOnlineMeetingDetailResponse.
        :type: PageParticipant
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
        if not isinstance(other, ShowOnlineMeetingDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
