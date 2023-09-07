# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateScheduledTaskOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'scheduled_policy': 'ScheduledTaskPolicy',
        'instance_number': 'IntegerRange'
    }

    attribute_map = {
        'name': 'name',
        'scheduled_policy': 'scheduled_policy',
        'instance_number': 'instance_number'
    }

    def __init__(self, name=None, scheduled_policy=None, instance_number=None):
        """CreateScheduledTaskOption

        The model defined in huaweicloud sdk

        :param name: 计划任务名称
        :type name: str
        :param scheduled_policy: 
        :type scheduled_policy: :class:`huaweicloudsdkas.v1.ScheduledTaskPolicy`
        :param instance_number: 
        :type instance_number: :class:`huaweicloudsdkas.v1.IntegerRange`
        """
        
        

        self._name = None
        self._scheduled_policy = None
        self._instance_number = None
        self.discriminator = None

        self.name = name
        self.scheduled_policy = scheduled_policy
        self.instance_number = instance_number

    @property
    def name(self):
        """Gets the name of this CreateScheduledTaskOption.

        计划任务名称

        :return: The name of this CreateScheduledTaskOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateScheduledTaskOption.

        计划任务名称

        :param name: The name of this CreateScheduledTaskOption.
        :type name: str
        """
        self._name = name

    @property
    def scheduled_policy(self):
        """Gets the scheduled_policy of this CreateScheduledTaskOption.

        :return: The scheduled_policy of this CreateScheduledTaskOption.
        :rtype: :class:`huaweicloudsdkas.v1.ScheduledTaskPolicy`
        """
        return self._scheduled_policy

    @scheduled_policy.setter
    def scheduled_policy(self, scheduled_policy):
        """Sets the scheduled_policy of this CreateScheduledTaskOption.

        :param scheduled_policy: The scheduled_policy of this CreateScheduledTaskOption.
        :type scheduled_policy: :class:`huaweicloudsdkas.v1.ScheduledTaskPolicy`
        """
        self._scheduled_policy = scheduled_policy

    @property
    def instance_number(self):
        """Gets the instance_number of this CreateScheduledTaskOption.

        :return: The instance_number of this CreateScheduledTaskOption.
        :rtype: :class:`huaweicloudsdkas.v1.IntegerRange`
        """
        return self._instance_number

    @instance_number.setter
    def instance_number(self, instance_number):
        """Sets the instance_number of this CreateScheduledTaskOption.

        :param instance_number: The instance_number of this CreateScheduledTaskOption.
        :type instance_number: :class:`huaweicloudsdkas.v1.IntegerRange`
        """
        self._instance_number = instance_number

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
        if not isinstance(other, CreateScheduledTaskOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
