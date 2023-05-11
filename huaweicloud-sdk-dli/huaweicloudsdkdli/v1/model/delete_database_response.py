# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDatabaseResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'job_id': 'str',
        'job_mode': 'str',
        'job_type': 'str'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'job_id': 'job_id',
        'job_mode': 'job_mode',
        'job_type': 'job_type'
    }

    def __init__(self, is_success=None, message=None, job_id=None, job_mode=None, job_type=None):
        """DeleteDatabaseResponse

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息为空。
        :type message: str
        :param job_id: 异步删除数据库的时候返回的删除作业ID
        :type job_id: str
        :param job_mode: 删除数据库的时候的方式，是同步删除还是异步删除
        :type job_mode: str
        :param job_type: 异步执行作业时返回执行删除作业类型
        :type job_type: str
        """
        
        super(DeleteDatabaseResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._job_id = None
        self._job_mode = None
        self._job_type = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if job_id is not None:
            self.job_id = job_id
        if job_mode is not None:
            self.job_mode = job_mode
        if job_type is not None:
            self.job_type = job_type

    @property
    def is_success(self):
        """Gets the is_success of this DeleteDatabaseResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this DeleteDatabaseResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this DeleteDatabaseResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this DeleteDatabaseResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this DeleteDatabaseResponse.

        系统提示信息，执行成功时，信息为空。

        :return: The message of this DeleteDatabaseResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DeleteDatabaseResponse.

        系统提示信息，执行成功时，信息为空。

        :param message: The message of this DeleteDatabaseResponse.
        :type message: str
        """
        self._message = message

    @property
    def job_id(self):
        """Gets the job_id of this DeleteDatabaseResponse.

        异步删除数据库的时候返回的删除作业ID

        :return: The job_id of this DeleteDatabaseResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this DeleteDatabaseResponse.

        异步删除数据库的时候返回的删除作业ID

        :param job_id: The job_id of this DeleteDatabaseResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_mode(self):
        """Gets the job_mode of this DeleteDatabaseResponse.

        删除数据库的时候的方式，是同步删除还是异步删除

        :return: The job_mode of this DeleteDatabaseResponse.
        :rtype: str
        """
        return self._job_mode

    @job_mode.setter
    def job_mode(self, job_mode):
        """Sets the job_mode of this DeleteDatabaseResponse.

        删除数据库的时候的方式，是同步删除还是异步删除

        :param job_mode: The job_mode of this DeleteDatabaseResponse.
        :type job_mode: str
        """
        self._job_mode = job_mode

    @property
    def job_type(self):
        """Gets the job_type of this DeleteDatabaseResponse.

        异步执行作业时返回执行删除作业类型

        :return: The job_type of this DeleteDatabaseResponse.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this DeleteDatabaseResponse.

        异步执行作业时返回执行删除作业类型

        :param job_type: The job_type of this DeleteDatabaseResponse.
        :type job_type: str
        """
        self._job_type = job_type

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
        if not isinstance(other, DeleteDatabaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
