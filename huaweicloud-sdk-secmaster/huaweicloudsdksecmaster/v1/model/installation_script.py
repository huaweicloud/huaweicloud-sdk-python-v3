# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstallationScript:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'commands': 'str',
        'os_type': 'str'
    }

    attribute_map = {
        'commands': 'commands',
        'os_type': 'os_type'
    }

    def __init__(self, commands=None, os_type=None):
        r"""InstallationScript

        The model defined in huaweicloud sdk

        :param commands: 方法
        :type commands: str
        :param os_type: 操作系统类型
        :type os_type: str
        """
        
        

        self._commands = None
        self._os_type = None
        self.discriminator = None

        if commands is not None:
            self.commands = commands
        if os_type is not None:
            self.os_type = os_type

    @property
    def commands(self):
        r"""Gets the commands of this InstallationScript.

        方法

        :return: The commands of this InstallationScript.
        :rtype: str
        """
        return self._commands

    @commands.setter
    def commands(self, commands):
        r"""Sets the commands of this InstallationScript.

        方法

        :param commands: The commands of this InstallationScript.
        :type commands: str
        """
        self._commands = commands

    @property
    def os_type(self):
        r"""Gets the os_type of this InstallationScript.

        操作系统类型

        :return: The os_type of this InstallationScript.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this InstallationScript.

        操作系统类型

        :param os_type: The os_type of this InstallationScript.
        :type os_type: str
        """
        self._os_type = os_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InstallationScript):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
