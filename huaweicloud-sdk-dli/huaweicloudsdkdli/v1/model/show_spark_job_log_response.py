# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSparkJobLogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        '_from': 'int',
        'total': 'int',
        'log': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        '_from': 'from',
        'total': 'total',
        'log': 'log'
    }

    def __init__(self, id=None, _from=None, total=None, log=None):
        r"""ShowSparkJobLogResponse

        The model defined in huaweicloud sdk

        :param id: 批处理作业的id。
        :type id: str
        :param _from: 日志起始索引。
        :type _from: int
        :param total: 日志的总记录数。
        :type total: int
        :param log: 显示当前批处理作业日志。
        :type log: list[str]
        """
        
        super(ShowSparkJobLogResponse, self).__init__()

        self._id = None
        self.__from = None
        self._total = None
        self._log = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if _from is not None:
            self._from = _from
        if total is not None:
            self.total = total
        if log is not None:
            self.log = log

    @property
    def id(self):
        r"""Gets the id of this ShowSparkJobLogResponse.

        批处理作业的id。

        :return: The id of this ShowSparkJobLogResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowSparkJobLogResponse.

        批处理作业的id。

        :param id: The id of this ShowSparkJobLogResponse.
        :type id: str
        """
        self._id = id

    @property
    def _from(self):
        r"""Gets the _from of this ShowSparkJobLogResponse.

        日志起始索引。

        :return: The _from of this ShowSparkJobLogResponse.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ShowSparkJobLogResponse.

        日志起始索引。

        :param _from: The _from of this ShowSparkJobLogResponse.
        :type _from: int
        """
        self.__from = _from

    @property
    def total(self):
        r"""Gets the total of this ShowSparkJobLogResponse.

        日志的总记录数。

        :return: The total of this ShowSparkJobLogResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowSparkJobLogResponse.

        日志的总记录数。

        :param total: The total of this ShowSparkJobLogResponse.
        :type total: int
        """
        self._total = total

    @property
    def log(self):
        r"""Gets the log of this ShowSparkJobLogResponse.

        显示当前批处理作业日志。

        :return: The log of this ShowSparkJobLogResponse.
        :rtype: list[str]
        """
        return self._log

    @log.setter
    def log(self, log):
        r"""Sets the log of this ShowSparkJobLogResponse.

        显示当前批处理作业日志。

        :param log: The log of this ShowSparkJobLogResponse.
        :type log: list[str]
        """
        self._log = log

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
        if not isinstance(other, ShowSparkJobLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
