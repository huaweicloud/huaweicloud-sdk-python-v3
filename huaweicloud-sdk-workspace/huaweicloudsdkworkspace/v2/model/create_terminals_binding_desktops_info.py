# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTerminalsBindingDesktopsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'line': 'int',
        'mac': 'str',
        'desktop_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'line': 'line',
        'mac': 'mac',
        'desktop_name': 'desktop_name',
        'description': 'description'
    }

    def __init__(self, line=None, mac=None, desktop_name=None, description=None):
        """CreateTerminalsBindingDesktopsInfo

        The model defined in huaweicloud sdk

        :param line: 行号,用于批量导入
        :type line: int
        :param mac: 终端mac地址
        :type mac: str
        :param desktop_name: 桌面名称，用于批量导入
        :type desktop_name: str
        :param description: 描述
        :type description: str
        """
        
        

        self._line = None
        self._mac = None
        self._desktop_name = None
        self._description = None
        self.discriminator = None

        if line is not None:
            self.line = line
        if mac is not None:
            self.mac = mac
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if description is not None:
            self.description = description

    @property
    def line(self):
        """Gets the line of this CreateTerminalsBindingDesktopsInfo.

        行号,用于批量导入

        :return: The line of this CreateTerminalsBindingDesktopsInfo.
        :rtype: int
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this CreateTerminalsBindingDesktopsInfo.

        行号,用于批量导入

        :param line: The line of this CreateTerminalsBindingDesktopsInfo.
        :type line: int
        """
        self._line = line

    @property
    def mac(self):
        """Gets the mac of this CreateTerminalsBindingDesktopsInfo.

        终端mac地址

        :return: The mac of this CreateTerminalsBindingDesktopsInfo.
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this CreateTerminalsBindingDesktopsInfo.

        终端mac地址

        :param mac: The mac of this CreateTerminalsBindingDesktopsInfo.
        :type mac: str
        """
        self._mac = mac

    @property
    def desktop_name(self):
        """Gets the desktop_name of this CreateTerminalsBindingDesktopsInfo.

        桌面名称，用于批量导入

        :return: The desktop_name of this CreateTerminalsBindingDesktopsInfo.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        """Sets the desktop_name of this CreateTerminalsBindingDesktopsInfo.

        桌面名称，用于批量导入

        :param desktop_name: The desktop_name of this CreateTerminalsBindingDesktopsInfo.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def description(self):
        """Gets the description of this CreateTerminalsBindingDesktopsInfo.

        描述

        :return: The description of this CreateTerminalsBindingDesktopsInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateTerminalsBindingDesktopsInfo.

        描述

        :param description: The description of this CreateTerminalsBindingDesktopsInfo.
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
        if not isinstance(other, CreateTerminalsBindingDesktopsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
