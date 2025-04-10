# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOneClickAlarmsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'one_click_alarms': 'list[ListOneClickAlarmsRespOneClickAlarms]'
    }

    attribute_map = {
        'one_click_alarms': 'one_click_alarms'
    }

    def __init__(self, one_click_alarms=None):
        r"""ListOneClickAlarmsResponse

        The model defined in huaweicloud sdk

        :param one_click_alarms: 一键告警列表
        :type one_click_alarms: list[:class:`huaweicloudsdkces.v2.ListOneClickAlarmsRespOneClickAlarms`]
        """
        
        super(ListOneClickAlarmsResponse, self).__init__()

        self._one_click_alarms = None
        self.discriminator = None

        if one_click_alarms is not None:
            self.one_click_alarms = one_click_alarms

    @property
    def one_click_alarms(self):
        r"""Gets the one_click_alarms of this ListOneClickAlarmsResponse.

        一键告警列表

        :return: The one_click_alarms of this ListOneClickAlarmsResponse.
        :rtype: list[:class:`huaweicloudsdkces.v2.ListOneClickAlarmsRespOneClickAlarms`]
        """
        return self._one_click_alarms

    @one_click_alarms.setter
    def one_click_alarms(self, one_click_alarms):
        r"""Sets the one_click_alarms of this ListOneClickAlarmsResponse.

        一键告警列表

        :param one_click_alarms: The one_click_alarms of this ListOneClickAlarmsResponse.
        :type one_click_alarms: list[:class:`huaweicloudsdkces.v2.ListOneClickAlarmsRespOneClickAlarms`]
        """
        self._one_click_alarms = one_click_alarms

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
        if not isinstance(other, ListOneClickAlarmsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
