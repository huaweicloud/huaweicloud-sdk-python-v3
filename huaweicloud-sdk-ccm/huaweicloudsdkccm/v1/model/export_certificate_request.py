# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportCertificateRequest:


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
        'body': 'ExportCertificateRequestBody'
    }

    attribute_map = {
        'certificate_id': 'certificate_id',
        'body': 'body'
    }

    def __init__(self, certificate_id=None, body=None):
        """ExportCertificateRequest - a model defined in huaweicloud sdk"""
        
        

        self._certificate_id = None
        self._body = None
        self.discriminator = None

        self.certificate_id = certificate_id
        if body is not None:
            self.body = body

    @property
    def certificate_id(self):
        """Gets the certificate_id of this ExportCertificateRequest.

        certificate_id

        :return: The certificate_id of this ExportCertificateRequest.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this ExportCertificateRequest.

        certificate_id

        :param certificate_id: The certificate_id of this ExportCertificateRequest.
        :type: str
        """
        self._certificate_id = certificate_id

    @property
    def body(self):
        """Gets the body of this ExportCertificateRequest.


        :return: The body of this ExportCertificateRequest.
        :rtype: ExportCertificateRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ExportCertificateRequest.


        :param body: The body of this ExportCertificateRequest.
        :type: ExportCertificateRequestBody
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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExportCertificateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
