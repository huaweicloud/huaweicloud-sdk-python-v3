# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KafkaAuthInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'security_protocol': 'str',
        'sasl_plain_auth_info': 'SaslPlainAuthInfo'
    }

    attribute_map = {
        'security_protocol': 'security_protocol',
        'sasl_plain_auth_info': 'sasl_plain_auth_info'
    }

    def __init__(self, security_protocol=None, sasl_plain_auth_info=None):
        r"""KafkaAuthInfo

        The model defined in huaweicloud sdk

        :param security_protocol: 安全协议
        :type security_protocol: str
        :param sasl_plain_auth_info: 
        :type sasl_plain_auth_info: :class:`huaweicloudsdkiotanalytics.v1.SaslPlainAuthInfo`
        """
        
        

        self._security_protocol = None
        self._sasl_plain_auth_info = None
        self.discriminator = None

        self.security_protocol = security_protocol
        if sasl_plain_auth_info is not None:
            self.sasl_plain_auth_info = sasl_plain_auth_info

    @property
    def security_protocol(self):
        r"""Gets the security_protocol of this KafkaAuthInfo.

        安全协议

        :return: The security_protocol of this KafkaAuthInfo.
        :rtype: str
        """
        return self._security_protocol

    @security_protocol.setter
    def security_protocol(self, security_protocol):
        r"""Sets the security_protocol of this KafkaAuthInfo.

        安全协议

        :param security_protocol: The security_protocol of this KafkaAuthInfo.
        :type security_protocol: str
        """
        self._security_protocol = security_protocol

    @property
    def sasl_plain_auth_info(self):
        r"""Gets the sasl_plain_auth_info of this KafkaAuthInfo.

        :return: The sasl_plain_auth_info of this KafkaAuthInfo.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.SaslPlainAuthInfo`
        """
        return self._sasl_plain_auth_info

    @sasl_plain_auth_info.setter
    def sasl_plain_auth_info(self, sasl_plain_auth_info):
        r"""Sets the sasl_plain_auth_info of this KafkaAuthInfo.

        :param sasl_plain_auth_info: The sasl_plain_auth_info of this KafkaAuthInfo.
        :type sasl_plain_auth_info: :class:`huaweicloudsdkiotanalytics.v1.SaslPlainAuthInfo`
        """
        self._sasl_plain_auth_info = sasl_plain_auth_info

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
        if not isinstance(other, KafkaAuthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
