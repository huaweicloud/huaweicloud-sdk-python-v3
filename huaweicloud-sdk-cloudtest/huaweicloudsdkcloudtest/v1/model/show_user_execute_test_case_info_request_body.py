# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUserExecuteTestCaseInfoRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'execute_start_time': 'str',
        'execute_end_time': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'execute_start_time': 'execute_start_time',
        'execute_end_time': 'execute_end_time'
    }

    def __init__(self, offset=None, limit=None, execute_start_time=None, execute_end_time=None):
        r"""ShowUserExecuteTestCaseInfoRequestBody

        The model defined in huaweicloud sdk

        :param offset: 起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于20000
        :type offset: int
        :param limit: 每页显示的条目数量,最大支持100条
        :type limit: int
        :param execute_start_time: 用例执行时间段开始
        :type execute_start_time: str
        :param execute_end_time: 用例执行时间段截止
        :type execute_end_time: str
        """
        
        

        self._offset = None
        self._limit = None
        self._execute_start_time = None
        self._execute_end_time = None
        self.discriminator = None

        self.offset = offset
        self.limit = limit
        self.execute_start_time = execute_start_time
        self.execute_end_time = execute_end_time

    @property
    def offset(self):
        r"""Gets the offset of this ShowUserExecuteTestCaseInfoRequestBody.

        起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于20000

        :return: The offset of this ShowUserExecuteTestCaseInfoRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowUserExecuteTestCaseInfoRequestBody.

        起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于20000

        :param offset: The offset of this ShowUserExecuteTestCaseInfoRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowUserExecuteTestCaseInfoRequestBody.

        每页显示的条目数量,最大支持100条

        :return: The limit of this ShowUserExecuteTestCaseInfoRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowUserExecuteTestCaseInfoRequestBody.

        每页显示的条目数量,最大支持100条

        :param limit: The limit of this ShowUserExecuteTestCaseInfoRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def execute_start_time(self):
        r"""Gets the execute_start_time of this ShowUserExecuteTestCaseInfoRequestBody.

        用例执行时间段开始

        :return: The execute_start_time of this ShowUserExecuteTestCaseInfoRequestBody.
        :rtype: str
        """
        return self._execute_start_time

    @execute_start_time.setter
    def execute_start_time(self, execute_start_time):
        r"""Sets the execute_start_time of this ShowUserExecuteTestCaseInfoRequestBody.

        用例执行时间段开始

        :param execute_start_time: The execute_start_time of this ShowUserExecuteTestCaseInfoRequestBody.
        :type execute_start_time: str
        """
        self._execute_start_time = execute_start_time

    @property
    def execute_end_time(self):
        r"""Gets the execute_end_time of this ShowUserExecuteTestCaseInfoRequestBody.

        用例执行时间段截止

        :return: The execute_end_time of this ShowUserExecuteTestCaseInfoRequestBody.
        :rtype: str
        """
        return self._execute_end_time

    @execute_end_time.setter
    def execute_end_time(self, execute_end_time):
        r"""Sets the execute_end_time of this ShowUserExecuteTestCaseInfoRequestBody.

        用例执行时间段截止

        :param execute_end_time: The execute_end_time of this ShowUserExecuteTestCaseInfoRequestBody.
        :type execute_end_time: str
        """
        self._execute_end_time = execute_end_time

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
        if not isinstance(other, ShowUserExecuteTestCaseInfoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
