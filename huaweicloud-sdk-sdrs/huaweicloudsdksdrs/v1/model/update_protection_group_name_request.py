# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateProtectionGroupNameRequest:

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
        'body': 'UpdateProtectionGroupNameRequestBody'
    }

    attribute_map = {
        'server_group_id': 'server_group_id',
        'body': 'body'
    }

    def __init__(self, server_group_id=None, body=None):
        r"""UpdateProtectionGroupNameRequest

        The model defined in huaweicloud sdk

        :param server_group_id: 保护组ID。
        :type server_group_id: str
        :param body: Body of the UpdateProtectionGroupNameRequest
        :type body: :class:`huaweicloudsdksdrs.v1.UpdateProtectionGroupNameRequestBody`
        """
        
        

        self._server_group_id = None
        self._body = None
        self.discriminator = None

        self.server_group_id = server_group_id
        if body is not None:
            self.body = body

    @property
    def server_group_id(self):
        r"""Gets the server_group_id of this UpdateProtectionGroupNameRequest.

        保护组ID。

        :return: The server_group_id of this UpdateProtectionGroupNameRequest.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        r"""Sets the server_group_id of this UpdateProtectionGroupNameRequest.

        保护组ID。

        :param server_group_id: The server_group_id of this UpdateProtectionGroupNameRequest.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def body(self):
        r"""Gets the body of this UpdateProtectionGroupNameRequest.

        :return: The body of this UpdateProtectionGroupNameRequest.
        :rtype: :class:`huaweicloudsdksdrs.v1.UpdateProtectionGroupNameRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateProtectionGroupNameRequest.

        :param body: The body of this UpdateProtectionGroupNameRequest.
        :type body: :class:`huaweicloudsdksdrs.v1.UpdateProtectionGroupNameRequestBody`
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
        if not isinstance(other, UpdateProtectionGroupNameRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
