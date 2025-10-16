# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlertNoticeConfigList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_notice_configs': 'list[AlertNoticeConfig]'
    }

    attribute_map = {
        'alert_notice_configs': 'alert_notice_configs'
    }

    def __init__(self, alert_notice_configs=None):
        r"""AlertNoticeConfigList

        The model defined in huaweicloud sdk

        :param alert_notice_configs: **参数解释：** 告警通知配置列表，包含多条告警通知配置信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type alert_notice_configs: list[:class:`huaweicloudsdkwaf.v1.AlertNoticeConfig`]
        """
        
        

        self._alert_notice_configs = None
        self.discriminator = None

        self.alert_notice_configs = alert_notice_configs

    @property
    def alert_notice_configs(self):
        r"""Gets the alert_notice_configs of this AlertNoticeConfigList.

        **参数解释：** 告警通知配置列表，包含多条告警通知配置信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The alert_notice_configs of this AlertNoticeConfigList.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.AlertNoticeConfig`]
        """
        return self._alert_notice_configs

    @alert_notice_configs.setter
    def alert_notice_configs(self, alert_notice_configs):
        r"""Sets the alert_notice_configs of this AlertNoticeConfigList.

        **参数解释：** 告警通知配置列表，包含多条告警通知配置信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param alert_notice_configs: The alert_notice_configs of this AlertNoticeConfigList.
        :type alert_notice_configs: list[:class:`huaweicloudsdkwaf.v1.AlertNoticeConfig`]
        """
        self._alert_notice_configs = alert_notice_configs

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
        if not isinstance(other, AlertNoticeConfigList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
