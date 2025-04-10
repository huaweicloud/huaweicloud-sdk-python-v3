# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeviceDataRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disk_quota': 'int',
        'age': 'int',
        'state': 'str'
    }

    attribute_map = {
        'disk_quota': 'disk_quota',
        'age': 'age',
        'state': 'state'
    }

    def __init__(self, disk_quota=None, age=None, state=None):
        r"""DeviceDataRecord

        The model defined in huaweicloud sdk

        :param disk_quota: 磁盘配额，单位MB，参考值，只能保证在这个值左右
        :type disk_quota: int
        :param age: 老化时间，日志压缩文件名时间戳老于这个时间就会发生老化删除
        :type age: int
        :param state: 配置开关，true启用数据打印，false不启用数据打印
        :type state: str
        """
        
        

        self._disk_quota = None
        self._age = None
        self._state = None
        self.discriminator = None

        self.disk_quota = disk_quota
        self.age = age
        self.state = state

    @property
    def disk_quota(self):
        r"""Gets the disk_quota of this DeviceDataRecord.

        磁盘配额，单位MB，参考值，只能保证在这个值左右

        :return: The disk_quota of this DeviceDataRecord.
        :rtype: int
        """
        return self._disk_quota

    @disk_quota.setter
    def disk_quota(self, disk_quota):
        r"""Sets the disk_quota of this DeviceDataRecord.

        磁盘配额，单位MB，参考值，只能保证在这个值左右

        :param disk_quota: The disk_quota of this DeviceDataRecord.
        :type disk_quota: int
        """
        self._disk_quota = disk_quota

    @property
    def age(self):
        r"""Gets the age of this DeviceDataRecord.

        老化时间，日志压缩文件名时间戳老于这个时间就会发生老化删除

        :return: The age of this DeviceDataRecord.
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        r"""Sets the age of this DeviceDataRecord.

        老化时间，日志压缩文件名时间戳老于这个时间就会发生老化删除

        :param age: The age of this DeviceDataRecord.
        :type age: int
        """
        self._age = age

    @property
    def state(self):
        r"""Gets the state of this DeviceDataRecord.

        配置开关，true启用数据打印，false不启用数据打印

        :return: The state of this DeviceDataRecord.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this DeviceDataRecord.

        配置开关，true启用数据打印，false不启用数据打印

        :param state: The state of this DeviceDataRecord.
        :type state: str
        """
        self._state = state

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
        if not isinstance(other, DeviceDataRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
