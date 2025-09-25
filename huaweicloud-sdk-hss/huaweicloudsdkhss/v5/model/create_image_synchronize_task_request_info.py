# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateImageSynchronizeTaskRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sync_all_registries': 'bool',
        'registry_info': 'list[CreateImageSynchronizeTaskRequestInfoRegistryInfo]'
    }

    attribute_map = {
        'sync_all_registries': 'sync_all_registries',
        'registry_info': 'registry_info'
    }

    def __init__(self, sync_all_registries=None, registry_info=None):
        r"""CreateImageSynchronizeTaskRequestInfo

        The model defined in huaweicloud sdk

        :param sync_all_registries: 同步全部仓库镜像 | true 同步全部镜像 false 指定镜像仓同步
        :type sync_all_registries: bool
        :param registry_info: 待同步镜像仓
        :type registry_info: list[:class:`huaweicloudsdkhss.v5.CreateImageSynchronizeTaskRequestInfoRegistryInfo`]
        """
        
        

        self._sync_all_registries = None
        self._registry_info = None
        self.discriminator = None

        self.sync_all_registries = sync_all_registries
        if registry_info is not None:
            self.registry_info = registry_info

    @property
    def sync_all_registries(self):
        r"""Gets the sync_all_registries of this CreateImageSynchronizeTaskRequestInfo.

        同步全部仓库镜像 | true 同步全部镜像 false 指定镜像仓同步

        :return: The sync_all_registries of this CreateImageSynchronizeTaskRequestInfo.
        :rtype: bool
        """
        return self._sync_all_registries

    @sync_all_registries.setter
    def sync_all_registries(self, sync_all_registries):
        r"""Sets the sync_all_registries of this CreateImageSynchronizeTaskRequestInfo.

        同步全部仓库镜像 | true 同步全部镜像 false 指定镜像仓同步

        :param sync_all_registries: The sync_all_registries of this CreateImageSynchronizeTaskRequestInfo.
        :type sync_all_registries: bool
        """
        self._sync_all_registries = sync_all_registries

    @property
    def registry_info(self):
        r"""Gets the registry_info of this CreateImageSynchronizeTaskRequestInfo.

        待同步镜像仓

        :return: The registry_info of this CreateImageSynchronizeTaskRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.CreateImageSynchronizeTaskRequestInfoRegistryInfo`]
        """
        return self._registry_info

    @registry_info.setter
    def registry_info(self, registry_info):
        r"""Sets the registry_info of this CreateImageSynchronizeTaskRequestInfo.

        待同步镜像仓

        :param registry_info: The registry_info of this CreateImageSynchronizeTaskRequestInfo.
        :type registry_info: list[:class:`huaweicloudsdkhss.v5.CreateImageSynchronizeTaskRequestInfoRegistryInfo`]
        """
        self._registry_info = registry_info

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
        if not isinstance(other, CreateImageSynchronizeTaskRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
