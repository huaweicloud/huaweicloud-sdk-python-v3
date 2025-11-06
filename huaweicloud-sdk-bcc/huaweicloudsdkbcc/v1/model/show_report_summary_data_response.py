# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReportSummaryDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_item_name': 'str',
        'data_length': 'int',
        'dimension_name': 'str',
        'dimension_data': 'list[str]',
        'value_name': 'list[str]',
        'value_data': 'list[list[float]]'
    }

    attribute_map = {
        'data_item_name': 'data_item_name',
        'data_length': 'data_length',
        'dimension_name': 'dimension_name',
        'dimension_data': 'dimension_data',
        'value_name': 'value_name',
        'value_data': 'value_data'
    }

    def __init__(self, data_item_name=None, data_length=None, dimension_name=None, dimension_data=None, value_name=None, value_data=None):
        r"""ShowReportSummaryDataResponse

        The model defined in huaweicloud sdk

        :param data_item_name: 数据项名称，例如task-status-pie
        :type data_item_name: str
        :param data_length: 数据点个数，例如10
        :type data_length: int
        :param dimension_name: 数据维度名称，例如区域、日期、任务类型、资源类型
        :type dimension_name: str
        :param dimension_data: 数据维度取值，长度等于data_length，例如[\&quot;success\&quot;,\&quot;failed\&quot;,\&quot;skipped\&quot;]，[\&quot;202401\&quot;,\&quot;202402\&quot;,\&quot;202403&#39;]
        :type dimension_data: list[str]
        :param value_name: 数据取值名称，例如[任务数量、任务成功率，资源数量、资源保护率、资源合规率
        :type value_name: list[str]
        :param value_data: 数据取值，和value_name相对应，可以是多组数据，例如[[100,0.98,0.97],[99,0.98.0.99]]
        :type value_data: list[list[float]]
        """
        
        super().__init__()

        self._data_item_name = None
        self._data_length = None
        self._dimension_name = None
        self._dimension_data = None
        self._value_name = None
        self._value_data = None
        self.discriminator = None

        if data_item_name is not None:
            self.data_item_name = data_item_name
        if data_length is not None:
            self.data_length = data_length
        if dimension_name is not None:
            self.dimension_name = dimension_name
        if dimension_data is not None:
            self.dimension_data = dimension_data
        if value_name is not None:
            self.value_name = value_name
        if value_data is not None:
            self.value_data = value_data

    @property
    def data_item_name(self):
        r"""Gets the data_item_name of this ShowReportSummaryDataResponse.

        数据项名称，例如task-status-pie

        :return: The data_item_name of this ShowReportSummaryDataResponse.
        :rtype: str
        """
        return self._data_item_name

    @data_item_name.setter
    def data_item_name(self, data_item_name):
        r"""Sets the data_item_name of this ShowReportSummaryDataResponse.

        数据项名称，例如task-status-pie

        :param data_item_name: The data_item_name of this ShowReportSummaryDataResponse.
        :type data_item_name: str
        """
        self._data_item_name = data_item_name

    @property
    def data_length(self):
        r"""Gets the data_length of this ShowReportSummaryDataResponse.

        数据点个数，例如10

        :return: The data_length of this ShowReportSummaryDataResponse.
        :rtype: int
        """
        return self._data_length

    @data_length.setter
    def data_length(self, data_length):
        r"""Sets the data_length of this ShowReportSummaryDataResponse.

        数据点个数，例如10

        :param data_length: The data_length of this ShowReportSummaryDataResponse.
        :type data_length: int
        """
        self._data_length = data_length

    @property
    def dimension_name(self):
        r"""Gets the dimension_name of this ShowReportSummaryDataResponse.

        数据维度名称，例如区域、日期、任务类型、资源类型

        :return: The dimension_name of this ShowReportSummaryDataResponse.
        :rtype: str
        """
        return self._dimension_name

    @dimension_name.setter
    def dimension_name(self, dimension_name):
        r"""Sets the dimension_name of this ShowReportSummaryDataResponse.

        数据维度名称，例如区域、日期、任务类型、资源类型

        :param dimension_name: The dimension_name of this ShowReportSummaryDataResponse.
        :type dimension_name: str
        """
        self._dimension_name = dimension_name

    @property
    def dimension_data(self):
        r"""Gets the dimension_data of this ShowReportSummaryDataResponse.

        数据维度取值，长度等于data_length，例如[\"success\",\"failed\",\"skipped\"]，[\"202401\",\"202402\",\"202403']

        :return: The dimension_data of this ShowReportSummaryDataResponse.
        :rtype: list[str]
        """
        return self._dimension_data

    @dimension_data.setter
    def dimension_data(self, dimension_data):
        r"""Sets the dimension_data of this ShowReportSummaryDataResponse.

        数据维度取值，长度等于data_length，例如[\"success\",\"failed\",\"skipped\"]，[\"202401\",\"202402\",\"202403']

        :param dimension_data: The dimension_data of this ShowReportSummaryDataResponse.
        :type dimension_data: list[str]
        """
        self._dimension_data = dimension_data

    @property
    def value_name(self):
        r"""Gets the value_name of this ShowReportSummaryDataResponse.

        数据取值名称，例如[任务数量、任务成功率，资源数量、资源保护率、资源合规率

        :return: The value_name of this ShowReportSummaryDataResponse.
        :rtype: list[str]
        """
        return self._value_name

    @value_name.setter
    def value_name(self, value_name):
        r"""Sets the value_name of this ShowReportSummaryDataResponse.

        数据取值名称，例如[任务数量、任务成功率，资源数量、资源保护率、资源合规率

        :param value_name: The value_name of this ShowReportSummaryDataResponse.
        :type value_name: list[str]
        """
        self._value_name = value_name

    @property
    def value_data(self):
        r"""Gets the value_data of this ShowReportSummaryDataResponse.

        数据取值，和value_name相对应，可以是多组数据，例如[[100,0.98,0.97],[99,0.98.0.99]]

        :return: The value_data of this ShowReportSummaryDataResponse.
        :rtype: list[list[float]]
        """
        return self._value_data

    @value_data.setter
    def value_data(self, value_data):
        r"""Sets the value_data of this ShowReportSummaryDataResponse.

        数据取值，和value_name相对应，可以是多组数据，例如[[100,0.98,0.97],[99,0.98.0.99]]

        :param value_data: The value_data of this ShowReportSummaryDataResponse.
        :type value_data: list[list[float]]
        """
        self._value_data = value_data

    def to_dict(self):
        import warnings
        warnings.warn("ShowReportSummaryDataResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowReportSummaryDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
