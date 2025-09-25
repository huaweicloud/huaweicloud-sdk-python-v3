# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMonthlyOperationReportDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation_summary_info': 'OperationSummaryInfo',
        'protect_info': 'ProtectInfo',
        'risk_handle_info': 'RiskHandleInfo'
    }

    attribute_map = {
        'operation_summary_info': 'operation_summary_info',
        'protect_info': 'protect_info',
        'risk_handle_info': 'risk_handle_info'
    }

    def __init__(self, operation_summary_info=None, protect_info=None, risk_handle_info=None):
        r"""ShowMonthlyOperationReportDetailResponse

        The model defined in huaweicloud sdk

        :param operation_summary_info: 
        :type operation_summary_info: :class:`huaweicloudsdkhss.v5.OperationSummaryInfo`
        :param protect_info: 
        :type protect_info: :class:`huaweicloudsdkhss.v5.ProtectInfo`
        :param risk_handle_info: 
        :type risk_handle_info: :class:`huaweicloudsdkhss.v5.RiskHandleInfo`
        """
        
        super(ShowMonthlyOperationReportDetailResponse, self).__init__()

        self._operation_summary_info = None
        self._protect_info = None
        self._risk_handle_info = None
        self.discriminator = None

        if operation_summary_info is not None:
            self.operation_summary_info = operation_summary_info
        if protect_info is not None:
            self.protect_info = protect_info
        if risk_handle_info is not None:
            self.risk_handle_info = risk_handle_info

    @property
    def operation_summary_info(self):
        r"""Gets the operation_summary_info of this ShowMonthlyOperationReportDetailResponse.

        :return: The operation_summary_info of this ShowMonthlyOperationReportDetailResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.OperationSummaryInfo`
        """
        return self._operation_summary_info

    @operation_summary_info.setter
    def operation_summary_info(self, operation_summary_info):
        r"""Sets the operation_summary_info of this ShowMonthlyOperationReportDetailResponse.

        :param operation_summary_info: The operation_summary_info of this ShowMonthlyOperationReportDetailResponse.
        :type operation_summary_info: :class:`huaweicloudsdkhss.v5.OperationSummaryInfo`
        """
        self._operation_summary_info = operation_summary_info

    @property
    def protect_info(self):
        r"""Gets the protect_info of this ShowMonthlyOperationReportDetailResponse.

        :return: The protect_info of this ShowMonthlyOperationReportDetailResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.ProtectInfo`
        """
        return self._protect_info

    @protect_info.setter
    def protect_info(self, protect_info):
        r"""Sets the protect_info of this ShowMonthlyOperationReportDetailResponse.

        :param protect_info: The protect_info of this ShowMonthlyOperationReportDetailResponse.
        :type protect_info: :class:`huaweicloudsdkhss.v5.ProtectInfo`
        """
        self._protect_info = protect_info

    @property
    def risk_handle_info(self):
        r"""Gets the risk_handle_info of this ShowMonthlyOperationReportDetailResponse.

        :return: The risk_handle_info of this ShowMonthlyOperationReportDetailResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.RiskHandleInfo`
        """
        return self._risk_handle_info

    @risk_handle_info.setter
    def risk_handle_info(self, risk_handle_info):
        r"""Sets the risk_handle_info of this ShowMonthlyOperationReportDetailResponse.

        :param risk_handle_info: The risk_handle_info of this ShowMonthlyOperationReportDetailResponse.
        :type risk_handle_info: :class:`huaweicloudsdkhss.v5.RiskHandleInfo`
        """
        self._risk_handle_info = risk_handle_info

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
        if not isinstance(other, ShowMonthlyOperationReportDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
