# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAutopilotClusterUpgradeFeatureGatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_version': 'str',
        'kind': 'str',
        'metadata': 'Metadata',
        'upgrade_feature_gates': 'dict(str, str)'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'upgrade_feature_gates': 'upgradeFeatureGates'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, upgrade_feature_gates=None):
        r"""ListAutopilotClusterUpgradeFeatureGatesResponse

        The model defined in huaweicloud sdk

        :param api_version: API版本
        :type api_version: str
        :param kind: 资源类型
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcce.v3.Metadata`
        :param upgrade_feature_gates: 特性开关信息,格式为key/value键值对。 - Key: 目前有下列值：DisplayPreCheckDetail(展示所有集群升级前检查项详情),EvsSnapshot(使用EVS快照备份集群), LabelForSkippedNode(支持为集群升级过程中跳过的节点打标签), UpgradeStrategy(集群升级策略) - Value: Support 支持,Disable 关闭,Default 使用CCE服务默认规则判断
        :type upgrade_feature_gates: dict(str, str)
        """
        
        super(ListAutopilotClusterUpgradeFeatureGatesResponse, self).__init__()

        self._api_version = None
        self._kind = None
        self._metadata = None
        self._upgrade_feature_gates = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if upgrade_feature_gates is not None:
            self.upgrade_feature_gates = upgrade_feature_gates

    @property
    def api_version(self):
        r"""Gets the api_version of this ListAutopilotClusterUpgradeFeatureGatesResponse.

        API版本

        :return: The api_version of this ListAutopilotClusterUpgradeFeatureGatesResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this ListAutopilotClusterUpgradeFeatureGatesResponse.

        API版本

        :param api_version: The api_version of this ListAutopilotClusterUpgradeFeatureGatesResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this ListAutopilotClusterUpgradeFeatureGatesResponse.

        资源类型

        :return: The kind of this ListAutopilotClusterUpgradeFeatureGatesResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this ListAutopilotClusterUpgradeFeatureGatesResponse.

        资源类型

        :param kind: The kind of this ListAutopilotClusterUpgradeFeatureGatesResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        r"""Gets the metadata of this ListAutopilotClusterUpgradeFeatureGatesResponse.

        :return: The metadata of this ListAutopilotClusterUpgradeFeatureGatesResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.Metadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ListAutopilotClusterUpgradeFeatureGatesResponse.

        :param metadata: The metadata of this ListAutopilotClusterUpgradeFeatureGatesResponse.
        :type metadata: :class:`huaweicloudsdkcce.v3.Metadata`
        """
        self._metadata = metadata

    @property
    def upgrade_feature_gates(self):
        r"""Gets the upgrade_feature_gates of this ListAutopilotClusterUpgradeFeatureGatesResponse.

        特性开关信息,格式为key/value键值对。 - Key: 目前有下列值：DisplayPreCheckDetail(展示所有集群升级前检查项详情),EvsSnapshot(使用EVS快照备份集群), LabelForSkippedNode(支持为集群升级过程中跳过的节点打标签), UpgradeStrategy(集群升级策略) - Value: Support 支持,Disable 关闭,Default 使用CCE服务默认规则判断

        :return: The upgrade_feature_gates of this ListAutopilotClusterUpgradeFeatureGatesResponse.
        :rtype: dict(str, str)
        """
        return self._upgrade_feature_gates

    @upgrade_feature_gates.setter
    def upgrade_feature_gates(self, upgrade_feature_gates):
        r"""Sets the upgrade_feature_gates of this ListAutopilotClusterUpgradeFeatureGatesResponse.

        特性开关信息,格式为key/value键值对。 - Key: 目前有下列值：DisplayPreCheckDetail(展示所有集群升级前检查项详情),EvsSnapshot(使用EVS快照备份集群), LabelForSkippedNode(支持为集群升级过程中跳过的节点打标签), UpgradeStrategy(集群升级策略) - Value: Support 支持,Disable 关闭,Default 使用CCE服务默认规则判断

        :param upgrade_feature_gates: The upgrade_feature_gates of this ListAutopilotClusterUpgradeFeatureGatesResponse.
        :type upgrade_feature_gates: dict(str, str)
        """
        self._upgrade_feature_gates = upgrade_feature_gates

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
        if not isinstance(other, ListAutopilotClusterUpgradeFeatureGatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
