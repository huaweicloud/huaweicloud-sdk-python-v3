# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDDoSFlowResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flow_bps': 'list[FlowBps]',
        'flow_pps': 'list[FlowPps]'
    }

    attribute_map = {
        'flow_bps': 'flow_bps',
        'flow_pps': 'flow_pps'
    }

    def __init__(self, flow_bps=None, flow_pps=None):
        r"""ListDDoSFlowResponse

        The model defined in huaweicloud sdk

        :param flow_bps: 当请求type&#x3D;bps时必返回
        :type flow_bps: list[:class:`huaweicloudsdkaad.v2.FlowBps`]
        :param flow_pps: 当请求type&#x3D;pps时必返回
        :type flow_pps: list[:class:`huaweicloudsdkaad.v2.FlowPps`]
        """
        
        super(ListDDoSFlowResponse, self).__init__()

        self._flow_bps = None
        self._flow_pps = None
        self.discriminator = None

        if flow_bps is not None:
            self.flow_bps = flow_bps
        if flow_pps is not None:
            self.flow_pps = flow_pps

    @property
    def flow_bps(self):
        r"""Gets the flow_bps of this ListDDoSFlowResponse.

        当请求type=bps时必返回

        :return: The flow_bps of this ListDDoSFlowResponse.
        :rtype: list[:class:`huaweicloudsdkaad.v2.FlowBps`]
        """
        return self._flow_bps

    @flow_bps.setter
    def flow_bps(self, flow_bps):
        r"""Sets the flow_bps of this ListDDoSFlowResponse.

        当请求type=bps时必返回

        :param flow_bps: The flow_bps of this ListDDoSFlowResponse.
        :type flow_bps: list[:class:`huaweicloudsdkaad.v2.FlowBps`]
        """
        self._flow_bps = flow_bps

    @property
    def flow_pps(self):
        r"""Gets the flow_pps of this ListDDoSFlowResponse.

        当请求type=pps时必返回

        :return: The flow_pps of this ListDDoSFlowResponse.
        :rtype: list[:class:`huaweicloudsdkaad.v2.FlowPps`]
        """
        return self._flow_pps

    @flow_pps.setter
    def flow_pps(self, flow_pps):
        r"""Sets the flow_pps of this ListDDoSFlowResponse.

        当请求type=pps时必返回

        :param flow_pps: The flow_pps of this ListDDoSFlowResponse.
        :type flow_pps: list[:class:`huaweicloudsdkaad.v2.FlowPps`]
        """
        self._flow_pps = flow_pps

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListDDoSFlowResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
