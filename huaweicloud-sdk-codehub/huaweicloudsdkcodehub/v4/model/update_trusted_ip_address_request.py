# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTrustedIpAddressRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'ip_id': 'int',
        'body': 'AddTrustedIpAddressRequestBody'
    }

    attribute_map = {
        'id': 'id',
        'ip_id': 'ip_id',
        'body': 'body'
    }

    def __init__(self, id=None, ip_id=None, body=None):
        """UpdateTrustedIpAddressRequest

        The model defined in huaweicloud sdk

        :param id: 仓库id
        :type id: int
        :param ip_id: ip的id
        :type ip_id: int
        :param body: Body of the UpdateTrustedIpAddressRequest
        :type body: :class:`huaweicloudsdkcodehub.v4.AddTrustedIpAddressRequestBody`
        """
        
        

        self._id = None
        self._ip_id = None
        self._body = None
        self.discriminator = None

        self.id = id
        self.ip_id = ip_id
        if body is not None:
            self.body = body

    @property
    def id(self):
        """Gets the id of this UpdateTrustedIpAddressRequest.

        仓库id

        :return: The id of this UpdateTrustedIpAddressRequest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateTrustedIpAddressRequest.

        仓库id

        :param id: The id of this UpdateTrustedIpAddressRequest.
        :type id: int
        """
        self._id = id

    @property
    def ip_id(self):
        """Gets the ip_id of this UpdateTrustedIpAddressRequest.

        ip的id

        :return: The ip_id of this UpdateTrustedIpAddressRequest.
        :rtype: int
        """
        return self._ip_id

    @ip_id.setter
    def ip_id(self, ip_id):
        """Sets the ip_id of this UpdateTrustedIpAddressRequest.

        ip的id

        :param ip_id: The ip_id of this UpdateTrustedIpAddressRequest.
        :type ip_id: int
        """
        self._ip_id = ip_id

    @property
    def body(self):
        """Gets the body of this UpdateTrustedIpAddressRequest.

        :return: The body of this UpdateTrustedIpAddressRequest.
        :rtype: :class:`huaweicloudsdkcodehub.v4.AddTrustedIpAddressRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateTrustedIpAddressRequest.

        :param body: The body of this UpdateTrustedIpAddressRequest.
        :type body: :class:`huaweicloudsdkcodehub.v4.AddTrustedIpAddressRequestBody`
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
        if not isinstance(other, UpdateTrustedIpAddressRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
