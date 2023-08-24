# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AIMResolveDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resolve_id': 'str',
        'task_id': 'str',
        'task_name': 'str',
        'send_account': 'str',
        'tpl_id': 'str',
        'tpl_name': 'str',
        'cust_flag': 'str',
        'aim_url': 'str',
        'result_code': 'str',
        'generate_date': 'str',
        'expire_date': 'str',
        'resolved_time': 'str',
        'resolved_status': 'str'
    }

    attribute_map = {
        'resolve_id': 'resolve_id',
        'task_id': 'task_id',
        'task_name': 'task_name',
        'send_account': 'send_account',
        'tpl_id': 'tpl_id',
        'tpl_name': 'tpl_name',
        'cust_flag': 'cust_flag',
        'aim_url': 'aim_url',
        'result_code': 'result_code',
        'generate_date': 'generate_date',
        'expire_date': 'expire_date',
        'resolved_time': 'resolved_time',
        'resolved_status': 'resolved_status'
    }

    def __init__(self, resolve_id=None, task_id=None, task_name=None, send_account=None, tpl_id=None, tpl_name=None, cust_flag=None, aim_url=None, result_code=None, generate_date=None, expire_date=None, resolved_time=None, resolved_status=None):
        """AIMResolveDetail

        The model defined in huaweicloud sdk

        :param resolve_id: 解析详情唯一标识ID。
        :type resolve_id: str
        :param task_id: 任务ID。
        :type task_id: str
        :param task_name: 任务名称。
        :type task_name: str
        :param send_account: 发送的用户名。
        :type send_account: str
        :param tpl_id: 智能信息模板ID。
        :type tpl_id: str
        :param tpl_name: 智能信息模板名称。
        :type tpl_name: str
        :param cust_flag: 创建解析任务时填写用户唯一标识，手机号码或者任何的唯一标识，唯一标识不超过64个字符。发送智能信息时则必须填客户的手机号码。此处为手机号。样例为：130****0001。
        :type cust_flag: str
        :param aim_url: 智能信息短链，通过自己的短信渠道发送时，需要把该短链添加到短信模板中，并确保发送短信时的签名与创建短链时的签名保持一致。
        :type aim_url: str
        :param result_code: 短链申请结果返回码。 - 0：成功 - 非0：失败，具体请参见错误码。 
        :type result_code: str
        :param generate_date: 短链生成时间。样例为：2019-10-12T07:20:50Z。
        :type generate_date: str
        :param expire_date: 短链到期时间。样例为：2019-10-12T07:20:50Z。
        :type expire_date: str
        :param resolved_time: 解析时间。样例为：2019-10-12T07:20:50Z。
        :type resolved_time: str
        :param resolved_status: 解析状态。 - success：解析成功 - fail：解析失败 - unresolved：未解析 
        :type resolved_status: str
        """
        
        

        self._resolve_id = None
        self._task_id = None
        self._task_name = None
        self._send_account = None
        self._tpl_id = None
        self._tpl_name = None
        self._cust_flag = None
        self._aim_url = None
        self._result_code = None
        self._generate_date = None
        self._expire_date = None
        self._resolved_time = None
        self._resolved_status = None
        self.discriminator = None

        if resolve_id is not None:
            self.resolve_id = resolve_id
        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if send_account is not None:
            self.send_account = send_account
        if tpl_id is not None:
            self.tpl_id = tpl_id
        if tpl_name is not None:
            self.tpl_name = tpl_name
        if cust_flag is not None:
            self.cust_flag = cust_flag
        if aim_url is not None:
            self.aim_url = aim_url
        if result_code is not None:
            self.result_code = result_code
        if generate_date is not None:
            self.generate_date = generate_date
        if expire_date is not None:
            self.expire_date = expire_date
        if resolved_time is not None:
            self.resolved_time = resolved_time
        if resolved_status is not None:
            self.resolved_status = resolved_status

    @property
    def resolve_id(self):
        """Gets the resolve_id of this AIMResolveDetail.

        解析详情唯一标识ID。

        :return: The resolve_id of this AIMResolveDetail.
        :rtype: str
        """
        return self._resolve_id

    @resolve_id.setter
    def resolve_id(self, resolve_id):
        """Sets the resolve_id of this AIMResolveDetail.

        解析详情唯一标识ID。

        :param resolve_id: The resolve_id of this AIMResolveDetail.
        :type resolve_id: str
        """
        self._resolve_id = resolve_id

    @property
    def task_id(self):
        """Gets the task_id of this AIMResolveDetail.

        任务ID。

        :return: The task_id of this AIMResolveDetail.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this AIMResolveDetail.

        任务ID。

        :param task_id: The task_id of this AIMResolveDetail.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        """Gets the task_name of this AIMResolveDetail.

        任务名称。

        :return: The task_name of this AIMResolveDetail.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this AIMResolveDetail.

        任务名称。

        :param task_name: The task_name of this AIMResolveDetail.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def send_account(self):
        """Gets the send_account of this AIMResolveDetail.

        发送的用户名。

        :return: The send_account of this AIMResolveDetail.
        :rtype: str
        """
        return self._send_account

    @send_account.setter
    def send_account(self, send_account):
        """Sets the send_account of this AIMResolveDetail.

        发送的用户名。

        :param send_account: The send_account of this AIMResolveDetail.
        :type send_account: str
        """
        self._send_account = send_account

    @property
    def tpl_id(self):
        """Gets the tpl_id of this AIMResolveDetail.

        智能信息模板ID。

        :return: The tpl_id of this AIMResolveDetail.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        """Sets the tpl_id of this AIMResolveDetail.

        智能信息模板ID。

        :param tpl_id: The tpl_id of this AIMResolveDetail.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def tpl_name(self):
        """Gets the tpl_name of this AIMResolveDetail.

        智能信息模板名称。

        :return: The tpl_name of this AIMResolveDetail.
        :rtype: str
        """
        return self._tpl_name

    @tpl_name.setter
    def tpl_name(self, tpl_name):
        """Sets the tpl_name of this AIMResolveDetail.

        智能信息模板名称。

        :param tpl_name: The tpl_name of this AIMResolveDetail.
        :type tpl_name: str
        """
        self._tpl_name = tpl_name

    @property
    def cust_flag(self):
        """Gets the cust_flag of this AIMResolveDetail.

        创建解析任务时填写用户唯一标识，手机号码或者任何的唯一标识，唯一标识不超过64个字符。发送智能信息时则必须填客户的手机号码。此处为手机号。样例为：130****0001。

        :return: The cust_flag of this AIMResolveDetail.
        :rtype: str
        """
        return self._cust_flag

    @cust_flag.setter
    def cust_flag(self, cust_flag):
        """Sets the cust_flag of this AIMResolveDetail.

        创建解析任务时填写用户唯一标识，手机号码或者任何的唯一标识，唯一标识不超过64个字符。发送智能信息时则必须填客户的手机号码。此处为手机号。样例为：130****0001。

        :param cust_flag: The cust_flag of this AIMResolveDetail.
        :type cust_flag: str
        """
        self._cust_flag = cust_flag

    @property
    def aim_url(self):
        """Gets the aim_url of this AIMResolveDetail.

        智能信息短链，通过自己的短信渠道发送时，需要把该短链添加到短信模板中，并确保发送短信时的签名与创建短链时的签名保持一致。

        :return: The aim_url of this AIMResolveDetail.
        :rtype: str
        """
        return self._aim_url

    @aim_url.setter
    def aim_url(self, aim_url):
        """Sets the aim_url of this AIMResolveDetail.

        智能信息短链，通过自己的短信渠道发送时，需要把该短链添加到短信模板中，并确保发送短信时的签名与创建短链时的签名保持一致。

        :param aim_url: The aim_url of this AIMResolveDetail.
        :type aim_url: str
        """
        self._aim_url = aim_url

    @property
    def result_code(self):
        """Gets the result_code of this AIMResolveDetail.

        短链申请结果返回码。 - 0：成功 - 非0：失败，具体请参见错误码。 

        :return: The result_code of this AIMResolveDetail.
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """Sets the result_code of this AIMResolveDetail.

        短链申请结果返回码。 - 0：成功 - 非0：失败，具体请参见错误码。 

        :param result_code: The result_code of this AIMResolveDetail.
        :type result_code: str
        """
        self._result_code = result_code

    @property
    def generate_date(self):
        """Gets the generate_date of this AIMResolveDetail.

        短链生成时间。样例为：2019-10-12T07:20:50Z。

        :return: The generate_date of this AIMResolveDetail.
        :rtype: str
        """
        return self._generate_date

    @generate_date.setter
    def generate_date(self, generate_date):
        """Sets the generate_date of this AIMResolveDetail.

        短链生成时间。样例为：2019-10-12T07:20:50Z。

        :param generate_date: The generate_date of this AIMResolveDetail.
        :type generate_date: str
        """
        self._generate_date = generate_date

    @property
    def expire_date(self):
        """Gets the expire_date of this AIMResolveDetail.

        短链到期时间。样例为：2019-10-12T07:20:50Z。

        :return: The expire_date of this AIMResolveDetail.
        :rtype: str
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        """Sets the expire_date of this AIMResolveDetail.

        短链到期时间。样例为：2019-10-12T07:20:50Z。

        :param expire_date: The expire_date of this AIMResolveDetail.
        :type expire_date: str
        """
        self._expire_date = expire_date

    @property
    def resolved_time(self):
        """Gets the resolved_time of this AIMResolveDetail.

        解析时间。样例为：2019-10-12T07:20:50Z。

        :return: The resolved_time of this AIMResolveDetail.
        :rtype: str
        """
        return self._resolved_time

    @resolved_time.setter
    def resolved_time(self, resolved_time):
        """Sets the resolved_time of this AIMResolveDetail.

        解析时间。样例为：2019-10-12T07:20:50Z。

        :param resolved_time: The resolved_time of this AIMResolveDetail.
        :type resolved_time: str
        """
        self._resolved_time = resolved_time

    @property
    def resolved_status(self):
        """Gets the resolved_status of this AIMResolveDetail.

        解析状态。 - success：解析成功 - fail：解析失败 - unresolved：未解析 

        :return: The resolved_status of this AIMResolveDetail.
        :rtype: str
        """
        return self._resolved_status

    @resolved_status.setter
    def resolved_status(self, resolved_status):
        """Sets the resolved_status of this AIMResolveDetail.

        解析状态。 - success：解析成功 - fail：解析失败 - unresolved：未解析 

        :param resolved_status: The resolved_status of this AIMResolveDetail.
        :type resolved_status: str
        """
        self._resolved_status = resolved_status

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
        if not isinstance(other, AIMResolveDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
