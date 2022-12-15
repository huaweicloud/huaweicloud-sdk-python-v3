# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimpleResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'quota': 'int',
        'used': 'int'
    }

    attribute_map = {
        'type': 'type',
        'quota': 'quota',
        'used': 'used'
    }

    def __init__(self, type=None, quota=None, used=None):
        """SimpleResource

        The model defined in huaweicloud sdk

        :param type: 资源类别。 general_instances：普通桌面 ram：内存 cores：CPU volumes：磁盘数量 volume_gigabytes：磁盘容量 gpu_instances：GPU桌面 deh：云办公主机 users：用户 policy_groups: 策略组 Cores: CPU(配额工具使用)
        :type type: str
        :param quota: 配额数
        :type quota: int
        :param used: 配额已用值
        :type used: int
        """
        
        

        self._type = None
        self._quota = None
        self._used = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if quota is not None:
            self.quota = quota
        if used is not None:
            self.used = used

    @property
    def type(self):
        """Gets the type of this SimpleResource.

        资源类别。 general_instances：普通桌面 ram：内存 cores：CPU volumes：磁盘数量 volume_gigabytes：磁盘容量 gpu_instances：GPU桌面 deh：云办公主机 users：用户 policy_groups: 策略组 Cores: CPU(配额工具使用)

        :return: The type of this SimpleResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SimpleResource.

        资源类别。 general_instances：普通桌面 ram：内存 cores：CPU volumes：磁盘数量 volume_gigabytes：磁盘容量 gpu_instances：GPU桌面 deh：云办公主机 users：用户 policy_groups: 策略组 Cores: CPU(配额工具使用)

        :param type: The type of this SimpleResource.
        :type type: str
        """
        self._type = type

    @property
    def quota(self):
        """Gets the quota of this SimpleResource.

        配额数

        :return: The quota of this SimpleResource.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this SimpleResource.

        配额数

        :param quota: The quota of this SimpleResource.
        :type quota: int
        """
        self._quota = quota

    @property
    def used(self):
        """Gets the used of this SimpleResource.

        配额已用值

        :return: The used of this SimpleResource.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this SimpleResource.

        配额已用值

        :param used: The used of this SimpleResource.
        :type used: int
        """
        self._used = used

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
        if not isinstance(other, SimpleResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
