# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TriggerConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'trigger_settings': 'TriggerSetting'
    }

    attribute_map = {
        'type': 'type',
        'trigger_settings': 'trigger_settings'
    }

    def __init__(self, type=None, trigger_settings=None):
        r"""TriggerConfig

        The model defined in huaweicloud sdk

        :param type: 触发类型，镜像签名、老化规则只支持manual(手动)、scheduled(定时+手动)；同步策略支持manual(手动)、scheduled(定时+手动)、event_based(事件触发+手动)
        :type type: str
        :param trigger_settings: 
        :type trigger_settings: :class:`huaweicloudsdkswr.v2.TriggerSetting`
        """
        
        

        self._type = None
        self._trigger_settings = None
        self.discriminator = None

        self.type = type
        if trigger_settings is not None:
            self.trigger_settings = trigger_settings

    @property
    def type(self):
        r"""Gets the type of this TriggerConfig.

        触发类型，镜像签名、老化规则只支持manual(手动)、scheduled(定时+手动)；同步策略支持manual(手动)、scheduled(定时+手动)、event_based(事件触发+手动)

        :return: The type of this TriggerConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TriggerConfig.

        触发类型，镜像签名、老化规则只支持manual(手动)、scheduled(定时+手动)；同步策略支持manual(手动)、scheduled(定时+手动)、event_based(事件触发+手动)

        :param type: The type of this TriggerConfig.
        :type type: str
        """
        self._type = type

    @property
    def trigger_settings(self):
        r"""Gets the trigger_settings of this TriggerConfig.

        :return: The trigger_settings of this TriggerConfig.
        :rtype: :class:`huaweicloudsdkswr.v2.TriggerSetting`
        """
        return self._trigger_settings

    @trigger_settings.setter
    def trigger_settings(self, trigger_settings):
        r"""Sets the trigger_settings of this TriggerConfig.

        :param trigger_settings: The trigger_settings of this TriggerConfig.
        :type trigger_settings: :class:`huaweicloudsdkswr.v2.TriggerSetting`
        """
        self._trigger_settings = trigger_settings

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
        if not isinstance(other, TriggerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
