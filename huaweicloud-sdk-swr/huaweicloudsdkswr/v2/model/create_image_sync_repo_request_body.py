# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        r"""CreateImageSyncRepoRequestBody

        The model defined in huaweicloud sdk

        :param remote_region_id: 目标region ID。
        :type remote_region_id: str
        :param remote_namespace: 目标组织
        :type remote_namespace: str
        :param sync_auto: 自动同步，默认为false
        :type sync_auto: bool
        :param override: 是否覆盖，默认为false
        :type override: bool
        """
        
        

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
        r"""Gets the remote_region_id of this CreateImageSyncRepoRequestBody.

        目标region ID。

        :return: The remote_region_id of this CreateImageSyncRepoRequestBody.
        :rtype: str
        """
        return self._remote_region_id

    @remote_region_id.setter
    def remote_region_id(self, remote_region_id):
        r"""Sets the remote_region_id of this CreateImageSyncRepoRequestBody.

        目标region ID。

        :param remote_region_id: The remote_region_id of this CreateImageSyncRepoRequestBody.
        :type remote_region_id: str
        """
        self._remote_region_id = remote_region_id

    @property
    def remote_namespace(self):
        r"""Gets the remote_namespace of this CreateImageSyncRepoRequestBody.

        目标组织

        :return: The remote_namespace of this CreateImageSyncRepoRequestBody.
        :rtype: str
        """
        return self._remote_namespace

    @remote_namespace.setter
    def remote_namespace(self, remote_namespace):
        r"""Sets the remote_namespace of this CreateImageSyncRepoRequestBody.

        目标组织

        :param remote_namespace: The remote_namespace of this CreateImageSyncRepoRequestBody.
        :type remote_namespace: str
        """
        self._remote_namespace = remote_namespace

    @property
    def sync_auto(self):
        r"""Gets the sync_auto of this CreateImageSyncRepoRequestBody.

        自动同步，默认为false

        :return: The sync_auto of this CreateImageSyncRepoRequestBody.
        :rtype: bool
        """
        return self._sync_auto

    @sync_auto.setter
    def sync_auto(self, sync_auto):
        r"""Sets the sync_auto of this CreateImageSyncRepoRequestBody.

        自动同步，默认为false

        :param sync_auto: The sync_auto of this CreateImageSyncRepoRequestBody.
        :type sync_auto: bool
        """
        self._sync_auto = sync_auto

    @property
    def override(self):
        r"""Gets the override of this CreateImageSyncRepoRequestBody.

        是否覆盖，默认为false

        :return: The override of this CreateImageSyncRepoRequestBody.
        :rtype: bool
        """
        return self._override

    @override.setter
    def override(self, override):
        r"""Sets the override of this CreateImageSyncRepoRequestBody.

        是否覆盖，默认为false

        :param override: The override of this CreateImageSyncRepoRequestBody.
        :type override: bool
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
        if not isinstance(other, CreateImageSyncRepoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
