# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceDiagnosisResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'diagnosis': 'list[DiagnosisItemResult]'
    }

    attribute_map = {
        'diagnosis': 'diagnosis'
    }

    def __init__(self, diagnosis=None):
        """ListInstanceDiagnosisResponse

        The model defined in huaweicloud sdk

        :param diagnosis: diagnosis info
        :type diagnosis: list[:class:`huaweicloudsdkrds.v3.DiagnosisItemResult`]
        """
        
        super(ListInstanceDiagnosisResponse, self).__init__()

        self._diagnosis = None
        self.discriminator = None

        if diagnosis is not None:
            self.diagnosis = diagnosis

    @property
    def diagnosis(self):
        """Gets the diagnosis of this ListInstanceDiagnosisResponse.

        diagnosis info

        :return: The diagnosis of this ListInstanceDiagnosisResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.DiagnosisItemResult`]
        """
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, diagnosis):
        """Sets the diagnosis of this ListInstanceDiagnosisResponse.

        diagnosis info

        :param diagnosis: The diagnosis of this ListInstanceDiagnosisResponse.
        :type diagnosis: list[:class:`huaweicloudsdkrds.v3.DiagnosisItemResult`]
        """
        self._diagnosis = diagnosis

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
        if not isinstance(other, ListInstanceDiagnosisResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
