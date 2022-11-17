# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServerRemoteConsoleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'remote_console': 'ServerRemoteConsole'
    }

    attribute_map = {
        'remote_console': 'remote_console'
    }

    def __init__(self, remote_console=None):
        """ShowServerRemoteConsoleResponse

        The model defined in huaweicloud sdk

        :param remote_console: 
        :type remote_console: :class:`huaweicloudsdkecs.v2.ServerRemoteConsole`
        """
        
        super(ShowServerRemoteConsoleResponse, self).__init__()

        self._remote_console = None
        self.discriminator = None

        if remote_console is not None:
            self.remote_console = remote_console

    @property
    def remote_console(self):
        """Gets the remote_console of this ShowServerRemoteConsoleResponse.

        :return: The remote_console of this ShowServerRemoteConsoleResponse.
        :rtype: :class:`huaweicloudsdkecs.v2.ServerRemoteConsole`
        """
        return self._remote_console

    @remote_console.setter
    def remote_console(self, remote_console):
        """Sets the remote_console of this ShowServerRemoteConsoleResponse.

        :param remote_console: The remote_console of this ShowServerRemoteConsoleResponse.
        :type remote_console: :class:`huaweicloudsdkecs.v2.ServerRemoteConsole`
        """
        self._remote_console = remote_console

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
        if not isinstance(other, ShowServerRemoteConsoleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
