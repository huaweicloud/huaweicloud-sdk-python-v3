# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCommandResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_id': 'int',
        'command_id': 'int',
        'command_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'service_id': 'service_id',
        'command_id': 'command_id',
        'command_name': 'command_name',
        'description': 'description'
    }

    def __init__(self, service_id=None, command_id=None, command_name=None, description=None):
        r"""UpdateCommandResponse

        The model defined in huaweicloud sdk

        :param service_id: 命令所属服务id
        :type service_id: int
        :param command_id: 命令id
        :type command_id: int
        :param command_name: 命令名称
        :type command_name: str
        :param description: 命令描述
        :type description: str
        """
        
        super(UpdateCommandResponse, self).__init__()

        self._service_id = None
        self._command_id = None
        self._command_name = None
        self._description = None
        self.discriminator = None

        if service_id is not None:
            self.service_id = service_id
        if command_id is not None:
            self.command_id = command_id
        if command_name is not None:
            self.command_name = command_name
        if description is not None:
            self.description = description

    @property
    def service_id(self):
        r"""Gets the service_id of this UpdateCommandResponse.

        命令所属服务id

        :return: The service_id of this UpdateCommandResponse.
        :rtype: int
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this UpdateCommandResponse.

        命令所属服务id

        :param service_id: The service_id of this UpdateCommandResponse.
        :type service_id: int
        """
        self._service_id = service_id

    @property
    def command_id(self):
        r"""Gets the command_id of this UpdateCommandResponse.

        命令id

        :return: The command_id of this UpdateCommandResponse.
        :rtype: int
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        r"""Sets the command_id of this UpdateCommandResponse.

        命令id

        :param command_id: The command_id of this UpdateCommandResponse.
        :type command_id: int
        """
        self._command_id = command_id

    @property
    def command_name(self):
        r"""Gets the command_name of this UpdateCommandResponse.

        命令名称

        :return: The command_name of this UpdateCommandResponse.
        :rtype: str
        """
        return self._command_name

    @command_name.setter
    def command_name(self, command_name):
        r"""Sets the command_name of this UpdateCommandResponse.

        命令名称

        :param command_name: The command_name of this UpdateCommandResponse.
        :type command_name: str
        """
        self._command_name = command_name

    @property
    def description(self):
        r"""Gets the description of this UpdateCommandResponse.

        命令描述

        :return: The description of this UpdateCommandResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateCommandResponse.

        命令描述

        :param description: The description of this UpdateCommandResponse.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, UpdateCommandResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
