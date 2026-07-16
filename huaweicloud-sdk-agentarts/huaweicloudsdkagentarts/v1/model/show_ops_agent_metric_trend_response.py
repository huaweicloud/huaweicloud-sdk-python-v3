# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsAgentMetricTrendResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'line_list': 'list[FrontLine]'
    }

    attribute_map = {
        'line_list': 'line_list'
    }

    def __init__(self, line_list=None):
        r"""ShowOpsAgentMetricTrendResponse

        The model defined in huaweicloud sdk

        :param line_list: 趋势图数据
        :type line_list: list[:class:`huaweicloudsdkagentarts.v1.FrontLine`]
        """
        
        super().__init__()

        self._line_list = None
        self.discriminator = None

        if line_list is not None:
            self.line_list = line_list

    @property
    def line_list(self):
        r"""Gets the line_list of this ShowOpsAgentMetricTrendResponse.

        趋势图数据

        :return: The line_list of this ShowOpsAgentMetricTrendResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.FrontLine`]
        """
        return self._line_list

    @line_list.setter
    def line_list(self, line_list):
        r"""Sets the line_list of this ShowOpsAgentMetricTrendResponse.

        趋势图数据

        :param line_list: The line_list of this ShowOpsAgentMetricTrendResponse.
        :type line_list: list[:class:`huaweicloudsdkagentarts.v1.FrontLine`]
        """
        self._line_list = line_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowOpsAgentMetricTrendResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowOpsAgentMetricTrendResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
