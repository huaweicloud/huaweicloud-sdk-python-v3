# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateServerGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_group': 'CreateServerGroupResult'
    }

    attribute_map = {
        'server_group': 'server_group'
    }

    def __init__(self, server_group=None):
        """CreateServerGroupResponse

        The model defined in huaweicloud sdk

        :param server_group: 
        :type server_group: :class:`huaweicloudsdkecs.v2.CreateServerGroupResult`
        """
        
        super(CreateServerGroupResponse, self).__init__()

        self._server_group = None
        self.discriminator = None

        if server_group is not None:
            self.server_group = server_group

    @property
    def server_group(self):
        """Gets the server_group of this CreateServerGroupResponse.

        :return: The server_group of this CreateServerGroupResponse.
        :rtype: :class:`huaweicloudsdkecs.v2.CreateServerGroupResult`
        """
        return self._server_group

    @server_group.setter
    def server_group(self, server_group):
        """Sets the server_group of this CreateServerGroupResponse.

        :param server_group: The server_group of this CreateServerGroupResponse.
        :type server_group: :class:`huaweicloudsdkecs.v2.CreateServerGroupResult`
        """
        self._server_group = server_group

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
        if not isinstance(other, CreateServerGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
