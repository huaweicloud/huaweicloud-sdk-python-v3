# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUpgradeDbMajorVersionStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'target_version': 'str',
        'start_time': 'str',
        'report_expiration_time': 'str',
        'detail': 'str'
    }

    attribute_map = {
        'status': 'status',
        'target_version': 'target_version',
        'start_time': 'start_time',
        'report_expiration_time': 'report_expiration_time',
        'detail': 'detail'
    }

    def __init__(self, status=None, target_version=None, start_time=None, report_expiration_time=None, detail=None):
        """ShowUpgradeDbMajorVersionStatusResponse

        The model defined in huaweicloud sdk

        :param status: 实例大版本升级状态 \&quot; running\&quot;：预检查或大版本升级进行中 \&quot; success\&quot;：预检查或大版本升级成功 \&quot; failed\&quot;：预检查或大版本升级失败
        :type status: str
        :param target_version: 目标版本。
        :type target_version: str
        :param start_time: 开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type start_time: str
        :param report_expiration_time: 检查成功时，检查报告到期时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。 该字段仅在action为check时返回。
        :type report_expiration_time: str
        :param detail: 预检查或升级报告信息。
        :type detail: str
        """
        
        super(ShowUpgradeDbMajorVersionStatusResponse, self).__init__()

        self._status = None
        self._target_version = None
        self._start_time = None
        self._report_expiration_time = None
        self._detail = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if target_version is not None:
            self.target_version = target_version
        if start_time is not None:
            self.start_time = start_time
        if report_expiration_time is not None:
            self.report_expiration_time = report_expiration_time
        if detail is not None:
            self.detail = detail

    @property
    def status(self):
        """Gets the status of this ShowUpgradeDbMajorVersionStatusResponse.

        实例大版本升级状态 \" running\"：预检查或大版本升级进行中 \" success\"：预检查或大版本升级成功 \" failed\"：预检查或大版本升级失败

        :return: The status of this ShowUpgradeDbMajorVersionStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowUpgradeDbMajorVersionStatusResponse.

        实例大版本升级状态 \" running\"：预检查或大版本升级进行中 \" success\"：预检查或大版本升级成功 \" failed\"：预检查或大版本升级失败

        :param status: The status of this ShowUpgradeDbMajorVersionStatusResponse.
        :type status: str
        """
        self._status = status

    @property
    def target_version(self):
        """Gets the target_version of this ShowUpgradeDbMajorVersionStatusResponse.

        目标版本。

        :return: The target_version of this ShowUpgradeDbMajorVersionStatusResponse.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        """Sets the target_version of this ShowUpgradeDbMajorVersionStatusResponse.

        目标版本。

        :param target_version: The target_version of this ShowUpgradeDbMajorVersionStatusResponse.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def start_time(self):
        """Gets the start_time of this ShowUpgradeDbMajorVersionStatusResponse.

        开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The start_time of this ShowUpgradeDbMajorVersionStatusResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowUpgradeDbMajorVersionStatusResponse.

        开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param start_time: The start_time of this ShowUpgradeDbMajorVersionStatusResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def report_expiration_time(self):
        """Gets the report_expiration_time of this ShowUpgradeDbMajorVersionStatusResponse.

        检查成功时，检查报告到期时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。 该字段仅在action为check时返回。

        :return: The report_expiration_time of this ShowUpgradeDbMajorVersionStatusResponse.
        :rtype: str
        """
        return self._report_expiration_time

    @report_expiration_time.setter
    def report_expiration_time(self, report_expiration_time):
        """Sets the report_expiration_time of this ShowUpgradeDbMajorVersionStatusResponse.

        检查成功时，检查报告到期时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。 该字段仅在action为check时返回。

        :param report_expiration_time: The report_expiration_time of this ShowUpgradeDbMajorVersionStatusResponse.
        :type report_expiration_time: str
        """
        self._report_expiration_time = report_expiration_time

    @property
    def detail(self):
        """Gets the detail of this ShowUpgradeDbMajorVersionStatusResponse.

        预检查或升级报告信息。

        :return: The detail of this ShowUpgradeDbMajorVersionStatusResponse.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ShowUpgradeDbMajorVersionStatusResponse.

        预检查或升级报告信息。

        :param detail: The detail of this ShowUpgradeDbMajorVersionStatusResponse.
        :type detail: str
        """
        self._detail = detail

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
        if not isinstance(other, ShowUpgradeDbMajorVersionStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
