# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgenciesPermissionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'system_permission_display_names': 'list[str]',
        'wanted_system_permission_display_names': 'list[str]'
    }

    attribute_map = {
        'system_permission_display_names': 'system_permission_display_names',
        'wanted_system_permission_display_names': 'wanted_system_permission_display_names'
    }

    def __init__(self, system_permission_display_names=None, wanted_system_permission_display_names=None):
        r"""AgenciesPermissionInfo

        The model defined in huaweicloud sdk

        :param system_permission_display_names: 委托权限项。
        :type system_permission_display_names: list[str]
        :param wanted_system_permission_display_names: 需要委托的权限项。
        :type wanted_system_permission_display_names: list[str]
        """
        
        

        self._system_permission_display_names = None
        self._wanted_system_permission_display_names = None
        self.discriminator = None

        if system_permission_display_names is not None:
            self.system_permission_display_names = system_permission_display_names
        if wanted_system_permission_display_names is not None:
            self.wanted_system_permission_display_names = wanted_system_permission_display_names

    @property
    def system_permission_display_names(self):
        r"""Gets the system_permission_display_names of this AgenciesPermissionInfo.

        委托权限项。

        :return: The system_permission_display_names of this AgenciesPermissionInfo.
        :rtype: list[str]
        """
        return self._system_permission_display_names

    @system_permission_display_names.setter
    def system_permission_display_names(self, system_permission_display_names):
        r"""Sets the system_permission_display_names of this AgenciesPermissionInfo.

        委托权限项。

        :param system_permission_display_names: The system_permission_display_names of this AgenciesPermissionInfo.
        :type system_permission_display_names: list[str]
        """
        self._system_permission_display_names = system_permission_display_names

    @property
    def wanted_system_permission_display_names(self):
        r"""Gets the wanted_system_permission_display_names of this AgenciesPermissionInfo.

        需要委托的权限项。

        :return: The wanted_system_permission_display_names of this AgenciesPermissionInfo.
        :rtype: list[str]
        """
        return self._wanted_system_permission_display_names

    @wanted_system_permission_display_names.setter
    def wanted_system_permission_display_names(self, wanted_system_permission_display_names):
        r"""Sets the wanted_system_permission_display_names of this AgenciesPermissionInfo.

        需要委托的权限项。

        :param wanted_system_permission_display_names: The wanted_system_permission_display_names of this AgenciesPermissionInfo.
        :type wanted_system_permission_display_names: list[str]
        """
        self._wanted_system_permission_display_names = wanted_system_permission_display_names

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
        if not isinstance(other, AgenciesPermissionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
