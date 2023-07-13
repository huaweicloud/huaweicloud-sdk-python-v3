# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupResources:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vault_id': 'str',
        'resource_list': 'list[ResourceInfo]'
    }

    attribute_map = {
        'vault_id': 'vault_id',
        'resource_list': 'resource_list'
    }

    def __init__(self, vault_id=None, resource_list=None):
        """BackupResources

        The model defined in huaweicloud sdk

        :param vault_id: 选择需要绑定的存储库ID，不为空
        :type vault_id: str
        :param resource_list: 需要开启备份功能的主机情况列表
        :type resource_list: list[:class:`huaweicloudsdkhss.v5.ResourceInfo`]
        """
        
        

        self._vault_id = None
        self._resource_list = None
        self.discriminator = None

        if vault_id is not None:
            self.vault_id = vault_id
        if resource_list is not None:
            self.resource_list = resource_list

    @property
    def vault_id(self):
        """Gets the vault_id of this BackupResources.

        选择需要绑定的存储库ID，不为空

        :return: The vault_id of this BackupResources.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this BackupResources.

        选择需要绑定的存储库ID，不为空

        :param vault_id: The vault_id of this BackupResources.
        :type vault_id: str
        """
        self._vault_id = vault_id

    @property
    def resource_list(self):
        """Gets the resource_list of this BackupResources.

        需要开启备份功能的主机情况列表

        :return: The resource_list of this BackupResources.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ResourceInfo`]
        """
        return self._resource_list

    @resource_list.setter
    def resource_list(self, resource_list):
        """Sets the resource_list of this BackupResources.

        需要开启备份功能的主机情况列表

        :param resource_list: The resource_list of this BackupResources.
        :type resource_list: list[:class:`huaweicloudsdkhss.v5.ResourceInfo`]
        """
        self._resource_list = resource_list

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
        if not isinstance(other, BackupResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
