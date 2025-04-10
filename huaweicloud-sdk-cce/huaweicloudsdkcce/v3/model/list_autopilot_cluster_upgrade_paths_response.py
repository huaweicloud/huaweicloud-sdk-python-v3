# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAutopilotClusterUpgradePathsResponse(SdkResponse):

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
        'upgrade_paths': 'list[UpgradePath]'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'upgrade_paths': 'upgradePaths'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, upgrade_paths=None):
        r"""ListAutopilotClusterUpgradePathsResponse

        The model defined in huaweicloud sdk

        :param api_version: API版本
        :type api_version: str
        :param kind: 资源类型
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcce.v3.Metadata`
        :param upgrade_paths: 升级路径集合
        :type upgrade_paths: list[:class:`huaweicloudsdkcce.v3.UpgradePath`]
        """
        
        super(ListAutopilotClusterUpgradePathsResponse, self).__init__()

        self._api_version = None
        self._kind = None
        self._metadata = None
        self._upgrade_paths = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if upgrade_paths is not None:
            self.upgrade_paths = upgrade_paths

    @property
    def api_version(self):
        r"""Gets the api_version of this ListAutopilotClusterUpgradePathsResponse.

        API版本

        :return: The api_version of this ListAutopilotClusterUpgradePathsResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this ListAutopilotClusterUpgradePathsResponse.

        API版本

        :param api_version: The api_version of this ListAutopilotClusterUpgradePathsResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this ListAutopilotClusterUpgradePathsResponse.

        资源类型

        :return: The kind of this ListAutopilotClusterUpgradePathsResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this ListAutopilotClusterUpgradePathsResponse.

        资源类型

        :param kind: The kind of this ListAutopilotClusterUpgradePathsResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        r"""Gets the metadata of this ListAutopilotClusterUpgradePathsResponse.

        :return: The metadata of this ListAutopilotClusterUpgradePathsResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.Metadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ListAutopilotClusterUpgradePathsResponse.

        :param metadata: The metadata of this ListAutopilotClusterUpgradePathsResponse.
        :type metadata: :class:`huaweicloudsdkcce.v3.Metadata`
        """
        self._metadata = metadata

    @property
    def upgrade_paths(self):
        r"""Gets the upgrade_paths of this ListAutopilotClusterUpgradePathsResponse.

        升级路径集合

        :return: The upgrade_paths of this ListAutopilotClusterUpgradePathsResponse.
        :rtype: list[:class:`huaweicloudsdkcce.v3.UpgradePath`]
        """
        return self._upgrade_paths

    @upgrade_paths.setter
    def upgrade_paths(self, upgrade_paths):
        r"""Sets the upgrade_paths of this ListAutopilotClusterUpgradePathsResponse.

        升级路径集合

        :param upgrade_paths: The upgrade_paths of this ListAutopilotClusterUpgradePathsResponse.
        :type upgrade_paths: list[:class:`huaweicloudsdkcce.v3.UpgradePath`]
        """
        self._upgrade_paths = upgrade_paths

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
        if not isinstance(other, ListAutopilotClusterUpgradePathsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
