# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDomainLogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'logs': 'list[CdnLog]'
    }

    attribute_map = {
        'total': 'total',
        'logs': 'logs'
    }

    def __init__(self, total=None, logs=None):
        """ListDomainLogsResponse

        The model defined in huaweicloud sdk

        :param total: 日志总数。
        :type total: int
        :param logs: 日志列表数据。
        :type logs: list[:class:`huaweicloudsdkvod.v1.CdnLog`]
        """
        
        super(ListDomainLogsResponse, self).__init__()

        self._total = None
        self._logs = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if logs is not None:
            self.logs = logs

    @property
    def total(self):
        """Gets the total of this ListDomainLogsResponse.

        日志总数。

        :return: The total of this ListDomainLogsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListDomainLogsResponse.

        日志总数。

        :param total: The total of this ListDomainLogsResponse.
        :type total: int
        """
        self._total = total

    @property
    def logs(self):
        """Gets the logs of this ListDomainLogsResponse.

        日志列表数据。

        :return: The logs of this ListDomainLogsResponse.
        :rtype: list[:class:`huaweicloudsdkvod.v1.CdnLog`]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this ListDomainLogsResponse.

        日志列表数据。

        :param logs: The logs of this ListDomainLogsResponse.
        :type logs: list[:class:`huaweicloudsdkvod.v1.CdnLog`]
        """
        self._logs = logs

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
        if not isinstance(other, ListDomainLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
