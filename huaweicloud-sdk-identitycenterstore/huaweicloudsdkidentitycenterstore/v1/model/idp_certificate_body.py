# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdpCertificateBody:

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
        'status': 'str'
    }

    attribute_map = {
        'certificate_id': 'certificate_id',
        'status': 'status'
    }

    def __init__(self, certificate_id=None, status=None):
        r"""IdpCertificateBody

        The model defined in huaweicloud sdk

        :param certificate_id: 证书全局唯一标识符（ID）
        :type certificate_id: str
        :param status: 证书状态
        :type status: str
        """
        
        

        self._certificate_id = None
        self._status = None
        self.discriminator = None

        self.certificate_id = certificate_id
        self.status = status

    @property
    def certificate_id(self):
        r"""Gets the certificate_id of this IdpCertificateBody.

        证书全局唯一标识符（ID）

        :return: The certificate_id of this IdpCertificateBody.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        r"""Sets the certificate_id of this IdpCertificateBody.

        证书全局唯一标识符（ID）

        :param certificate_id: The certificate_id of this IdpCertificateBody.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

    @property
    def status(self):
        r"""Gets the status of this IdpCertificateBody.

        证书状态

        :return: The status of this IdpCertificateBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IdpCertificateBody.

        证书状态

        :param status: The status of this IdpCertificateBody.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, IdpCertificateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
