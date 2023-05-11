# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpExtraInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup': 'OpExtendInfoBckup',
        'common': 'OpExtendInfoCommon',
        'delete': 'OpExtendInfoDelete',
        'sync': 'OpExtendInfoSync',
        'remove_resources': 'OpExtendInfoRemoveResources',
        'replication': 'OpExtendInfoReplication',
        'resource': 'Resource',
        'restore': 'OpExtendInfoRestore',
        'vault_delete': 'OpExtendInfoVaultDelete'
    }

    attribute_map = {
        'backup': 'backup',
        'common': 'common',
        'delete': 'delete',
        'sync': 'sync',
        'remove_resources': 'remove_resources',
        'replication': 'replication',
        'resource': 'resource',
        'restore': 'restore',
        'vault_delete': 'vault_delete'
    }

    def __init__(self, backup=None, common=None, delete=None, sync=None, remove_resources=None, replication=None, resource=None, restore=None, vault_delete=None):
        """OpExtraInfo

        The model defined in huaweicloud sdk

        :param backup: 
        :type backup: :class:`huaweicloudsdkcbr.v1.OpExtendInfoBckup`
        :param common: 
        :type common: :class:`huaweicloudsdkcbr.v1.OpExtendInfoCommon`
        :param delete: 
        :type delete: :class:`huaweicloudsdkcbr.v1.OpExtendInfoDelete`
        :param sync: 
        :type sync: :class:`huaweicloudsdkcbr.v1.OpExtendInfoSync`
        :param remove_resources: 
        :type remove_resources: :class:`huaweicloudsdkcbr.v1.OpExtendInfoRemoveResources`
        :param replication: 
        :type replication: :class:`huaweicloudsdkcbr.v1.OpExtendInfoReplication`
        :param resource: 
        :type resource: :class:`huaweicloudsdkcbr.v1.Resource`
        :param restore: 
        :type restore: :class:`huaweicloudsdkcbr.v1.OpExtendInfoRestore`
        :param vault_delete: 
        :type vault_delete: :class:`huaweicloudsdkcbr.v1.OpExtendInfoVaultDelete`
        """
        
        

        self._backup = None
        self._common = None
        self._delete = None
        self._sync = None
        self._remove_resources = None
        self._replication = None
        self._resource = None
        self._restore = None
        self._vault_delete = None
        self.discriminator = None

        if backup is not None:
            self.backup = backup
        self.common = common
        if delete is not None:
            self.delete = delete
        if sync is not None:
            self.sync = sync
        if remove_resources is not None:
            self.remove_resources = remove_resources
        if replication is not None:
            self.replication = replication
        self.resource = resource
        if restore is not None:
            self.restore = restore
        if vault_delete is not None:
            self.vault_delete = vault_delete

    @property
    def backup(self):
        """Gets the backup of this OpExtraInfo.

        :return: The backup of this OpExtraInfo.
        :rtype: :class:`huaweicloudsdkcbr.v1.OpExtendInfoBckup`
        """
        return self._backup

    @backup.setter
    def backup(self, backup):
        """Sets the backup of this OpExtraInfo.

        :param backup: The backup of this OpExtraInfo.
        :type backup: :class:`huaweicloudsdkcbr.v1.OpExtendInfoBckup`
        """
        self._backup = backup

    @property
    def common(self):
        """Gets the common of this OpExtraInfo.

        :return: The common of this OpExtraInfo.
        :rtype: :class:`huaweicloudsdkcbr.v1.OpExtendInfoCommon`
        """
        return self._common

    @common.setter
    def common(self, common):
        """Sets the common of this OpExtraInfo.

        :param common: The common of this OpExtraInfo.
        :type common: :class:`huaweicloudsdkcbr.v1.OpExtendInfoCommon`
        """
        self._common = common

    @property
    def delete(self):
        """Gets the delete of this OpExtraInfo.

        :return: The delete of this OpExtraInfo.
        :rtype: :class:`huaweicloudsdkcbr.v1.OpExtendInfoDelete`
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """Sets the delete of this OpExtraInfo.

        :param delete: The delete of this OpExtraInfo.
        :type delete: :class:`huaweicloudsdkcbr.v1.OpExtendInfoDelete`
        """
        self._delete = delete

    @property
    def sync(self):
        """Gets the sync of this OpExtraInfo.

        :return: The sync of this OpExtraInfo.
        :rtype: :class:`huaweicloudsdkcbr.v1.OpExtendInfoSync`
        """
        return self._sync

    @sync.setter
    def sync(self, sync):
        """Sets the sync of this OpExtraInfo.

        :param sync: The sync of this OpExtraInfo.
        :type sync: :class:`huaweicloudsdkcbr.v1.OpExtendInfoSync`
        """
        self._sync = sync

    @property
    def remove_resources(self):
        """Gets the remove_resources of this OpExtraInfo.

        :return: The remove_resources of this OpExtraInfo.
        :rtype: :class:`huaweicloudsdkcbr.v1.OpExtendInfoRemoveResources`
        """
        return self._remove_resources

    @remove_resources.setter
    def remove_resources(self, remove_resources):
        """Sets the remove_resources of this OpExtraInfo.

        :param remove_resources: The remove_resources of this OpExtraInfo.
        :type remove_resources: :class:`huaweicloudsdkcbr.v1.OpExtendInfoRemoveResources`
        """
        self._remove_resources = remove_resources

    @property
    def replication(self):
        """Gets the replication of this OpExtraInfo.

        :return: The replication of this OpExtraInfo.
        :rtype: :class:`huaweicloudsdkcbr.v1.OpExtendInfoReplication`
        """
        return self._replication

    @replication.setter
    def replication(self, replication):
        """Sets the replication of this OpExtraInfo.

        :param replication: The replication of this OpExtraInfo.
        :type replication: :class:`huaweicloudsdkcbr.v1.OpExtendInfoReplication`
        """
        self._replication = replication

    @property
    def resource(self):
        """Gets the resource of this OpExtraInfo.

        :return: The resource of this OpExtraInfo.
        :rtype: :class:`huaweicloudsdkcbr.v1.Resource`
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this OpExtraInfo.

        :param resource: The resource of this OpExtraInfo.
        :type resource: :class:`huaweicloudsdkcbr.v1.Resource`
        """
        self._resource = resource

    @property
    def restore(self):
        """Gets the restore of this OpExtraInfo.

        :return: The restore of this OpExtraInfo.
        :rtype: :class:`huaweicloudsdkcbr.v1.OpExtendInfoRestore`
        """
        return self._restore

    @restore.setter
    def restore(self, restore):
        """Sets the restore of this OpExtraInfo.

        :param restore: The restore of this OpExtraInfo.
        :type restore: :class:`huaweicloudsdkcbr.v1.OpExtendInfoRestore`
        """
        self._restore = restore

    @property
    def vault_delete(self):
        """Gets the vault_delete of this OpExtraInfo.

        :return: The vault_delete of this OpExtraInfo.
        :rtype: :class:`huaweicloudsdkcbr.v1.OpExtendInfoVaultDelete`
        """
        return self._vault_delete

    @vault_delete.setter
    def vault_delete(self, vault_delete):
        """Sets the vault_delete of this OpExtraInfo.

        :param vault_delete: The vault_delete of this OpExtraInfo.
        :type vault_delete: :class:`huaweicloudsdkcbr.v1.OpExtendInfoVaultDelete`
        """
        self._vault_delete = vault_delete

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
        if not isinstance(other, OpExtraInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
