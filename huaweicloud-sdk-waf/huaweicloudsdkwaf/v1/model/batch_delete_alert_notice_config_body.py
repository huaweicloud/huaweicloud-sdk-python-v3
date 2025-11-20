# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteAlertNoticeConfigBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_notice_configs': 'list[DeleteAlertNoticeConfigBody]'
    }

    attribute_map = {
        'alert_notice_configs': 'alert_notice_configs'
    }

    def __init__(self, alert_notice_configs=None):
        r"""BatchDeleteAlertNoticeConfigBody

        The model defined in huaweicloud sdk

        :param alert_notice_configs: **参数解释：** 需要删除的告警id列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type alert_notice_configs: list[:class:`huaweicloudsdkwaf.v1.DeleteAlertNoticeConfigBody`]
        """
        
        

        self._alert_notice_configs = None
        self.discriminator = None

        self.alert_notice_configs = alert_notice_configs

    @property
    def alert_notice_configs(self):
        r"""Gets the alert_notice_configs of this BatchDeleteAlertNoticeConfigBody.

        **参数解释：** 需要删除的告警id列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The alert_notice_configs of this BatchDeleteAlertNoticeConfigBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.DeleteAlertNoticeConfigBody`]
        """
        return self._alert_notice_configs

    @alert_notice_configs.setter
    def alert_notice_configs(self, alert_notice_configs):
        r"""Sets the alert_notice_configs of this BatchDeleteAlertNoticeConfigBody.

        **参数解释：** 需要删除的告警id列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param alert_notice_configs: The alert_notice_configs of this BatchDeleteAlertNoticeConfigBody.
        :type alert_notice_configs: list[:class:`huaweicloudsdkwaf.v1.DeleteAlertNoticeConfigBody`]
        """
        self._alert_notice_configs = alert_notice_configs

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchDeleteAlertNoticeConfigBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
