# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMessageTraceRespTrace:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'bool',
        'trace_type': 'str',
        'timestamp': 'float',
        'group_name': 'str',
        'cost_time': 'float',
        'request_id': 'str',
        'consume_status': 'float',
        'topic': 'str',
        'msg_id': 'str',
        'offset_msg_id': 'str',
        'tags': 'str',
        'keys': 'str',
        'store_host': 'str',
        'client_host': 'str',
        'retry_times': 'int',
        'body_length': 'float',
        'msg_type': 'str',
        'transaction_state': 'str',
        'transaction_id': 'str',
        'from_transaction_check': 'bool'
    }

    attribute_map = {
        'success': 'success',
        'trace_type': 'trace_type',
        'timestamp': 'timestamp',
        'group_name': 'group_name',
        'cost_time': 'cost_time',
        'request_id': 'request_id',
        'consume_status': 'consume_status',
        'topic': 'topic',
        'msg_id': 'msg_id',
        'offset_msg_id': 'offset_msg_id',
        'tags': 'tags',
        'keys': 'keys',
        'store_host': 'store_host',
        'client_host': 'client_host',
        'retry_times': 'retry_times',
        'body_length': 'body_length',
        'msg_type': 'msg_type',
        'transaction_state': 'transaction_state',
        'transaction_id': 'transaction_id',
        'from_transaction_check': 'from_transaction_check'
    }

    def __init__(self, success=None, trace_type=None, timestamp=None, group_name=None, cost_time=None, request_id=None, consume_status=None, topic=None, msg_id=None, offset_msg_id=None, tags=None, keys=None, store_host=None, client_host=None, retry_times=None, body_length=None, msg_type=None, transaction_state=None, transaction_id=None, from_transaction_check=None):
        r"""ListMessageTraceRespTrace

        The model defined in huaweicloud sdk

        :param success: 是否成功。
        :type success: bool
        :param trace_type: 轨迹类型
        :type trace_type: str
        :param timestamp: 时间。
        :type timestamp: float
        :param group_name: 生产组或消费组。
        :type group_name: str
        :param cost_time: 耗时。
        :type cost_time: float
        :param request_id: 请求ID。
        :type request_id: str
        :param consume_status: 消费状态：  - 0-消费成功  - 1-消费超时  - 2-消费发生异常   - 3-消费返回NULL  - 5-消费失败
        :type consume_status: float
        :param topic: 主题名称。
        :type topic: str
        :param msg_id: 消息ID。
        :type msg_id: str
        :param offset_msg_id: offset消息ID。
        :type offset_msg_id: str
        :param tags: 消息的标签。
        :type tags: str
        :param keys: 消息的keys。
        :type keys: str
        :param store_host: 存储消息的主机IP。
        :type store_host: str
        :param client_host: 产生消息的主机IP。
        :type client_host: str
        :param retry_times: 重试次数。
        :type retry_times: int
        :param body_length: 消息体长度。
        :type body_length: float
        :param msg_type: 消息类型。
        :type msg_type: str
        :param transaction_state: 事务状态。
        :type transaction_state: str
        :param transaction_id: 事务ID。
        :type transaction_id: str
        :param from_transaction_check: 是否为事务回查的响应。
        :type from_transaction_check: bool
        """
        
        

        self._success = None
        self._trace_type = None
        self._timestamp = None
        self._group_name = None
        self._cost_time = None
        self._request_id = None
        self._consume_status = None
        self._topic = None
        self._msg_id = None
        self._offset_msg_id = None
        self._tags = None
        self._keys = None
        self._store_host = None
        self._client_host = None
        self._retry_times = None
        self._body_length = None
        self._msg_type = None
        self._transaction_state = None
        self._transaction_id = None
        self._from_transaction_check = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if trace_type is not None:
            self.trace_type = trace_type
        if timestamp is not None:
            self.timestamp = timestamp
        if group_name is not None:
            self.group_name = group_name
        if cost_time is not None:
            self.cost_time = cost_time
        if request_id is not None:
            self.request_id = request_id
        if consume_status is not None:
            self.consume_status = consume_status
        if topic is not None:
            self.topic = topic
        if msg_id is not None:
            self.msg_id = msg_id
        if offset_msg_id is not None:
            self.offset_msg_id = offset_msg_id
        if tags is not None:
            self.tags = tags
        if keys is not None:
            self.keys = keys
        if store_host is not None:
            self.store_host = store_host
        if client_host is not None:
            self.client_host = client_host
        if retry_times is not None:
            self.retry_times = retry_times
        if body_length is not None:
            self.body_length = body_length
        if msg_type is not None:
            self.msg_type = msg_type
        if transaction_state is not None:
            self.transaction_state = transaction_state
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if from_transaction_check is not None:
            self.from_transaction_check = from_transaction_check

    @property
    def success(self):
        r"""Gets the success of this ListMessageTraceRespTrace.

        是否成功。

        :return: The success of this ListMessageTraceRespTrace.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ListMessageTraceRespTrace.

        是否成功。

        :param success: The success of this ListMessageTraceRespTrace.
        :type success: bool
        """
        self._success = success

    @property
    def trace_type(self):
        r"""Gets the trace_type of this ListMessageTraceRespTrace.

        轨迹类型

        :return: The trace_type of this ListMessageTraceRespTrace.
        :rtype: str
        """
        return self._trace_type

    @trace_type.setter
    def trace_type(self, trace_type):
        r"""Sets the trace_type of this ListMessageTraceRespTrace.

        轨迹类型

        :param trace_type: The trace_type of this ListMessageTraceRespTrace.
        :type trace_type: str
        """
        self._trace_type = trace_type

    @property
    def timestamp(self):
        r"""Gets the timestamp of this ListMessageTraceRespTrace.

        时间。

        :return: The timestamp of this ListMessageTraceRespTrace.
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this ListMessageTraceRespTrace.

        时间。

        :param timestamp: The timestamp of this ListMessageTraceRespTrace.
        :type timestamp: float
        """
        self._timestamp = timestamp

    @property
    def group_name(self):
        r"""Gets the group_name of this ListMessageTraceRespTrace.

        生产组或消费组。

        :return: The group_name of this ListMessageTraceRespTrace.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ListMessageTraceRespTrace.

        生产组或消费组。

        :param group_name: The group_name of this ListMessageTraceRespTrace.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def cost_time(self):
        r"""Gets the cost_time of this ListMessageTraceRespTrace.

        耗时。

        :return: The cost_time of this ListMessageTraceRespTrace.
        :rtype: float
        """
        return self._cost_time

    @cost_time.setter
    def cost_time(self, cost_time):
        r"""Sets the cost_time of this ListMessageTraceRespTrace.

        耗时。

        :param cost_time: The cost_time of this ListMessageTraceRespTrace.
        :type cost_time: float
        """
        self._cost_time = cost_time

    @property
    def request_id(self):
        r"""Gets the request_id of this ListMessageTraceRespTrace.

        请求ID。

        :return: The request_id of this ListMessageTraceRespTrace.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListMessageTraceRespTrace.

        请求ID。

        :param request_id: The request_id of this ListMessageTraceRespTrace.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def consume_status(self):
        r"""Gets the consume_status of this ListMessageTraceRespTrace.

        消费状态：  - 0-消费成功  - 1-消费超时  - 2-消费发生异常   - 3-消费返回NULL  - 5-消费失败

        :return: The consume_status of this ListMessageTraceRespTrace.
        :rtype: float
        """
        return self._consume_status

    @consume_status.setter
    def consume_status(self, consume_status):
        r"""Sets the consume_status of this ListMessageTraceRespTrace.

        消费状态：  - 0-消费成功  - 1-消费超时  - 2-消费发生异常   - 3-消费返回NULL  - 5-消费失败

        :param consume_status: The consume_status of this ListMessageTraceRespTrace.
        :type consume_status: float
        """
        self._consume_status = consume_status

    @property
    def topic(self):
        r"""Gets the topic of this ListMessageTraceRespTrace.

        主题名称。

        :return: The topic of this ListMessageTraceRespTrace.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this ListMessageTraceRespTrace.

        主题名称。

        :param topic: The topic of this ListMessageTraceRespTrace.
        :type topic: str
        """
        self._topic = topic

    @property
    def msg_id(self):
        r"""Gets the msg_id of this ListMessageTraceRespTrace.

        消息ID。

        :return: The msg_id of this ListMessageTraceRespTrace.
        :rtype: str
        """
        return self._msg_id

    @msg_id.setter
    def msg_id(self, msg_id):
        r"""Sets the msg_id of this ListMessageTraceRespTrace.

        消息ID。

        :param msg_id: The msg_id of this ListMessageTraceRespTrace.
        :type msg_id: str
        """
        self._msg_id = msg_id

    @property
    def offset_msg_id(self):
        r"""Gets the offset_msg_id of this ListMessageTraceRespTrace.

        offset消息ID。

        :return: The offset_msg_id of this ListMessageTraceRespTrace.
        :rtype: str
        """
        return self._offset_msg_id

    @offset_msg_id.setter
    def offset_msg_id(self, offset_msg_id):
        r"""Sets the offset_msg_id of this ListMessageTraceRespTrace.

        offset消息ID。

        :param offset_msg_id: The offset_msg_id of this ListMessageTraceRespTrace.
        :type offset_msg_id: str
        """
        self._offset_msg_id = offset_msg_id

    @property
    def tags(self):
        r"""Gets the tags of this ListMessageTraceRespTrace.

        消息的标签。

        :return: The tags of this ListMessageTraceRespTrace.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListMessageTraceRespTrace.

        消息的标签。

        :param tags: The tags of this ListMessageTraceRespTrace.
        :type tags: str
        """
        self._tags = tags

    @property
    def keys(self):
        r"""Gets the keys of this ListMessageTraceRespTrace.

        消息的keys。

        :return: The keys of this ListMessageTraceRespTrace.
        :rtype: str
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        r"""Sets the keys of this ListMessageTraceRespTrace.

        消息的keys。

        :param keys: The keys of this ListMessageTraceRespTrace.
        :type keys: str
        """
        self._keys = keys

    @property
    def store_host(self):
        r"""Gets the store_host of this ListMessageTraceRespTrace.

        存储消息的主机IP。

        :return: The store_host of this ListMessageTraceRespTrace.
        :rtype: str
        """
        return self._store_host

    @store_host.setter
    def store_host(self, store_host):
        r"""Sets the store_host of this ListMessageTraceRespTrace.

        存储消息的主机IP。

        :param store_host: The store_host of this ListMessageTraceRespTrace.
        :type store_host: str
        """
        self._store_host = store_host

    @property
    def client_host(self):
        r"""Gets the client_host of this ListMessageTraceRespTrace.

        产生消息的主机IP。

        :return: The client_host of this ListMessageTraceRespTrace.
        :rtype: str
        """
        return self._client_host

    @client_host.setter
    def client_host(self, client_host):
        r"""Sets the client_host of this ListMessageTraceRespTrace.

        产生消息的主机IP。

        :param client_host: The client_host of this ListMessageTraceRespTrace.
        :type client_host: str
        """
        self._client_host = client_host

    @property
    def retry_times(self):
        r"""Gets the retry_times of this ListMessageTraceRespTrace.

        重试次数。

        :return: The retry_times of this ListMessageTraceRespTrace.
        :rtype: int
        """
        return self._retry_times

    @retry_times.setter
    def retry_times(self, retry_times):
        r"""Sets the retry_times of this ListMessageTraceRespTrace.

        重试次数。

        :param retry_times: The retry_times of this ListMessageTraceRespTrace.
        :type retry_times: int
        """
        self._retry_times = retry_times

    @property
    def body_length(self):
        r"""Gets the body_length of this ListMessageTraceRespTrace.

        消息体长度。

        :return: The body_length of this ListMessageTraceRespTrace.
        :rtype: float
        """
        return self._body_length

    @body_length.setter
    def body_length(self, body_length):
        r"""Sets the body_length of this ListMessageTraceRespTrace.

        消息体长度。

        :param body_length: The body_length of this ListMessageTraceRespTrace.
        :type body_length: float
        """
        self._body_length = body_length

    @property
    def msg_type(self):
        r"""Gets the msg_type of this ListMessageTraceRespTrace.

        消息类型。

        :return: The msg_type of this ListMessageTraceRespTrace.
        :rtype: str
        """
        return self._msg_type

    @msg_type.setter
    def msg_type(self, msg_type):
        r"""Sets the msg_type of this ListMessageTraceRespTrace.

        消息类型。

        :param msg_type: The msg_type of this ListMessageTraceRespTrace.
        :type msg_type: str
        """
        self._msg_type = msg_type

    @property
    def transaction_state(self):
        r"""Gets the transaction_state of this ListMessageTraceRespTrace.

        事务状态。

        :return: The transaction_state of this ListMessageTraceRespTrace.
        :rtype: str
        """
        return self._transaction_state

    @transaction_state.setter
    def transaction_state(self, transaction_state):
        r"""Sets the transaction_state of this ListMessageTraceRespTrace.

        事务状态。

        :param transaction_state: The transaction_state of this ListMessageTraceRespTrace.
        :type transaction_state: str
        """
        self._transaction_state = transaction_state

    @property
    def transaction_id(self):
        r"""Gets the transaction_id of this ListMessageTraceRespTrace.

        事务ID。

        :return: The transaction_id of this ListMessageTraceRespTrace.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        r"""Sets the transaction_id of this ListMessageTraceRespTrace.

        事务ID。

        :param transaction_id: The transaction_id of this ListMessageTraceRespTrace.
        :type transaction_id: str
        """
        self._transaction_id = transaction_id

    @property
    def from_transaction_check(self):
        r"""Gets the from_transaction_check of this ListMessageTraceRespTrace.

        是否为事务回查的响应。

        :return: The from_transaction_check of this ListMessageTraceRespTrace.
        :rtype: bool
        """
        return self._from_transaction_check

    @from_transaction_check.setter
    def from_transaction_check(self, from_transaction_check):
        r"""Sets the from_transaction_check of this ListMessageTraceRespTrace.

        是否为事务回查的响应。

        :param from_transaction_check: The from_transaction_check of this ListMessageTraceRespTrace.
        :type from_transaction_check: bool
        """
        self._from_transaction_check = from_transaction_check

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
        if not isinstance(other, ListMessageTraceRespTrace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
