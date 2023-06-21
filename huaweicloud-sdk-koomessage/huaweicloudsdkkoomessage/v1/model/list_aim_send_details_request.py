# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAimSendDetailsRequest:

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
        'tpl_id': 'str',
        'sms_sign': 'str',
        'cust_flag': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'tpl_id': 'tpl_id',
        'sms_sign': 'sms_sign',
        'cust_flag': 'cust_flag',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, task_id=None, tpl_id=None, sms_sign=None, cust_flag=None, begin_time=None, end_time=None, offset=None, limit=None):
        """ListAimSendDetailsRequest

        The model defined in huaweicloud sdk

        :param task_id: 任务ID。
        :type task_id: str
        :param tpl_id: 智能信息模板ID。
        :type tpl_id: str
        :param sms_sign: 签名。
        :type sms_sign: str
        :param cust_flag: 创建解析任务时填写用户唯一标识。  &gt; 手机号码或者任何的唯一标识，唯一标识不超过64个字符。发送智能信息时则必须填客户的手机号码。此处为手机号。样例为：130****0001。 
        :type cust_flag: str
        :param begin_time:  发送开始时间。格式为：2019-10-12T07:20:50Z。  &gt; 需同时传入end_time才能生效，单独传begin_time不会作为过滤条件。 
        :type begin_time: str
        :param end_time: 发送结束时间。格式为：2019-10-12T07:20:50Z。  &gt; 需同时传入begin_time才能生效，单独传end_time不会作为过滤条件。 
        :type end_time: str
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0。  &gt;为提高查询效率，offset+limit须小于等于10000，超出范围查询为空。 
        :type offset: int
        :param limit: 每页显示的条目数量。 
        :type limit: int
        """
        
        

        self._task_id = None
        self._tpl_id = None
        self._sms_sign = None
        self._cust_flag = None
        self._begin_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if tpl_id is not None:
            self.tpl_id = tpl_id
        if sms_sign is not None:
            self.sms_sign = sms_sign
        if cust_flag is not None:
            self.cust_flag = cust_flag
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        self.offset = offset
        self.limit = limit

    @property
    def task_id(self):
        """Gets the task_id of this ListAimSendDetailsRequest.

        任务ID。

        :return: The task_id of this ListAimSendDetailsRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ListAimSendDetailsRequest.

        任务ID。

        :param task_id: The task_id of this ListAimSendDetailsRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def tpl_id(self):
        """Gets the tpl_id of this ListAimSendDetailsRequest.

        智能信息模板ID。

        :return: The tpl_id of this ListAimSendDetailsRequest.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        """Sets the tpl_id of this ListAimSendDetailsRequest.

        智能信息模板ID。

        :param tpl_id: The tpl_id of this ListAimSendDetailsRequest.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def sms_sign(self):
        """Gets the sms_sign of this ListAimSendDetailsRequest.

        签名。

        :return: The sms_sign of this ListAimSendDetailsRequest.
        :rtype: str
        """
        return self._sms_sign

    @sms_sign.setter
    def sms_sign(self, sms_sign):
        """Sets the sms_sign of this ListAimSendDetailsRequest.

        签名。

        :param sms_sign: The sms_sign of this ListAimSendDetailsRequest.
        :type sms_sign: str
        """
        self._sms_sign = sms_sign

    @property
    def cust_flag(self):
        """Gets the cust_flag of this ListAimSendDetailsRequest.

        创建解析任务时填写用户唯一标识。  > 手机号码或者任何的唯一标识，唯一标识不超过64个字符。发送智能信息时则必须填客户的手机号码。此处为手机号。样例为：130****0001。 

        :return: The cust_flag of this ListAimSendDetailsRequest.
        :rtype: str
        """
        return self._cust_flag

    @cust_flag.setter
    def cust_flag(self, cust_flag):
        """Sets the cust_flag of this ListAimSendDetailsRequest.

        创建解析任务时填写用户唯一标识。  > 手机号码或者任何的唯一标识，唯一标识不超过64个字符。发送智能信息时则必须填客户的手机号码。此处为手机号。样例为：130****0001。 

        :param cust_flag: The cust_flag of this ListAimSendDetailsRequest.
        :type cust_flag: str
        """
        self._cust_flag = cust_flag

    @property
    def begin_time(self):
        """Gets the begin_time of this ListAimSendDetailsRequest.

         发送开始时间。格式为：2019-10-12T07:20:50Z。  > 需同时传入end_time才能生效，单独传begin_time不会作为过滤条件。 

        :return: The begin_time of this ListAimSendDetailsRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ListAimSendDetailsRequest.

         发送开始时间。格式为：2019-10-12T07:20:50Z。  > 需同时传入end_time才能生效，单独传begin_time不会作为过滤条件。 

        :param begin_time: The begin_time of this ListAimSendDetailsRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ListAimSendDetailsRequest.

        发送结束时间。格式为：2019-10-12T07:20:50Z。  > 需同时传入begin_time才能生效，单独传end_time不会作为过滤条件。 

        :return: The end_time of this ListAimSendDetailsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListAimSendDetailsRequest.

        发送结束时间。格式为：2019-10-12T07:20:50Z。  > 需同时传入begin_time才能生效，单独传end_time不会作为过滤条件。 

        :param end_time: The end_time of this ListAimSendDetailsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def offset(self):
        """Gets the offset of this ListAimSendDetailsRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。  >为提高查询效率，offset+limit须小于等于10000，超出范围查询为空。 

        :return: The offset of this ListAimSendDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAimSendDetailsRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。  >为提高查询效率，offset+limit须小于等于10000，超出范围查询为空。 

        :param offset: The offset of this ListAimSendDetailsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListAimSendDetailsRequest.

        每页显示的条目数量。 

        :return: The limit of this ListAimSendDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAimSendDetailsRequest.

        每页显示的条目数量。 

        :param limit: The limit of this ListAimSendDetailsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListAimSendDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
