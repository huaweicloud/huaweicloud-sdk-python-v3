# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePromInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'body': 'PromInstanceRequestModel'
    }

    attribute_map = {
        'region': 'region',
        'body': 'body'
    }

    def __init__(self, region=None, body=None):
        r"""CreatePromInstanceRequest

        The model defined in huaweicloud sdk

        :param region: Prometheus实例所属Region，一般为承载REST服务端点的服务器域名或IP，不同服务不同区域的名称不同。
        :type region: str
        :param body: Body of the CreatePromInstanceRequest
        :type body: :class:`huaweicloudsdkaom.v2.PromInstanceRequestModel`
        """
        
        

        self._region = None
        self._body = None
        self.discriminator = None

        self.region = region
        if body is not None:
            self.body = body

    @property
    def region(self):
        r"""Gets the region of this CreatePromInstanceRequest.

        Prometheus实例所属Region，一般为承载REST服务端点的服务器域名或IP，不同服务不同区域的名称不同。

        :return: The region of this CreatePromInstanceRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CreatePromInstanceRequest.

        Prometheus实例所属Region，一般为承载REST服务端点的服务器域名或IP，不同服务不同区域的名称不同。

        :param region: The region of this CreatePromInstanceRequest.
        :type region: str
        """
        self._region = region

    @property
    def body(self):
        r"""Gets the body of this CreatePromInstanceRequest.

        :return: The body of this CreatePromInstanceRequest.
        :rtype: :class:`huaweicloudsdkaom.v2.PromInstanceRequestModel`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreatePromInstanceRequest.

        :param body: The body of this CreatePromInstanceRequest.
        :type body: :class:`huaweicloudsdkaom.v2.PromInstanceRequestModel`
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
        if not isinstance(other, CreatePromInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
