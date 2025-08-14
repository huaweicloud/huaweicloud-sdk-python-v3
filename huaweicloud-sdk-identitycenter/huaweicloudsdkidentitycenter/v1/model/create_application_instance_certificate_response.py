# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateApplicationInstanceCertificateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_instance_certificate': 'CertificateDto'
    }

    attribute_map = {
        'application_instance_certificate': 'application_instance_certificate'
    }

    def __init__(self, application_instance_certificate=None):
        r"""CreateApplicationInstanceCertificateResponse

        The model defined in huaweicloud sdk

        :param application_instance_certificate: 
        :type application_instance_certificate: :class:`huaweicloudsdkidentitycenter.v1.CertificateDto`
        """
        
        super(CreateApplicationInstanceCertificateResponse, self).__init__()

        self._application_instance_certificate = None
        self.discriminator = None

        if application_instance_certificate is not None:
            self.application_instance_certificate = application_instance_certificate

    @property
    def application_instance_certificate(self):
        r"""Gets the application_instance_certificate of this CreateApplicationInstanceCertificateResponse.

        :return: The application_instance_certificate of this CreateApplicationInstanceCertificateResponse.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.CertificateDto`
        """
        return self._application_instance_certificate

    @application_instance_certificate.setter
    def application_instance_certificate(self, application_instance_certificate):
        r"""Sets the application_instance_certificate of this CreateApplicationInstanceCertificateResponse.

        :param application_instance_certificate: The application_instance_certificate of this CreateApplicationInstanceCertificateResponse.
        :type application_instance_certificate: :class:`huaweicloudsdkidentitycenter.v1.CertificateDto`
        """
        self._application_instance_certificate = application_instance_certificate

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
        if not isinstance(other, CreateApplicationInstanceCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
