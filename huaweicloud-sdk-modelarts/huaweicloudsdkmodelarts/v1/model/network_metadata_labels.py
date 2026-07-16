# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkMetadataLabels:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os_modelarts_name': 'str',
        'os_modelarts_workspace_id': 'str'
    }

    attribute_map = {
        'os_modelarts_name': 'os.modelarts/name',
        'os_modelarts_workspace_id': 'os.modelarts/workspace.id'
    }

    def __init__(self, os_modelarts_name=None, os_modelarts_workspace_id=None):
        r"""NetworkMetadataLabels

        The model defined in huaweicloud sdk

        :param os_modelarts_name: **参数解释**：资源池的显示名称。 **取值范围**：只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度为4-32。
        :type os_modelarts_name: str
        :param os_modelarts_workspace_id: **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc) **取值范围**：不涉及。
        :type os_modelarts_workspace_id: str
        """
        
        

        self._os_modelarts_name = None
        self._os_modelarts_workspace_id = None
        self.discriminator = None

        self.os_modelarts_name = os_modelarts_name
        if os_modelarts_workspace_id is not None:
            self.os_modelarts_workspace_id = os_modelarts_workspace_id

    @property
    def os_modelarts_name(self):
        r"""Gets the os_modelarts_name of this NetworkMetadataLabels.

        **参数解释**：资源池的显示名称。 **取值范围**：只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度为4-32。

        :return: The os_modelarts_name of this NetworkMetadataLabels.
        :rtype: str
        """
        return self._os_modelarts_name

    @os_modelarts_name.setter
    def os_modelarts_name(self, os_modelarts_name):
        r"""Sets the os_modelarts_name of this NetworkMetadataLabels.

        **参数解释**：资源池的显示名称。 **取值范围**：只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度为4-32。

        :param os_modelarts_name: The os_modelarts_name of this NetworkMetadataLabels.
        :type os_modelarts_name: str
        """
        self._os_modelarts_name = os_modelarts_name

    @property
    def os_modelarts_workspace_id(self):
        r"""Gets the os_modelarts_workspace_id of this NetworkMetadataLabels.

        **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc) **取值范围**：不涉及。

        :return: The os_modelarts_workspace_id of this NetworkMetadataLabels.
        :rtype: str
        """
        return self._os_modelarts_workspace_id

    @os_modelarts_workspace_id.setter
    def os_modelarts_workspace_id(self, os_modelarts_workspace_id):
        r"""Sets the os_modelarts_workspace_id of this NetworkMetadataLabels.

        **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc) **取值范围**：不涉及。

        :param os_modelarts_workspace_id: The os_modelarts_workspace_id of this NetworkMetadataLabels.
        :type os_modelarts_workspace_id: str
        """
        self._os_modelarts_workspace_id = os_modelarts_workspace_id

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
        if not isinstance(other, NetworkMetadataLabels):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
