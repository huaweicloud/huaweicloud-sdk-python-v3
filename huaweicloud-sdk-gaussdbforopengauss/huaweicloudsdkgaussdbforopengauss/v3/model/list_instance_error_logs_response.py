# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceErrorLogsResponse(SdkResponse):

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
        'log_files': 'list[InstanceLogFile]'
    }

    attribute_map = {
        'total': 'total',
        'log_files': 'log_files'
    }

    def __init__(self, total=None, log_files=None):
        r"""ListInstanceErrorLogsResponse

        The model defined in huaweicloud sdk

        :param total: 总条数
        :type total: int
        :param log_files: 日志文件列表
        :type log_files: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.InstanceLogFile`]
        """
        
        super(ListInstanceErrorLogsResponse, self).__init__()

        self._total = None
        self._log_files = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if log_files is not None:
            self.log_files = log_files

    @property
    def total(self):
        r"""Gets the total of this ListInstanceErrorLogsResponse.

        总条数

        :return: The total of this ListInstanceErrorLogsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInstanceErrorLogsResponse.

        总条数

        :param total: The total of this ListInstanceErrorLogsResponse.
        :type total: int
        """
        self._total = total

    @property
    def log_files(self):
        r"""Gets the log_files of this ListInstanceErrorLogsResponse.

        日志文件列表

        :return: The log_files of this ListInstanceErrorLogsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.InstanceLogFile`]
        """
        return self._log_files

    @log_files.setter
    def log_files(self, log_files):
        r"""Sets the log_files of this ListInstanceErrorLogsResponse.

        日志文件列表

        :param log_files: The log_files of this ListInstanceErrorLogsResponse.
        :type log_files: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.InstanceLogFile`]
        """
        self._log_files = log_files

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
        if not isinstance(other, ListInstanceErrorLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
