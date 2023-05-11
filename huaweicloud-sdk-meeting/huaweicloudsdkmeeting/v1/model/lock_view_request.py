# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LockViewRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'conference_id': 'str',
        'participant_id': 'str',
        'x_conference_authorization': 'str',
        'body': 'RestLockSiteViewReqBody'
    }

    attribute_map = {
        'conference_id': 'conferenceID',
        'participant_id': 'participantID',
        'x_conference_authorization': 'X-Conference-Authorization',
        'body': 'body'
    }

    def __init__(self, conference_id=None, participant_id=None, x_conference_authorization=None, body=None):
        """LockViewRequest

        The model defined in huaweicloud sdk

        :param conference_id: 会议ID。
        :type conference_id: str
        :param participant_id: 专业会议终端的与会者标识。
        :type participant_id: str
        :param x_conference_authorization: 会控Token，通过[[获取会控token](https://support.huaweicloud.com/api-meeting/meeting_21_0027.html)](tag:hws)[[获取会控token](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0027.html)](tag:hk)接口获得。
        :type x_conference_authorization: str
        :param body: Body of the LockViewRequest
        :type body: :class:`huaweicloudsdkmeeting.v1.RestLockSiteViewReqBody`
        """
        
        

        self._conference_id = None
        self._participant_id = None
        self._x_conference_authorization = None
        self._body = None
        self.discriminator = None

        self.conference_id = conference_id
        self.participant_id = participant_id
        self.x_conference_authorization = x_conference_authorization
        if body is not None:
            self.body = body

    @property
    def conference_id(self):
        """Gets the conference_id of this LockViewRequest.

        会议ID。

        :return: The conference_id of this LockViewRequest.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this LockViewRequest.

        会议ID。

        :param conference_id: The conference_id of this LockViewRequest.
        :type conference_id: str
        """
        self._conference_id = conference_id

    @property
    def participant_id(self):
        """Gets the participant_id of this LockViewRequest.

        专业会议终端的与会者标识。

        :return: The participant_id of this LockViewRequest.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id):
        """Sets the participant_id of this LockViewRequest.

        专业会议终端的与会者标识。

        :param participant_id: The participant_id of this LockViewRequest.
        :type participant_id: str
        """
        self._participant_id = participant_id

    @property
    def x_conference_authorization(self):
        """Gets the x_conference_authorization of this LockViewRequest.

        会控Token，通过[[获取会控token](https://support.huaweicloud.com/api-meeting/meeting_21_0027.html)](tag:hws)[[获取会控token](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0027.html)](tag:hk)接口获得。

        :return: The x_conference_authorization of this LockViewRequest.
        :rtype: str
        """
        return self._x_conference_authorization

    @x_conference_authorization.setter
    def x_conference_authorization(self, x_conference_authorization):
        """Sets the x_conference_authorization of this LockViewRequest.

        会控Token，通过[[获取会控token](https://support.huaweicloud.com/api-meeting/meeting_21_0027.html)](tag:hws)[[获取会控token](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0027.html)](tag:hk)接口获得。

        :param x_conference_authorization: The x_conference_authorization of this LockViewRequest.
        :type x_conference_authorization: str
        """
        self._x_conference_authorization = x_conference_authorization

    @property
    def body(self):
        """Gets the body of this LockViewRequest.

        :return: The body of this LockViewRequest.
        :rtype: :class:`huaweicloudsdkmeeting.v1.RestLockSiteViewReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this LockViewRequest.

        :param body: The body of this LockViewRequest.
        :type body: :class:`huaweicloudsdkmeeting.v1.RestLockSiteViewReqBody`
        """
        self._body = body

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
        if not isinstance(other, LockViewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
