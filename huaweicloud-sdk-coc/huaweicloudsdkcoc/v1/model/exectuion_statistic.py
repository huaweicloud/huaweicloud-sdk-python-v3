# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExectuionStatistic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_status': 'str',
        'instance_count': 'int',
        'batch_indexes': 'list[int]'
    }

    attribute_map = {
        'instance_status': 'instance_status',
        'instance_count': 'instance_count',
        'batch_indexes': 'batch_indexes'
    }

    def __init__(self, instance_status=None, instance_count=None, batch_indexes=None):
        r"""ExectuionStatistic

        The model defined in huaweicloud sdk

        :param instance_status: 执行实例状态
        :type instance_status: str
        :param instance_count: 该状态下执行实例个数
        :type instance_count: int
        :param batch_indexes: 该状态下批次index列表
        :type batch_indexes: list[int]
        """
        
        

        self._instance_status = None
        self._instance_count = None
        self._batch_indexes = None
        self.discriminator = None

        self.instance_status = instance_status
        self.instance_count = instance_count
        self.batch_indexes = batch_indexes

    @property
    def instance_status(self):
        r"""Gets the instance_status of this ExectuionStatistic.

        执行实例状态

        :return: The instance_status of this ExectuionStatistic.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this ExectuionStatistic.

        执行实例状态

        :param instance_status: The instance_status of this ExectuionStatistic.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def instance_count(self):
        r"""Gets the instance_count of this ExectuionStatistic.

        该状态下执行实例个数

        :return: The instance_count of this ExectuionStatistic.
        :rtype: int
        """
        return self._instance_count

    @instance_count.setter
    def instance_count(self, instance_count):
        r"""Sets the instance_count of this ExectuionStatistic.

        该状态下执行实例个数

        :param instance_count: The instance_count of this ExectuionStatistic.
        :type instance_count: int
        """
        self._instance_count = instance_count

    @property
    def batch_indexes(self):
        r"""Gets the batch_indexes of this ExectuionStatistic.

        该状态下批次index列表

        :return: The batch_indexes of this ExectuionStatistic.
        :rtype: list[int]
        """
        return self._batch_indexes

    @batch_indexes.setter
    def batch_indexes(self, batch_indexes):
        r"""Sets the batch_indexes of this ExectuionStatistic.

        该状态下批次index列表

        :param batch_indexes: The batch_indexes of this ExectuionStatistic.
        :type batch_indexes: list[int]
        """
        self._batch_indexes = batch_indexes

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
        if not isinstance(other, ExectuionStatistic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
