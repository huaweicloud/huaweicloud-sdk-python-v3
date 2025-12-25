# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NoticeTypeNotificationTemplateList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notice_type': 'str',
        'alarm_notification_template_id': 'str',
        'alarm_notification_template_name': 'str'
    }

    attribute_map = {
        'notice_type': 'notice_type',
        'alarm_notification_template_id': 'alarm_notification_template_id',
        'alarm_notification_template_name': 'alarm_notification_template_name'
    }

    def __init__(self, notice_type=None, alarm_notification_template_id=None, alarm_notification_template_name=None):
        r"""NoticeTypeNotificationTemplateList

        The model defined in huaweicloud sdk

        :param notice_type: 通知类型, sms(短信)/email/http(s)/smn/welink/dingding(钉钉)/wechat(微信)/feishu(飞书)/wecomgroup(微信企业版)
        :type notice_type: str
        :param alarm_notification_template_id: **参数解释**： 通知模板id **约束限制**： 不涉及。 **取值范围**： 长度为[3,64]个字符。 **默认取值**： 不涉及 
        :type alarm_notification_template_id: str
        :param alarm_notification_template_name: **参数解释**： 通知模板名 **约束限制**： 不涉及。 **取值范围**： 长度为[1,200]个字符。 **默认取值**： 不涉及 
        :type alarm_notification_template_name: str
        """
        
        

        self._notice_type = None
        self._alarm_notification_template_id = None
        self._alarm_notification_template_name = None
        self.discriminator = None

        self.notice_type = notice_type
        self.alarm_notification_template_id = alarm_notification_template_id
        if alarm_notification_template_name is not None:
            self.alarm_notification_template_name = alarm_notification_template_name

    @property
    def notice_type(self):
        r"""Gets the notice_type of this NoticeTypeNotificationTemplateList.

        通知类型, sms(短信)/email/http(s)/smn/welink/dingding(钉钉)/wechat(微信)/feishu(飞书)/wecomgroup(微信企业版)

        :return: The notice_type of this NoticeTypeNotificationTemplateList.
        :rtype: str
        """
        return self._notice_type

    @notice_type.setter
    def notice_type(self, notice_type):
        r"""Sets the notice_type of this NoticeTypeNotificationTemplateList.

        通知类型, sms(短信)/email/http(s)/smn/welink/dingding(钉钉)/wechat(微信)/feishu(飞书)/wecomgroup(微信企业版)

        :param notice_type: The notice_type of this NoticeTypeNotificationTemplateList.
        :type notice_type: str
        """
        self._notice_type = notice_type

    @property
    def alarm_notification_template_id(self):
        r"""Gets the alarm_notification_template_id of this NoticeTypeNotificationTemplateList.

        **参数解释**： 通知模板id **约束限制**： 不涉及。 **取值范围**： 长度为[3,64]个字符。 **默认取值**： 不涉及 

        :return: The alarm_notification_template_id of this NoticeTypeNotificationTemplateList.
        :rtype: str
        """
        return self._alarm_notification_template_id

    @alarm_notification_template_id.setter
    def alarm_notification_template_id(self, alarm_notification_template_id):
        r"""Sets the alarm_notification_template_id of this NoticeTypeNotificationTemplateList.

        **参数解释**： 通知模板id **约束限制**： 不涉及。 **取值范围**： 长度为[3,64]个字符。 **默认取值**： 不涉及 

        :param alarm_notification_template_id: The alarm_notification_template_id of this NoticeTypeNotificationTemplateList.
        :type alarm_notification_template_id: str
        """
        self._alarm_notification_template_id = alarm_notification_template_id

    @property
    def alarm_notification_template_name(self):
        r"""Gets the alarm_notification_template_name of this NoticeTypeNotificationTemplateList.

        **参数解释**： 通知模板名 **约束限制**： 不涉及。 **取值范围**： 长度为[1,200]个字符。 **默认取值**： 不涉及 

        :return: The alarm_notification_template_name of this NoticeTypeNotificationTemplateList.
        :rtype: str
        """
        return self._alarm_notification_template_name

    @alarm_notification_template_name.setter
    def alarm_notification_template_name(self, alarm_notification_template_name):
        r"""Sets the alarm_notification_template_name of this NoticeTypeNotificationTemplateList.

        **参数解释**： 通知模板名 **约束限制**： 不涉及。 **取值范围**： 长度为[1,200]个字符。 **默认取值**： 不涉及 

        :param alarm_notification_template_name: The alarm_notification_template_name of this NoticeTypeNotificationTemplateList.
        :type alarm_notification_template_name: str
        """
        self._alarm_notification_template_name = alarm_notification_template_name

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
        if not isinstance(other, NoticeTypeNotificationTemplateList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
