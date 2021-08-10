# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RevokeCertificateRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cert_id': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'cert_id': 'cert_id',
        'reason': 'reason'
    }

    def __init__(self, cert_id=None, reason=None):
        """RevokeCertificateRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._cert_id = None
        self._reason = None
        self.discriminator = None

        if cert_id is not None:
            self.cert_id = cert_id
        if reason is not None:
            self.reason = reason

    @property
    def cert_id(self):
        """Gets the cert_id of this RevokeCertificateRequestBody.

        证书ID

        :return: The cert_id of this RevokeCertificateRequestBody.
        :rtype: str
        """
        return self._cert_id

    @cert_id.setter
    def cert_id(self, cert_id):
        """Sets the cert_id of this RevokeCertificateRequestBody.

        证书ID

        :param cert_id: The cert_id of this RevokeCertificateRequestBody.
        :type: str
        """
        self._cert_id = cert_id

    @property
    def reason(self):
        """Gets the reason of this RevokeCertificateRequestBody.

        吊销理由

        :return: The reason of this RevokeCertificateRequestBody.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this RevokeCertificateRequestBody.

        吊销理由

        :param reason: The reason of this RevokeCertificateRequestBody.
        :type: str
        """
        self._reason = reason

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
        if not isinstance(other, RevokeCertificateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
