# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        r"""ShowRealTimeInfoOfMeetingResponse

        The model defined in huaweicloud sdk

        :param attendees: 被邀请与会者信息，包括预约会议时邀请的与会者和会中主持人邀请的与会者，已经加入会议的和未加入会议的都返回。
        :type attendees: list[:class:`huaweicloudsdkmeeting.v1.RealTimeAttendee`]
        :param participants: 在线与会者列表信息，包括已加入会议、被邀请正在呼叫中、正在加入会议的与会者列表等。 &gt; * 同一个帐号用不同类型终端（手机端或者PC端等）加入会议时，是不同的在线与会者 &gt; * 未加入或者已离会与会者，不在在线与会者列表中 
        :type participants: list[:class:`huaweicloudsdkmeeting.v1.RealTimeParticipant`]
        :param conf_info: 
        :type conf_info: :class:`huaweicloudsdkmeeting.v1.RealTimeConfInfo`
        """
        
        super(ShowRealTimeInfoOfMeetingResponse, self).__init__()

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
        r"""Gets the attendees of this ShowRealTimeInfoOfMeetingResponse.

        被邀请与会者信息，包括预约会议时邀请的与会者和会中主持人邀请的与会者，已经加入会议的和未加入会议的都返回。

        :return: The attendees of this ShowRealTimeInfoOfMeetingResponse.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.RealTimeAttendee`]
        """
        return self._attendees

    @attendees.setter
    def attendees(self, attendees):
        r"""Sets the attendees of this ShowRealTimeInfoOfMeetingResponse.

        被邀请与会者信息，包括预约会议时邀请的与会者和会中主持人邀请的与会者，已经加入会议的和未加入会议的都返回。

        :param attendees: The attendees of this ShowRealTimeInfoOfMeetingResponse.
        :type attendees: list[:class:`huaweicloudsdkmeeting.v1.RealTimeAttendee`]
        """
        self._attendees = attendees

    @property
    def participants(self):
        r"""Gets the participants of this ShowRealTimeInfoOfMeetingResponse.

        在线与会者列表信息，包括已加入会议、被邀请正在呼叫中、正在加入会议的与会者列表等。 > * 同一个帐号用不同类型终端（手机端或者PC端等）加入会议时，是不同的在线与会者 > * 未加入或者已离会与会者，不在在线与会者列表中 

        :return: The participants of this ShowRealTimeInfoOfMeetingResponse.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.RealTimeParticipant`]
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        r"""Sets the participants of this ShowRealTimeInfoOfMeetingResponse.

        在线与会者列表信息，包括已加入会议、被邀请正在呼叫中、正在加入会议的与会者列表等。 > * 同一个帐号用不同类型终端（手机端或者PC端等）加入会议时，是不同的在线与会者 > * 未加入或者已离会与会者，不在在线与会者列表中 

        :param participants: The participants of this ShowRealTimeInfoOfMeetingResponse.
        :type participants: list[:class:`huaweicloudsdkmeeting.v1.RealTimeParticipant`]
        """
        self._participants = participants

    @property
    def conf_info(self):
        r"""Gets the conf_info of this ShowRealTimeInfoOfMeetingResponse.

        :return: The conf_info of this ShowRealTimeInfoOfMeetingResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.RealTimeConfInfo`
        """
        return self._conf_info

    @conf_info.setter
    def conf_info(self, conf_info):
        r"""Sets the conf_info of this ShowRealTimeInfoOfMeetingResponse.

        :param conf_info: The conf_info of this ShowRealTimeInfoOfMeetingResponse.
        :type conf_info: :class:`huaweicloudsdkmeeting.v1.RealTimeConfInfo`
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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowRealTimeInfoOfMeetingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
