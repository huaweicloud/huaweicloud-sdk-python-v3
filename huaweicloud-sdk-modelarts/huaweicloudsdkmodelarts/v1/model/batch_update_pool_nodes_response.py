# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdatePoolNodesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success_node_names': 'list[str]',
        'fail_node_names': 'list[str]'
    }

    attribute_map = {
        'success_node_names': 'successNodeNames',
        'fail_node_names': 'failNodeNames'
    }

    def __init__(self, success_node_names=None, fail_node_names=None):
        r"""BatchUpdatePoolNodesResponse

        The model defined in huaweicloud sdk

        :param success_node_names: **参数解释**：更新成功的节点名称列表。
        :type success_node_names: list[str]
        :param fail_node_names: **参数解释**：更新失败的节点名称列表。
        :type fail_node_names: list[str]
        """
        
        super().__init__()

        self._success_node_names = None
        self._fail_node_names = None
        self.discriminator = None

        if success_node_names is not None:
            self.success_node_names = success_node_names
        if fail_node_names is not None:
            self.fail_node_names = fail_node_names

    @property
    def success_node_names(self):
        r"""Gets the success_node_names of this BatchUpdatePoolNodesResponse.

        **参数解释**：更新成功的节点名称列表。

        :return: The success_node_names of this BatchUpdatePoolNodesResponse.
        :rtype: list[str]
        """
        return self._success_node_names

    @success_node_names.setter
    def success_node_names(self, success_node_names):
        r"""Sets the success_node_names of this BatchUpdatePoolNodesResponse.

        **参数解释**：更新成功的节点名称列表。

        :param success_node_names: The success_node_names of this BatchUpdatePoolNodesResponse.
        :type success_node_names: list[str]
        """
        self._success_node_names = success_node_names

    @property
    def fail_node_names(self):
        r"""Gets the fail_node_names of this BatchUpdatePoolNodesResponse.

        **参数解释**：更新失败的节点名称列表。

        :return: The fail_node_names of this BatchUpdatePoolNodesResponse.
        :rtype: list[str]
        """
        return self._fail_node_names

    @fail_node_names.setter
    def fail_node_names(self, fail_node_names):
        r"""Sets the fail_node_names of this BatchUpdatePoolNodesResponse.

        **参数解释**：更新失败的节点名称列表。

        :param fail_node_names: The fail_node_names of this BatchUpdatePoolNodesResponse.
        :type fail_node_names: list[str]
        """
        self._fail_node_names = fail_node_names

    def to_dict(self):
        import warnings
        warnings.warn("BatchUpdatePoolNodesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchUpdatePoolNodesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
