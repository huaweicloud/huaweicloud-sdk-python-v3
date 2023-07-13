# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDiagnoseResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'result': 'list[DiagnoseResourceVo]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'result': 'result'
    }

    def __init__(self, total_count=None, result=None):
        """ListDiagnoseResourcesResponse

        The model defined in huaweicloud sdk

        :param total_count: 总数
        :type total_count: int
        :param result: 诊断记录列表
        :type result: list[:class:`huaweicloudsdkosm.v2.DiagnoseResourceVo`]
        """
        
        super(ListDiagnoseResourcesResponse, self).__init__()

        self._total_count = None
        self._result = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if result is not None:
            self.result = result

    @property
    def total_count(self):
        """Gets the total_count of this ListDiagnoseResourcesResponse.

        总数

        :return: The total_count of this ListDiagnoseResourcesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListDiagnoseResourcesResponse.

        总数

        :param total_count: The total_count of this ListDiagnoseResourcesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def result(self):
        """Gets the result of this ListDiagnoseResourcesResponse.

        诊断记录列表

        :return: The result of this ListDiagnoseResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkosm.v2.DiagnoseResourceVo`]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ListDiagnoseResourcesResponse.

        诊断记录列表

        :param result: The result of this ListDiagnoseResourcesResponse.
        :type result: list[:class:`huaweicloudsdkosm.v2.DiagnoseResourceVo`]
        """
        self._result = result

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
        if not isinstance(other, ListDiagnoseResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
