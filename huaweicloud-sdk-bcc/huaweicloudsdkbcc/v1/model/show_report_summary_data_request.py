# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReportSummaryDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'report_id': 'str',
        'data_item_name': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'report_id': 'report_id',
        'data_item_name': 'data_item_name'
    }

    def __init__(self, domain_id=None, report_id=None, data_item_name=None):
        r"""ShowReportSummaryDataRequest

        The model defined in huaweicloud sdk

        :param domain_id: 租户ID
        :type domain_id: str
        :param report_id: 报告ID
        :type report_id: str
        :param data_item_name: 数据项名称，取值范围：task-status-pie,task-type-pie,task-status-region-column,task-trend-curve,resource-protection-pie,resource-compliance-pie,resource-protection-region-column,resource-compliance-region-column,resource-trend-curve
        :type data_item_name: str
        """
        
        

        self._domain_id = None
        self._report_id = None
        self._data_item_name = None
        self.discriminator = None

        self.domain_id = domain_id
        self.report_id = report_id
        self.data_item_name = data_item_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowReportSummaryDataRequest.

        租户ID

        :return: The domain_id of this ShowReportSummaryDataRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowReportSummaryDataRequest.

        租户ID

        :param domain_id: The domain_id of this ShowReportSummaryDataRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def report_id(self):
        r"""Gets the report_id of this ShowReportSummaryDataRequest.

        报告ID

        :return: The report_id of this ShowReportSummaryDataRequest.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this ShowReportSummaryDataRequest.

        报告ID

        :param report_id: The report_id of this ShowReportSummaryDataRequest.
        :type report_id: str
        """
        self._report_id = report_id

    @property
    def data_item_name(self):
        r"""Gets the data_item_name of this ShowReportSummaryDataRequest.

        数据项名称，取值范围：task-status-pie,task-type-pie,task-status-region-column,task-trend-curve,resource-protection-pie,resource-compliance-pie,resource-protection-region-column,resource-compliance-region-column,resource-trend-curve

        :return: The data_item_name of this ShowReportSummaryDataRequest.
        :rtype: str
        """
        return self._data_item_name

    @data_item_name.setter
    def data_item_name(self, data_item_name):
        r"""Sets the data_item_name of this ShowReportSummaryDataRequest.

        数据项名称，取值范围：task-status-pie,task-type-pie,task-status-region-column,task-trend-curve,resource-protection-pie,resource-compliance-pie,resource-protection-region-column,resource-compliance-region-column,resource-trend-curve

        :param data_item_name: The data_item_name of this ShowReportSummaryDataRequest.
        :type data_item_name: str
        """
        self._data_item_name = data_item_name

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
        if not isinstance(other, ShowReportSummaryDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
