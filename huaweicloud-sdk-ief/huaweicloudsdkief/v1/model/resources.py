# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Resources:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limits': 'LimitsRequests',
        'requests': 'LimitsRequests'
    }

    attribute_map = {
        'limits': 'limits',
        'requests': 'requests'
    }

    def __init__(self, limits=None, requests=None):
        r"""Resources

        The model defined in huaweicloud sdk

        :param limits: 
        :type limits: :class:`huaweicloudsdkief.v1.LimitsRequests`
        :param requests: 
        :type requests: :class:`huaweicloudsdkief.v1.LimitsRequests`
        """
        
        

        self._limits = None
        self._requests = None
        self.discriminator = None

        if limits is not None:
            self.limits = limits
        if requests is not None:
            self.requests = requests

    @property
    def limits(self):
        r"""Gets the limits of this Resources.

        :return: The limits of this Resources.
        :rtype: :class:`huaweicloudsdkief.v1.LimitsRequests`
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        r"""Sets the limits of this Resources.

        :param limits: The limits of this Resources.
        :type limits: :class:`huaweicloudsdkief.v1.LimitsRequests`
        """
        self._limits = limits

    @property
    def requests(self):
        r"""Gets the requests of this Resources.

        :return: The requests of this Resources.
        :rtype: :class:`huaweicloudsdkief.v1.LimitsRequests`
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        r"""Sets the requests of this Resources.

        :param requests: The requests of this Resources.
        :type requests: :class:`huaweicloudsdkief.v1.LimitsRequests`
        """
        self._requests = requests

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
        if not isinstance(other, Resources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
