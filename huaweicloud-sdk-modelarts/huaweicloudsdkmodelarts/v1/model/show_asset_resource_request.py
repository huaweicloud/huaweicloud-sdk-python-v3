# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAssetResourceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'workspace_id': 'str',
        'resource_name': 'str',
        'check_locale': 'bool'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'workspace_id': 'workspace_id',
        'resource_name': 'resource_name',
        'check_locale': 'check_locale'
    }

    def __init__(self, asset_id=None, workspace_id=None, resource_name=None, check_locale=None):
        r"""ShowAssetResourceRequest

        The model defined in huaweicloud sdk

        :param asset_id: **参数解释**：资产id。 **约束限制**：1-36字符，英文字母，数字，下划线，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_id: str
        :param workspace_id: 工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。
        :type workspace_id: str
        :param resource_name: **参数解释**：静态资源名称。 **约束限制**：当前只支持readme文件查询（docs/RELEASE.md）。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type resource_name: str
        :param check_locale: **参数解释**：查询资源时是否拼接区域信息。如果为false，则直接查询docs/RELEASE.md文件；如果为true，则会优先匹配带有区域信息的文件（请求头传递x-language，如英文查询docs/RELEASE_en-US.md）。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type check_locale: bool
        """
        
        

        self._asset_id = None
        self._workspace_id = None
        self._resource_name = None
        self._check_locale = None
        self.discriminator = None

        self.asset_id = asset_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        self.resource_name = resource_name
        if check_locale is not None:
            self.check_locale = check_locale

    @property
    def asset_id(self):
        r"""Gets the asset_id of this ShowAssetResourceRequest.

        **参数解释**：资产id。 **约束限制**：1-36字符，英文字母，数字，下划线，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_id of this ShowAssetResourceRequest.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this ShowAssetResourceRequest.

        **参数解释**：资产id。 **约束限制**：1-36字符，英文字母，数字，下划线，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_id: The asset_id of this ShowAssetResourceRequest.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowAssetResourceRequest.

        工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。

        :return: The workspace_id of this ShowAssetResourceRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowAssetResourceRequest.

        工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。

        :param workspace_id: The workspace_id of this ShowAssetResourceRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ShowAssetResourceRequest.

        **参数解释**：静态资源名称。 **约束限制**：当前只支持readme文件查询（docs/RELEASE.md）。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The resource_name of this ShowAssetResourceRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ShowAssetResourceRequest.

        **参数解释**：静态资源名称。 **约束限制**：当前只支持readme文件查询（docs/RELEASE.md）。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param resource_name: The resource_name of this ShowAssetResourceRequest.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def check_locale(self):
        r"""Gets the check_locale of this ShowAssetResourceRequest.

        **参数解释**：查询资源时是否拼接区域信息。如果为false，则直接查询docs/RELEASE.md文件；如果为true，则会优先匹配带有区域信息的文件（请求头传递x-language，如英文查询docs/RELEASE_en-US.md）。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The check_locale of this ShowAssetResourceRequest.
        :rtype: bool
        """
        return self._check_locale

    @check_locale.setter
    def check_locale(self, check_locale):
        r"""Sets the check_locale of this ShowAssetResourceRequest.

        **参数解释**：查询资源时是否拼接区域信息。如果为false，则直接查询docs/RELEASE.md文件；如果为true，则会优先匹配带有区域信息的文件（请求头传递x-language，如英文查询docs/RELEASE_en-US.md）。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param check_locale: The check_locale of this ShowAssetResourceRequest.
        :type check_locale: bool
        """
        self._check_locale = check_locale

    def to_dict(self):
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
        if not isinstance(other, ShowAssetResourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
