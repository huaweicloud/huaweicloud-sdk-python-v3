# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteOneClickAlarmsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'one_click_alarm_ids': 'list[str]'
    }

    attribute_map = {
        'one_click_alarm_ids': 'one_click_alarm_ids'
    }

    def __init__(self, one_click_alarm_ids=None):
        """BatchDeleteOneClickAlarmsRequestBody

        The model defined in huaweicloud sdk

        :param one_click_alarm_ids: 需要批量删除的一键告警ID列表
        :type one_click_alarm_ids: list[str]
        """
        
        

        self._one_click_alarm_ids = None
        self.discriminator = None

        self.one_click_alarm_ids = one_click_alarm_ids

    @property
    def one_click_alarm_ids(self):
        """Gets the one_click_alarm_ids of this BatchDeleteOneClickAlarmsRequestBody.

        需要批量删除的一键告警ID列表

        :return: The one_click_alarm_ids of this BatchDeleteOneClickAlarmsRequestBody.
        :rtype: list[str]
        """
        return self._one_click_alarm_ids

    @one_click_alarm_ids.setter
    def one_click_alarm_ids(self, one_click_alarm_ids):
        """Sets the one_click_alarm_ids of this BatchDeleteOneClickAlarmsRequestBody.

        需要批量删除的一键告警ID列表

        :param one_click_alarm_ids: The one_click_alarm_ids of this BatchDeleteOneClickAlarmsRequestBody.
        :type one_click_alarm_ids: list[str]
        """
        self._one_click_alarm_ids = one_click_alarm_ids

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
        if not isinstance(other, BatchDeleteOneClickAlarmsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
