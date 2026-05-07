# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUpgradePathsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_infos': 'list[VersionInfosResult]',
        'version_edges': 'list[UpgradePathsResult]'
    }

    attribute_map = {
        'version_infos': 'version_infos',
        'version_edges': 'version_edges'
    }

    def __init__(self, version_infos=None, version_edges=None):
        r"""ListUpgradePathsResponse

        The model defined in huaweicloud sdk

        :param version_infos: **参数解释**: 版本信息详情 
        :type version_infos: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.VersionInfosResult`]
        :param version_edges: **参数解释**: 支持的升级路径列表 
        :type version_edges: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.UpgradePathsResult`]
        """
        
        super().__init__()

        self._version_infos = None
        self._version_edges = None
        self.discriminator = None

        if version_infos is not None:
            self.version_infos = version_infos
        if version_edges is not None:
            self.version_edges = version_edges

    @property
    def version_infos(self):
        r"""Gets the version_infos of this ListUpgradePathsResponse.

        **参数解释**: 版本信息详情 

        :return: The version_infos of this ListUpgradePathsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.VersionInfosResult`]
        """
        return self._version_infos

    @version_infos.setter
    def version_infos(self, version_infos):
        r"""Sets the version_infos of this ListUpgradePathsResponse.

        **参数解释**: 版本信息详情 

        :param version_infos: The version_infos of this ListUpgradePathsResponse.
        :type version_infos: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.VersionInfosResult`]
        """
        self._version_infos = version_infos

    @property
    def version_edges(self):
        r"""Gets the version_edges of this ListUpgradePathsResponse.

        **参数解释**: 支持的升级路径列表 

        :return: The version_edges of this ListUpgradePathsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.UpgradePathsResult`]
        """
        return self._version_edges

    @version_edges.setter
    def version_edges(self, version_edges):
        r"""Sets the version_edges of this ListUpgradePathsResponse.

        **参数解释**: 支持的升级路径列表 

        :param version_edges: The version_edges of this ListUpgradePathsResponse.
        :type version_edges: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.UpgradePathsResult`]
        """
        self._version_edges = version_edges

    def to_dict(self):
        import warnings
        warnings.warn("ListUpgradePathsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListUpgradePathsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
