# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebHookEventCfgDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_type': 'str',
        'cfgs': 'str'
    }

    attribute_map = {
        'event_type': 'event_type',
        'cfgs': 'cfgs'
    }

    def __init__(self, event_type=None, cfgs=None):
        r"""WebHookEventCfgDto

        The model defined in huaweicloud sdk

        :param event_type: **参数解释：** 事件类型。 **取值范围：** 最小1个字节，最大255字节
        :type event_type: str
        :param cfgs: **参数解释：** 配置信息。 **取值范围：** 最小1个字节，最大255字节
        :type cfgs: str
        """
        
        

        self._event_type = None
        self._cfgs = None
        self.discriminator = None

        if event_type is not None:
            self.event_type = event_type
        if cfgs is not None:
            self.cfgs = cfgs

    @property
    def event_type(self):
        r"""Gets the event_type of this WebHookEventCfgDto.

        **参数解释：** 事件类型。 **取值范围：** 最小1个字节，最大255字节

        :return: The event_type of this WebHookEventCfgDto.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this WebHookEventCfgDto.

        **参数解释：** 事件类型。 **取值范围：** 最小1个字节，最大255字节

        :param event_type: The event_type of this WebHookEventCfgDto.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def cfgs(self):
        r"""Gets the cfgs of this WebHookEventCfgDto.

        **参数解释：** 配置信息。 **取值范围：** 最小1个字节，最大255字节

        :return: The cfgs of this WebHookEventCfgDto.
        :rtype: str
        """
        return self._cfgs

    @cfgs.setter
    def cfgs(self, cfgs):
        r"""Sets the cfgs of this WebHookEventCfgDto.

        **参数解释：** 配置信息。 **取值范围：** 最小1个字节，最大255字节

        :param cfgs: The cfgs of this WebHookEventCfgDto.
        :type cfgs: str
        """
        self._cfgs = cfgs

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
        if not isinstance(other, WebHookEventCfgDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
