# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RiskBackupTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cycle': 'str',
        'db_id': 'str',
        'status': 'int'
    }

    attribute_map = {
        'cycle': 'cycle',
        'db_id': 'db_id',
        'status': 'status'
    }

    def __init__(self, cycle=None, db_id=None, status=None):
        r"""RiskBackupTemplate

        The model defined in huaweicloud sdk

        :param cycle: 备份周期 - PER_DAY: 每天 - PER_WEEK: 每周 - PER_MONTH: 每月 - PER_HOUR: 每小时 - FIVE_MIN: 每5分钟
        :type cycle: str
        :param db_id: 数据库ID
        :type db_id: str
        :param status: 备份开关    - 0：关闭    - 1：开启
        :type status: int
        """
        
        

        self._cycle = None
        self._db_id = None
        self._status = None
        self.discriminator = None

        if cycle is not None:
            self.cycle = cycle
        self.db_id = db_id
        self.status = status

    @property
    def cycle(self):
        r"""Gets the cycle of this RiskBackupTemplate.

        备份周期 - PER_DAY: 每天 - PER_WEEK: 每周 - PER_MONTH: 每月 - PER_HOUR: 每小时 - FIVE_MIN: 每5分钟

        :return: The cycle of this RiskBackupTemplate.
        :rtype: str
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        r"""Sets the cycle of this RiskBackupTemplate.

        备份周期 - PER_DAY: 每天 - PER_WEEK: 每周 - PER_MONTH: 每月 - PER_HOUR: 每小时 - FIVE_MIN: 每5分钟

        :param cycle: The cycle of this RiskBackupTemplate.
        :type cycle: str
        """
        self._cycle = cycle

    @property
    def db_id(self):
        r"""Gets the db_id of this RiskBackupTemplate.

        数据库ID

        :return: The db_id of this RiskBackupTemplate.
        :rtype: str
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        r"""Sets the db_id of this RiskBackupTemplate.

        数据库ID

        :param db_id: The db_id of this RiskBackupTemplate.
        :type db_id: str
        """
        self._db_id = db_id

    @property
    def status(self):
        r"""Gets the status of this RiskBackupTemplate.

        备份开关    - 0：关闭    - 1：开启

        :return: The status of this RiskBackupTemplate.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RiskBackupTemplate.

        备份开关    - 0：关闭    - 1：开启

        :param status: The status of this RiskBackupTemplate.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, RiskBackupTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
