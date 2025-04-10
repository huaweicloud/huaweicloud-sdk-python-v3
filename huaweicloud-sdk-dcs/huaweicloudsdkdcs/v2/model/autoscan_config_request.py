# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoscanConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_auto_scan': 'bool',
        'schedule_at': 'list[str]'
    }

    attribute_map = {
        'enable_auto_scan': 'enable_auto_scan',
        'schedule_at': 'schedule_at'
    }

    def __init__(self, enable_auto_scan=None, schedule_at=None):
        r"""AutoscanConfigRequest

        The model defined in huaweicloud sdk

        :param enable_auto_scan: 是否开启自动分析
        :type enable_auto_scan: bool
        :param schedule_at: 每日分析时间，时间格式为21:00，时间为UTC时间
        :type schedule_at: list[str]
        """
        
        

        self._enable_auto_scan = None
        self._schedule_at = None
        self.discriminator = None

        self.enable_auto_scan = enable_auto_scan
        self.schedule_at = schedule_at

    @property
    def enable_auto_scan(self):
        r"""Gets the enable_auto_scan of this AutoscanConfigRequest.

        是否开启自动分析

        :return: The enable_auto_scan of this AutoscanConfigRequest.
        :rtype: bool
        """
        return self._enable_auto_scan

    @enable_auto_scan.setter
    def enable_auto_scan(self, enable_auto_scan):
        r"""Sets the enable_auto_scan of this AutoscanConfigRequest.

        是否开启自动分析

        :param enable_auto_scan: The enable_auto_scan of this AutoscanConfigRequest.
        :type enable_auto_scan: bool
        """
        self._enable_auto_scan = enable_auto_scan

    @property
    def schedule_at(self):
        r"""Gets the schedule_at of this AutoscanConfigRequest.

        每日分析时间，时间格式为21:00，时间为UTC时间

        :return: The schedule_at of this AutoscanConfigRequest.
        :rtype: list[str]
        """
        return self._schedule_at

    @schedule_at.setter
    def schedule_at(self, schedule_at):
        r"""Sets the schedule_at of this AutoscanConfigRequest.

        每日分析时间，时间格式为21:00，时间为UTC时间

        :param schedule_at: The schedule_at of this AutoscanConfigRequest.
        :type schedule_at: list[str]
        """
        self._schedule_at = schedule_at

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
        if not isinstance(other, AutoscanConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
