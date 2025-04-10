# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeployCertificateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'certificate_id': 'str',
        'body': 'DeployCertificateRequestBody'
    }

    attribute_map = {
        'certificate_id': 'certificate_id',
        'body': 'body'
    }

    def __init__(self, certificate_id=None, body=None):
        r"""DeployCertificateRequest

        The model defined in huaweicloud sdk

        :param certificate_id: 证书id。
        :type certificate_id: str
        :param body: Body of the DeployCertificateRequest
        :type body: :class:`huaweicloudsdkscm.v3.DeployCertificateRequestBody`
        """
        
        

        self._certificate_id = None
        self._body = None
        self.discriminator = None

        self.certificate_id = certificate_id
        if body is not None:
            self.body = body

    @property
    def certificate_id(self):
        r"""Gets the certificate_id of this DeployCertificateRequest.

        证书id。

        :return: The certificate_id of this DeployCertificateRequest.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        r"""Sets the certificate_id of this DeployCertificateRequest.

        证书id。

        :param certificate_id: The certificate_id of this DeployCertificateRequest.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

    @property
    def body(self):
        r"""Gets the body of this DeployCertificateRequest.

        :return: The body of this DeployCertificateRequest.
        :rtype: :class:`huaweicloudsdkscm.v3.DeployCertificateRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this DeployCertificateRequest.

        :param body: The body of this DeployCertificateRequest.
        :type body: :class:`huaweicloudsdkscm.v3.DeployCertificateRequestBody`
        """
        self._body = body

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
        if not isinstance(other, DeployCertificateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
