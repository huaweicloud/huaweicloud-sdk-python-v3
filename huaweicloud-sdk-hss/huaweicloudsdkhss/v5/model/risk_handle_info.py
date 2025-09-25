# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RiskHandleInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'free_report_info': 'RiskHandleInfoFreeReportInfo',
        'vul_info': 'RiskHandleInfoVulInfo',
        'base_line_info': 'RiskHandleInfoBaseLineInfo',
        'alarm_info': 'RiskHandleInfoAlarmInfo'
    }

    attribute_map = {
        'free_report_info': 'free_report_info',
        'vul_info': 'vul_info',
        'base_line_info': 'base_line_info',
        'alarm_info': 'alarm_info'
    }

    def __init__(self, free_report_info=None, vul_info=None, base_line_info=None, alarm_info=None):
        r"""RiskHandleInfo

        The model defined in huaweicloud sdk

        :param free_report_info: 
        :type free_report_info: :class:`huaweicloudsdkhss.v5.RiskHandleInfoFreeReportInfo`
        :param vul_info: 
        :type vul_info: :class:`huaweicloudsdkhss.v5.RiskHandleInfoVulInfo`
        :param base_line_info: 
        :type base_line_info: :class:`huaweicloudsdkhss.v5.RiskHandleInfoBaseLineInfo`
        :param alarm_info: 
        :type alarm_info: :class:`huaweicloudsdkhss.v5.RiskHandleInfoAlarmInfo`
        """
        
        

        self._free_report_info = None
        self._vul_info = None
        self._base_line_info = None
        self._alarm_info = None
        self.discriminator = None

        if free_report_info is not None:
            self.free_report_info = free_report_info
        if vul_info is not None:
            self.vul_info = vul_info
        if base_line_info is not None:
            self.base_line_info = base_line_info
        if alarm_info is not None:
            self.alarm_info = alarm_info

    @property
    def free_report_info(self):
        r"""Gets the free_report_info of this RiskHandleInfo.

        :return: The free_report_info of this RiskHandleInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.RiskHandleInfoFreeReportInfo`
        """
        return self._free_report_info

    @free_report_info.setter
    def free_report_info(self, free_report_info):
        r"""Sets the free_report_info of this RiskHandleInfo.

        :param free_report_info: The free_report_info of this RiskHandleInfo.
        :type free_report_info: :class:`huaweicloudsdkhss.v5.RiskHandleInfoFreeReportInfo`
        """
        self._free_report_info = free_report_info

    @property
    def vul_info(self):
        r"""Gets the vul_info of this RiskHandleInfo.

        :return: The vul_info of this RiskHandleInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.RiskHandleInfoVulInfo`
        """
        return self._vul_info

    @vul_info.setter
    def vul_info(self, vul_info):
        r"""Sets the vul_info of this RiskHandleInfo.

        :param vul_info: The vul_info of this RiskHandleInfo.
        :type vul_info: :class:`huaweicloudsdkhss.v5.RiskHandleInfoVulInfo`
        """
        self._vul_info = vul_info

    @property
    def base_line_info(self):
        r"""Gets the base_line_info of this RiskHandleInfo.

        :return: The base_line_info of this RiskHandleInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.RiskHandleInfoBaseLineInfo`
        """
        return self._base_line_info

    @base_line_info.setter
    def base_line_info(self, base_line_info):
        r"""Sets the base_line_info of this RiskHandleInfo.

        :param base_line_info: The base_line_info of this RiskHandleInfo.
        :type base_line_info: :class:`huaweicloudsdkhss.v5.RiskHandleInfoBaseLineInfo`
        """
        self._base_line_info = base_line_info

    @property
    def alarm_info(self):
        r"""Gets the alarm_info of this RiskHandleInfo.

        :return: The alarm_info of this RiskHandleInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.RiskHandleInfoAlarmInfo`
        """
        return self._alarm_info

    @alarm_info.setter
    def alarm_info(self, alarm_info):
        r"""Sets the alarm_info of this RiskHandleInfo.

        :param alarm_info: The alarm_info of this RiskHandleInfo.
        :type alarm_info: :class:`huaweicloudsdkhss.v5.RiskHandleInfoAlarmInfo`
        """
        self._alarm_info = alarm_info

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
        if not isinstance(other, RiskHandleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
