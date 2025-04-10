# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlarmConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_configs': 'list[AlarmConfig]',
        'data': 'object'
    }

    attribute_map = {
        'alarm_configs': 'alarm_configs',
        'data': 'data'
    }

    def __init__(self, alarm_configs=None, data=None):
        r"""ShowAlarmConfigResponse

        The model defined in huaweicloud sdk

        :param alarm_configs: 告警配置列表
        :type alarm_configs: list[:class:`huaweicloudsdkcfw.v1.AlarmConfig`]
        :param data: 
        :type data: object
        """
        
        super(ShowAlarmConfigResponse, self).__init__()

        self._alarm_configs = None
        self._data = None
        self.discriminator = None

        if alarm_configs is not None:
            self.alarm_configs = alarm_configs
        if data is not None:
            self.data = data

    @property
    def alarm_configs(self):
        r"""Gets the alarm_configs of this ShowAlarmConfigResponse.

        告警配置列表

        :return: The alarm_configs of this ShowAlarmConfigResponse.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AlarmConfig`]
        """
        return self._alarm_configs

    @alarm_configs.setter
    def alarm_configs(self, alarm_configs):
        r"""Sets the alarm_configs of this ShowAlarmConfigResponse.

        告警配置列表

        :param alarm_configs: The alarm_configs of this ShowAlarmConfigResponse.
        :type alarm_configs: list[:class:`huaweicloudsdkcfw.v1.AlarmConfig`]
        """
        self._alarm_configs = alarm_configs

    @property
    def data(self):
        r"""Gets the data of this ShowAlarmConfigResponse.

        :return: The data of this ShowAlarmConfigResponse.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ShowAlarmConfigResponse.

        :param data: The data of this ShowAlarmConfigResponse.
        :type data: object
        """
        self._data = data

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
        if not isinstance(other, ShowAlarmConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
