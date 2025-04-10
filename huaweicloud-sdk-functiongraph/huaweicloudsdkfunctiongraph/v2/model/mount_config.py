# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MountConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mount_user': 'MountUser',
        'func_mounts': 'list[FuncMount]'
    }

    attribute_map = {
        'mount_user': 'mount_user',
        'func_mounts': 'func_mounts'
    }

    def __init__(self, mount_user=None, func_mounts=None):
        r"""MountConfig

        The model defined in huaweicloud sdk

        :param mount_user: 
        :type mount_user: :class:`huaweicloudsdkfunctiongraph.v2.MountUser`
        :param func_mounts: 函数挂载列表。
        :type func_mounts: list[:class:`huaweicloudsdkfunctiongraph.v2.FuncMount`]
        """
        
        

        self._mount_user = None
        self._func_mounts = None
        self.discriminator = None

        self.mount_user = mount_user
        self.func_mounts = func_mounts

    @property
    def mount_user(self):
        r"""Gets the mount_user of this MountConfig.

        :return: The mount_user of this MountConfig.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.MountUser`
        """
        return self._mount_user

    @mount_user.setter
    def mount_user(self, mount_user):
        r"""Sets the mount_user of this MountConfig.

        :param mount_user: The mount_user of this MountConfig.
        :type mount_user: :class:`huaweicloudsdkfunctiongraph.v2.MountUser`
        """
        self._mount_user = mount_user

    @property
    def func_mounts(self):
        r"""Gets the func_mounts of this MountConfig.

        函数挂载列表。

        :return: The func_mounts of this MountConfig.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.FuncMount`]
        """
        return self._func_mounts

    @func_mounts.setter
    def func_mounts(self, func_mounts):
        r"""Sets the func_mounts of this MountConfig.

        函数挂载列表。

        :param func_mounts: The func_mounts of this MountConfig.
        :type func_mounts: list[:class:`huaweicloudsdkfunctiongraph.v2.FuncMount`]
        """
        self._func_mounts = func_mounts

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
        if not isinstance(other, MountConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
