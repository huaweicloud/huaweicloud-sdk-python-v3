# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateOneClickAlarmsEnabledStateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'one_click_alarm_id': 'str',
        'body': 'BatchEnableAlarmsRequestBody'
    }

    attribute_map = {
        'one_click_alarm_id': 'one_click_alarm_id',
        'body': 'body'
    }

    def __init__(self, one_click_alarm_id=None, body=None):
        """BatchUpdateOneClickAlarmsEnabledStateRequest

        The model defined in huaweicloud sdk

        :param one_click_alarm_id: 一键告警ID
        :type one_click_alarm_id: str
        :param body: Body of the BatchUpdateOneClickAlarmsEnabledStateRequest
        :type body: :class:`huaweicloudsdkces.v2.BatchEnableAlarmsRequestBody`
        """
        
        

        self._one_click_alarm_id = None
        self._body = None
        self.discriminator = None

        self.one_click_alarm_id = one_click_alarm_id
        if body is not None:
            self.body = body

    @property
    def one_click_alarm_id(self):
        """Gets the one_click_alarm_id of this BatchUpdateOneClickAlarmsEnabledStateRequest.

        一键告警ID

        :return: The one_click_alarm_id of this BatchUpdateOneClickAlarmsEnabledStateRequest.
        :rtype: str
        """
        return self._one_click_alarm_id

    @one_click_alarm_id.setter
    def one_click_alarm_id(self, one_click_alarm_id):
        """Sets the one_click_alarm_id of this BatchUpdateOneClickAlarmsEnabledStateRequest.

        一键告警ID

        :param one_click_alarm_id: The one_click_alarm_id of this BatchUpdateOneClickAlarmsEnabledStateRequest.
        :type one_click_alarm_id: str
        """
        self._one_click_alarm_id = one_click_alarm_id

    @property
    def body(self):
        """Gets the body of this BatchUpdateOneClickAlarmsEnabledStateRequest.

        :return: The body of this BatchUpdateOneClickAlarmsEnabledStateRequest.
        :rtype: :class:`huaweicloudsdkces.v2.BatchEnableAlarmsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchUpdateOneClickAlarmsEnabledStateRequest.

        :param body: The body of this BatchUpdateOneClickAlarmsEnabledStateRequest.
        :type body: :class:`huaweicloudsdkces.v2.BatchEnableAlarmsRequestBody`
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
        if not isinstance(other, BatchUpdateOneClickAlarmsEnabledStateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
