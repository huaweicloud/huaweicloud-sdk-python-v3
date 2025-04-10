# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDiagnosisTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'results': 'list[Item]'
    }

    attribute_map = {
        'results': 'results'
    }

    def __init__(self, results=None):
        r"""DeleteDiagnosisTaskResponse

        The model defined in huaweicloud sdk

        :param results: 删除实例诊断结果
        :type results: list[:class:`huaweicloudsdkdcs.v2.Item`]
        """
        
        super(DeleteDiagnosisTaskResponse, self).__init__()

        self._results = None
        self.discriminator = None

        if results is not None:
            self.results = results

    @property
    def results(self):
        r"""Gets the results of this DeleteDiagnosisTaskResponse.

        删除实例诊断结果

        :return: The results of this DeleteDiagnosisTaskResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.Item`]
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this DeleteDiagnosisTaskResponse.

        删除实例诊断结果

        :param results: The results of this DeleteDiagnosisTaskResponse.
        :type results: list[:class:`huaweicloudsdkdcs.v2.Item`]
        """
        self._results = results

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
        if not isinstance(other, DeleteDiagnosisTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
