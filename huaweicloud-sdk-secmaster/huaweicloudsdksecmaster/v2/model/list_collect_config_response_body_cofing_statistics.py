# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCollectConfigResponseBodyCofingStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_num': 'float',
        'daily_traffic': 'float',
        'log_num': 'float',
        'product_all_num': 'float',
        'product_in_num': 'float',
        'vendor_num': 'float'
    }

    attribute_map = {
        'account_num': 'account_num',
        'daily_traffic': 'daily_traffic',
        'log_num': 'log_num',
        'product_all_num': 'product_all_num',
        'product_in_num': 'product_in_num',
        'vendor_num': 'vendor_num'
    }

    def __init__(self, account_num=None, daily_traffic=None, log_num=None, product_all_num=None, product_in_num=None, vendor_num=None):
        r"""ListCollectConfigResponseBodyCofingStatistics

        The model defined in huaweicloud sdk

        :param account_num: 账号接入数量
        :type account_num: float
        :param daily_traffic: 每日流量，单位：Byte
        :type daily_traffic: float
        :param log_num: 已接入日志数量
        :type log_num: float
        :param product_all_num: 云产品总数量
        :type product_all_num: float
        :param product_in_num: 接入云产品数量
        :type product_in_num: float
        :param vendor_num: 云厂商数量
        :type vendor_num: float
        """
        
        

        self._account_num = None
        self._daily_traffic = None
        self._log_num = None
        self._product_all_num = None
        self._product_in_num = None
        self._vendor_num = None
        self.discriminator = None

        if account_num is not None:
            self.account_num = account_num
        if daily_traffic is not None:
            self.daily_traffic = daily_traffic
        if log_num is not None:
            self.log_num = log_num
        if product_all_num is not None:
            self.product_all_num = product_all_num
        if product_in_num is not None:
            self.product_in_num = product_in_num
        if vendor_num is not None:
            self.vendor_num = vendor_num

    @property
    def account_num(self):
        r"""Gets the account_num of this ListCollectConfigResponseBodyCofingStatistics.

        账号接入数量

        :return: The account_num of this ListCollectConfigResponseBodyCofingStatistics.
        :rtype: float
        """
        return self._account_num

    @account_num.setter
    def account_num(self, account_num):
        r"""Sets the account_num of this ListCollectConfigResponseBodyCofingStatistics.

        账号接入数量

        :param account_num: The account_num of this ListCollectConfigResponseBodyCofingStatistics.
        :type account_num: float
        """
        self._account_num = account_num

    @property
    def daily_traffic(self):
        r"""Gets the daily_traffic of this ListCollectConfigResponseBodyCofingStatistics.

        每日流量，单位：Byte

        :return: The daily_traffic of this ListCollectConfigResponseBodyCofingStatistics.
        :rtype: float
        """
        return self._daily_traffic

    @daily_traffic.setter
    def daily_traffic(self, daily_traffic):
        r"""Sets the daily_traffic of this ListCollectConfigResponseBodyCofingStatistics.

        每日流量，单位：Byte

        :param daily_traffic: The daily_traffic of this ListCollectConfigResponseBodyCofingStatistics.
        :type daily_traffic: float
        """
        self._daily_traffic = daily_traffic

    @property
    def log_num(self):
        r"""Gets the log_num of this ListCollectConfigResponseBodyCofingStatistics.

        已接入日志数量

        :return: The log_num of this ListCollectConfigResponseBodyCofingStatistics.
        :rtype: float
        """
        return self._log_num

    @log_num.setter
    def log_num(self, log_num):
        r"""Sets the log_num of this ListCollectConfigResponseBodyCofingStatistics.

        已接入日志数量

        :param log_num: The log_num of this ListCollectConfigResponseBodyCofingStatistics.
        :type log_num: float
        """
        self._log_num = log_num

    @property
    def product_all_num(self):
        r"""Gets the product_all_num of this ListCollectConfigResponseBodyCofingStatistics.

        云产品总数量

        :return: The product_all_num of this ListCollectConfigResponseBodyCofingStatistics.
        :rtype: float
        """
        return self._product_all_num

    @product_all_num.setter
    def product_all_num(self, product_all_num):
        r"""Sets the product_all_num of this ListCollectConfigResponseBodyCofingStatistics.

        云产品总数量

        :param product_all_num: The product_all_num of this ListCollectConfigResponseBodyCofingStatistics.
        :type product_all_num: float
        """
        self._product_all_num = product_all_num

    @property
    def product_in_num(self):
        r"""Gets the product_in_num of this ListCollectConfigResponseBodyCofingStatistics.

        接入云产品数量

        :return: The product_in_num of this ListCollectConfigResponseBodyCofingStatistics.
        :rtype: float
        """
        return self._product_in_num

    @product_in_num.setter
    def product_in_num(self, product_in_num):
        r"""Sets the product_in_num of this ListCollectConfigResponseBodyCofingStatistics.

        接入云产品数量

        :param product_in_num: The product_in_num of this ListCollectConfigResponseBodyCofingStatistics.
        :type product_in_num: float
        """
        self._product_in_num = product_in_num

    @property
    def vendor_num(self):
        r"""Gets the vendor_num of this ListCollectConfigResponseBodyCofingStatistics.

        云厂商数量

        :return: The vendor_num of this ListCollectConfigResponseBodyCofingStatistics.
        :rtype: float
        """
        return self._vendor_num

    @vendor_num.setter
    def vendor_num(self, vendor_num):
        r"""Sets the vendor_num of this ListCollectConfigResponseBodyCofingStatistics.

        云厂商数量

        :param vendor_num: The vendor_num of this ListCollectConfigResponseBodyCofingStatistics.
        :type vendor_num: float
        """
        self._vendor_num = vendor_num

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
        if not isinstance(other, ListCollectConfigResponseBodyCofingStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
