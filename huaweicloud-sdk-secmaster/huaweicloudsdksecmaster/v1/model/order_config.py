# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrderConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'threshold_list': 'list[UsageThreshold]',
        'alert_config': 'AlertConfig'
    }

    attribute_map = {
        'threshold_list': 'threshold_list',
        'alert_config': 'alert_config'
    }

    def __init__(self, threshold_list=None, alert_config=None):
        r"""OrderConfig

        The model defined in huaweicloud sdk

        :param threshold_list: 阈值列表
        :type threshold_list: list[:class:`huaweicloudsdksecmaster.v1.UsageThreshold`]
        :param alert_config: 
        :type alert_config: :class:`huaweicloudsdksecmaster.v1.AlertConfig`
        """
        
        

        self._threshold_list = None
        self._alert_config = None
        self.discriminator = None

        if threshold_list is not None:
            self.threshold_list = threshold_list
        if alert_config is not None:
            self.alert_config = alert_config

    @property
    def threshold_list(self):
        r"""Gets the threshold_list of this OrderConfig.

        阈值列表

        :return: The threshold_list of this OrderConfig.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.UsageThreshold`]
        """
        return self._threshold_list

    @threshold_list.setter
    def threshold_list(self, threshold_list):
        r"""Sets the threshold_list of this OrderConfig.

        阈值列表

        :param threshold_list: The threshold_list of this OrderConfig.
        :type threshold_list: list[:class:`huaweicloudsdksecmaster.v1.UsageThreshold`]
        """
        self._threshold_list = threshold_list

    @property
    def alert_config(self):
        r"""Gets the alert_config of this OrderConfig.

        :return: The alert_config of this OrderConfig.
        :rtype: :class:`huaweicloudsdksecmaster.v1.AlertConfig`
        """
        return self._alert_config

    @alert_config.setter
    def alert_config(self, alert_config):
        r"""Sets the alert_config of this OrderConfig.

        :param alert_config: The alert_config of this OrderConfig.
        :type alert_config: :class:`huaweicloudsdksecmaster.v1.AlertConfig`
        """
        self._alert_config = alert_config

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
        if not isinstance(other, OrderConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
