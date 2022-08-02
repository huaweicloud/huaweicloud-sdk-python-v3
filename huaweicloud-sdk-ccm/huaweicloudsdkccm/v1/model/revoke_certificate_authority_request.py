# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RevokeCertificateAuthorityRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ca_id': 'str',
        'body': 'RevokeCertificateRequestBody'
    }

    attribute_map = {
        'ca_id': 'ca_id',
        'body': 'body'
    }

    def __init__(self, ca_id=None, body=None):
        """RevokeCertificateAuthorityRequest

        The model defined in huaweicloud sdk

        :param ca_id: 所要吊销的子CA ID。
        :type ca_id: str
        :param body: Body of the RevokeCertificateAuthorityRequest
        :type body: :class:`huaweicloudsdkccm.v1.RevokeCertificateRequestBody`
        """
        
        

        self._ca_id = None
        self._body = None
        self.discriminator = None

        self.ca_id = ca_id
        if body is not None:
            self.body = body

    @property
    def ca_id(self):
        """Gets the ca_id of this RevokeCertificateAuthorityRequest.

        所要吊销的子CA ID。

        :return: The ca_id of this RevokeCertificateAuthorityRequest.
        :rtype: str
        """
        return self._ca_id

    @ca_id.setter
    def ca_id(self, ca_id):
        """Sets the ca_id of this RevokeCertificateAuthorityRequest.

        所要吊销的子CA ID。

        :param ca_id: The ca_id of this RevokeCertificateAuthorityRequest.
        :type ca_id: str
        """
        self._ca_id = ca_id

    @property
    def body(self):
        """Gets the body of this RevokeCertificateAuthorityRequest.


        :return: The body of this RevokeCertificateAuthorityRequest.
        :rtype: :class:`huaweicloudsdkccm.v1.RevokeCertificateRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this RevokeCertificateAuthorityRequest.


        :param body: The body of this RevokeCertificateAuthorityRequest.
        :type body: :class:`huaweicloudsdkccm.v1.RevokeCertificateRequestBody`
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
        if not isinstance(other, RevokeCertificateAuthorityRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
