# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLtsErrorLogDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_log_list': 'list[LtsLogErrorDetail]'
    }

    attribute_map = {
        'error_log_list': 'error_log_list'
    }

    def __init__(self, error_log_list=None):
        r"""ListLtsErrorLogDetailsResponse

        The model defined in huaweicloud sdk

        :param error_log_list: 错误日志列表。
        :type error_log_list: list[:class:`huaweicloudsdkgaussdb.v3.LtsLogErrorDetail`]
        """
        
        super(ListLtsErrorLogDetailsResponse, self).__init__()

        self._error_log_list = None
        self.discriminator = None

        if error_log_list is not None:
            self.error_log_list = error_log_list

    @property
    def error_log_list(self):
        r"""Gets the error_log_list of this ListLtsErrorLogDetailsResponse.

        错误日志列表。

        :return: The error_log_list of this ListLtsErrorLogDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.LtsLogErrorDetail`]
        """
        return self._error_log_list

    @error_log_list.setter
    def error_log_list(self, error_log_list):
        r"""Sets the error_log_list of this ListLtsErrorLogDetailsResponse.

        错误日志列表。

        :param error_log_list: The error_log_list of this ListLtsErrorLogDetailsResponse.
        :type error_log_list: list[:class:`huaweicloudsdkgaussdb.v3.LtsLogErrorDetail`]
        """
        self._error_log_list = error_log_list

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
        if not isinstance(other, ListLtsErrorLogDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
