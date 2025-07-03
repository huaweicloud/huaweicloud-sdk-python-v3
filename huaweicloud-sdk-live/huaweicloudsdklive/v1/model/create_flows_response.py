# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFlowsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flow': 'FlowDetailRespBody'
    }

    attribute_map = {
        'flow': 'flow'
    }

    def __init__(self, flow=None):
        r"""CreateFlowsResponse

        The model defined in huaweicloud sdk

        :param flow: 
        :type flow: :class:`huaweicloudsdklive.v1.FlowDetailRespBody`
        """
        
        super(CreateFlowsResponse, self).__init__()

        self._flow = None
        self.discriminator = None

        if flow is not None:
            self.flow = flow

    @property
    def flow(self):
        r"""Gets the flow of this CreateFlowsResponse.

        :return: The flow of this CreateFlowsResponse.
        :rtype: :class:`huaweicloudsdklive.v1.FlowDetailRespBody`
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        r"""Sets the flow of this CreateFlowsResponse.

        :param flow: The flow of this CreateFlowsResponse.
        :type flow: :class:`huaweicloudsdklive.v1.FlowDetailRespBody`
        """
        self._flow = flow

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
        if not isinstance(other, CreateFlowsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
