# coding: utf-8

import pprint
import re

import six





class CreateImageSyncRepoRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'remote_region_id': 'str',
        'remote_namespace': 'str',
        'sync_auto': 'bool',
        'override': 'bool'
    }

    attribute_map = {
        'remote_region_id': 'remoteRegionId',
        'remote_namespace': 'remoteNamespace',
        'sync_auto': 'syncAuto',
        'override': 'override'
    }

    def __init__(self, remote_region_id=None, remote_namespace=None, sync_auto=None, override=None):
        """CreateImageSyncRepoRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._remote_region_id = None
        self._remote_namespace = None
        self._sync_auto = None
        self._override = None
        self.discriminator = None

        self.remote_region_id = remote_region_id
        self.remote_namespace = remote_namespace
        if sync_auto is not None:
            self.sync_auto = sync_auto
        if override is not None:
            self.override = override

    @property
    def remote_region_id(self):
        """Gets the remote_region_id of this CreateImageSyncRepoRequestBody.

        目标region ID。

        :return: The remote_region_id of this CreateImageSyncRepoRequestBody.
        :rtype: str
        """
        return self._remote_region_id

    @remote_region_id.setter
    def remote_region_id(self, remote_region_id):
        """Sets the remote_region_id of this CreateImageSyncRepoRequestBody.

        目标region ID。

        :param remote_region_id: The remote_region_id of this CreateImageSyncRepoRequestBody.
        :type: str
        """
        self._remote_region_id = remote_region_id

    @property
    def remote_namespace(self):
        """Gets the remote_namespace of this CreateImageSyncRepoRequestBody.

        目标组织

        :return: The remote_namespace of this CreateImageSyncRepoRequestBody.
        :rtype: str
        """
        return self._remote_namespace

    @remote_namespace.setter
    def remote_namespace(self, remote_namespace):
        """Sets the remote_namespace of this CreateImageSyncRepoRequestBody.

        目标组织

        :param remote_namespace: The remote_namespace of this CreateImageSyncRepoRequestBody.
        :type: str
        """
        self._remote_namespace = remote_namespace

    @property
    def sync_auto(self):
        """Gets the sync_auto of this CreateImageSyncRepoRequestBody.

        自动同步，默认为false

        :return: The sync_auto of this CreateImageSyncRepoRequestBody.
        :rtype: bool
        """
        return self._sync_auto

    @sync_auto.setter
    def sync_auto(self, sync_auto):
        """Sets the sync_auto of this CreateImageSyncRepoRequestBody.

        自动同步，默认为false

        :param sync_auto: The sync_auto of this CreateImageSyncRepoRequestBody.
        :type: bool
        """
        self._sync_auto = sync_auto

    @property
    def override(self):
        """Gets the override of this CreateImageSyncRepoRequestBody.

        是否覆盖，默认为false

        :return: The override of this CreateImageSyncRepoRequestBody.
        :rtype: bool
        """
        return self._override

    @override.setter
    def override(self, override):
        """Sets the override of this CreateImageSyncRepoRequestBody.

        是否覆盖，默认为false

        :param override: The override of this CreateImageSyncRepoRequestBody.
        :type: bool
        """
        self._override = override

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateImageSyncRepoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
