# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterBackupStrategyBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'period': 'str',
        'prefix': 'str',
        'keepday': 'int',
        'bucket': 'str',
        'base_path': 'str',
        'agency': 'str'
    }

    attribute_map = {
        'period': 'period',
        'prefix': 'prefix',
        'keepday': 'keepday',
        'bucket': 'bucket',
        'base_path': 'basePath',
        'agency': 'agency'
    }

    def __init__(self, period=None, prefix=None, keepday=None, bucket=None, base_path=None, agency=None):
        """CreateClusterBackupStrategyBody

        The model defined in huaweicloud sdk

        :param period: 每天自动创建快照的时间点。只支持整点，后面需加上时区，格式为“HH:mm z”，“HH:mm”表示整点时间，“z”表示时区。比如“00:00 GMT+08:00”、“01:00 GMT+08:00”等。
        :type period: str
        :param prefix: 自动创建的快照的前缀，需要用户自己手动输入。只能包含1~32位小写字母、数字、中划线或者下划线，并且以小写字母开头。
        :type prefix: str
        :param keepday: 自动创建快照的保留天数。取值范围：1-90。
        :type keepday: int
        :param bucket: 备份使用的OBS桶名称。
        :type bucket: str
        :param base_path: 快照在OBS桶中的存放路径。
        :type base_path: str
        :param agency: 委托名称，委托给CSS，允许CSS调用您的其他云服务。   &gt;如果bucket、basePath和agency三个参数同时为空，则系统会自动创建OBS桶和IAM代理（若创建失败，则需要手工配置正确的参数）。
        :type agency: str
        """
        
        

        self._period = None
        self._prefix = None
        self._keepday = None
        self._bucket = None
        self._base_path = None
        self._agency = None
        self.discriminator = None

        self.period = period
        self.prefix = prefix
        self.keepday = keepday
        if bucket is not None:
            self.bucket = bucket
        if base_path is not None:
            self.base_path = base_path
        if agency is not None:
            self.agency = agency

    @property
    def period(self):
        """Gets the period of this CreateClusterBackupStrategyBody.

        每天自动创建快照的时间点。只支持整点，后面需加上时区，格式为“HH:mm z”，“HH:mm”表示整点时间，“z”表示时区。比如“00:00 GMT+08:00”、“01:00 GMT+08:00”等。

        :return: The period of this CreateClusterBackupStrategyBody.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this CreateClusterBackupStrategyBody.

        每天自动创建快照的时间点。只支持整点，后面需加上时区，格式为“HH:mm z”，“HH:mm”表示整点时间，“z”表示时区。比如“00:00 GMT+08:00”、“01:00 GMT+08:00”等。

        :param period: The period of this CreateClusterBackupStrategyBody.
        :type period: str
        """
        self._period = period

    @property
    def prefix(self):
        """Gets the prefix of this CreateClusterBackupStrategyBody.

        自动创建的快照的前缀，需要用户自己手动输入。只能包含1~32位小写字母、数字、中划线或者下划线，并且以小写字母开头。

        :return: The prefix of this CreateClusterBackupStrategyBody.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this CreateClusterBackupStrategyBody.

        自动创建的快照的前缀，需要用户自己手动输入。只能包含1~32位小写字母、数字、中划线或者下划线，并且以小写字母开头。

        :param prefix: The prefix of this CreateClusterBackupStrategyBody.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def keepday(self):
        """Gets the keepday of this CreateClusterBackupStrategyBody.

        自动创建快照的保留天数。取值范围：1-90。

        :return: The keepday of this CreateClusterBackupStrategyBody.
        :rtype: int
        """
        return self._keepday

    @keepday.setter
    def keepday(self, keepday):
        """Sets the keepday of this CreateClusterBackupStrategyBody.

        自动创建快照的保留天数。取值范围：1-90。

        :param keepday: The keepday of this CreateClusterBackupStrategyBody.
        :type keepday: int
        """
        self._keepday = keepday

    @property
    def bucket(self):
        """Gets the bucket of this CreateClusterBackupStrategyBody.

        备份使用的OBS桶名称。

        :return: The bucket of this CreateClusterBackupStrategyBody.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this CreateClusterBackupStrategyBody.

        备份使用的OBS桶名称。

        :param bucket: The bucket of this CreateClusterBackupStrategyBody.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def base_path(self):
        """Gets the base_path of this CreateClusterBackupStrategyBody.

        快照在OBS桶中的存放路径。

        :return: The base_path of this CreateClusterBackupStrategyBody.
        :rtype: str
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        """Sets the base_path of this CreateClusterBackupStrategyBody.

        快照在OBS桶中的存放路径。

        :param base_path: The base_path of this CreateClusterBackupStrategyBody.
        :type base_path: str
        """
        self._base_path = base_path

    @property
    def agency(self):
        """Gets the agency of this CreateClusterBackupStrategyBody.

        委托名称，委托给CSS，允许CSS调用您的其他云服务。   >如果bucket、basePath和agency三个参数同时为空，则系统会自动创建OBS桶和IAM代理（若创建失败，则需要手工配置正确的参数）。

        :return: The agency of this CreateClusterBackupStrategyBody.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        """Sets the agency of this CreateClusterBackupStrategyBody.

        委托名称，委托给CSS，允许CSS调用您的其他云服务。   >如果bucket、basePath和agency三个参数同时为空，则系统会自动创建OBS桶和IAM代理（若创建失败，则需要手工配置正确的参数）。

        :param agency: The agency of this CreateClusterBackupStrategyBody.
        :type agency: str
        """
        self._agency = agency

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
        if not isinstance(other, CreateClusterBackupStrategyBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
