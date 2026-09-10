# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteWorkspacesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_ids': 'list[str]'
    }

    attribute_map = {
        'workspace_ids': 'workspace_ids'
    }

    def __init__(self, workspace_ids=None):
        r"""BatchDeleteWorkspacesRequestBody

        The model defined in huaweicloud sdk

        :param workspace_ids: 待删除的工作空间ID列表，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace_ids: list[str]
        """
        
        

        self._workspace_ids = None
        self.discriminator = None

        self.workspace_ids = workspace_ids

    @property
    def workspace_ids(self):
        r"""Gets the workspace_ids of this BatchDeleteWorkspacesRequestBody.

        待删除的工作空间ID列表，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace_ids of this BatchDeleteWorkspacesRequestBody.
        :rtype: list[str]
        """
        return self._workspace_ids

    @workspace_ids.setter
    def workspace_ids(self, workspace_ids):
        r"""Sets the workspace_ids of this BatchDeleteWorkspacesRequestBody.

        待删除的工作空间ID列表，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace_ids: The workspace_ids of this BatchDeleteWorkspacesRequestBody.
        :type workspace_ids: list[str]
        """
        self._workspace_ids = workspace_ids

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
        if not isinstance(other, BatchDeleteWorkspacesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
