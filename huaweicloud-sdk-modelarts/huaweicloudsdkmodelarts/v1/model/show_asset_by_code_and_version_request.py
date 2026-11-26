# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAssetByCodeAndVersionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_code': 'str',
        'asset_version': 'str',
        'workspace_id': 'str',
        'asset_type': 'str'
    }

    attribute_map = {
        'asset_code': 'asset_code',
        'asset_version': 'asset_version',
        'workspace_id': 'workspace_id',
        'asset_type': 'asset_type'
    }

    def __init__(self, asset_code=None, asset_version=None, workspace_id=None, asset_type=None):
        r"""ShowAssetByCodeAndVersionRequest

        The model defined in huaweicloud sdk

        :param asset_code: **参数解释**：资产code。 **约束限制**：1-60字符，英文字母，数字，中划线，下划线，点。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_code: str
        :param asset_version: **参数解释**：资产version。 **约束限制**：数字或为格式x.y.z， x,y,z均为数字。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_version: str
        :param workspace_id: 工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。
        :type workspace_id: str
        :param asset_type: **参数解释**:资产类型。 **约束限制**:不涉及。 **取值范围**:不涉及。 **默认取值**:MODEL。
        :type asset_type: str
        """
        
        

        self._asset_code = None
        self._asset_version = None
        self._workspace_id = None
        self._asset_type = None
        self.discriminator = None

        self.asset_code = asset_code
        self.asset_version = asset_version
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if asset_type is not None:
            self.asset_type = asset_type

    @property
    def asset_code(self):
        r"""Gets the asset_code of this ShowAssetByCodeAndVersionRequest.

        **参数解释**：资产code。 **约束限制**：1-60字符，英文字母，数字，中划线，下划线，点。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_code of this ShowAssetByCodeAndVersionRequest.
        :rtype: str
        """
        return self._asset_code

    @asset_code.setter
    def asset_code(self, asset_code):
        r"""Sets the asset_code of this ShowAssetByCodeAndVersionRequest.

        **参数解释**：资产code。 **约束限制**：1-60字符，英文字母，数字，中划线，下划线，点。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_code: The asset_code of this ShowAssetByCodeAndVersionRequest.
        :type asset_code: str
        """
        self._asset_code = asset_code

    @property
    def asset_version(self):
        r"""Gets the asset_version of this ShowAssetByCodeAndVersionRequest.

        **参数解释**：资产version。 **约束限制**：数字或为格式x.y.z， x,y,z均为数字。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_version of this ShowAssetByCodeAndVersionRequest.
        :rtype: str
        """
        return self._asset_version

    @asset_version.setter
    def asset_version(self, asset_version):
        r"""Sets the asset_version of this ShowAssetByCodeAndVersionRequest.

        **参数解释**：资产version。 **约束限制**：数字或为格式x.y.z， x,y,z均为数字。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_version: The asset_version of this ShowAssetByCodeAndVersionRequest.
        :type asset_version: str
        """
        self._asset_version = asset_version

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowAssetByCodeAndVersionRequest.

        工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。

        :return: The workspace_id of this ShowAssetByCodeAndVersionRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowAssetByCodeAndVersionRequest.

        工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。

        :param workspace_id: The workspace_id of this ShowAssetByCodeAndVersionRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def asset_type(self):
        r"""Gets the asset_type of this ShowAssetByCodeAndVersionRequest.

        **参数解释**:资产类型。 **约束限制**:不涉及。 **取值范围**:不涉及。 **默认取值**:MODEL。

        :return: The asset_type of this ShowAssetByCodeAndVersionRequest.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this ShowAssetByCodeAndVersionRequest.

        **参数解释**:资产类型。 **约束限制**:不涉及。 **取值范围**:不涉及。 **默认取值**:MODEL。

        :param asset_type: The asset_type of this ShowAssetByCodeAndVersionRequest.
        :type asset_type: str
        """
        self._asset_type = asset_type

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
        if not isinstance(other, ShowAssetByCodeAndVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
