# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Quota:

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
        'instance_quota': 'int',
        'vcpus_quota': 'int',
        'ram_quota': 'int',
        'availability_instance_quota': 'int',
        'availability_vcpus_quota': 'int',
        'availability_ram_quota': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'instance_quota': 'instance_quota',
        'vcpus_quota': 'vcpus_quota',
        'ram_quota': 'ram_quota',
        'availability_instance_quota': 'availability_instance_quota',
        'availability_vcpus_quota': 'availability_vcpus_quota',
        'availability_ram_quota': 'availability_ram_quota'
    }

    def __init__(self, enterprise_project_id=None, enterprise_project_name=None, instance_quota=None, vcpus_quota=None, ram_quota=None, availability_instance_quota=None, availability_vcpus_quota=None, availability_ram_quota=None):
        r"""Quota

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param enterprise_project_name: 企业项目名称。
        :type enterprise_project_name: str
        :param instance_quota: 实例个数配额。
        :type instance_quota: int
        :param vcpus_quota: CPU核数配额。
        :type vcpus_quota: int
        :param ram_quota: 内存使用配额，单位为GB。
        :type ram_quota: int
        :param availability_instance_quota: 实例剩余配额。
        :type availability_instance_quota: int
        :param availability_vcpus_quota: CPU核数剩余配额。
        :type availability_vcpus_quota: int
        :param availability_ram_quota: 内存剩余配额。
        :type availability_ram_quota: int
        """
        
        

        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._instance_quota = None
        self._vcpus_quota = None
        self._ram_quota = None
        self._availability_instance_quota = None
        self._availability_vcpus_quota = None
        self._availability_ram_quota = None
        self.discriminator = None

        self.enterprise_project_id = enterprise_project_id
        self.enterprise_project_name = enterprise_project_name
        self.instance_quota = instance_quota
        self.vcpus_quota = vcpus_quota
        self.ram_quota = ram_quota
        self.availability_instance_quota = availability_instance_quota
        if availability_vcpus_quota is not None:
            self.availability_vcpus_quota = availability_vcpus_quota
        self.availability_ram_quota = availability_ram_quota

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this Quota.

        企业项目ID。

        :return: The enterprise_project_id of this Quota.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this Quota.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this Quota.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this Quota.

        企业项目名称。

        :return: The enterprise_project_name of this Quota.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this Quota.

        企业项目名称。

        :param enterprise_project_name: The enterprise_project_name of this Quota.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def instance_quota(self):
        r"""Gets the instance_quota of this Quota.

        实例个数配额。

        :return: The instance_quota of this Quota.
        :rtype: int
        """
        return self._instance_quota

    @instance_quota.setter
    def instance_quota(self, instance_quota):
        r"""Sets the instance_quota of this Quota.

        实例个数配额。

        :param instance_quota: The instance_quota of this Quota.
        :type instance_quota: int
        """
        self._instance_quota = instance_quota

    @property
    def vcpus_quota(self):
        r"""Gets the vcpus_quota of this Quota.

        CPU核数配额。

        :return: The vcpus_quota of this Quota.
        :rtype: int
        """
        return self._vcpus_quota

    @vcpus_quota.setter
    def vcpus_quota(self, vcpus_quota):
        r"""Sets the vcpus_quota of this Quota.

        CPU核数配额。

        :param vcpus_quota: The vcpus_quota of this Quota.
        :type vcpus_quota: int
        """
        self._vcpus_quota = vcpus_quota

    @property
    def ram_quota(self):
        r"""Gets the ram_quota of this Quota.

        内存使用配额，单位为GB。

        :return: The ram_quota of this Quota.
        :rtype: int
        """
        return self._ram_quota

    @ram_quota.setter
    def ram_quota(self, ram_quota):
        r"""Sets the ram_quota of this Quota.

        内存使用配额，单位为GB。

        :param ram_quota: The ram_quota of this Quota.
        :type ram_quota: int
        """
        self._ram_quota = ram_quota

    @property
    def availability_instance_quota(self):
        r"""Gets the availability_instance_quota of this Quota.

        实例剩余配额。

        :return: The availability_instance_quota of this Quota.
        :rtype: int
        """
        return self._availability_instance_quota

    @availability_instance_quota.setter
    def availability_instance_quota(self, availability_instance_quota):
        r"""Sets the availability_instance_quota of this Quota.

        实例剩余配额。

        :param availability_instance_quota: The availability_instance_quota of this Quota.
        :type availability_instance_quota: int
        """
        self._availability_instance_quota = availability_instance_quota

    @property
    def availability_vcpus_quota(self):
        r"""Gets the availability_vcpus_quota of this Quota.

        CPU核数剩余配额。

        :return: The availability_vcpus_quota of this Quota.
        :rtype: int
        """
        return self._availability_vcpus_quota

    @availability_vcpus_quota.setter
    def availability_vcpus_quota(self, availability_vcpus_quota):
        r"""Sets the availability_vcpus_quota of this Quota.

        CPU核数剩余配额。

        :param availability_vcpus_quota: The availability_vcpus_quota of this Quota.
        :type availability_vcpus_quota: int
        """
        self._availability_vcpus_quota = availability_vcpus_quota

    @property
    def availability_ram_quota(self):
        r"""Gets the availability_ram_quota of this Quota.

        内存剩余配额。

        :return: The availability_ram_quota of this Quota.
        :rtype: int
        """
        return self._availability_ram_quota

    @availability_ram_quota.setter
    def availability_ram_quota(self, availability_ram_quota):
        r"""Sets the availability_ram_quota of this Quota.

        内存剩余配额。

        :param availability_ram_quota: The availability_ram_quota of this Quota.
        :type availability_ram_quota: int
        """
        self._availability_ram_quota = availability_ram_quota

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
        if not isinstance(other, Quota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
