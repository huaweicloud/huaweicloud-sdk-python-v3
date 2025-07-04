# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCertificatesByTagRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_instances': 'str',
        'body': 'ListCertificatesByTagRequestBody'
    }

    attribute_map = {
        'resource_instances': 'resource_instances',
        'body': 'body'
    }

    def __init__(self, resource_instances=None, body=None):
        r"""ListCertificatesByTagRequest

        The model defined in huaweicloud sdk

        :param resource_instances: 定值为resource_instances。
        :type resource_instances: str
        :param body: Body of the ListCertificatesByTagRequest
        :type body: :class:`huaweicloudsdkscm.v3.ListCertificatesByTagRequestBody`
        """
        
        

        self._resource_instances = None
        self._body = None
        self.discriminator = None

        self.resource_instances = resource_instances
        if body is not None:
            self.body = body

    @property
    def resource_instances(self):
        r"""Gets the resource_instances of this ListCertificatesByTagRequest.

        定值为resource_instances。

        :return: The resource_instances of this ListCertificatesByTagRequest.
        :rtype: str
        """
        return self._resource_instances

    @resource_instances.setter
    def resource_instances(self, resource_instances):
        r"""Sets the resource_instances of this ListCertificatesByTagRequest.

        定值为resource_instances。

        :param resource_instances: The resource_instances of this ListCertificatesByTagRequest.
        :type resource_instances: str
        """
        self._resource_instances = resource_instances

    @property
    def body(self):
        r"""Gets the body of this ListCertificatesByTagRequest.

        :return: The body of this ListCertificatesByTagRequest.
        :rtype: :class:`huaweicloudsdkscm.v3.ListCertificatesByTagRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListCertificatesByTagRequest.

        :param body: The body of this ListCertificatesByTagRequest.
        :type body: :class:`huaweicloudsdkscm.v3.ListCertificatesByTagRequestBody`
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
        if not isinstance(other, ListCertificatesByTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
