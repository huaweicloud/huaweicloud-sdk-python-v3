# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCommandResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'command_name': 'str',
        'command_param': 'ComandParam'
    }

    attribute_map = {
        'command_name': 'command_name',
        'command_param': 'command_param'
    }

    def __init__(self, command_name=None, command_param=None):
        """ShowCommandResponse

        The model defined in huaweicloud sdk

        :param command_name: 命令名称，分为：START、STOP、DELETE、SYNC
        :type command_name: str
        :param command_param: 
        :type command_param: :class:`huaweicloudsdksms.v3.ComandParam`
        """
        
        super(ShowCommandResponse, self).__init__()

        self._command_name = None
        self._command_param = None
        self.discriminator = None

        if command_name is not None:
            self.command_name = command_name
        if command_param is not None:
            self.command_param = command_param

    @property
    def command_name(self):
        """Gets the command_name of this ShowCommandResponse.

        命令名称，分为：START、STOP、DELETE、SYNC

        :return: The command_name of this ShowCommandResponse.
        :rtype: str
        """
        return self._command_name

    @command_name.setter
    def command_name(self, command_name):
        """Sets the command_name of this ShowCommandResponse.

        命令名称，分为：START、STOP、DELETE、SYNC

        :param command_name: The command_name of this ShowCommandResponse.
        :type command_name: str
        """
        self._command_name = command_name

    @property
    def command_param(self):
        """Gets the command_param of this ShowCommandResponse.

        :return: The command_param of this ShowCommandResponse.
        :rtype: :class:`huaweicloudsdksms.v3.ComandParam`
        """
        return self._command_param

    @command_param.setter
    def command_param(self, command_param):
        """Sets the command_param of this ShowCommandResponse.

        :param command_param: The command_param of this ShowCommandResponse.
        :type command_param: :class:`huaweicloudsdksms.v3.ComandParam`
        """
        self._command_param = command_param

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
        if not isinstance(other, ShowCommandResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
