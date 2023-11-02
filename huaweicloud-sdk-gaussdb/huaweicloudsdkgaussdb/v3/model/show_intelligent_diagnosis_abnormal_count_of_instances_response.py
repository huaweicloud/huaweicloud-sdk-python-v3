# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIntelligentDiagnosisAbnormalCountOfInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'diagnosis_info': 'list[DiagnosisInfo]'
    }

    attribute_map = {
        'diagnosis_info': 'diagnosis_info'
    }

    def __init__(self, diagnosis_info=None):
        """ShowIntelligentDiagnosisAbnormalCountOfInstancesResponse

        The model defined in huaweicloud sdk

        :param diagnosis_info: 诊断信息列表。
        :type diagnosis_info: list[:class:`huaweicloudsdkgaussdb.v3.DiagnosisInfo`]
        """
        
        super(ShowIntelligentDiagnosisAbnormalCountOfInstancesResponse, self).__init__()

        self._diagnosis_info = None
        self.discriminator = None

        if diagnosis_info is not None:
            self.diagnosis_info = diagnosis_info

    @property
    def diagnosis_info(self):
        """Gets the diagnosis_info of this ShowIntelligentDiagnosisAbnormalCountOfInstancesResponse.

        诊断信息列表。

        :return: The diagnosis_info of this ShowIntelligentDiagnosisAbnormalCountOfInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.DiagnosisInfo`]
        """
        return self._diagnosis_info

    @diagnosis_info.setter
    def diagnosis_info(self, diagnosis_info):
        """Sets the diagnosis_info of this ShowIntelligentDiagnosisAbnormalCountOfInstancesResponse.

        诊断信息列表。

        :param diagnosis_info: The diagnosis_info of this ShowIntelligentDiagnosisAbnormalCountOfInstancesResponse.
        :type diagnosis_info: list[:class:`huaweicloudsdkgaussdb.v3.DiagnosisInfo`]
        """
        self._diagnosis_info = diagnosis_info

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
        if not isinstance(other, ShowIntelligentDiagnosisAbnormalCountOfInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
