# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricResponse:

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
        'total': 'int',
        'draft_total': 'int',
        'release_total': 'int'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'total': 'total',
        'draft_total': 'draft_total',
        'release_total': 'release_total'
    }

    def __init__(self, metric_name=None, total=None, draft_total=None, release_total=None):
        r"""MetricResponse

        The model defined in huaweicloud sdk

        :param metric_name: 指标名
        :type metric_name: str
        :param total: 总数
        :type total: int
        :param draft_total: 草稿类型的总数
        :type draft_total: int
        :param release_total: 已发布版本总数
        :type release_total: int
        """
        
        

        self._metric_name = None
        self._total = None
        self._draft_total = None
        self._release_total = None
        self.discriminator = None

        if metric_name is not None:
            self.metric_name = metric_name
        if total is not None:
            self.total = total
        if draft_total is not None:
            self.draft_total = draft_total
        if release_total is not None:
            self.release_total = release_total

    @property
    def metric_name(self):
        r"""Gets the metric_name of this MetricResponse.

        指标名

        :return: The metric_name of this MetricResponse.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this MetricResponse.

        指标名

        :param metric_name: The metric_name of this MetricResponse.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def total(self):
        r"""Gets the total of this MetricResponse.

        总数

        :return: The total of this MetricResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this MetricResponse.

        总数

        :param total: The total of this MetricResponse.
        :type total: int
        """
        self._total = total

    @property
    def draft_total(self):
        r"""Gets the draft_total of this MetricResponse.

        草稿类型的总数

        :return: The draft_total of this MetricResponse.
        :rtype: int
        """
        return self._draft_total

    @draft_total.setter
    def draft_total(self, draft_total):
        r"""Sets the draft_total of this MetricResponse.

        草稿类型的总数

        :param draft_total: The draft_total of this MetricResponse.
        :type draft_total: int
        """
        self._draft_total = draft_total

    @property
    def release_total(self):
        r"""Gets the release_total of this MetricResponse.

        已发布版本总数

        :return: The release_total of this MetricResponse.
        :rtype: int
        """
        return self._release_total

    @release_total.setter
    def release_total(self, release_total):
        r"""Sets the release_total of this MetricResponse.

        已发布版本总数

        :param release_total: The release_total of this MetricResponse.
        :type release_total: int
        """
        self._release_total = release_total

    def to_dict(self):
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
        if not isinstance(other, MetricResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
