# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMessageDiagnosisReportResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'abnormal_item_num': 'int',
        'failed_item_num': 'int',
        'normal_item_num': 'int',
        'diagnosis_dimension_list': 'list[KafkaMessageDiagnosisDimensionEntity]'
    }

    attribute_map = {
        'abnormal_item_num': 'abnormal_item_num',
        'failed_item_num': 'failed_item_num',
        'normal_item_num': 'normal_item_num',
        'diagnosis_dimension_list': 'diagnosis_dimension_list'
    }

    def __init__(self, abnormal_item_num=None, failed_item_num=None, normal_item_num=None, diagnosis_dimension_list=None):
        r"""ShowMessageDiagnosisReportResponse

        The model defined in huaweicloud sdk

        :param abnormal_item_num: 诊断异常的诊断项总和
        :type abnormal_item_num: int
        :param failed_item_num: 诊断失败的诊断项总和
        :type failed_item_num: int
        :param normal_item_num: 诊断正常的诊断项总和
        :type normal_item_num: int
        :param diagnosis_dimension_list: 诊断维度列表
        :type diagnosis_dimension_list: list[:class:`huaweicloudsdkkafka.v2.KafkaMessageDiagnosisDimensionEntity`]
        """
        
        super(ShowMessageDiagnosisReportResponse, self).__init__()

        self._abnormal_item_num = None
        self._failed_item_num = None
        self._normal_item_num = None
        self._diagnosis_dimension_list = None
        self.discriminator = None

        if abnormal_item_num is not None:
            self.abnormal_item_num = abnormal_item_num
        if failed_item_num is not None:
            self.failed_item_num = failed_item_num
        if normal_item_num is not None:
            self.normal_item_num = normal_item_num
        if diagnosis_dimension_list is not None:
            self.diagnosis_dimension_list = diagnosis_dimension_list

    @property
    def abnormal_item_num(self):
        r"""Gets the abnormal_item_num of this ShowMessageDiagnosisReportResponse.

        诊断异常的诊断项总和

        :return: The abnormal_item_num of this ShowMessageDiagnosisReportResponse.
        :rtype: int
        """
        return self._abnormal_item_num

    @abnormal_item_num.setter
    def abnormal_item_num(self, abnormal_item_num):
        r"""Sets the abnormal_item_num of this ShowMessageDiagnosisReportResponse.

        诊断异常的诊断项总和

        :param abnormal_item_num: The abnormal_item_num of this ShowMessageDiagnosisReportResponse.
        :type abnormal_item_num: int
        """
        self._abnormal_item_num = abnormal_item_num

    @property
    def failed_item_num(self):
        r"""Gets the failed_item_num of this ShowMessageDiagnosisReportResponse.

        诊断失败的诊断项总和

        :return: The failed_item_num of this ShowMessageDiagnosisReportResponse.
        :rtype: int
        """
        return self._failed_item_num

    @failed_item_num.setter
    def failed_item_num(self, failed_item_num):
        r"""Sets the failed_item_num of this ShowMessageDiagnosisReportResponse.

        诊断失败的诊断项总和

        :param failed_item_num: The failed_item_num of this ShowMessageDiagnosisReportResponse.
        :type failed_item_num: int
        """
        self._failed_item_num = failed_item_num

    @property
    def normal_item_num(self):
        r"""Gets the normal_item_num of this ShowMessageDiagnosisReportResponse.

        诊断正常的诊断项总和

        :return: The normal_item_num of this ShowMessageDiagnosisReportResponse.
        :rtype: int
        """
        return self._normal_item_num

    @normal_item_num.setter
    def normal_item_num(self, normal_item_num):
        r"""Sets the normal_item_num of this ShowMessageDiagnosisReportResponse.

        诊断正常的诊断项总和

        :param normal_item_num: The normal_item_num of this ShowMessageDiagnosisReportResponse.
        :type normal_item_num: int
        """
        self._normal_item_num = normal_item_num

    @property
    def diagnosis_dimension_list(self):
        r"""Gets the diagnosis_dimension_list of this ShowMessageDiagnosisReportResponse.

        诊断维度列表

        :return: The diagnosis_dimension_list of this ShowMessageDiagnosisReportResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.KafkaMessageDiagnosisDimensionEntity`]
        """
        return self._diagnosis_dimension_list

    @diagnosis_dimension_list.setter
    def diagnosis_dimension_list(self, diagnosis_dimension_list):
        r"""Sets the diagnosis_dimension_list of this ShowMessageDiagnosisReportResponse.

        诊断维度列表

        :param diagnosis_dimension_list: The diagnosis_dimension_list of this ShowMessageDiagnosisReportResponse.
        :type diagnosis_dimension_list: list[:class:`huaweicloudsdkkafka.v2.KafkaMessageDiagnosisDimensionEntity`]
        """
        self._diagnosis_dimension_list = diagnosis_dimension_list

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
        if not isinstance(other, ShowMessageDiagnosisReportResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
