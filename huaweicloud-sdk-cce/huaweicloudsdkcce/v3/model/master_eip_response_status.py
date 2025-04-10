# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MasterEIPResponseStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'private_endpoint': 'str',
        'public_endpoint': 'str'
    }

    attribute_map = {
        'private_endpoint': 'privateEndpoint',
        'public_endpoint': 'publicEndpoint'
    }

    def __init__(self, private_endpoint=None, public_endpoint=None):
        r"""MasterEIPResponseStatus

        The model defined in huaweicloud sdk

        :param private_endpoint: 集群访问的PrivateIP(HA集群返回VIP)
        :type private_endpoint: str
        :param public_endpoint: 集群访问的PublicIP
        :type public_endpoint: str
        """
        
        

        self._private_endpoint = None
        self._public_endpoint = None
        self.discriminator = None

        if private_endpoint is not None:
            self.private_endpoint = private_endpoint
        if public_endpoint is not None:
            self.public_endpoint = public_endpoint

    @property
    def private_endpoint(self):
        r"""Gets the private_endpoint of this MasterEIPResponseStatus.

        集群访问的PrivateIP(HA集群返回VIP)

        :return: The private_endpoint of this MasterEIPResponseStatus.
        :rtype: str
        """
        return self._private_endpoint

    @private_endpoint.setter
    def private_endpoint(self, private_endpoint):
        r"""Sets the private_endpoint of this MasterEIPResponseStatus.

        集群访问的PrivateIP(HA集群返回VIP)

        :param private_endpoint: The private_endpoint of this MasterEIPResponseStatus.
        :type private_endpoint: str
        """
        self._private_endpoint = private_endpoint

    @property
    def public_endpoint(self):
        r"""Gets the public_endpoint of this MasterEIPResponseStatus.

        集群访问的PublicIP

        :return: The public_endpoint of this MasterEIPResponseStatus.
        :rtype: str
        """
        return self._public_endpoint

    @public_endpoint.setter
    def public_endpoint(self, public_endpoint):
        r"""Sets the public_endpoint of this MasterEIPResponseStatus.

        集群访问的PublicIP

        :param public_endpoint: The public_endpoint of this MasterEIPResponseStatus.
        :type public_endpoint: str
        """
        self._public_endpoint = public_endpoint

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
        if not isinstance(other, MasterEIPResponseStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
