# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CronTriggerScheduler:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cron': 'str',
        'target_replica': 'int'
    }

    attribute_map = {
        'cron': 'cron',
        'target_replica': 'target_replica'
    }

    def __init__(self, cron=None, target_replica=None):
        """CronTriggerScheduler

        The model defined in huaweicloud sdk

        :param cron: 触发时间点，以五位cron表达式表示。
        :type cron: str
        :param target_replica: 要求达到的实例数。
        :type target_replica: int
        """
        
        

        self._cron = None
        self._target_replica = None
        self.discriminator = None

        if cron is not None:
            self.cron = cron
        if target_replica is not None:
            self.target_replica = target_replica

    @property
    def cron(self):
        """Gets the cron of this CronTriggerScheduler.

        触发时间点，以五位cron表达式表示。

        :return: The cron of this CronTriggerScheduler.
        :rtype: str
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        """Sets the cron of this CronTriggerScheduler.

        触发时间点，以五位cron表达式表示。

        :param cron: The cron of this CronTriggerScheduler.
        :type cron: str
        """
        self._cron = cron

    @property
    def target_replica(self):
        """Gets the target_replica of this CronTriggerScheduler.

        要求达到的实例数。

        :return: The target_replica of this CronTriggerScheduler.
        :rtype: int
        """
        return self._target_replica

    @target_replica.setter
    def target_replica(self, target_replica):
        """Sets the target_replica of this CronTriggerScheduler.

        要求达到的实例数。

        :param target_replica: The target_replica of this CronTriggerScheduler.
        :type target_replica: int
        """
        self._target_replica = target_replica

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
        if not isinstance(other, CronTriggerScheduler):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
