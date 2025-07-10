# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyDesktopAttributesReqDesktop:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'computer_name': 'str',
        'self_backup_management': 'str'
    }

    attribute_map = {
        'computer_name': 'computer_name',
        'self_backup_management': 'self_backup_management'
    }

    def __init__(self, computer_name=None, self_backup_management=None):
        r"""ModifyDesktopAttributesReqDesktop

        The model defined in huaweicloud sdk

        :param computer_name: 桌面名。
        :type computer_name: str
        :param self_backup_management: 是否开启快照的操作类型,\&quot;0\&quot;:关闭 \&quot;1\&quot;:开启。
        :type self_backup_management: str
        """
        
        

        self._computer_name = None
        self._self_backup_management = None
        self.discriminator = None

        if computer_name is not None:
            self.computer_name = computer_name
        if self_backup_management is not None:
            self.self_backup_management = self_backup_management

    @property
    def computer_name(self):
        r"""Gets the computer_name of this ModifyDesktopAttributesReqDesktop.

        桌面名。

        :return: The computer_name of this ModifyDesktopAttributesReqDesktop.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        r"""Sets the computer_name of this ModifyDesktopAttributesReqDesktop.

        桌面名。

        :param computer_name: The computer_name of this ModifyDesktopAttributesReqDesktop.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def self_backup_management(self):
        r"""Gets the self_backup_management of this ModifyDesktopAttributesReqDesktop.

        是否开启快照的操作类型,\"0\":关闭 \"1\":开启。

        :return: The self_backup_management of this ModifyDesktopAttributesReqDesktop.
        :rtype: str
        """
        return self._self_backup_management

    @self_backup_management.setter
    def self_backup_management(self, self_backup_management):
        r"""Sets the self_backup_management of this ModifyDesktopAttributesReqDesktop.

        是否开启快照的操作类型,\"0\":关闭 \"1\":开启。

        :param self_backup_management: The self_backup_management of this ModifyDesktopAttributesReqDesktop.
        :type self_backup_management: str
        """
        self._self_backup_management = self_backup_management

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
        if not isinstance(other, ModifyDesktopAttributesReqDesktop):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
