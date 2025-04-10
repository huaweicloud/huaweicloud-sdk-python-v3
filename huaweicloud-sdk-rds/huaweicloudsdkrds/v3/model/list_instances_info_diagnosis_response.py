# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesInfoDiagnosisResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'diagnosis': 'str',
        'total_count': 'int',
        'instances': 'list[DiagnosisInstancesInfoResult]'
    }

    attribute_map = {
        'diagnosis': 'diagnosis',
        'total_count': 'total_count',
        'instances': 'instances'
    }

    def __init__(self, diagnosis=None, total_count=None, instances=None):
        r"""ListInstancesInfoDiagnosisResponse

        The model defined in huaweicloud sdk

        :param diagnosis: 诊断项
        :type diagnosis: str
        :param total_count: 实例数量
        :type total_count: int
        :param instances: 实例信息
        :type instances: list[:class:`huaweicloudsdkrds.v3.DiagnosisInstancesInfoResult`]
        """
        
        super(ListInstancesInfoDiagnosisResponse, self).__init__()

        self._diagnosis = None
        self._total_count = None
        self._instances = None
        self.discriminator = None

        if diagnosis is not None:
            self.diagnosis = diagnosis
        if total_count is not None:
            self.total_count = total_count
        if instances is not None:
            self.instances = instances

    @property
    def diagnosis(self):
        r"""Gets the diagnosis of this ListInstancesInfoDiagnosisResponse.

        诊断项

        :return: The diagnosis of this ListInstancesInfoDiagnosisResponse.
        :rtype: str
        """
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, diagnosis):
        r"""Sets the diagnosis of this ListInstancesInfoDiagnosisResponse.

        诊断项

        :param diagnosis: The diagnosis of this ListInstancesInfoDiagnosisResponse.
        :type diagnosis: str
        """
        self._diagnosis = diagnosis

    @property
    def total_count(self):
        r"""Gets the total_count of this ListInstancesInfoDiagnosisResponse.

        实例数量

        :return: The total_count of this ListInstancesInfoDiagnosisResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListInstancesInfoDiagnosisResponse.

        实例数量

        :param total_count: The total_count of this ListInstancesInfoDiagnosisResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def instances(self):
        r"""Gets the instances of this ListInstancesInfoDiagnosisResponse.

        实例信息

        :return: The instances of this ListInstancesInfoDiagnosisResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.DiagnosisInstancesInfoResult`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this ListInstancesInfoDiagnosisResponse.

        实例信息

        :param instances: The instances of this ListInstancesInfoDiagnosisResponse.
        :type instances: list[:class:`huaweicloudsdkrds.v3.DiagnosisInstancesInfoResult`]
        """
        self._instances = instances

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
        if not isinstance(other, ListInstancesInfoDiagnosisResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
