# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAutoScanConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_auto_scan': 'bool',
        'first_scan_at': 'str',
        'interval': 'int',
        'timeout': 'int',
        'scan_keys_count': 'int'
    }

    attribute_map = {
        'enable_auto_scan': 'enable_auto_scan',
        'first_scan_at': 'first_scan_at',
        'interval': 'interval',
        'timeout': 'timeout',
        'scan_keys_count': 'scan_keys_count'
    }

    def __init__(self, enable_auto_scan=None, first_scan_at=None, interval=None, timeout=None, scan_keys_count=None):
        r"""UpdateAutoScanConfigRequestBody

        The model defined in huaweicloud sdk

        :param enable_auto_scan: 启用自动扫描
        :type enable_auto_scan: bool
        :param first_scan_at: 首次扫描时间，例如：2023-07-07T15:00:05.000
        :type first_scan_at: str
        :param interval: 间隔时间(秒)
        :type interval: int
        :param timeout: 超时时间(秒)
        :type timeout: int
        :param scan_keys_count: 扫描密钥计数
        :type scan_keys_count: int
        """
        
        

        self._enable_auto_scan = None
        self._first_scan_at = None
        self._interval = None
        self._timeout = None
        self._scan_keys_count = None
        self.discriminator = None

        if enable_auto_scan is not None:
            self.enable_auto_scan = enable_auto_scan
        if first_scan_at is not None:
            self.first_scan_at = first_scan_at
        if interval is not None:
            self.interval = interval
        if timeout is not None:
            self.timeout = timeout
        if scan_keys_count is not None:
            self.scan_keys_count = scan_keys_count

    @property
    def enable_auto_scan(self):
        r"""Gets the enable_auto_scan of this UpdateAutoScanConfigRequestBody.

        启用自动扫描

        :return: The enable_auto_scan of this UpdateAutoScanConfigRequestBody.
        :rtype: bool
        """
        return self._enable_auto_scan

    @enable_auto_scan.setter
    def enable_auto_scan(self, enable_auto_scan):
        r"""Sets the enable_auto_scan of this UpdateAutoScanConfigRequestBody.

        启用自动扫描

        :param enable_auto_scan: The enable_auto_scan of this UpdateAutoScanConfigRequestBody.
        :type enable_auto_scan: bool
        """
        self._enable_auto_scan = enable_auto_scan

    @property
    def first_scan_at(self):
        r"""Gets the first_scan_at of this UpdateAutoScanConfigRequestBody.

        首次扫描时间，例如：2023-07-07T15:00:05.000

        :return: The first_scan_at of this UpdateAutoScanConfigRequestBody.
        :rtype: str
        """
        return self._first_scan_at

    @first_scan_at.setter
    def first_scan_at(self, first_scan_at):
        r"""Sets the first_scan_at of this UpdateAutoScanConfigRequestBody.

        首次扫描时间，例如：2023-07-07T15:00:05.000

        :param first_scan_at: The first_scan_at of this UpdateAutoScanConfigRequestBody.
        :type first_scan_at: str
        """
        self._first_scan_at = first_scan_at

    @property
    def interval(self):
        r"""Gets the interval of this UpdateAutoScanConfigRequestBody.

        间隔时间(秒)

        :return: The interval of this UpdateAutoScanConfigRequestBody.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this UpdateAutoScanConfigRequestBody.

        间隔时间(秒)

        :param interval: The interval of this UpdateAutoScanConfigRequestBody.
        :type interval: int
        """
        self._interval = interval

    @property
    def timeout(self):
        r"""Gets the timeout of this UpdateAutoScanConfigRequestBody.

        超时时间(秒)

        :return: The timeout of this UpdateAutoScanConfigRequestBody.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this UpdateAutoScanConfigRequestBody.

        超时时间(秒)

        :param timeout: The timeout of this UpdateAutoScanConfigRequestBody.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def scan_keys_count(self):
        r"""Gets the scan_keys_count of this UpdateAutoScanConfigRequestBody.

        扫描密钥计数

        :return: The scan_keys_count of this UpdateAutoScanConfigRequestBody.
        :rtype: int
        """
        return self._scan_keys_count

    @scan_keys_count.setter
    def scan_keys_count(self, scan_keys_count):
        r"""Sets the scan_keys_count of this UpdateAutoScanConfigRequestBody.

        扫描密钥计数

        :param scan_keys_count: The scan_keys_count of this UpdateAutoScanConfigRequestBody.
        :type scan_keys_count: int
        """
        self._scan_keys_count = scan_keys_count

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
        if not isinstance(other, UpdateAutoScanConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
