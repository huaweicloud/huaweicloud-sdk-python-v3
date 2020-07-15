# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowRealTimeInfoOfMeetingResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'attendees': 'list[RealTimeAttendee]',
        'participants': 'list[RealTimeParticipant]',
        'conf_info': 'RealTimeConfInfo'
    }

    attribute_map = {
        'attendees': 'attendees',
        'participants': 'participants',
        'conf_info': 'confInfo'
    }

    def __init__(self, attendees=None, participants=None, conf_info=None):
        """ShowRealTimeInfoOfMeetingResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._attendees = None
        self._participants = None
        self._conf_info = None
        self.discriminator = None

        if attendees is not None:
            self.attendees = attendees
        if participants is not None:
            self.participants = participants
        if conf_info is not None:
            self.conf_info = conf_info

    @property
    def attendees(self):
        """Gets the attendees of this ShowRealTimeInfoOfMeetingResponse.

        所有参加会议的与会者列表，包括未入会的以及在线的与会者信息。

        :return: The attendees of this ShowRealTimeInfoOfMeetingResponse.
        :rtype: list[RealTimeAttendee]
        """
        return self._attendees

    @attendees.setter
    def attendees(self, attendees):
        """Sets the attendees of this ShowRealTimeInfoOfMeetingResponse.

        所有参加会议的与会者列表，包括未入会的以及在线的与会者信息。

        :param attendees: The attendees of this ShowRealTimeInfoOfMeetingResponse.
        :type: list[RealTimeAttendee]
        """
        self._attendees = attendees

    @property
    def participants(self):
        """Gets the participants of this ShowRealTimeInfoOfMeetingResponse.

        在线会场列表，包括已进入会议、呼叫中、正在加入会议的与会者列表等。

        :return: The participants of this ShowRealTimeInfoOfMeetingResponse.
        :rtype: list[RealTimeParticipant]
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """Sets the participants of this ShowRealTimeInfoOfMeetingResponse.

        在线会场列表，包括已进入会议、呼叫中、正在加入会议的与会者列表等。

        :param participants: The participants of this ShowRealTimeInfoOfMeetingResponse.
        :type: list[RealTimeParticipant]
        """
        self._participants = participants

    @property
    def conf_info(self):
        """Gets the conf_info of this ShowRealTimeInfoOfMeetingResponse.


        :return: The conf_info of this ShowRealTimeInfoOfMeetingResponse.
        :rtype: RealTimeConfInfo
        """
        return self._conf_info

    @conf_info.setter
    def conf_info(self, conf_info):
        """Sets the conf_info of this ShowRealTimeInfoOfMeetingResponse.


        :param conf_info: The conf_info of this ShowRealTimeInfoOfMeetingResponse.
        :type: RealTimeConfInfo
        """
        self._conf_info = conf_info

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
        if not isinstance(other, ShowRealTimeInfoOfMeetingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
