# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogoffUserSessionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_ids': 'list[str]',
        'message_type': 'int',
        'message': 'str',
        'title': 'str',
        'delay_time': 'int',
        'transaction_id': 'str'
    }

    attribute_map = {
        'session_ids': 'session_ids',
        'message_type': 'message_type',
        'message': 'message',
        'title': 'title',
        'delay_time': 'delay_time',
        'transaction_id': 'transaction_id'
    }

    def __init__(self, session_ids=None, message_type=None, message=None, title=None, delay_time=None, transaction_id=None):
        """LogoffUserSessionReq

        The model defined in huaweicloud sdk

        :param session_ids: 会话信息id列表
        :type session_ids: list[str]
        :param message_type: 客户端弹框级别，代表给会话发消息时的严重程度（比如info、warning、error级别） 0-&gt;info; 1-&gt; warn; 2-&gt;serious;
        :type message_type: int
        :param message: 客户端弹框内容
        :type message: str
        :param title: 弹框标题
        :type title: str
        :param delay_time: 延迟多长时间注销会话
        :type delay_time: int
        :param transaction_id: 事务id，用作客户端日志定位跟踪
        :type transaction_id: str
        """
        
        

        self._session_ids = None
        self._message_type = None
        self._message = None
        self._title = None
        self._delay_time = None
        self._transaction_id = None
        self.discriminator = None

        if session_ids is not None:
            self.session_ids = session_ids
        self.message_type = message_type
        if message is not None:
            self.message = message
        if title is not None:
            self.title = title
        self.delay_time = delay_time
        if transaction_id is not None:
            self.transaction_id = transaction_id

    @property
    def session_ids(self):
        """Gets the session_ids of this LogoffUserSessionReq.

        会话信息id列表

        :return: The session_ids of this LogoffUserSessionReq.
        :rtype: list[str]
        """
        return self._session_ids

    @session_ids.setter
    def session_ids(self, session_ids):
        """Sets the session_ids of this LogoffUserSessionReq.

        会话信息id列表

        :param session_ids: The session_ids of this LogoffUserSessionReq.
        :type session_ids: list[str]
        """
        self._session_ids = session_ids

    @property
    def message_type(self):
        """Gets the message_type of this LogoffUserSessionReq.

        客户端弹框级别，代表给会话发消息时的严重程度（比如info、warning、error级别） 0->info; 1-> warn; 2->serious;

        :return: The message_type of this LogoffUserSessionReq.
        :rtype: int
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this LogoffUserSessionReq.

        客户端弹框级别，代表给会话发消息时的严重程度（比如info、warning、error级别） 0->info; 1-> warn; 2->serious;

        :param message_type: The message_type of this LogoffUserSessionReq.
        :type message_type: int
        """
        self._message_type = message_type

    @property
    def message(self):
        """Gets the message of this LogoffUserSessionReq.

        客户端弹框内容

        :return: The message of this LogoffUserSessionReq.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this LogoffUserSessionReq.

        客户端弹框内容

        :param message: The message of this LogoffUserSessionReq.
        :type message: str
        """
        self._message = message

    @property
    def title(self):
        """Gets the title of this LogoffUserSessionReq.

        弹框标题

        :return: The title of this LogoffUserSessionReq.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LogoffUserSessionReq.

        弹框标题

        :param title: The title of this LogoffUserSessionReq.
        :type title: str
        """
        self._title = title

    @property
    def delay_time(self):
        """Gets the delay_time of this LogoffUserSessionReq.

        延迟多长时间注销会话

        :return: The delay_time of this LogoffUserSessionReq.
        :rtype: int
        """
        return self._delay_time

    @delay_time.setter
    def delay_time(self, delay_time):
        """Sets the delay_time of this LogoffUserSessionReq.

        延迟多长时间注销会话

        :param delay_time: The delay_time of this LogoffUserSessionReq.
        :type delay_time: int
        """
        self._delay_time = delay_time

    @property
    def transaction_id(self):
        """Gets the transaction_id of this LogoffUserSessionReq.

        事务id，用作客户端日志定位跟踪

        :return: The transaction_id of this LogoffUserSessionReq.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this LogoffUserSessionReq.

        事务id，用作客户端日志定位跟踪

        :param transaction_id: The transaction_id of this LogoffUserSessionReq.
        :type transaction_id: str
        """
        self._transaction_id = transaction_id

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
        if not isinstance(other, LogoffUserSessionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
