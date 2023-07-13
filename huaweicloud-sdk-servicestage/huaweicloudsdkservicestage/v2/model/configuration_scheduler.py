# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationScheduler:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'affinity': 'SchedulerAffinity',
        'anti_affinity': 'SchedulerAffinity'
    }

    attribute_map = {
        'affinity': 'affinity',
        'anti_affinity': 'anti-affinity'
    }

    def __init__(self, affinity=None, anti_affinity=None):
        """ConfigurationScheduler

        The model defined in huaweicloud sdk

        :param affinity: 
        :type affinity: :class:`huaweicloudsdkservicestage.v2.SchedulerAffinity`
        :param anti_affinity: 
        :type anti_affinity: :class:`huaweicloudsdkservicestage.v2.SchedulerAffinity`
        """
        
        

        self._affinity = None
        self._anti_affinity = None
        self.discriminator = None

        if affinity is not None:
            self.affinity = affinity
        if anti_affinity is not None:
            self.anti_affinity = anti_affinity

    @property
    def affinity(self):
        """Gets the affinity of this ConfigurationScheduler.

        :return: The affinity of this ConfigurationScheduler.
        :rtype: :class:`huaweicloudsdkservicestage.v2.SchedulerAffinity`
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        """Sets the affinity of this ConfigurationScheduler.

        :param affinity: The affinity of this ConfigurationScheduler.
        :type affinity: :class:`huaweicloudsdkservicestage.v2.SchedulerAffinity`
        """
        self._affinity = affinity

    @property
    def anti_affinity(self):
        """Gets the anti_affinity of this ConfigurationScheduler.

        :return: The anti_affinity of this ConfigurationScheduler.
        :rtype: :class:`huaweicloudsdkservicestage.v2.SchedulerAffinity`
        """
        return self._anti_affinity

    @anti_affinity.setter
    def anti_affinity(self, anti_affinity):
        """Sets the anti_affinity of this ConfigurationScheduler.

        :param anti_affinity: The anti_affinity of this ConfigurationScheduler.
        :type anti_affinity: :class:`huaweicloudsdkservicestage.v2.SchedulerAffinity`
        """
        self._anti_affinity = anti_affinity

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
        if not isinstance(other, ConfigurationScheduler):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
