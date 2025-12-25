# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCollectConfigResponseBodyDataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_all_num': 'float',
        'account_successful_num': 'float',
        'csvc': 'str',
        'datasets': 'list[ListCollectConfigResponseBodyDatasets]',
        'last_modified_time': 'float',
        'log_all_num': 'float',
        'log_in_num': 'float',
        'log_in_num_last_one_hour': 'float',
        'process_status': 'str',
        'vendor': 'str'
    }

    attribute_map = {
        'account_all_num': 'account_all_num',
        'account_successful_num': 'account_successful_num',
        'csvc': 'csvc',
        'datasets': 'datasets',
        'last_modified_time': 'last_modified_time',
        'log_all_num': 'log_all_num',
        'log_in_num': 'log_in_num',
        'log_in_num_last_one_hour': 'log_in_num_last_one_hour',
        'process_status': 'process_status',
        'vendor': 'vendor'
    }

    def __init__(self, account_all_num=None, account_successful_num=None, csvc=None, datasets=None, last_modified_time=None, log_all_num=None, log_in_num=None, log_in_num_last_one_hour=None, process_status=None, vendor=None):
        r"""ListCollectConfigResponseBodyDataList

        The model defined in huaweicloud sdk

        :param account_all_num: 接入账号总数量
        :type account_all_num: float
        :param account_successful_num: 成功接入账号数量
        :type account_successful_num: float
        :param csvc: 云产品ID
        :type csvc: str
        :param datasets: 日志数据
        :type datasets: list[:class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyDatasets`]
        :param last_modified_time: 上次修改时间
        :type last_modified_time: float
        :param log_all_num: 日志总数量
        :type log_all_num: float
        :param log_in_num: 接入日志数量
        :type log_in_num: float
        :param log_in_num_last_one_hour: 过去一个小时接入
        :type log_in_num_last_one_hour: float
        :param process_status: 状态
        :type process_status: str
        :param vendor: 云厂商ID
        :type vendor: str
        """
        
        

        self._account_all_num = None
        self._account_successful_num = None
        self._csvc = None
        self._datasets = None
        self._last_modified_time = None
        self._log_all_num = None
        self._log_in_num = None
        self._log_in_num_last_one_hour = None
        self._process_status = None
        self._vendor = None
        self.discriminator = None

        if account_all_num is not None:
            self.account_all_num = account_all_num
        if account_successful_num is not None:
            self.account_successful_num = account_successful_num
        if csvc is not None:
            self.csvc = csvc
        if datasets is not None:
            self.datasets = datasets
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if log_all_num is not None:
            self.log_all_num = log_all_num
        if log_in_num is not None:
            self.log_in_num = log_in_num
        if log_in_num_last_one_hour is not None:
            self.log_in_num_last_one_hour = log_in_num_last_one_hour
        if process_status is not None:
            self.process_status = process_status
        if vendor is not None:
            self.vendor = vendor

    @property
    def account_all_num(self):
        r"""Gets the account_all_num of this ListCollectConfigResponseBodyDataList.

        接入账号总数量

        :return: The account_all_num of this ListCollectConfigResponseBodyDataList.
        :rtype: float
        """
        return self._account_all_num

    @account_all_num.setter
    def account_all_num(self, account_all_num):
        r"""Sets the account_all_num of this ListCollectConfigResponseBodyDataList.

        接入账号总数量

        :param account_all_num: The account_all_num of this ListCollectConfigResponseBodyDataList.
        :type account_all_num: float
        """
        self._account_all_num = account_all_num

    @property
    def account_successful_num(self):
        r"""Gets the account_successful_num of this ListCollectConfigResponseBodyDataList.

        成功接入账号数量

        :return: The account_successful_num of this ListCollectConfigResponseBodyDataList.
        :rtype: float
        """
        return self._account_successful_num

    @account_successful_num.setter
    def account_successful_num(self, account_successful_num):
        r"""Sets the account_successful_num of this ListCollectConfigResponseBodyDataList.

        成功接入账号数量

        :param account_successful_num: The account_successful_num of this ListCollectConfigResponseBodyDataList.
        :type account_successful_num: float
        """
        self._account_successful_num = account_successful_num

    @property
    def csvc(self):
        r"""Gets the csvc of this ListCollectConfigResponseBodyDataList.

        云产品ID

        :return: The csvc of this ListCollectConfigResponseBodyDataList.
        :rtype: str
        """
        return self._csvc

    @csvc.setter
    def csvc(self, csvc):
        r"""Sets the csvc of this ListCollectConfigResponseBodyDataList.

        云产品ID

        :param csvc: The csvc of this ListCollectConfigResponseBodyDataList.
        :type csvc: str
        """
        self._csvc = csvc

    @property
    def datasets(self):
        r"""Gets the datasets of this ListCollectConfigResponseBodyDataList.

        日志数据

        :return: The datasets of this ListCollectConfigResponseBodyDataList.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyDatasets`]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        r"""Sets the datasets of this ListCollectConfigResponseBodyDataList.

        日志数据

        :param datasets: The datasets of this ListCollectConfigResponseBodyDataList.
        :type datasets: list[:class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyDatasets`]
        """
        self._datasets = datasets

    @property
    def last_modified_time(self):
        r"""Gets the last_modified_time of this ListCollectConfigResponseBodyDataList.

        上次修改时间

        :return: The last_modified_time of this ListCollectConfigResponseBodyDataList.
        :rtype: float
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        r"""Sets the last_modified_time of this ListCollectConfigResponseBodyDataList.

        上次修改时间

        :param last_modified_time: The last_modified_time of this ListCollectConfigResponseBodyDataList.
        :type last_modified_time: float
        """
        self._last_modified_time = last_modified_time

    @property
    def log_all_num(self):
        r"""Gets the log_all_num of this ListCollectConfigResponseBodyDataList.

        日志总数量

        :return: The log_all_num of this ListCollectConfigResponseBodyDataList.
        :rtype: float
        """
        return self._log_all_num

    @log_all_num.setter
    def log_all_num(self, log_all_num):
        r"""Sets the log_all_num of this ListCollectConfigResponseBodyDataList.

        日志总数量

        :param log_all_num: The log_all_num of this ListCollectConfigResponseBodyDataList.
        :type log_all_num: float
        """
        self._log_all_num = log_all_num

    @property
    def log_in_num(self):
        r"""Gets the log_in_num of this ListCollectConfigResponseBodyDataList.

        接入日志数量

        :return: The log_in_num of this ListCollectConfigResponseBodyDataList.
        :rtype: float
        """
        return self._log_in_num

    @log_in_num.setter
    def log_in_num(self, log_in_num):
        r"""Sets the log_in_num of this ListCollectConfigResponseBodyDataList.

        接入日志数量

        :param log_in_num: The log_in_num of this ListCollectConfigResponseBodyDataList.
        :type log_in_num: float
        """
        self._log_in_num = log_in_num

    @property
    def log_in_num_last_one_hour(self):
        r"""Gets the log_in_num_last_one_hour of this ListCollectConfigResponseBodyDataList.

        过去一个小时接入

        :return: The log_in_num_last_one_hour of this ListCollectConfigResponseBodyDataList.
        :rtype: float
        """
        return self._log_in_num_last_one_hour

    @log_in_num_last_one_hour.setter
    def log_in_num_last_one_hour(self, log_in_num_last_one_hour):
        r"""Sets the log_in_num_last_one_hour of this ListCollectConfigResponseBodyDataList.

        过去一个小时接入

        :param log_in_num_last_one_hour: The log_in_num_last_one_hour of this ListCollectConfigResponseBodyDataList.
        :type log_in_num_last_one_hour: float
        """
        self._log_in_num_last_one_hour = log_in_num_last_one_hour

    @property
    def process_status(self):
        r"""Gets the process_status of this ListCollectConfigResponseBodyDataList.

        状态

        :return: The process_status of this ListCollectConfigResponseBodyDataList.
        :rtype: str
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        r"""Sets the process_status of this ListCollectConfigResponseBodyDataList.

        状态

        :param process_status: The process_status of this ListCollectConfigResponseBodyDataList.
        :type process_status: str
        """
        self._process_status = process_status

    @property
    def vendor(self):
        r"""Gets the vendor of this ListCollectConfigResponseBodyDataList.

        云厂商ID

        :return: The vendor of this ListCollectConfigResponseBodyDataList.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this ListCollectConfigResponseBodyDataList.

        云厂商ID

        :param vendor: The vendor of this ListCollectConfigResponseBodyDataList.
        :type vendor: str
        """
        self._vendor = vendor

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
        if not isinstance(other, ListCollectConfigResponseBodyDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
