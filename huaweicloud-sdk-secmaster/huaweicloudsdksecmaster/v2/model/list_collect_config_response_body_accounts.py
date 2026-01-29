# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCollectConfigResponseBodyAccounts:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_id': 'str',
        'last_log_date': 'float',
        'log_count': 'str',
        'name': 'str',
        'process_status': 'str',
        'sink_msg': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'last_log_date': 'last_log_date',
        'log_count': 'log_count',
        'name': 'name',
        'process_status': 'process_status',
        'sink_msg': 'sink_msg'
    }

    def __init__(self, account_id=None, last_log_date=None, log_count=None, name=None, process_status=None, sink_msg=None):
        r"""ListCollectConfigResponseBodyAccounts

        The model defined in huaweicloud sdk

        :param account_id: 账号ID
        :type account_id: str
        :param last_log_date: 最近接入时间
        :type last_log_date: float
        :param log_count: 最近一小时接入数量
        :type log_count: str
        :param name: 账号名称
        :type name: str
        :param process_status: 接入状态
        :type process_status: str
        :param sink_msg: 错误信息
        :type sink_msg: str
        """
        
        

        self._account_id = None
        self._last_log_date = None
        self._log_count = None
        self._name = None
        self._process_status = None
        self._sink_msg = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if last_log_date is not None:
            self.last_log_date = last_log_date
        if log_count is not None:
            self.log_count = log_count
        if name is not None:
            self.name = name
        if process_status is not None:
            self.process_status = process_status
        if sink_msg is not None:
            self.sink_msg = sink_msg

    @property
    def account_id(self):
        r"""Gets the account_id of this ListCollectConfigResponseBodyAccounts.

        账号ID

        :return: The account_id of this ListCollectConfigResponseBodyAccounts.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this ListCollectConfigResponseBodyAccounts.

        账号ID

        :param account_id: The account_id of this ListCollectConfigResponseBodyAccounts.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def last_log_date(self):
        r"""Gets the last_log_date of this ListCollectConfigResponseBodyAccounts.

        最近接入时间

        :return: The last_log_date of this ListCollectConfigResponseBodyAccounts.
        :rtype: float
        """
        return self._last_log_date

    @last_log_date.setter
    def last_log_date(self, last_log_date):
        r"""Sets the last_log_date of this ListCollectConfigResponseBodyAccounts.

        最近接入时间

        :param last_log_date: The last_log_date of this ListCollectConfigResponseBodyAccounts.
        :type last_log_date: float
        """
        self._last_log_date = last_log_date

    @property
    def log_count(self):
        r"""Gets the log_count of this ListCollectConfigResponseBodyAccounts.

        最近一小时接入数量

        :return: The log_count of this ListCollectConfigResponseBodyAccounts.
        :rtype: str
        """
        return self._log_count

    @log_count.setter
    def log_count(self, log_count):
        r"""Sets the log_count of this ListCollectConfigResponseBodyAccounts.

        最近一小时接入数量

        :param log_count: The log_count of this ListCollectConfigResponseBodyAccounts.
        :type log_count: str
        """
        self._log_count = log_count

    @property
    def name(self):
        r"""Gets the name of this ListCollectConfigResponseBodyAccounts.

        账号名称

        :return: The name of this ListCollectConfigResponseBodyAccounts.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListCollectConfigResponseBodyAccounts.

        账号名称

        :param name: The name of this ListCollectConfigResponseBodyAccounts.
        :type name: str
        """
        self._name = name

    @property
    def process_status(self):
        r"""Gets the process_status of this ListCollectConfigResponseBodyAccounts.

        接入状态

        :return: The process_status of this ListCollectConfigResponseBodyAccounts.
        :rtype: str
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        r"""Sets the process_status of this ListCollectConfigResponseBodyAccounts.

        接入状态

        :param process_status: The process_status of this ListCollectConfigResponseBodyAccounts.
        :type process_status: str
        """
        self._process_status = process_status

    @property
    def sink_msg(self):
        r"""Gets the sink_msg of this ListCollectConfigResponseBodyAccounts.

        错误信息

        :return: The sink_msg of this ListCollectConfigResponseBodyAccounts.
        :rtype: str
        """
        return self._sink_msg

    @sink_msg.setter
    def sink_msg(self, sink_msg):
        r"""Sets the sink_msg of this ListCollectConfigResponseBodyAccounts.

        错误信息

        :param sink_msg: The sink_msg of this ListCollectConfigResponseBodyAccounts.
        :type sink_msg: str
        """
        self._sink_msg = sink_msg

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListCollectConfigResponseBodyAccounts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
