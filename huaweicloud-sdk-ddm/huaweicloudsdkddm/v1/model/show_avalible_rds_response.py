# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAvalibleRdsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_data_nodes': 'list[TargetDn4Restore]'
    }

    attribute_map = {
        'target_data_nodes': 'target_data_nodes'
    }

    def __init__(self, target_data_nodes=None):
        r"""ShowAvalibleRdsResponse

        The model defined in huaweicloud sdk

        :param target_data_nodes: 可用目标DN。
        :type target_data_nodes: list[:class:`huaweicloudsdkddm.v1.TargetDn4Restore`]
        """
        
        super().__init__()

        self._target_data_nodes = None
        self.discriminator = None

        if target_data_nodes is not None:
            self.target_data_nodes = target_data_nodes

    @property
    def target_data_nodes(self):
        r"""Gets the target_data_nodes of this ShowAvalibleRdsResponse.

        可用目标DN。

        :return: The target_data_nodes of this ShowAvalibleRdsResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.TargetDn4Restore`]
        """
        return self._target_data_nodes

    @target_data_nodes.setter
    def target_data_nodes(self, target_data_nodes):
        r"""Sets the target_data_nodes of this ShowAvalibleRdsResponse.

        可用目标DN。

        :param target_data_nodes: The target_data_nodes of this ShowAvalibleRdsResponse.
        :type target_data_nodes: list[:class:`huaweicloudsdkddm.v1.TargetDn4Restore`]
        """
        self._target_data_nodes = target_data_nodes

    def to_dict(self):
        import warnings
        warnings.warn("ShowAvalibleRdsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowAvalibleRdsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
