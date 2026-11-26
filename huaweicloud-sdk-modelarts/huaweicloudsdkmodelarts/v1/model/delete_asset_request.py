# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAssetRequest:

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
        'force_delete': 'bool'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'workspace_id': 'workspace_id',
        'force_delete': 'force_delete'
    }

    def __init__(self, asset_id=None, workspace_id=None, force_delete=None):
        r"""DeleteAssetRequest

        The model defined in huaweicloud sdk

        :param asset_id: **参数解释**：资产id。 **约束限制**：1-36字符，英文字母，数字，下划线，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_id: str
        :param workspace_id: 工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。
        :type workspace_id: str
        :param force_delete: **参数解释**：数据集资产是否删除OBS桶中的数据，boolean类型，取值true：删除OBS桶中的数据，取值false：仅删除记录不删除OBS桶中的数据。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type force_delete: bool
        """
        
        

        self._asset_id = None
        self._workspace_id = None
        self._force_delete = None
        self.discriminator = None

        self.asset_id = asset_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if force_delete is not None:
            self.force_delete = force_delete

    @property
    def asset_id(self):
        r"""Gets the asset_id of this DeleteAssetRequest.

        **参数解释**：资产id。 **约束限制**：1-36字符，英文字母，数字，下划线，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_id of this DeleteAssetRequest.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this DeleteAssetRequest.

        **参数解释**：资产id。 **约束限制**：1-36字符，英文字母，数字，下划线，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_id: The asset_id of this DeleteAssetRequest.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this DeleteAssetRequest.

        工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。

        :return: The workspace_id of this DeleteAssetRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this DeleteAssetRequest.

        工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。

        :param workspace_id: The workspace_id of this DeleteAssetRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def force_delete(self):
        r"""Gets the force_delete of this DeleteAssetRequest.

        **参数解释**：数据集资产是否删除OBS桶中的数据，boolean类型，取值true：删除OBS桶中的数据，取值false：仅删除记录不删除OBS桶中的数据。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The force_delete of this DeleteAssetRequest.
        :rtype: bool
        """
        return self._force_delete

    @force_delete.setter
    def force_delete(self, force_delete):
        r"""Sets the force_delete of this DeleteAssetRequest.

        **参数解释**：数据集资产是否删除OBS桶中的数据，boolean类型，取值true：删除OBS桶中的数据，取值false：仅删除记录不删除OBS桶中的数据。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param force_delete: The force_delete of this DeleteAssetRequest.
        :type force_delete: bool
        """
        self._force_delete = force_delete

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
        if not isinstance(other, DeleteAssetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
