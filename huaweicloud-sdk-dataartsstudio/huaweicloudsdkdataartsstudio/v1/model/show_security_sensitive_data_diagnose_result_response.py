# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecuritySensitiveDataDiagnoseResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'scanning': 'bool',
        'check_time': 'int',
        'classification': 'ClassificationResult',
        'rule': 'IdentificationRuleResult',
        'masking': 'DataMaskingResult'
    }

    attribute_map = {
        'task_id': 'task_id',
        'scanning': 'scanning',
        'check_time': 'check_time',
        'classification': 'classification',
        'rule': 'rule',
        'masking': 'masking'
    }

    def __init__(self, task_id=None, scanning=None, check_time=None, classification=None, rule=None, masking=None):
        r"""ShowSecuritySensitiveDataDiagnoseResultResponse

        The model defined in huaweicloud sdk

        :param task_id: 诊断任务id
        :type task_id: str
        :param scanning: 是否正在扫描
        :type scanning: bool
        :param check_time: 最新检测时间。
        :type check_time: int
        :param classification: 
        :type classification: :class:`huaweicloudsdkdataartsstudio.v1.ClassificationResult`
        :param rule: 
        :type rule: :class:`huaweicloudsdkdataartsstudio.v1.IdentificationRuleResult`
        :param masking: 
        :type masking: :class:`huaweicloudsdkdataartsstudio.v1.DataMaskingResult`
        """
        
        super(ShowSecuritySensitiveDataDiagnoseResultResponse, self).__init__()

        self._task_id = None
        self._scanning = None
        self._check_time = None
        self._classification = None
        self._rule = None
        self._masking = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if scanning is not None:
            self.scanning = scanning
        if check_time is not None:
            self.check_time = check_time
        if classification is not None:
            self.classification = classification
        if rule is not None:
            self.rule = rule
        if masking is not None:
            self.masking = masking

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowSecuritySensitiveDataDiagnoseResultResponse.

        诊断任务id

        :return: The task_id of this ShowSecuritySensitiveDataDiagnoseResultResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowSecuritySensitiveDataDiagnoseResultResponse.

        诊断任务id

        :param task_id: The task_id of this ShowSecuritySensitiveDataDiagnoseResultResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def scanning(self):
        r"""Gets the scanning of this ShowSecuritySensitiveDataDiagnoseResultResponse.

        是否正在扫描

        :return: The scanning of this ShowSecuritySensitiveDataDiagnoseResultResponse.
        :rtype: bool
        """
        return self._scanning

    @scanning.setter
    def scanning(self, scanning):
        r"""Sets the scanning of this ShowSecuritySensitiveDataDiagnoseResultResponse.

        是否正在扫描

        :param scanning: The scanning of this ShowSecuritySensitiveDataDiagnoseResultResponse.
        :type scanning: bool
        """
        self._scanning = scanning

    @property
    def check_time(self):
        r"""Gets the check_time of this ShowSecuritySensitiveDataDiagnoseResultResponse.

        最新检测时间。

        :return: The check_time of this ShowSecuritySensitiveDataDiagnoseResultResponse.
        :rtype: int
        """
        return self._check_time

    @check_time.setter
    def check_time(self, check_time):
        r"""Sets the check_time of this ShowSecuritySensitiveDataDiagnoseResultResponse.

        最新检测时间。

        :param check_time: The check_time of this ShowSecuritySensitiveDataDiagnoseResultResponse.
        :type check_time: int
        """
        self._check_time = check_time

    @property
    def classification(self):
        r"""Gets the classification of this ShowSecuritySensitiveDataDiagnoseResultResponse.

        :return: The classification of this ShowSecuritySensitiveDataDiagnoseResultResponse.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ClassificationResult`
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        r"""Sets the classification of this ShowSecuritySensitiveDataDiagnoseResultResponse.

        :param classification: The classification of this ShowSecuritySensitiveDataDiagnoseResultResponse.
        :type classification: :class:`huaweicloudsdkdataartsstudio.v1.ClassificationResult`
        """
        self._classification = classification

    @property
    def rule(self):
        r"""Gets the rule of this ShowSecuritySensitiveDataDiagnoseResultResponse.

        :return: The rule of this ShowSecuritySensitiveDataDiagnoseResultResponse.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.IdentificationRuleResult`
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        r"""Sets the rule of this ShowSecuritySensitiveDataDiagnoseResultResponse.

        :param rule: The rule of this ShowSecuritySensitiveDataDiagnoseResultResponse.
        :type rule: :class:`huaweicloudsdkdataartsstudio.v1.IdentificationRuleResult`
        """
        self._rule = rule

    @property
    def masking(self):
        r"""Gets the masking of this ShowSecuritySensitiveDataDiagnoseResultResponse.

        :return: The masking of this ShowSecuritySensitiveDataDiagnoseResultResponse.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DataMaskingResult`
        """
        return self._masking

    @masking.setter
    def masking(self, masking):
        r"""Sets the masking of this ShowSecuritySensitiveDataDiagnoseResultResponse.

        :param masking: The masking of this ShowSecuritySensitiveDataDiagnoseResultResponse.
        :type masking: :class:`huaweicloudsdkdataartsstudio.v1.DataMaskingResult`
        """
        self._masking = masking

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
        if not isinstance(other, ShowSecuritySensitiveDataDiagnoseResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
