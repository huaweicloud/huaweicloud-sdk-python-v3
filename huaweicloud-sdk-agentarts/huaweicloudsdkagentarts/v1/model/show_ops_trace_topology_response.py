# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsTraceTopologyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topology_root_span_name': 'str',
        'topology_root_span_id': 'int',
        'topology_span_list': 'list[TraceTopologyInfo]'
    }

    attribute_map = {
        'topology_root_span_name': 'topology_root_span_name',
        'topology_root_span_id': 'topology_root_span_id',
        'topology_span_list': 'topology_span_list'
    }

    def __init__(self, topology_root_span_name=None, topology_root_span_id=None, topology_span_list=None):
        r"""ShowOpsTraceTopologyResponse

        The model defined in huaweicloud sdk

        :param topology_root_span_name: 拓扑根节点名称
        :type topology_root_span_name: str
        :param topology_root_span_id: 拓扑根节点id
        :type topology_root_span_id: int
        :param topology_span_list: span列表
        :type topology_span_list: list[:class:`huaweicloudsdkagentarts.v1.TraceTopologyInfo`]
        """
        
        super().__init__()

        self._topology_root_span_name = None
        self._topology_root_span_id = None
        self._topology_span_list = None
        self.discriminator = None

        if topology_root_span_name is not None:
            self.topology_root_span_name = topology_root_span_name
        if topology_root_span_id is not None:
            self.topology_root_span_id = topology_root_span_id
        if topology_span_list is not None:
            self.topology_span_list = topology_span_list

    @property
    def topology_root_span_name(self):
        r"""Gets the topology_root_span_name of this ShowOpsTraceTopologyResponse.

        拓扑根节点名称

        :return: The topology_root_span_name of this ShowOpsTraceTopologyResponse.
        :rtype: str
        """
        return self._topology_root_span_name

    @topology_root_span_name.setter
    def topology_root_span_name(self, topology_root_span_name):
        r"""Sets the topology_root_span_name of this ShowOpsTraceTopologyResponse.

        拓扑根节点名称

        :param topology_root_span_name: The topology_root_span_name of this ShowOpsTraceTopologyResponse.
        :type topology_root_span_name: str
        """
        self._topology_root_span_name = topology_root_span_name

    @property
    def topology_root_span_id(self):
        r"""Gets the topology_root_span_id of this ShowOpsTraceTopologyResponse.

        拓扑根节点id

        :return: The topology_root_span_id of this ShowOpsTraceTopologyResponse.
        :rtype: int
        """
        return self._topology_root_span_id

    @topology_root_span_id.setter
    def topology_root_span_id(self, topology_root_span_id):
        r"""Sets the topology_root_span_id of this ShowOpsTraceTopologyResponse.

        拓扑根节点id

        :param topology_root_span_id: The topology_root_span_id of this ShowOpsTraceTopologyResponse.
        :type topology_root_span_id: int
        """
        self._topology_root_span_id = topology_root_span_id

    @property
    def topology_span_list(self):
        r"""Gets the topology_span_list of this ShowOpsTraceTopologyResponse.

        span列表

        :return: The topology_span_list of this ShowOpsTraceTopologyResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.TraceTopologyInfo`]
        """
        return self._topology_span_list

    @topology_span_list.setter
    def topology_span_list(self, topology_span_list):
        r"""Sets the topology_span_list of this ShowOpsTraceTopologyResponse.

        span列表

        :param topology_span_list: The topology_span_list of this ShowOpsTraceTopologyResponse.
        :type topology_span_list: list[:class:`huaweicloudsdkagentarts.v1.TraceTopologyInfo`]
        """
        self._topology_span_list = topology_span_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowOpsTraceTopologyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowOpsTraceTopologyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
