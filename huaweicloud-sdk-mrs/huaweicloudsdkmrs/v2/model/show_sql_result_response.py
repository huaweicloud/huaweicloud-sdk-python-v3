# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlResultResponse(SdkResponse):

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
        'message': 'str',
        'statement': 'str',
        'status': 'str',
        'result_location': 'str',
        'content': 'list[list[str]]'
    }

    attribute_map = {
        'id': 'id',
        'message': 'message',
        'statement': 'statement',
        'status': 'status',
        'result_location': 'result_location',
        'content': 'content'
    }

    def __init__(self, id=None, message=None, statement=None, status=None, result_location=None, content=None):
        """ShowSqlResultResponse

        The model defined in huaweicloud sdk

        :param id: SQL的执行id。执行select、show和desc语句时才会生成id，其他操作id为空
        :type id: str
        :param message: 错误信息。
        :type message: str
        :param statement: 执行的SQL语句。
        :type statement: str
        :param status: SQL的执行状态。 - QUEUED - WAITING_FOR_RESOURCES - PLANNING - STARTING - RUNNING - FINISHING - FINISHED - FAILED
        :type status: str
        :param result_location: SQL查询语句的最终结果归档路径。 说明： 只有select的语句才会在将SQL的执行结果转储到result_location中。
        :type result_location: str
        :param content: SQL的执行结果。 说明： 只有非select的语句才会在content中返回结果，如果SQL中没有结果，content为空。
        :type content: list[list[str]]
        """
        
        super(ShowSqlResultResponse, self).__init__()

        self._id = None
        self._message = None
        self._statement = None
        self._status = None
        self._result_location = None
        self._content = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if message is not None:
            self.message = message
        if statement is not None:
            self.statement = statement
        if status is not None:
            self.status = status
        if result_location is not None:
            self.result_location = result_location
        if content is not None:
            self.content = content

    @property
    def id(self):
        """Gets the id of this ShowSqlResultResponse.

        SQL的执行id。执行select、show和desc语句时才会生成id，其他操作id为空

        :return: The id of this ShowSqlResultResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowSqlResultResponse.

        SQL的执行id。执行select、show和desc语句时才会生成id，其他操作id为空

        :param id: The id of this ShowSqlResultResponse.
        :type id: str
        """
        self._id = id

    @property
    def message(self):
        """Gets the message of this ShowSqlResultResponse.

        错误信息。

        :return: The message of this ShowSqlResultResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowSqlResultResponse.

        错误信息。

        :param message: The message of this ShowSqlResultResponse.
        :type message: str
        """
        self._message = message

    @property
    def statement(self):
        """Gets the statement of this ShowSqlResultResponse.

        执行的SQL语句。

        :return: The statement of this ShowSqlResultResponse.
        :rtype: str
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        """Sets the statement of this ShowSqlResultResponse.

        执行的SQL语句。

        :param statement: The statement of this ShowSqlResultResponse.
        :type statement: str
        """
        self._statement = statement

    @property
    def status(self):
        """Gets the status of this ShowSqlResultResponse.

        SQL的执行状态。 - QUEUED - WAITING_FOR_RESOURCES - PLANNING - STARTING - RUNNING - FINISHING - FINISHED - FAILED

        :return: The status of this ShowSqlResultResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowSqlResultResponse.

        SQL的执行状态。 - QUEUED - WAITING_FOR_RESOURCES - PLANNING - STARTING - RUNNING - FINISHING - FINISHED - FAILED

        :param status: The status of this ShowSqlResultResponse.
        :type status: str
        """
        self._status = status

    @property
    def result_location(self):
        """Gets the result_location of this ShowSqlResultResponse.

        SQL查询语句的最终结果归档路径。 说明： 只有select的语句才会在将SQL的执行结果转储到result_location中。

        :return: The result_location of this ShowSqlResultResponse.
        :rtype: str
        """
        return self._result_location

    @result_location.setter
    def result_location(self, result_location):
        """Sets the result_location of this ShowSqlResultResponse.

        SQL查询语句的最终结果归档路径。 说明： 只有select的语句才会在将SQL的执行结果转储到result_location中。

        :param result_location: The result_location of this ShowSqlResultResponse.
        :type result_location: str
        """
        self._result_location = result_location

    @property
    def content(self):
        """Gets the content of this ShowSqlResultResponse.

        SQL的执行结果。 说明： 只有非select的语句才会在content中返回结果，如果SQL中没有结果，content为空。

        :return: The content of this ShowSqlResultResponse.
        :rtype: list[list[str]]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ShowSqlResultResponse.

        SQL的执行结果。 说明： 只有非select的语句才会在content中返回结果，如果SQL中没有结果，content为空。

        :param content: The content of this ShowSqlResultResponse.
        :type content: list[list[str]]
        """
        self._content = content

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
        if not isinstance(other, ShowSqlResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
