# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddServerGroupMemberRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'server_group_id': 'str',
        'body': 'AddServerGroupMemberRequestBody'
    }

    attribute_map = {
        'server_group_id': 'server_group_id',
        'body': 'body'
    }

    def __init__(self, server_group_id=None, body=None):
        """AddServerGroupMemberRequest

        The model defined in huaweicloud sdk

        :param server_group_id: 云服务器组ID。
        :type server_group_id: str
        :param body: Body of the AddServerGroupMemberRequest
        :type body: :class:`huaweicloudsdkecs.v2.AddServerGroupMemberRequestBody`
        """
        
        

        self._server_group_id = None
        self._body = None
        self.discriminator = None

        self.server_group_id = server_group_id
        if body is not None:
            self.body = body

    @property
    def server_group_id(self):
        """Gets the server_group_id of this AddServerGroupMemberRequest.

        云服务器组ID。

        :return: The server_group_id of this AddServerGroupMemberRequest.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this AddServerGroupMemberRequest.

        云服务器组ID。

        :param server_group_id: The server_group_id of this AddServerGroupMemberRequest.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def body(self):
        """Gets the body of this AddServerGroupMemberRequest.


        :return: The body of this AddServerGroupMemberRequest.
        :rtype: :class:`huaweicloudsdkecs.v2.AddServerGroupMemberRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this AddServerGroupMemberRequest.


        :param body: The body of this AddServerGroupMemberRequest.
        :type body: :class:`huaweicloudsdkecs.v2.AddServerGroupMemberRequestBody`
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
        if not isinstance(other, AddServerGroupMemberRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
