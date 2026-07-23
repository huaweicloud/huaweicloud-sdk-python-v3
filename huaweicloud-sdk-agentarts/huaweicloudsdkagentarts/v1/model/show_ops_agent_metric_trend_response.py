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
        'line_list': 'list[FrontLine]',
        'step': 'str'
    }

    attribute_map = {
        'line_list': 'line_list',
        'step': 'step'
    }

    def __init__(self, line_list=None, step=None):
        r"""ShowOpsAgentMetricTrendResponse

        The model defined in huaweicloud sdk

        :param line_list: 趋势图数据
        :type line_list: list[:class:`huaweicloudsdkagentarts.v1.FrontLine`]
        :param step: 步长 
        :type step: str
        """
        
        super().__init__()

        self._line_list = None
        self._step = None
        self.discriminator = None

        if line_list is not None:
            self.line_list = line_list
        if step is not None:
            self.step = step

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

    @property
    def step(self):
        r"""Gets the step of this ShowOpsAgentMetricTrendResponse.

        步长 

        :return: The step of this ShowOpsAgentMetricTrendResponse.
        :rtype: str
        """
        return self._step

    @step.setter
    def step(self, step):
        r"""Sets the step of this ShowOpsAgentMetricTrendResponse.

        步长 

        :param step: The step of this ShowOpsAgentMetricTrendResponse.
        :type step: str
        """
        self._step = step

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
