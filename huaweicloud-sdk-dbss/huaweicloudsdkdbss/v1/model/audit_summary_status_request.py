# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuditSummaryStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'oper_type': 'str',
        'query_begin_time': 'int',
        'query_end_time': 'int'
    }

    attribute_map = {
        'code': 'code',
        'oper_type': 'oper_type',
        'query_begin_time': 'query_begin_time',
        'query_end_time': 'query_end_time'
    }

    def __init__(self, code=None, oper_type=None, query_begin_time=None, query_end_time=None):
        r"""AuditSummaryStatusRequest

        The model defined in huaweicloud sdk

        :param code: 操作码，operType为switch时必输入  - on: 开启  - off: 关闭
        :type code: str
        :param oper_type: 操作类型  - switch: 任务开关  - execute: 立即刷新
        :type oper_type: str
        :param query_begin_time: 查询条件：开始时间
        :type query_begin_time: int
        :param query_end_time: 查询条件：结束时间
        :type query_end_time: int
        """
        
        

        self._code = None
        self._oper_type = None
        self._query_begin_time = None
        self._query_end_time = None
        self.discriminator = None

        if code is not None:
            self.code = code
        self.oper_type = oper_type
        if query_begin_time is not None:
            self.query_begin_time = query_begin_time
        if query_end_time is not None:
            self.query_end_time = query_end_time

    @property
    def code(self):
        r"""Gets the code of this AuditSummaryStatusRequest.

        操作码，operType为switch时必输入  - on: 开启  - off: 关闭

        :return: The code of this AuditSummaryStatusRequest.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this AuditSummaryStatusRequest.

        操作码，operType为switch时必输入  - on: 开启  - off: 关闭

        :param code: The code of this AuditSummaryStatusRequest.
        :type code: str
        """
        self._code = code

    @property
    def oper_type(self):
        r"""Gets the oper_type of this AuditSummaryStatusRequest.

        操作类型  - switch: 任务开关  - execute: 立即刷新

        :return: The oper_type of this AuditSummaryStatusRequest.
        :rtype: str
        """
        return self._oper_type

    @oper_type.setter
    def oper_type(self, oper_type):
        r"""Sets the oper_type of this AuditSummaryStatusRequest.

        操作类型  - switch: 任务开关  - execute: 立即刷新

        :param oper_type: The oper_type of this AuditSummaryStatusRequest.
        :type oper_type: str
        """
        self._oper_type = oper_type

    @property
    def query_begin_time(self):
        r"""Gets the query_begin_time of this AuditSummaryStatusRequest.

        查询条件：开始时间

        :return: The query_begin_time of this AuditSummaryStatusRequest.
        :rtype: int
        """
        return self._query_begin_time

    @query_begin_time.setter
    def query_begin_time(self, query_begin_time):
        r"""Sets the query_begin_time of this AuditSummaryStatusRequest.

        查询条件：开始时间

        :param query_begin_time: The query_begin_time of this AuditSummaryStatusRequest.
        :type query_begin_time: int
        """
        self._query_begin_time = query_begin_time

    @property
    def query_end_time(self):
        r"""Gets the query_end_time of this AuditSummaryStatusRequest.

        查询条件：结束时间

        :return: The query_end_time of this AuditSummaryStatusRequest.
        :rtype: int
        """
        return self._query_end_time

    @query_end_time.setter
    def query_end_time(self, query_end_time):
        r"""Sets the query_end_time of this AuditSummaryStatusRequest.

        查询条件：结束时间

        :param query_end_time: The query_end_time of this AuditSummaryStatusRequest.
        :type query_end_time: int
        """
        self._query_end_time = query_end_time

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
        if not isinstance(other, AuditSummaryStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
