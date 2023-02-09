# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlowLogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flow_logs': 'list[FlowLogResp]'
    }

    attribute_map = {
        'flow_logs': 'flow_logs'
    }

    def __init__(self, flow_logs=None):
        """ListFlowLogsResponse

        The model defined in huaweicloud sdk

        :param flow_logs: flow_log对象列表
        :type flow_logs: list[:class:`huaweicloudsdkvpc.v2.FlowLogResp`]
        """
        
        super(ListFlowLogsResponse, self).__init__()

        self._flow_logs = None
        self.discriminator = None

        if flow_logs is not None:
            self.flow_logs = flow_logs

    @property
    def flow_logs(self):
        """Gets the flow_logs of this ListFlowLogsResponse.

        flow_log对象列表

        :return: The flow_logs of this ListFlowLogsResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.FlowLogResp`]
        """
        return self._flow_logs

    @flow_logs.setter
    def flow_logs(self, flow_logs):
        """Sets the flow_logs of this ListFlowLogsResponse.

        flow_log对象列表

        :param flow_logs: The flow_logs of this ListFlowLogsResponse.
        :type flow_logs: list[:class:`huaweicloudsdkvpc.v2.FlowLogResp`]
        """
        self._flow_logs = flow_logs

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
        if not isinstance(other, ListFlowLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
