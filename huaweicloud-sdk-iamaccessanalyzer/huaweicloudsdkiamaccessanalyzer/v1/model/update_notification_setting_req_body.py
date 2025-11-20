# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNotificationSettingReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mc_switch': 'bool',
        'smn_topic_urns': 'list[str]'
    }

    attribute_map = {
        'mc_switch': 'mc_switch',
        'smn_topic_urns': 'smn_topic_urns'
    }

    def __init__(self, mc_switch=None, smn_topic_urns=None):
        r"""UpdateNotificationSettingReqBody

        The model defined in huaweicloud sdk

        :param mc_switch: 是否开启消息中心通知开关。
        :type mc_switch: bool
        :param smn_topic_urns: 消息通知配置的SMN主题URN列表。
        :type smn_topic_urns: list[str]
        """
        
        

        self._mc_switch = None
        self._smn_topic_urns = None
        self.discriminator = None

        self.mc_switch = mc_switch
        self.smn_topic_urns = smn_topic_urns

    @property
    def mc_switch(self):
        r"""Gets the mc_switch of this UpdateNotificationSettingReqBody.

        是否开启消息中心通知开关。

        :return: The mc_switch of this UpdateNotificationSettingReqBody.
        :rtype: bool
        """
        return self._mc_switch

    @mc_switch.setter
    def mc_switch(self, mc_switch):
        r"""Sets the mc_switch of this UpdateNotificationSettingReqBody.

        是否开启消息中心通知开关。

        :param mc_switch: The mc_switch of this UpdateNotificationSettingReqBody.
        :type mc_switch: bool
        """
        self._mc_switch = mc_switch

    @property
    def smn_topic_urns(self):
        r"""Gets the smn_topic_urns of this UpdateNotificationSettingReqBody.

        消息通知配置的SMN主题URN列表。

        :return: The smn_topic_urns of this UpdateNotificationSettingReqBody.
        :rtype: list[str]
        """
        return self._smn_topic_urns

    @smn_topic_urns.setter
    def smn_topic_urns(self, smn_topic_urns):
        r"""Sets the smn_topic_urns of this UpdateNotificationSettingReqBody.

        消息通知配置的SMN主题URN列表。

        :param smn_topic_urns: The smn_topic_urns of this UpdateNotificationSettingReqBody.
        :type smn_topic_urns: list[str]
        """
        self._smn_topic_urns = smn_topic_urns

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
        if not isinstance(other, UpdateNotificationSettingReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
