# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaShowServerRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'open_stack_api_version': 'str'
    }

    attribute_map = {
        'server_id': 'server_id',
        'open_stack_api_version': 'OpenStack-API-Version'
    }

    def __init__(self, server_id=None, open_stack_api_version=None):
        """NovaShowServerRequest

        The model defined in huaweicloud sdk

        :param server_id: 云服务器ID。
        :type server_id: str
        :param open_stack_api_version: 微版本头
        :type open_stack_api_version: str
        """
        
        

        self._server_id = None
        self._open_stack_api_version = None
        self.discriminator = None

        self.server_id = server_id
        if open_stack_api_version is not None:
            self.open_stack_api_version = open_stack_api_version

    @property
    def server_id(self):
        """Gets the server_id of this NovaShowServerRequest.

        云服务器ID。

        :return: The server_id of this NovaShowServerRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this NovaShowServerRequest.

        云服务器ID。

        :param server_id: The server_id of this NovaShowServerRequest.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def open_stack_api_version(self):
        """Gets the open_stack_api_version of this NovaShowServerRequest.

        微版本头

        :return: The open_stack_api_version of this NovaShowServerRequest.
        :rtype: str
        """
        return self._open_stack_api_version

    @open_stack_api_version.setter
    def open_stack_api_version(self, open_stack_api_version):
        """Sets the open_stack_api_version of this NovaShowServerRequest.

        微版本头

        :param open_stack_api_version: The open_stack_api_version of this NovaShowServerRequest.
        :type open_stack_api_version: str
        """
        self._open_stack_api_version = open_stack_api_version

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
        if not isinstance(other, NovaShowServerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
