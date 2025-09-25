# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CycleImageScanPolicyReqInfoRegistryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'registry_id': 'str',
        'registry_name': 'str',
        'registry_type': 'str'
    }

    attribute_map = {
        'registry_id': 'registry_id',
        'registry_name': 'registry_name',
        'registry_type': 'registry_type'
    }

    def __init__(self, registry_id=None, registry_name=None, registry_type=None):
        r"""CycleImageScanPolicyReqInfoRegistryInfo

        The model defined in huaweicloud sdk

        :param registry_id: 镜像仓库Id
        :type registry_id: str
        :param registry_name: 镜像仓库名称
        :type registry_name: str
        :param registry_type: 镜像仓库类型 | SwrPrivate:swr私有 SwrShared:swr共享 SwrEnterprise:swr企业 Harbor:harbor仓库 Jfrog:jfrog仓库 Other:其他仓库
        :type registry_type: str
        """
        
        

        self._registry_id = None
        self._registry_name = None
        self._registry_type = None
        self.discriminator = None

        if registry_id is not None:
            self.registry_id = registry_id
        if registry_name is not None:
            self.registry_name = registry_name
        if registry_type is not None:
            self.registry_type = registry_type

    @property
    def registry_id(self):
        r"""Gets the registry_id of this CycleImageScanPolicyReqInfoRegistryInfo.

        镜像仓库Id

        :return: The registry_id of this CycleImageScanPolicyReqInfoRegistryInfo.
        :rtype: str
        """
        return self._registry_id

    @registry_id.setter
    def registry_id(self, registry_id):
        r"""Sets the registry_id of this CycleImageScanPolicyReqInfoRegistryInfo.

        镜像仓库Id

        :param registry_id: The registry_id of this CycleImageScanPolicyReqInfoRegistryInfo.
        :type registry_id: str
        """
        self._registry_id = registry_id

    @property
    def registry_name(self):
        r"""Gets the registry_name of this CycleImageScanPolicyReqInfoRegistryInfo.

        镜像仓库名称

        :return: The registry_name of this CycleImageScanPolicyReqInfoRegistryInfo.
        :rtype: str
        """
        return self._registry_name

    @registry_name.setter
    def registry_name(self, registry_name):
        r"""Sets the registry_name of this CycleImageScanPolicyReqInfoRegistryInfo.

        镜像仓库名称

        :param registry_name: The registry_name of this CycleImageScanPolicyReqInfoRegistryInfo.
        :type registry_name: str
        """
        self._registry_name = registry_name

    @property
    def registry_type(self):
        r"""Gets the registry_type of this CycleImageScanPolicyReqInfoRegistryInfo.

        镜像仓库类型 | SwrPrivate:swr私有 SwrShared:swr共享 SwrEnterprise:swr企业 Harbor:harbor仓库 Jfrog:jfrog仓库 Other:其他仓库

        :return: The registry_type of this CycleImageScanPolicyReqInfoRegistryInfo.
        :rtype: str
        """
        return self._registry_type

    @registry_type.setter
    def registry_type(self, registry_type):
        r"""Sets the registry_type of this CycleImageScanPolicyReqInfoRegistryInfo.

        镜像仓库类型 | SwrPrivate:swr私有 SwrShared:swr共享 SwrEnterprise:swr企业 Harbor:harbor仓库 Jfrog:jfrog仓库 Other:其他仓库

        :param registry_type: The registry_type of this CycleImageScanPolicyReqInfoRegistryInfo.
        :type registry_type: str
        """
        self._registry_type = registry_type

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
        if not isinstance(other, CycleImageScanPolicyReqInfoRegistryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
