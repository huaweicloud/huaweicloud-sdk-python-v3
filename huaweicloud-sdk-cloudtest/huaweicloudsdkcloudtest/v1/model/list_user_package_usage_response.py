# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserPackageUsageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'result': 'list[PackageUsage]',
        'error': 'CommonResponseErrorOfAPITest'
    }

    attribute_map = {
        'status': 'status',
        'result': 'result',
        'error': 'error'
    }

    def __init__(self, status=None, result=None, error=None):
        r"""ListUserPackageUsageResponse

        The model defined in huaweicloud sdk

        :param status: 是否请求成功
        :type status: str
        :param result: 套餐用量信息列表
        :type result: list[:class:`huaweicloudsdkcloudtest.v1.PackageUsage`]
        :param error: 
        :type error: :class:`huaweicloudsdkcloudtest.v1.CommonResponseErrorOfAPITest`
        """
        
        super(ListUserPackageUsageResponse, self).__init__()

        self._status = None
        self._result = None
        self._error = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if result is not None:
            self.result = result
        if error is not None:
            self.error = error

    @property
    def status(self):
        r"""Gets the status of this ListUserPackageUsageResponse.

        是否请求成功

        :return: The status of this ListUserPackageUsageResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListUserPackageUsageResponse.

        是否请求成功

        :param status: The status of this ListUserPackageUsageResponse.
        :type status: str
        """
        self._status = status

    @property
    def result(self):
        r"""Gets the result of this ListUserPackageUsageResponse.

        套餐用量信息列表

        :return: The result of this ListUserPackageUsageResponse.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.PackageUsage`]
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ListUserPackageUsageResponse.

        套餐用量信息列表

        :param result: The result of this ListUserPackageUsageResponse.
        :type result: list[:class:`huaweicloudsdkcloudtest.v1.PackageUsage`]
        """
        self._result = result

    @property
    def error(self):
        r"""Gets the error of this ListUserPackageUsageResponse.

        :return: The error of this ListUserPackageUsageResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CommonResponseErrorOfAPITest`
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this ListUserPackageUsageResponse.

        :param error: The error of this ListUserPackageUsageResponse.
        :type error: :class:`huaweicloudsdkcloudtest.v1.CommonResponseErrorOfAPITest`
        """
        self._error = error

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
        if not isinstance(other, ListUserPackageUsageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
