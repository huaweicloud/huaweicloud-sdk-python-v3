# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectableAgentStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'int',
        'installed': 'bool',
        'is_old': 'bool',
        'message': 'str',
        'resource_id': 'str',
        'version': 'str'
    }

    attribute_map = {
        'code': 'code',
        'installed': 'installed',
        'is_old': 'is_old',
        'message': 'message',
        'resource_id': 'resource_id',
        'version': 'version'
    }

    def __init__(self, code=None, installed=None, is_old=None, message=None, resource_id=None, version=None):
        """ProtectableAgentStatus

        The model defined in huaweicloud sdk

        :param code: agent无法连接的错误码
        :type code: int
        :param installed: agent是否安装
        :type installed: bool
        :param is_old: agent是否为老版本
        :type is_old: bool
        :param message: agent无法连接的错误信息
        :type message: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param version: agent版本号
        :type version: str
        """
        
        

        self._code = None
        self._installed = None
        self._is_old = None
        self._message = None
        self._resource_id = None
        self._version = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if installed is not None:
            self.installed = installed
        if is_old is not None:
            self.is_old = is_old
        if message is not None:
            self.message = message
        if resource_id is not None:
            self.resource_id = resource_id
        if version is not None:
            self.version = version

    @property
    def code(self):
        """Gets the code of this ProtectableAgentStatus.

        agent无法连接的错误码

        :return: The code of this ProtectableAgentStatus.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ProtectableAgentStatus.

        agent无法连接的错误码

        :param code: The code of this ProtectableAgentStatus.
        :type code: int
        """
        self._code = code

    @property
    def installed(self):
        """Gets the installed of this ProtectableAgentStatus.

        agent是否安装

        :return: The installed of this ProtectableAgentStatus.
        :rtype: bool
        """
        return self._installed

    @installed.setter
    def installed(self, installed):
        """Sets the installed of this ProtectableAgentStatus.

        agent是否安装

        :param installed: The installed of this ProtectableAgentStatus.
        :type installed: bool
        """
        self._installed = installed

    @property
    def is_old(self):
        """Gets the is_old of this ProtectableAgentStatus.

        agent是否为老版本

        :return: The is_old of this ProtectableAgentStatus.
        :rtype: bool
        """
        return self._is_old

    @is_old.setter
    def is_old(self, is_old):
        """Sets the is_old of this ProtectableAgentStatus.

        agent是否为老版本

        :param is_old: The is_old of this ProtectableAgentStatus.
        :type is_old: bool
        """
        self._is_old = is_old

    @property
    def message(self):
        """Gets the message of this ProtectableAgentStatus.

        agent无法连接的错误信息

        :return: The message of this ProtectableAgentStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ProtectableAgentStatus.

        agent无法连接的错误信息

        :param message: The message of this ProtectableAgentStatus.
        :type message: str
        """
        self._message = message

    @property
    def resource_id(self):
        """Gets the resource_id of this ProtectableAgentStatus.

        资源ID

        :return: The resource_id of this ProtectableAgentStatus.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ProtectableAgentStatus.

        资源ID

        :param resource_id: The resource_id of this ProtectableAgentStatus.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def version(self):
        """Gets the version of this ProtectableAgentStatus.

        agent版本号

        :return: The version of this ProtectableAgentStatus.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ProtectableAgentStatus.

        agent版本号

        :param version: The version of this ProtectableAgentStatus.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ProtectableAgentStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
