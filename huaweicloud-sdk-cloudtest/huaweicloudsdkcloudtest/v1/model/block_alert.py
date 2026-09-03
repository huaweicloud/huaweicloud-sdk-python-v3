# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BlockAlert:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_template': 'AlertTemplate',
        'enable': 'str',
        'waiting_count': 'int'
    }

    attribute_map = {
        'alert_template': 'alert_template',
        'enable': 'enable',
        'waiting_count': 'waitingCount'
    }

    def __init__(self, alert_template=None, enable=None, waiting_count=None):
        r"""BlockAlert

        The model defined in huaweicloud sdk

        :param alert_template: 
        :type alert_template: :class:`huaweicloudsdkcloudtest.v1.AlertTemplate`
        :param enable: 阻塞告警开启 0关闭 1开启
        :type enable: str
        :param waiting_count: 等待队列大于多少个开始阻塞
        :type waiting_count: int
        """
        
        

        self._alert_template = None
        self._enable = None
        self._waiting_count = None
        self.discriminator = None

        if alert_template is not None:
            self.alert_template = alert_template
        if enable is not None:
            self.enable = enable
        if waiting_count is not None:
            self.waiting_count = waiting_count

    @property
    def alert_template(self):
        r"""Gets the alert_template of this BlockAlert.

        :return: The alert_template of this BlockAlert.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AlertTemplate`
        """
        return self._alert_template

    @alert_template.setter
    def alert_template(self, alert_template):
        r"""Sets the alert_template of this BlockAlert.

        :param alert_template: The alert_template of this BlockAlert.
        :type alert_template: :class:`huaweicloudsdkcloudtest.v1.AlertTemplate`
        """
        self._alert_template = alert_template

    @property
    def enable(self):
        r"""Gets the enable of this BlockAlert.

        阻塞告警开启 0关闭 1开启

        :return: The enable of this BlockAlert.
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this BlockAlert.

        阻塞告警开启 0关闭 1开启

        :param enable: The enable of this BlockAlert.
        :type enable: str
        """
        self._enable = enable

    @property
    def waiting_count(self):
        r"""Gets the waiting_count of this BlockAlert.

        等待队列大于多少个开始阻塞

        :return: The waiting_count of this BlockAlert.
        :rtype: int
        """
        return self._waiting_count

    @waiting_count.setter
    def waiting_count(self, waiting_count):
        r"""Sets the waiting_count of this BlockAlert.

        等待队列大于多少个开始阻塞

        :param waiting_count: The waiting_count of this BlockAlert.
        :type waiting_count: int
        """
        self._waiting_count = waiting_count

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
        if not isinstance(other, BlockAlert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
