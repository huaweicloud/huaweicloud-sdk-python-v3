# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAlertNoticeConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'alert_id': 'str',
        'body': 'UpdateAlertNoticeConfigRequestBody'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'alert_id': 'alert_id',
        'body': 'body'
    }

    def __init__(self, x_language=None, alert_id=None, body=None):
        """UpdateAlertNoticeConfigRequest

        The model defined in huaweicloud sdk

        :param x_language: zh-cn/en-us
        :type x_language: str
        :param alert_id: 告警通知id
        :type alert_id: str
        :param body: Body of the UpdateAlertNoticeConfigRequest
        :type body: :class:`huaweicloudsdkwaf.v1.UpdateAlertNoticeConfigRequestBody`
        """
        
        

        self._x_language = None
        self._alert_id = None
        self._body = None
        self.discriminator = None

        self.x_language = x_language
        self.alert_id = alert_id
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        """Gets the x_language of this UpdateAlertNoticeConfigRequest.

        zh-cn/en-us

        :return: The x_language of this UpdateAlertNoticeConfigRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this UpdateAlertNoticeConfigRequest.

        zh-cn/en-us

        :param x_language: The x_language of this UpdateAlertNoticeConfigRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def alert_id(self):
        """Gets the alert_id of this UpdateAlertNoticeConfigRequest.

        告警通知id

        :return: The alert_id of this UpdateAlertNoticeConfigRequest.
        :rtype: str
        """
        return self._alert_id

    @alert_id.setter
    def alert_id(self, alert_id):
        """Sets the alert_id of this UpdateAlertNoticeConfigRequest.

        告警通知id

        :param alert_id: The alert_id of this UpdateAlertNoticeConfigRequest.
        :type alert_id: str
        """
        self._alert_id = alert_id

    @property
    def body(self):
        """Gets the body of this UpdateAlertNoticeConfigRequest.

        :return: The body of this UpdateAlertNoticeConfigRequest.
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateAlertNoticeConfigRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateAlertNoticeConfigRequest.

        :param body: The body of this UpdateAlertNoticeConfigRequest.
        :type body: :class:`huaweicloudsdkwaf.v1.UpdateAlertNoticeConfigRequestBody`
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
        if not isinstance(other, UpdateAlertNoticeConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
