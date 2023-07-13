# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestAllowWaitingParticipantReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'participant_id': 'str',
        'allow_all': 'bool'
    }

    attribute_map = {
        'participant_id': 'participantID',
        'allow_all': 'allowAll'
    }

    def __init__(self, participant_id=None, allow_all=None):
        """RestAllowWaitingParticipantReqBody

        The model defined in huaweicloud sdk

        :param participant_id: 等候室成员标志。通过监听[[会议级事件推送中的“等候室成员列表信息”](https://support.huaweicloud.com/api-meeting/meeting_21_1507.html)](tag:hws)[[会议级事件推送中的“等候室成员列表信息”](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_1507.html)](tag:hk)事件获得。 
        :type participant_id: str
        :param allow_all: 允许所有等候者入会。 * false：指定等候者 * true：所有等候者入会 
        :type allow_all: bool
        """
        
        

        self._participant_id = None
        self._allow_all = None
        self.discriminator = None

        if participant_id is not None:
            self.participant_id = participant_id
        if allow_all is not None:
            self.allow_all = allow_all

    @property
    def participant_id(self):
        """Gets the participant_id of this RestAllowWaitingParticipantReqBody.

        等候室成员标志。通过监听[[会议级事件推送中的“等候室成员列表信息”](https://support.huaweicloud.com/api-meeting/meeting_21_1507.html)](tag:hws)[[会议级事件推送中的“等候室成员列表信息”](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_1507.html)](tag:hk)事件获得。 

        :return: The participant_id of this RestAllowWaitingParticipantReqBody.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id):
        """Sets the participant_id of this RestAllowWaitingParticipantReqBody.

        等候室成员标志。通过监听[[会议级事件推送中的“等候室成员列表信息”](https://support.huaweicloud.com/api-meeting/meeting_21_1507.html)](tag:hws)[[会议级事件推送中的“等候室成员列表信息”](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_1507.html)](tag:hk)事件获得。 

        :param participant_id: The participant_id of this RestAllowWaitingParticipantReqBody.
        :type participant_id: str
        """
        self._participant_id = participant_id

    @property
    def allow_all(self):
        """Gets the allow_all of this RestAllowWaitingParticipantReqBody.

        允许所有等候者入会。 * false：指定等候者 * true：所有等候者入会 

        :return: The allow_all of this RestAllowWaitingParticipantReqBody.
        :rtype: bool
        """
        return self._allow_all

    @allow_all.setter
    def allow_all(self, allow_all):
        """Sets the allow_all of this RestAllowWaitingParticipantReqBody.

        允许所有等候者入会。 * false：指定等候者 * true：所有等候者入会 

        :param allow_all: The allow_all of this RestAllowWaitingParticipantReqBody.
        :type allow_all: bool
        """
        self._allow_all = allow_all

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
        if not isinstance(other, RestAllowWaitingParticipantReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
