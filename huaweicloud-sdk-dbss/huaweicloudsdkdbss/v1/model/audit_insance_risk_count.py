# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuditInsanceRiskCount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'db_id': 'str',
        'db_ip': 'str',
        'db_name': 'str',
        'instance_id': 'str',
        'instance_name': 'str'
    }

    attribute_map = {
        'count': 'count',
        'db_id': 'db_id',
        'db_ip': 'db_ip',
        'db_name': 'db_name',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name'
    }

    def __init__(self, count=None, db_id=None, db_ip=None, db_name=None, instance_id=None, instance_name=None):
        r"""AuditInsanceRiskCount

        The model defined in huaweicloud sdk

        :param count: 风险数量
        :type count: int
        :param db_id: 数据库ID
        :type db_id: str
        :param db_ip: 数据库IP
        :type db_ip: str
        :param db_name: 数据库名称
        :type db_name: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param instance_name: 实例名称
        :type instance_name: str
        """
        
        

        self._count = None
        self._db_id = None
        self._db_ip = None
        self._db_name = None
        self._instance_id = None
        self._instance_name = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if db_id is not None:
            self.db_id = db_id
        if db_ip is not None:
            self.db_ip = db_ip
        if db_name is not None:
            self.db_name = db_name
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name

    @property
    def count(self):
        r"""Gets the count of this AuditInsanceRiskCount.

        风险数量

        :return: The count of this AuditInsanceRiskCount.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this AuditInsanceRiskCount.

        风险数量

        :param count: The count of this AuditInsanceRiskCount.
        :type count: int
        """
        self._count = count

    @property
    def db_id(self):
        r"""Gets the db_id of this AuditInsanceRiskCount.

        数据库ID

        :return: The db_id of this AuditInsanceRiskCount.
        :rtype: str
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        r"""Sets the db_id of this AuditInsanceRiskCount.

        数据库ID

        :param db_id: The db_id of this AuditInsanceRiskCount.
        :type db_id: str
        """
        self._db_id = db_id

    @property
    def db_ip(self):
        r"""Gets the db_ip of this AuditInsanceRiskCount.

        数据库IP

        :return: The db_ip of this AuditInsanceRiskCount.
        :rtype: str
        """
        return self._db_ip

    @db_ip.setter
    def db_ip(self, db_ip):
        r"""Sets the db_ip of this AuditInsanceRiskCount.

        数据库IP

        :param db_ip: The db_ip of this AuditInsanceRiskCount.
        :type db_ip: str
        """
        self._db_ip = db_ip

    @property
    def db_name(self):
        r"""Gets the db_name of this AuditInsanceRiskCount.

        数据库名称

        :return: The db_name of this AuditInsanceRiskCount.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this AuditInsanceRiskCount.

        数据库名称

        :param db_name: The db_name of this AuditInsanceRiskCount.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this AuditInsanceRiskCount.

        实例ID

        :return: The instance_id of this AuditInsanceRiskCount.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this AuditInsanceRiskCount.

        实例ID

        :param instance_id: The instance_id of this AuditInsanceRiskCount.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this AuditInsanceRiskCount.

        实例名称

        :return: The instance_name of this AuditInsanceRiskCount.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this AuditInsanceRiskCount.

        实例名称

        :param instance_name: The instance_name of this AuditInsanceRiskCount.
        :type instance_name: str
        """
        self._instance_name = instance_name

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
        if not isinstance(other, AuditInsanceRiskCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
