# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDiagnosisTaskDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'abnormal_item_sum': 'int',
        'failed_item_sum': 'int',
        'diagnosis_node_report_list': 'list[DiagnosisNodeReport]'
    }

    attribute_map = {
        'abnormal_item_sum': 'abnormal_item_sum',
        'failed_item_sum': 'failed_item_sum',
        'diagnosis_node_report_list': 'diagnosis_node_report_list'
    }

    def __init__(self, abnormal_item_sum=None, failed_item_sum=None, diagnosis_node_report_list=None):
        """ShowDiagnosisTaskDetailsResponse

        The model defined in huaweicloud sdk

        :param abnormal_item_sum: 诊断结果为异常的诊断项总数
        :type abnormal_item_sum: int
        :param failed_item_sum: 诊断失败的诊断项总数
        :type failed_item_sum: int
        :param diagnosis_node_report_list: 节点诊断报告列表
        :type diagnosis_node_report_list: list[:class:`huaweicloudsdkdcs.v2.DiagnosisNodeReport`]
        """
        
        super(ShowDiagnosisTaskDetailsResponse, self).__init__()

        self._abnormal_item_sum = None
        self._failed_item_sum = None
        self._diagnosis_node_report_list = None
        self.discriminator = None

        if abnormal_item_sum is not None:
            self.abnormal_item_sum = abnormal_item_sum
        if failed_item_sum is not None:
            self.failed_item_sum = failed_item_sum
        if diagnosis_node_report_list is not None:
            self.diagnosis_node_report_list = diagnosis_node_report_list

    @property
    def abnormal_item_sum(self):
        """Gets the abnormal_item_sum of this ShowDiagnosisTaskDetailsResponse.

        诊断结果为异常的诊断项总数

        :return: The abnormal_item_sum of this ShowDiagnosisTaskDetailsResponse.
        :rtype: int
        """
        return self._abnormal_item_sum

    @abnormal_item_sum.setter
    def abnormal_item_sum(self, abnormal_item_sum):
        """Sets the abnormal_item_sum of this ShowDiagnosisTaskDetailsResponse.

        诊断结果为异常的诊断项总数

        :param abnormal_item_sum: The abnormal_item_sum of this ShowDiagnosisTaskDetailsResponse.
        :type abnormal_item_sum: int
        """
        self._abnormal_item_sum = abnormal_item_sum

    @property
    def failed_item_sum(self):
        """Gets the failed_item_sum of this ShowDiagnosisTaskDetailsResponse.

        诊断失败的诊断项总数

        :return: The failed_item_sum of this ShowDiagnosisTaskDetailsResponse.
        :rtype: int
        """
        return self._failed_item_sum

    @failed_item_sum.setter
    def failed_item_sum(self, failed_item_sum):
        """Sets the failed_item_sum of this ShowDiagnosisTaskDetailsResponse.

        诊断失败的诊断项总数

        :param failed_item_sum: The failed_item_sum of this ShowDiagnosisTaskDetailsResponse.
        :type failed_item_sum: int
        """
        self._failed_item_sum = failed_item_sum

    @property
    def diagnosis_node_report_list(self):
        """Gets the diagnosis_node_report_list of this ShowDiagnosisTaskDetailsResponse.

        节点诊断报告列表

        :return: The diagnosis_node_report_list of this ShowDiagnosisTaskDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.DiagnosisNodeReport`]
        """
        return self._diagnosis_node_report_list

    @diagnosis_node_report_list.setter
    def diagnosis_node_report_list(self, diagnosis_node_report_list):
        """Sets the diagnosis_node_report_list of this ShowDiagnosisTaskDetailsResponse.

        节点诊断报告列表

        :param diagnosis_node_report_list: The diagnosis_node_report_list of this ShowDiagnosisTaskDetailsResponse.
        :type diagnosis_node_report_list: list[:class:`huaweicloudsdkdcs.v2.DiagnosisNodeReport`]
        """
        self._diagnosis_node_report_list = diagnosis_node_report_list

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
        if not isinstance(other, ShowDiagnosisTaskDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
