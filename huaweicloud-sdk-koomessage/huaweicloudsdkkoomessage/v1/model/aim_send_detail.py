# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AIMSendDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'msg_id': 'str',
        'task_id': 'str',
        'task_name': 'str',
        'tpl_id': 'str',
        'tpl_name': 'str',
        'cust_flag': 'str',
        'send_account': 'str',
        'send_status': 'str',
        'send_time': 'str',
        'receive_time': 'str',
        'result_code': 'str'
    }

    attribute_map = {
        'msg_id': 'msg_id',
        'task_id': 'task_id',
        'task_name': 'task_name',
        'tpl_id': 'tpl_id',
        'tpl_name': 'tpl_name',
        'cust_flag': 'cust_flag',
        'send_account': 'send_account',
        'send_status': 'send_status',
        'send_time': 'send_time',
        'receive_time': 'receive_time',
        'result_code': 'result_code'
    }

    def __init__(self, msg_id=None, task_id=None, task_name=None, tpl_id=None, tpl_name=None, cust_flag=None, send_account=None, send_status=None, send_time=None, receive_time=None, result_code=None):
        """AIMSendDetail

        The model defined in huaweicloud sdk

        :param msg_id: 发送明细的唯一标识ID。
        :type msg_id: str
        :param task_id: 任务ID。
        :type task_id: str
        :param task_name: 任务名称。
        :type task_name: str
        :param tpl_id: 智能信息模板ID。
        :type tpl_id: str
        :param tpl_name: 智能信息模板名称。
        :type tpl_name: str
        :param cust_flag: 创建解析任务时填写用户唯一标识，手机号码或者任何的唯一标识，唯一标识不超过64个字符。发送智能信息时则必须填客户的手机号码。此处为手机号。样例为：130****0001。
        :type cust_flag: str
        :param send_account: 发送的目标手机号。
        :type send_account: str
        :param send_status: 发送状态。 - success：发送成功  - fail：发送失败  - sending：发送中 
        :type send_status: str
        :param send_time: 发送时间。
        :type send_time: str
        :param receive_time: 接收时间。
        :type receive_time: str
        :param result_code: 发送错误码。
        :type result_code: str
        """
        
        

        self._msg_id = None
        self._task_id = None
        self._task_name = None
        self._tpl_id = None
        self._tpl_name = None
        self._cust_flag = None
        self._send_account = None
        self._send_status = None
        self._send_time = None
        self._receive_time = None
        self._result_code = None
        self.discriminator = None

        if msg_id is not None:
            self.msg_id = msg_id
        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if tpl_id is not None:
            self.tpl_id = tpl_id
        if tpl_name is not None:
            self.tpl_name = tpl_name
        if cust_flag is not None:
            self.cust_flag = cust_flag
        if send_account is not None:
            self.send_account = send_account
        if send_status is not None:
            self.send_status = send_status
        if send_time is not None:
            self.send_time = send_time
        if receive_time is not None:
            self.receive_time = receive_time
        if result_code is not None:
            self.result_code = result_code

    @property
    def msg_id(self):
        """Gets the msg_id of this AIMSendDetail.

        发送明细的唯一标识ID。

        :return: The msg_id of this AIMSendDetail.
        :rtype: str
        """
        return self._msg_id

    @msg_id.setter
    def msg_id(self, msg_id):
        """Sets the msg_id of this AIMSendDetail.

        发送明细的唯一标识ID。

        :param msg_id: The msg_id of this AIMSendDetail.
        :type msg_id: str
        """
        self._msg_id = msg_id

    @property
    def task_id(self):
        """Gets the task_id of this AIMSendDetail.

        任务ID。

        :return: The task_id of this AIMSendDetail.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this AIMSendDetail.

        任务ID。

        :param task_id: The task_id of this AIMSendDetail.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        """Gets the task_name of this AIMSendDetail.

        任务名称。

        :return: The task_name of this AIMSendDetail.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this AIMSendDetail.

        任务名称。

        :param task_name: The task_name of this AIMSendDetail.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def tpl_id(self):
        """Gets the tpl_id of this AIMSendDetail.

        智能信息模板ID。

        :return: The tpl_id of this AIMSendDetail.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        """Sets the tpl_id of this AIMSendDetail.

        智能信息模板ID。

        :param tpl_id: The tpl_id of this AIMSendDetail.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def tpl_name(self):
        """Gets the tpl_name of this AIMSendDetail.

        智能信息模板名称。

        :return: The tpl_name of this AIMSendDetail.
        :rtype: str
        """
        return self._tpl_name

    @tpl_name.setter
    def tpl_name(self, tpl_name):
        """Sets the tpl_name of this AIMSendDetail.

        智能信息模板名称。

        :param tpl_name: The tpl_name of this AIMSendDetail.
        :type tpl_name: str
        """
        self._tpl_name = tpl_name

    @property
    def cust_flag(self):
        """Gets the cust_flag of this AIMSendDetail.

        创建解析任务时填写用户唯一标识，手机号码或者任何的唯一标识，唯一标识不超过64个字符。发送智能信息时则必须填客户的手机号码。此处为手机号。样例为：130****0001。

        :return: The cust_flag of this AIMSendDetail.
        :rtype: str
        """
        return self._cust_flag

    @cust_flag.setter
    def cust_flag(self, cust_flag):
        """Sets the cust_flag of this AIMSendDetail.

        创建解析任务时填写用户唯一标识，手机号码或者任何的唯一标识，唯一标识不超过64个字符。发送智能信息时则必须填客户的手机号码。此处为手机号。样例为：130****0001。

        :param cust_flag: The cust_flag of this AIMSendDetail.
        :type cust_flag: str
        """
        self._cust_flag = cust_flag

    @property
    def send_account(self):
        """Gets the send_account of this AIMSendDetail.

        发送的目标手机号。

        :return: The send_account of this AIMSendDetail.
        :rtype: str
        """
        return self._send_account

    @send_account.setter
    def send_account(self, send_account):
        """Sets the send_account of this AIMSendDetail.

        发送的目标手机号。

        :param send_account: The send_account of this AIMSendDetail.
        :type send_account: str
        """
        self._send_account = send_account

    @property
    def send_status(self):
        """Gets the send_status of this AIMSendDetail.

        发送状态。 - success：发送成功  - fail：发送失败  - sending：发送中 

        :return: The send_status of this AIMSendDetail.
        :rtype: str
        """
        return self._send_status

    @send_status.setter
    def send_status(self, send_status):
        """Sets the send_status of this AIMSendDetail.

        发送状态。 - success：发送成功  - fail：发送失败  - sending：发送中 

        :param send_status: The send_status of this AIMSendDetail.
        :type send_status: str
        """
        self._send_status = send_status

    @property
    def send_time(self):
        """Gets the send_time of this AIMSendDetail.

        发送时间。

        :return: The send_time of this AIMSendDetail.
        :rtype: str
        """
        return self._send_time

    @send_time.setter
    def send_time(self, send_time):
        """Sets the send_time of this AIMSendDetail.

        发送时间。

        :param send_time: The send_time of this AIMSendDetail.
        :type send_time: str
        """
        self._send_time = send_time

    @property
    def receive_time(self):
        """Gets the receive_time of this AIMSendDetail.

        接收时间。

        :return: The receive_time of this AIMSendDetail.
        :rtype: str
        """
        return self._receive_time

    @receive_time.setter
    def receive_time(self, receive_time):
        """Sets the receive_time of this AIMSendDetail.

        接收时间。

        :param receive_time: The receive_time of this AIMSendDetail.
        :type receive_time: str
        """
        self._receive_time = receive_time

    @property
    def result_code(self):
        """Gets the result_code of this AIMSendDetail.

        发送错误码。

        :return: The result_code of this AIMSendDetail.
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """Sets the result_code of this AIMSendDetail.

        发送错误码。

        :param result_code: The result_code of this AIMSendDetail.
        :type result_code: str
        """
        self._result_code = result_code

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
        if not isinstance(other, AIMSendDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
