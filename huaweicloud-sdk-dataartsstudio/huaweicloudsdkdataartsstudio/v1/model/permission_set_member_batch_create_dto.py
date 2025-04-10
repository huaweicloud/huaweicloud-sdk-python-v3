# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionSetMemberBatchCreateDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'members': 'list[PermissionSetMemberCreateDTO2]',
        'auto_sync': 'bool'
    }

    attribute_map = {
        'members': 'members',
        'auto_sync': 'auto_sync'
    }

    def __init__(self, members=None, auto_sync=None):
        r"""PermissionSetMemberBatchCreateDTO

        The model defined in huaweicloud sdk

        :param members: 权限集成员创建参数列表
        :type members: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionSetMemberCreateDTO2`]
        :param auto_sync: 是否自动触发同步, 默认false
        :type auto_sync: bool
        """
        
        

        self._members = None
        self._auto_sync = None
        self.discriminator = None

        if members is not None:
            self.members = members
        if auto_sync is not None:
            self.auto_sync = auto_sync

    @property
    def members(self):
        r"""Gets the members of this PermissionSetMemberBatchCreateDTO.

        权限集成员创建参数列表

        :return: The members of this PermissionSetMemberBatchCreateDTO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionSetMemberCreateDTO2`]
        """
        return self._members

    @members.setter
    def members(self, members):
        r"""Sets the members of this PermissionSetMemberBatchCreateDTO.

        权限集成员创建参数列表

        :param members: The members of this PermissionSetMemberBatchCreateDTO.
        :type members: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionSetMemberCreateDTO2`]
        """
        self._members = members

    @property
    def auto_sync(self):
        r"""Gets the auto_sync of this PermissionSetMemberBatchCreateDTO.

        是否自动触发同步, 默认false

        :return: The auto_sync of this PermissionSetMemberBatchCreateDTO.
        :rtype: bool
        """
        return self._auto_sync

    @auto_sync.setter
    def auto_sync(self, auto_sync):
        r"""Sets the auto_sync of this PermissionSetMemberBatchCreateDTO.

        是否自动触发同步, 默认false

        :param auto_sync: The auto_sync of this PermissionSetMemberBatchCreateDTO.
        :type auto_sync: bool
        """
        self._auto_sync = auto_sync

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
        if not isinstance(other, PermissionSetMemberBatchCreateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
