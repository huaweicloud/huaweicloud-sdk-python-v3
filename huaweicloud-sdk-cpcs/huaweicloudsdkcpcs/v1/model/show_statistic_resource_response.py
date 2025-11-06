# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatisticResourceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_name': 'str',
        'datapoints': 'list[ShowStatisticResourceResponseBodyDatapoints]',
        'total_count': 'int'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'datapoints': 'datapoints',
        'total_count': 'total_count'
    }

    def __init__(self, metric_name=None, datapoints=None, total_count=None):
        r"""ShowStatisticResourceResponse

        The model defined in huaweicloud sdk

        :param metric_name: 资源名称
        :type metric_name: str
        :param datapoints: 资源分布
        :type datapoints: list[:class:`huaweicloudsdkcpcs.v1.ShowStatisticResourceResponseBodyDatapoints`]
        :param total_count: 总数
        :type total_count: int
        """
        
        super().__init__()

        self._metric_name = None
        self._datapoints = None
        self._total_count = None
        self.discriminator = None

        if metric_name is not None:
            self.metric_name = metric_name
        if datapoints is not None:
            self.datapoints = datapoints
        if total_count is not None:
            self.total_count = total_count

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ShowStatisticResourceResponse.

        资源名称

        :return: The metric_name of this ShowStatisticResourceResponse.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ShowStatisticResourceResponse.

        资源名称

        :param metric_name: The metric_name of this ShowStatisticResourceResponse.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def datapoints(self):
        r"""Gets the datapoints of this ShowStatisticResourceResponse.

        资源分布

        :return: The datapoints of this ShowStatisticResourceResponse.
        :rtype: list[:class:`huaweicloudsdkcpcs.v1.ShowStatisticResourceResponseBodyDatapoints`]
        """
        return self._datapoints

    @datapoints.setter
    def datapoints(self, datapoints):
        r"""Sets the datapoints of this ShowStatisticResourceResponse.

        资源分布

        :param datapoints: The datapoints of this ShowStatisticResourceResponse.
        :type datapoints: list[:class:`huaweicloudsdkcpcs.v1.ShowStatisticResourceResponseBodyDatapoints`]
        """
        self._datapoints = datapoints

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowStatisticResourceResponse.

        总数

        :return: The total_count of this ShowStatisticResourceResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowStatisticResourceResponse.

        总数

        :param total_count: The total_count of this ShowStatisticResourceResponse.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        import warnings
        warnings.warn("ShowStatisticResourceResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowStatisticResourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
