# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEipRequestBodySpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'egress': 'UpdateEipRequestBodySpecEgress',
        'ingress': 'UpdateEipRequestBodySpecIngress'
    }

    attribute_map = {
        'egress': 'egress',
        'ingress': 'ingress'
    }

    def __init__(self, egress=None, ingress=None):
        r"""UpdateEipRequestBodySpec

        The model defined in huaweicloud sdk

        :param egress: 
        :type egress: :class:`huaweicloudsdkcae.v1.UpdateEipRequestBodySpecEgress`
        :param ingress: 
        :type ingress: :class:`huaweicloudsdkcae.v1.UpdateEipRequestBodySpecIngress`
        """
        
        

        self._egress = None
        self._ingress = None
        self.discriminator = None

        if egress is not None:
            self.egress = egress
        if ingress is not None:
            self.ingress = ingress

    @property
    def egress(self):
        r"""Gets the egress of this UpdateEipRequestBodySpec.

        :return: The egress of this UpdateEipRequestBodySpec.
        :rtype: :class:`huaweicloudsdkcae.v1.UpdateEipRequestBodySpecEgress`
        """
        return self._egress

    @egress.setter
    def egress(self, egress):
        r"""Sets the egress of this UpdateEipRequestBodySpec.

        :param egress: The egress of this UpdateEipRequestBodySpec.
        :type egress: :class:`huaweicloudsdkcae.v1.UpdateEipRequestBodySpecEgress`
        """
        self._egress = egress

    @property
    def ingress(self):
        r"""Gets the ingress of this UpdateEipRequestBodySpec.

        :return: The ingress of this UpdateEipRequestBodySpec.
        :rtype: :class:`huaweicloudsdkcae.v1.UpdateEipRequestBodySpecIngress`
        """
        return self._ingress

    @ingress.setter
    def ingress(self, ingress):
        r"""Sets the ingress of this UpdateEipRequestBodySpec.

        :param ingress: The ingress of this UpdateEipRequestBodySpec.
        :type ingress: :class:`huaweicloudsdkcae.v1.UpdateEipRequestBodySpecIngress`
        """
        self._ingress = ingress

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
        if not isinstance(other, UpdateEipRequestBodySpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
