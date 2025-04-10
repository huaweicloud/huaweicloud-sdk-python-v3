# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMongodbErrorLogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_logs': 'list[MongodbErrorLogDetail]'
    }

    attribute_map = {
        'error_logs': 'error_logs'
    }

    def __init__(self, error_logs=None):
        r"""ListMongodbErrorLogsResponse

        The model defined in huaweicloud sdk

        :param error_logs: 错误日志具体信息。
        :type error_logs: list[:class:`huaweicloudsdkgaussdbfornosql.v3.MongodbErrorLogDetail`]
        """
        
        super(ListMongodbErrorLogsResponse, self).__init__()

        self._error_logs = None
        self.discriminator = None

        if error_logs is not None:
            self.error_logs = error_logs

    @property
    def error_logs(self):
        r"""Gets the error_logs of this ListMongodbErrorLogsResponse.

        错误日志具体信息。

        :return: The error_logs of this ListMongodbErrorLogsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.MongodbErrorLogDetail`]
        """
        return self._error_logs

    @error_logs.setter
    def error_logs(self, error_logs):
        r"""Sets the error_logs of this ListMongodbErrorLogsResponse.

        错误日志具体信息。

        :param error_logs: The error_logs of this ListMongodbErrorLogsResponse.
        :type error_logs: list[:class:`huaweicloudsdkgaussdbfornosql.v3.MongodbErrorLogDetail`]
        """
        self._error_logs = error_logs

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
        if not isinstance(other, ListMongodbErrorLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
