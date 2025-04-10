# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AnalyzerConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unused_access': 'AnalyzerConfigurationUnusedAccess'
    }

    attribute_map = {
        'unused_access': 'unused_access'
    }

    def __init__(self, unused_access=None):
        r"""AnalyzerConfiguration

        The model defined in huaweicloud sdk

        :param unused_access: 
        :type unused_access: :class:`huaweicloudsdkiamaccessanalyzer.v1.AnalyzerConfigurationUnusedAccess`
        """
        
        

        self._unused_access = None
        self.discriminator = None

        if unused_access is not None:
            self.unused_access = unused_access

    @property
    def unused_access(self):
        r"""Gets the unused_access of this AnalyzerConfiguration.

        :return: The unused_access of this AnalyzerConfiguration.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.AnalyzerConfigurationUnusedAccess`
        """
        return self._unused_access

    @unused_access.setter
    def unused_access(self, unused_access):
        r"""Sets the unused_access of this AnalyzerConfiguration.

        :param unused_access: The unused_access of this AnalyzerConfiguration.
        :type unused_access: :class:`huaweicloudsdkiamaccessanalyzer.v1.AnalyzerConfigurationUnusedAccess`
        """
        self._unused_access = unused_access

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
        if not isinstance(other, AnalyzerConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
