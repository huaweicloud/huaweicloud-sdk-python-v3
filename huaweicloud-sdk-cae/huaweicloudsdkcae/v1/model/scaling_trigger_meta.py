# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScalingTriggerMeta:

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
        'value': 'str',
        'period_type': 'str',
        'schedulers': 'list[CronTriggerScheduler]'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value',
        'period_type': 'period_type',
        'schedulers': 'schedulers'
    }

    def __init__(self, type=None, value=None, period_type=None, schedulers=None):
        """ScalingTriggerMeta

        The model defined in huaweicloud sdk

        :param type: 数据类型，当前只支持利用率，默认值为Utilization。  ScaleConfigurationDataTrigger.type为\&quot;cpu、memory\&quot;时，配置此参数。 
        :type type: str
        :param value: 触发指标的阈值。  ScaleConfigurationDataTrigger.type为\&quot;cpu、memory\&quot;时，配置此参数。 
        :type value: str
        :param period_type: 生效周期。  ScaleConfigurationDataTrigger.type为\&quot;cron\&quot;时，配置此参数。 
        :type period_type: str
        :param schedulers: 每个周期内触发的时间点和实例数。  ScaleConfigurationDataTrigger.type为\&quot;cron\&quot;时，配置此参数。 
        :type schedulers: list[:class:`huaweicloudsdkcae.v1.CronTriggerScheduler`]
        """
        
        

        self._type = None
        self._value = None
        self._period_type = None
        self._schedulers = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if period_type is not None:
            self.period_type = period_type
        if schedulers is not None:
            self.schedulers = schedulers

    @property
    def type(self):
        """Gets the type of this ScalingTriggerMeta.

        数据类型，当前只支持利用率，默认值为Utilization。  ScaleConfigurationDataTrigger.type为\"cpu、memory\"时，配置此参数。 

        :return: The type of this ScalingTriggerMeta.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ScalingTriggerMeta.

        数据类型，当前只支持利用率，默认值为Utilization。  ScaleConfigurationDataTrigger.type为\"cpu、memory\"时，配置此参数。 

        :param type: The type of this ScalingTriggerMeta.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        """Gets the value of this ScalingTriggerMeta.

        触发指标的阈值。  ScaleConfigurationDataTrigger.type为\"cpu、memory\"时，配置此参数。 

        :return: The value of this ScalingTriggerMeta.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ScalingTriggerMeta.

        触发指标的阈值。  ScaleConfigurationDataTrigger.type为\"cpu、memory\"时，配置此参数。 

        :param value: The value of this ScalingTriggerMeta.
        :type value: str
        """
        self._value = value

    @property
    def period_type(self):
        """Gets the period_type of this ScalingTriggerMeta.

        生效周期。  ScaleConfigurationDataTrigger.type为\"cron\"时，配置此参数。 

        :return: The period_type of this ScalingTriggerMeta.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this ScalingTriggerMeta.

        生效周期。  ScaleConfigurationDataTrigger.type为\"cron\"时，配置此参数。 

        :param period_type: The period_type of this ScalingTriggerMeta.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def schedulers(self):
        """Gets the schedulers of this ScalingTriggerMeta.

        每个周期内触发的时间点和实例数。  ScaleConfigurationDataTrigger.type为\"cron\"时，配置此参数。 

        :return: The schedulers of this ScalingTriggerMeta.
        :rtype: list[:class:`huaweicloudsdkcae.v1.CronTriggerScheduler`]
        """
        return self._schedulers

    @schedulers.setter
    def schedulers(self, schedulers):
        """Sets the schedulers of this ScalingTriggerMeta.

        每个周期内触发的时间点和实例数。  ScaleConfigurationDataTrigger.type为\"cron\"时，配置此参数。 

        :param schedulers: The schedulers of this ScalingTriggerMeta.
        :type schedulers: list[:class:`huaweicloudsdkcae.v1.CronTriggerScheduler`]
        """
        self._schedulers = schedulers

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
        if not isinstance(other, ScalingTriggerMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
