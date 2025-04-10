# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisassociateKeypairResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'server_id': 'str',
        'status': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'server_id': 'server_id',
        'status': 'status',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, task_id=None, server_id=None, status=None, error_code=None, error_msg=None):
        r"""DisassociateKeypairResponse

        The model defined in huaweicloud sdk

        :param task_id: 任务下发成功返回的ID。
        :type task_id: str
        :param server_id: 绑定的虚拟机id。
        :type server_id: str
        :param status: 任务下发的状态。SUCCESS或FAILED。
        :type status: str
        :param error_code: 任务下发失败返回的错误码。
        :type error_code: str
        :param error_msg: 任务下发失败返回的错误信息。
        :type error_msg: str
        """
        
        super(DisassociateKeypairResponse, self).__init__()

        self._task_id = None
        self._server_id = None
        self._status = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if server_id is not None:
            self.server_id = server_id
        if status is not None:
            self.status = status
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def task_id(self):
        r"""Gets the task_id of this DisassociateKeypairResponse.

        任务下发成功返回的ID。

        :return: The task_id of this DisassociateKeypairResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this DisassociateKeypairResponse.

        任务下发成功返回的ID。

        :param task_id: The task_id of this DisassociateKeypairResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def server_id(self):
        r"""Gets the server_id of this DisassociateKeypairResponse.

        绑定的虚拟机id。

        :return: The server_id of this DisassociateKeypairResponse.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this DisassociateKeypairResponse.

        绑定的虚拟机id。

        :param server_id: The server_id of this DisassociateKeypairResponse.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def status(self):
        r"""Gets the status of this DisassociateKeypairResponse.

        任务下发的状态。SUCCESS或FAILED。

        :return: The status of this DisassociateKeypairResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DisassociateKeypairResponse.

        任务下发的状态。SUCCESS或FAILED。

        :param status: The status of this DisassociateKeypairResponse.
        :type status: str
        """
        self._status = status

    @property
    def error_code(self):
        r"""Gets the error_code of this DisassociateKeypairResponse.

        任务下发失败返回的错误码。

        :return: The error_code of this DisassociateKeypairResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this DisassociateKeypairResponse.

        任务下发失败返回的错误码。

        :param error_code: The error_code of this DisassociateKeypairResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this DisassociateKeypairResponse.

        任务下发失败返回的错误信息。

        :return: The error_msg of this DisassociateKeypairResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this DisassociateKeypairResponse.

        任务下发失败返回的错误信息。

        :param error_msg: The error_msg of this DisassociateKeypairResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, DisassociateKeypairResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
