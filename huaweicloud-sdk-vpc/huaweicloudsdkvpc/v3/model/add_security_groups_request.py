# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddSecurityGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port_id': 'str',
        'body': 'AddSecurityGroupsRequestBody'
    }

    attribute_map = {
        'port_id': 'port_id',
        'body': 'body'
    }

    def __init__(self, port_id=None, body=None):
        """AddSecurityGroupsRequest

        The model defined in huaweicloud sdk

        :param port_id: 端口的唯一标识
        :type port_id: str
        :param body: Body of the AddSecurityGroupsRequest
        :type body: :class:`huaweicloudsdkvpc.v3.AddSecurityGroupsRequestBody`
        """
        
        

        self._port_id = None
        self._body = None
        self.discriminator = None

        self.port_id = port_id
        if body is not None:
            self.body = body

    @property
    def port_id(self):
        """Gets the port_id of this AddSecurityGroupsRequest.

        端口的唯一标识

        :return: The port_id of this AddSecurityGroupsRequest.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this AddSecurityGroupsRequest.

        端口的唯一标识

        :param port_id: The port_id of this AddSecurityGroupsRequest.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def body(self):
        """Gets the body of this AddSecurityGroupsRequest.

        :return: The body of this AddSecurityGroupsRequest.
        :rtype: :class:`huaweicloudsdkvpc.v3.AddSecurityGroupsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this AddSecurityGroupsRequest.

        :param body: The body of this AddSecurityGroupsRequest.
        :type body: :class:`huaweicloudsdkvpc.v3.AddSecurityGroupsRequestBody`
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
        if not isinstance(other, AddSecurityGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
