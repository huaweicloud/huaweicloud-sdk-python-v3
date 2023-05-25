# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationProbes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'liveness_probe': 'ComponentProbe',
        'readiness_probe': 'ComponentProbe'
    }

    attribute_map = {
        'liveness_probe': 'livenessProbe',
        'readiness_probe': 'readinessProbe'
    }

    def __init__(self, liveness_probe=None, readiness_probe=None):
        """ConfigurationProbes

        The model defined in huaweicloud sdk

        :param liveness_probe: 
        :type liveness_probe: :class:`huaweicloudsdkservicestage.v2.ComponentProbe`
        :param readiness_probe: 
        :type readiness_probe: :class:`huaweicloudsdkservicestage.v2.ComponentProbe`
        """
        
        

        self._liveness_probe = None
        self._readiness_probe = None
        self.discriminator = None

        if liveness_probe is not None:
            self.liveness_probe = liveness_probe
        if readiness_probe is not None:
            self.readiness_probe = readiness_probe

    @property
    def liveness_probe(self):
        """Gets the liveness_probe of this ConfigurationProbes.

        :return: The liveness_probe of this ConfigurationProbes.
        :rtype: :class:`huaweicloudsdkservicestage.v2.ComponentProbe`
        """
        return self._liveness_probe

    @liveness_probe.setter
    def liveness_probe(self, liveness_probe):
        """Sets the liveness_probe of this ConfigurationProbes.

        :param liveness_probe: The liveness_probe of this ConfigurationProbes.
        :type liveness_probe: :class:`huaweicloudsdkservicestage.v2.ComponentProbe`
        """
        self._liveness_probe = liveness_probe

    @property
    def readiness_probe(self):
        """Gets the readiness_probe of this ConfigurationProbes.

        :return: The readiness_probe of this ConfigurationProbes.
        :rtype: :class:`huaweicloudsdkservicestage.v2.ComponentProbe`
        """
        return self._readiness_probe

    @readiness_probe.setter
    def readiness_probe(self, readiness_probe):
        """Sets the readiness_probe of this ConfigurationProbes.

        :param readiness_probe: The readiness_probe of this ConfigurationProbes.
        :type readiness_probe: :class:`huaweicloudsdkservicestage.v2.ComponentProbe`
        """
        self._readiness_probe = readiness_probe

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
        if not isinstance(other, ConfigurationProbes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
