# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHostedDirectConnectRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hosted_connect': 'CreateHostedDirectConnect'
    }

    attribute_map = {
        'hosted_connect': 'hosted_connect'
    }

    def __init__(self, hosted_connect=None):
        """CreateHostedDirectConnectRequestBody

        The model defined in huaweicloud sdk

        :param hosted_connect: 
        :type hosted_connect: :class:`huaweicloudsdkdc.v3.CreateHostedDirectConnect`
        """
        
        

        self._hosted_connect = None
        self.discriminator = None

        self.hosted_connect = hosted_connect

    @property
    def hosted_connect(self):
        """Gets the hosted_connect of this CreateHostedDirectConnectRequestBody.

        :return: The hosted_connect of this CreateHostedDirectConnectRequestBody.
        :rtype: :class:`huaweicloudsdkdc.v3.CreateHostedDirectConnect`
        """
        return self._hosted_connect

    @hosted_connect.setter
    def hosted_connect(self, hosted_connect):
        """Sets the hosted_connect of this CreateHostedDirectConnectRequestBody.

        :param hosted_connect: The hosted_connect of this CreateHostedDirectConnectRequestBody.
        :type hosted_connect: :class:`huaweicloudsdkdc.v3.CreateHostedDirectConnect`
        """
        self._hosted_connect = hosted_connect

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
        if not isinstance(other, CreateHostedDirectConnectRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
