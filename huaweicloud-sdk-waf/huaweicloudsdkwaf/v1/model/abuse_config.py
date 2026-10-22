# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AbuseConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scope': 'AbuseScope',
        'threshold': 'AbuseThreshold'
    }

    attribute_map = {
        'scope': 'scope',
        'threshold': 'threshold'
    }

    def __init__(self, scope=None, threshold=None):
        r"""AbuseConfig

        The model defined in huaweicloud sdk

        :param scope: 
        :type scope: :class:`huaweicloudsdkwaf.v1.AbuseScope`
        :param threshold: 
        :type threshold: :class:`huaweicloudsdkwaf.v1.AbuseThreshold`
        """
        
        

        self._scope = None
        self._threshold = None
        self.discriminator = None

        if scope is not None:
            self.scope = scope
        if threshold is not None:
            self.threshold = threshold

    @property
    def scope(self):
        r"""Gets the scope of this AbuseConfig.

        :return: The scope of this AbuseConfig.
        :rtype: :class:`huaweicloudsdkwaf.v1.AbuseScope`
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this AbuseConfig.

        :param scope: The scope of this AbuseConfig.
        :type scope: :class:`huaweicloudsdkwaf.v1.AbuseScope`
        """
        self._scope = scope

    @property
    def threshold(self):
        r"""Gets the threshold of this AbuseConfig.

        :return: The threshold of this AbuseConfig.
        :rtype: :class:`huaweicloudsdkwaf.v1.AbuseThreshold`
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this AbuseConfig.

        :param threshold: The threshold of this AbuseConfig.
        :type threshold: :class:`huaweicloudsdkwaf.v1.AbuseThreshold`
        """
        self._threshold = threshold

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
        if not isinstance(other, AbuseConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
