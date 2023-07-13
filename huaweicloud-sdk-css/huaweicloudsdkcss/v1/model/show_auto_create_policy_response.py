# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAutoCreatePolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keepday': 'int',
        'period': 'str',
        'prefix': 'str',
        'bucket': 'str',
        'base_path': 'str',
        'agency': 'str',
        'enable': 'str'
    }

    attribute_map = {
        'keepday': 'keepday',
        'period': 'period',
        'prefix': 'prefix',
        'bucket': 'bucket',
        'base_path': 'basePath',
        'agency': 'agency',
        'enable': 'enable'
    }

    def __init__(self, keepday=None, period=None, prefix=None, bucket=None, base_path=None, agency=None, enable=None):
        """ShowAutoCreatePolicyResponse

        The model defined in huaweicloud sdk

        :param keepday: 快照保留的天数。
        :type keepday: int
        :param period: 每天快照创建时刻。
        :type period: str
        :param prefix: 快照命名前缀，需要用户自己手动输入。
        :type prefix: str
        :param bucket: 快照存放的OBS桶的桶名。
        :type bucket: str
        :param base_path: 快照在OBS桶中的存放路径。
        :type base_path: str
        :param agency: 访问OBS桶用到的委托。
        :type agency: str
        :param enable: 是否开启自动创建快照策略。 - true：表示开启自动创建快照策略。 - false：表示关闭自动创建快照策略。
        :type enable: str
        """
        
        super(ShowAutoCreatePolicyResponse, self).__init__()

        self._keepday = None
        self._period = None
        self._prefix = None
        self._bucket = None
        self._base_path = None
        self._agency = None
        self._enable = None
        self.discriminator = None

        if keepday is not None:
            self.keepday = keepday
        if period is not None:
            self.period = period
        if prefix is not None:
            self.prefix = prefix
        if bucket is not None:
            self.bucket = bucket
        if base_path is not None:
            self.base_path = base_path
        if agency is not None:
            self.agency = agency
        if enable is not None:
            self.enable = enable

    @property
    def keepday(self):
        """Gets the keepday of this ShowAutoCreatePolicyResponse.

        快照保留的天数。

        :return: The keepday of this ShowAutoCreatePolicyResponse.
        :rtype: int
        """
        return self._keepday

    @keepday.setter
    def keepday(self, keepday):
        """Sets the keepday of this ShowAutoCreatePolicyResponse.

        快照保留的天数。

        :param keepday: The keepday of this ShowAutoCreatePolicyResponse.
        :type keepday: int
        """
        self._keepday = keepday

    @property
    def period(self):
        """Gets the period of this ShowAutoCreatePolicyResponse.

        每天快照创建时刻。

        :return: The period of this ShowAutoCreatePolicyResponse.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ShowAutoCreatePolicyResponse.

        每天快照创建时刻。

        :param period: The period of this ShowAutoCreatePolicyResponse.
        :type period: str
        """
        self._period = period

    @property
    def prefix(self):
        """Gets the prefix of this ShowAutoCreatePolicyResponse.

        快照命名前缀，需要用户自己手动输入。

        :return: The prefix of this ShowAutoCreatePolicyResponse.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this ShowAutoCreatePolicyResponse.

        快照命名前缀，需要用户自己手动输入。

        :param prefix: The prefix of this ShowAutoCreatePolicyResponse.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def bucket(self):
        """Gets the bucket of this ShowAutoCreatePolicyResponse.

        快照存放的OBS桶的桶名。

        :return: The bucket of this ShowAutoCreatePolicyResponse.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this ShowAutoCreatePolicyResponse.

        快照存放的OBS桶的桶名。

        :param bucket: The bucket of this ShowAutoCreatePolicyResponse.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def base_path(self):
        """Gets the base_path of this ShowAutoCreatePolicyResponse.

        快照在OBS桶中的存放路径。

        :return: The base_path of this ShowAutoCreatePolicyResponse.
        :rtype: str
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        """Sets the base_path of this ShowAutoCreatePolicyResponse.

        快照在OBS桶中的存放路径。

        :param base_path: The base_path of this ShowAutoCreatePolicyResponse.
        :type base_path: str
        """
        self._base_path = base_path

    @property
    def agency(self):
        """Gets the agency of this ShowAutoCreatePolicyResponse.

        访问OBS桶用到的委托。

        :return: The agency of this ShowAutoCreatePolicyResponse.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        """Sets the agency of this ShowAutoCreatePolicyResponse.

        访问OBS桶用到的委托。

        :param agency: The agency of this ShowAutoCreatePolicyResponse.
        :type agency: str
        """
        self._agency = agency

    @property
    def enable(self):
        """Gets the enable of this ShowAutoCreatePolicyResponse.

        是否开启自动创建快照策略。 - true：表示开启自动创建快照策略。 - false：表示关闭自动创建快照策略。

        :return: The enable of this ShowAutoCreatePolicyResponse.
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this ShowAutoCreatePolicyResponse.

        是否开启自动创建快照策略。 - true：表示开启自动创建快照策略。 - false：表示关闭自动创建快照策略。

        :param enable: The enable of this ShowAutoCreatePolicyResponse.
        :type enable: str
        """
        self._enable = enable

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
        if not isinstance(other, ShowAutoCreatePolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
