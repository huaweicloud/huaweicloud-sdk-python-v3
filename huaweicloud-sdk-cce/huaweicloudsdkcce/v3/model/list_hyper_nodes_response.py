# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHyperNodesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hyper_node_list': 'list[HyperNode]'
    }

    attribute_map = {
        'hyper_node_list': 'hyperNodeList'
    }

    def __init__(self, hyper_node_list=None):
        r"""ListHyperNodesResponse

        The model defined in huaweicloud sdk

        :param hyper_node_list: 
        :type hyper_node_list: list[:class:`huaweicloudsdkcce.v3.HyperNode`]
        """
        
        super().__init__()

        self._hyper_node_list = None
        self.discriminator = None

        if hyper_node_list is not None:
            self.hyper_node_list = hyper_node_list

    @property
    def hyper_node_list(self):
        r"""Gets the hyper_node_list of this ListHyperNodesResponse.

        :return: The hyper_node_list of this ListHyperNodesResponse.
        :rtype: list[:class:`huaweicloudsdkcce.v3.HyperNode`]
        """
        return self._hyper_node_list

    @hyper_node_list.setter
    def hyper_node_list(self, hyper_node_list):
        r"""Sets the hyper_node_list of this ListHyperNodesResponse.

        :param hyper_node_list: The hyper_node_list of this ListHyperNodesResponse.
        :type hyper_node_list: list[:class:`huaweicloudsdkcce.v3.HyperNode`]
        """
        self._hyper_node_list = hyper_node_list

    def to_dict(self):
        import warnings
        warnings.warn("ListHyperNodesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListHyperNodesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
