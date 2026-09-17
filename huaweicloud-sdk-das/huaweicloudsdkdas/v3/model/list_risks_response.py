# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRisksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_code': 'str',
        'display_metric_codes': 'list[str]',
        'metric_names': 'list[str]',
        'units': 'list[str]',
        'items': 'list[RiskInfo]'
    }

    attribute_map = {
        'metric_code': 'metric_code',
        'display_metric_codes': 'display_metric_codes',
        'metric_names': 'metric_names',
        'units': 'units',
        'items': 'items'
    }

    def __init__(self, metric_code=None, display_metric_codes=None, metric_names=None, units=None, items=None):
        r"""ListRisksResponse

        The model defined in huaweicloud sdk

        :param metric_code: 指标名
        :type metric_code: str
        :param display_metric_codes: 指标展示名称
        :type display_metric_codes: list[str]
        :param metric_names: 指标名称
        :type metric_names: list[str]
        :param units: 单位
        :type units: list[str]
        :param items: 风险实例列表
        :type items: list[:class:`huaweicloudsdkdas.v3.RiskInfo`]
        """
        
        super().__init__()

        self._metric_code = None
        self._display_metric_codes = None
        self._metric_names = None
        self._units = None
        self._items = None
        self.discriminator = None

        if metric_code is not None:
            self.metric_code = metric_code
        if display_metric_codes is not None:
            self.display_metric_codes = display_metric_codes
        if metric_names is not None:
            self.metric_names = metric_names
        if units is not None:
            self.units = units
        if items is not None:
            self.items = items

    @property
    def metric_code(self):
        r"""Gets the metric_code of this ListRisksResponse.

        指标名

        :return: The metric_code of this ListRisksResponse.
        :rtype: str
        """
        return self._metric_code

    @metric_code.setter
    def metric_code(self, metric_code):
        r"""Sets the metric_code of this ListRisksResponse.

        指标名

        :param metric_code: The metric_code of this ListRisksResponse.
        :type metric_code: str
        """
        self._metric_code = metric_code

    @property
    def display_metric_codes(self):
        r"""Gets the display_metric_codes of this ListRisksResponse.

        指标展示名称

        :return: The display_metric_codes of this ListRisksResponse.
        :rtype: list[str]
        """
        return self._display_metric_codes

    @display_metric_codes.setter
    def display_metric_codes(self, display_metric_codes):
        r"""Sets the display_metric_codes of this ListRisksResponse.

        指标展示名称

        :param display_metric_codes: The display_metric_codes of this ListRisksResponse.
        :type display_metric_codes: list[str]
        """
        self._display_metric_codes = display_metric_codes

    @property
    def metric_names(self):
        r"""Gets the metric_names of this ListRisksResponse.

        指标名称

        :return: The metric_names of this ListRisksResponse.
        :rtype: list[str]
        """
        return self._metric_names

    @metric_names.setter
    def metric_names(self, metric_names):
        r"""Sets the metric_names of this ListRisksResponse.

        指标名称

        :param metric_names: The metric_names of this ListRisksResponse.
        :type metric_names: list[str]
        """
        self._metric_names = metric_names

    @property
    def units(self):
        r"""Gets the units of this ListRisksResponse.

        单位

        :return: The units of this ListRisksResponse.
        :rtype: list[str]
        """
        return self._units

    @units.setter
    def units(self, units):
        r"""Sets the units of this ListRisksResponse.

        单位

        :param units: The units of this ListRisksResponse.
        :type units: list[str]
        """
        self._units = units

    @property
    def items(self):
        r"""Gets the items of this ListRisksResponse.

        风险实例列表

        :return: The items of this ListRisksResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.RiskInfo`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListRisksResponse.

        风险实例列表

        :param items: The items of this ListRisksResponse.
        :type items: list[:class:`huaweicloudsdkdas.v3.RiskInfo`]
        """
        self._items = items

    def to_dict(self):
        import warnings
        warnings.warn("ListRisksResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListRisksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
