# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TerminalsBindingDesktopsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'mac': 'str',
        'desktop_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'mac': 'mac',
        'desktop_name': 'desktop_name',
        'description': 'description'
    }

    def __init__(self, id=None, mac=None, desktop_name=None, description=None):
        """TerminalsBindingDesktopsInfo

        The model defined in huaweicloud sdk

        :param id: MAC绑定策略ID
        :type id: str
        :param mac: 终端MAC地址
        :type mac: str
        :param desktop_name: 虚拟机名称
        :type desktop_name: str
        :param description: 描述
        :type description: str
        """
        
        

        self._id = None
        self._mac = None
        self._desktop_name = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if mac is not None:
            self.mac = mac
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this TerminalsBindingDesktopsInfo.

        MAC绑定策略ID

        :return: The id of this TerminalsBindingDesktopsInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TerminalsBindingDesktopsInfo.

        MAC绑定策略ID

        :param id: The id of this TerminalsBindingDesktopsInfo.
        :type id: str
        """
        self._id = id

    @property
    def mac(self):
        """Gets the mac of this TerminalsBindingDesktopsInfo.

        终端MAC地址

        :return: The mac of this TerminalsBindingDesktopsInfo.
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this TerminalsBindingDesktopsInfo.

        终端MAC地址

        :param mac: The mac of this TerminalsBindingDesktopsInfo.
        :type mac: str
        """
        self._mac = mac

    @property
    def desktop_name(self):
        """Gets the desktop_name of this TerminalsBindingDesktopsInfo.

        虚拟机名称

        :return: The desktop_name of this TerminalsBindingDesktopsInfo.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        """Sets the desktop_name of this TerminalsBindingDesktopsInfo.

        虚拟机名称

        :param desktop_name: The desktop_name of this TerminalsBindingDesktopsInfo.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def description(self):
        """Gets the description of this TerminalsBindingDesktopsInfo.

        描述

        :return: The description of this TerminalsBindingDesktopsInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TerminalsBindingDesktopsInfo.

        描述

        :param description: The description of this TerminalsBindingDesktopsInfo.
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
        if not isinstance(other, TerminalsBindingDesktopsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
