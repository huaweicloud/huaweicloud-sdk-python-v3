# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgentDaemonsetClusterNodesLabelResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_list': 'list[NodeLabelInfoResponse]',
        'total_num': 'int'
    }

    attribute_map = {
        'data_list': 'data_list',
        'total_num': 'total_num'
    }

    def __init__(self, data_list=None, total_num=None):
        r"""ListAgentDaemonsetClusterNodesLabelResponse

        The model defined in huaweicloud sdk

        :param data_list: **参数解释**: 数据列表 **取值范围**: 取值1-100 
        :type data_list: list[:class:`huaweicloudsdkhss.v5.NodeLabelInfoResponse`]
        :param total_num: **参数解释**: 集群NodeLabels总数 **取值范围**: 最小值0，最大值2147483647 
        :type total_num: int
        """
        
        super().__init__()

        self._data_list = None
        self._total_num = None
        self.discriminator = None

        if data_list is not None:
            self.data_list = data_list
        if total_num is not None:
            self.total_num = total_num

    @property
    def data_list(self):
        r"""Gets the data_list of this ListAgentDaemonsetClusterNodesLabelResponse.

        **参数解释**: 数据列表 **取值范围**: 取值1-100 

        :return: The data_list of this ListAgentDaemonsetClusterNodesLabelResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.NodeLabelInfoResponse`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ListAgentDaemonsetClusterNodesLabelResponse.

        **参数解释**: 数据列表 **取值范围**: 取值1-100 

        :param data_list: The data_list of this ListAgentDaemonsetClusterNodesLabelResponse.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.NodeLabelInfoResponse`]
        """
        self._data_list = data_list

    @property
    def total_num(self):
        r"""Gets the total_num of this ListAgentDaemonsetClusterNodesLabelResponse.

        **参数解释**: 集群NodeLabels总数 **取值范围**: 最小值0，最大值2147483647 

        :return: The total_num of this ListAgentDaemonsetClusterNodesLabelResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListAgentDaemonsetClusterNodesLabelResponse.

        **参数解释**: 集群NodeLabels总数 **取值范围**: 最小值0，最大值2147483647 

        :param total_num: The total_num of this ListAgentDaemonsetClusterNodesLabelResponse.
        :type total_num: int
        """
        self._total_num = total_num

    def to_dict(self):
        import warnings
        warnings.warn("ListAgentDaemonsetClusterNodesLabelResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAgentDaemonsetClusterNodesLabelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
