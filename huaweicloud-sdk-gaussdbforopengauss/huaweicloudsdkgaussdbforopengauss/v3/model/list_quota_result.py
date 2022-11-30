# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQuotaResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'instance_eps_quota': 'int',
        'vcpus_eps_quota': 'int',
        'ram_eps_quota': 'int',
        'volume_eps_quota': 'int',
        'instance_used': 'int',
        'vcpus_used': 'int',
        'ram_used': 'int',
        'volume_used': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'instance_eps_quota': 'instance_eps_quota',
        'vcpus_eps_quota': 'vcpus_eps_quota',
        'ram_eps_quota': 'ram_eps_quota',
        'volume_eps_quota': 'volume_eps_quota',
        'instance_used': 'instance_used',
        'vcpus_used': 'vcpus_used',
        'ram_used': 'ram_used',
        'volume_used': 'volume_used'
    }

    def __init__(self, enterprise_project_id=None, enterprise_project_name=None, instance_eps_quota=None, vcpus_eps_quota=None, ram_eps_quota=None, volume_eps_quota=None, instance_used=None, vcpus_used=None, ram_used=None, volume_used=None):
        """ListQuotaResult

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param enterprise_project_name: 企业项目名称。
        :type enterprise_project_name: str
        :param instance_eps_quota: EPS实例资源配额数量，值为-1时表示配额无限制。
        :type instance_eps_quota: int
        :param vcpus_eps_quota: EPS计算资源配额数量，值为-1时表示配额无限制。
        :type vcpus_eps_quota: int
        :param ram_eps_quota: EPS内存资源配额量，单位为GB，值为-1时表示配额无限制。
        :type ram_eps_quota: int
        :param volume_eps_quota: EPS磁盘资源配额量，单位为GB，值为-1时表示配额无限制。
        :type volume_eps_quota: int
        :param instance_used: EPS实例使用数量。
        :type instance_used: int
        :param vcpus_used: EPS计算资源使用数量。
        :type vcpus_used: int
        :param ram_used: EPS内存使用配额量，单位为GB。
        :type ram_used: int
        :param volume_used: EPS磁盘使用配额量，单位为GB。
        :type volume_used: int
        """
        
        

        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._instance_eps_quota = None
        self._vcpus_eps_quota = None
        self._ram_eps_quota = None
        self._volume_eps_quota = None
        self._instance_used = None
        self._vcpus_used = None
        self._ram_used = None
        self._volume_used = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if instance_eps_quota is not None:
            self.instance_eps_quota = instance_eps_quota
        if vcpus_eps_quota is not None:
            self.vcpus_eps_quota = vcpus_eps_quota
        if ram_eps_quota is not None:
            self.ram_eps_quota = ram_eps_quota
        if volume_eps_quota is not None:
            self.volume_eps_quota = volume_eps_quota
        if instance_used is not None:
            self.instance_used = instance_used
        if vcpus_used is not None:
            self.vcpus_used = vcpus_used
        if ram_used is not None:
            self.ram_used = ram_used
        if volume_used is not None:
            self.volume_used = volume_used

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListQuotaResult.

        企业项目ID。

        :return: The enterprise_project_id of this ListQuotaResult.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListQuotaResult.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListQuotaResult.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        """Gets the enterprise_project_name of this ListQuotaResult.

        企业项目名称。

        :return: The enterprise_project_name of this ListQuotaResult.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        """Sets the enterprise_project_name of this ListQuotaResult.

        企业项目名称。

        :param enterprise_project_name: The enterprise_project_name of this ListQuotaResult.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def instance_eps_quota(self):
        """Gets the instance_eps_quota of this ListQuotaResult.

        EPS实例资源配额数量，值为-1时表示配额无限制。

        :return: The instance_eps_quota of this ListQuotaResult.
        :rtype: int
        """
        return self._instance_eps_quota

    @instance_eps_quota.setter
    def instance_eps_quota(self, instance_eps_quota):
        """Sets the instance_eps_quota of this ListQuotaResult.

        EPS实例资源配额数量，值为-1时表示配额无限制。

        :param instance_eps_quota: The instance_eps_quota of this ListQuotaResult.
        :type instance_eps_quota: int
        """
        self._instance_eps_quota = instance_eps_quota

    @property
    def vcpus_eps_quota(self):
        """Gets the vcpus_eps_quota of this ListQuotaResult.

        EPS计算资源配额数量，值为-1时表示配额无限制。

        :return: The vcpus_eps_quota of this ListQuotaResult.
        :rtype: int
        """
        return self._vcpus_eps_quota

    @vcpus_eps_quota.setter
    def vcpus_eps_quota(self, vcpus_eps_quota):
        """Sets the vcpus_eps_quota of this ListQuotaResult.

        EPS计算资源配额数量，值为-1时表示配额无限制。

        :param vcpus_eps_quota: The vcpus_eps_quota of this ListQuotaResult.
        :type vcpus_eps_quota: int
        """
        self._vcpus_eps_quota = vcpus_eps_quota

    @property
    def ram_eps_quota(self):
        """Gets the ram_eps_quota of this ListQuotaResult.

        EPS内存资源配额量，单位为GB，值为-1时表示配额无限制。

        :return: The ram_eps_quota of this ListQuotaResult.
        :rtype: int
        """
        return self._ram_eps_quota

    @ram_eps_quota.setter
    def ram_eps_quota(self, ram_eps_quota):
        """Sets the ram_eps_quota of this ListQuotaResult.

        EPS内存资源配额量，单位为GB，值为-1时表示配额无限制。

        :param ram_eps_quota: The ram_eps_quota of this ListQuotaResult.
        :type ram_eps_quota: int
        """
        self._ram_eps_quota = ram_eps_quota

    @property
    def volume_eps_quota(self):
        """Gets the volume_eps_quota of this ListQuotaResult.

        EPS磁盘资源配额量，单位为GB，值为-1时表示配额无限制。

        :return: The volume_eps_quota of this ListQuotaResult.
        :rtype: int
        """
        return self._volume_eps_quota

    @volume_eps_quota.setter
    def volume_eps_quota(self, volume_eps_quota):
        """Sets the volume_eps_quota of this ListQuotaResult.

        EPS磁盘资源配额量，单位为GB，值为-1时表示配额无限制。

        :param volume_eps_quota: The volume_eps_quota of this ListQuotaResult.
        :type volume_eps_quota: int
        """
        self._volume_eps_quota = volume_eps_quota

    @property
    def instance_used(self):
        """Gets the instance_used of this ListQuotaResult.

        EPS实例使用数量。

        :return: The instance_used of this ListQuotaResult.
        :rtype: int
        """
        return self._instance_used

    @instance_used.setter
    def instance_used(self, instance_used):
        """Sets the instance_used of this ListQuotaResult.

        EPS实例使用数量。

        :param instance_used: The instance_used of this ListQuotaResult.
        :type instance_used: int
        """
        self._instance_used = instance_used

    @property
    def vcpus_used(self):
        """Gets the vcpus_used of this ListQuotaResult.

        EPS计算资源使用数量。

        :return: The vcpus_used of this ListQuotaResult.
        :rtype: int
        """
        return self._vcpus_used

    @vcpus_used.setter
    def vcpus_used(self, vcpus_used):
        """Sets the vcpus_used of this ListQuotaResult.

        EPS计算资源使用数量。

        :param vcpus_used: The vcpus_used of this ListQuotaResult.
        :type vcpus_used: int
        """
        self._vcpus_used = vcpus_used

    @property
    def ram_used(self):
        """Gets the ram_used of this ListQuotaResult.

        EPS内存使用配额量，单位为GB。

        :return: The ram_used of this ListQuotaResult.
        :rtype: int
        """
        return self._ram_used

    @ram_used.setter
    def ram_used(self, ram_used):
        """Sets the ram_used of this ListQuotaResult.

        EPS内存使用配额量，单位为GB。

        :param ram_used: The ram_used of this ListQuotaResult.
        :type ram_used: int
        """
        self._ram_used = ram_used

    @property
    def volume_used(self):
        """Gets the volume_used of this ListQuotaResult.

        EPS磁盘使用配额量，单位为GB。

        :return: The volume_used of this ListQuotaResult.
        :rtype: int
        """
        return self._volume_used

    @volume_used.setter
    def volume_used(self, volume_used):
        """Sets the volume_used of this ListQuotaResult.

        EPS磁盘使用配额量，单位为GB。

        :param volume_used: The volume_used of this ListQuotaResult.
        :type volume_used: int
        """
        self._volume_used = volume_used

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
        if not isinstance(other, ListQuotaResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
