# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EpsQuotasOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_projects_id': 'str',
        'instance_quota': 'int',
        'vcpus_quota': 'int',
        'ram_quota': 'int',
        'volume_quota': 'int'
    }

    attribute_map = {
        'enterprise_projects_id': 'enterprise_projects_id',
        'instance_quota': 'instance_quota',
        'vcpus_quota': 'vcpus_quota',
        'ram_quota': 'ram_quota',
        'volume_quota': 'volume_quota'
    }

    def __init__(self, enterprise_projects_id=None, instance_quota=None, vcpus_quota=None, ram_quota=None, volume_quota=None):
        """EpsQuotasOption

        The model defined in huaweicloud sdk

        :param enterprise_projects_id: 企业项目Id。
        :type enterprise_projects_id: str
        :param instance_quota: 实例的配额。取值范围：实际创建的实例个数 ~ 100,000。
        :type instance_quota: int
        :param vcpus_quota: cpu的配额。取值范围：实际使用的cpu核数 ~ 2,147,483,646。
        :type vcpus_quota: int
        :param ram_quota: 内存的配额。单位GB。取值范围：实际使用的内存 ~ 2,147,483,646。
        :type ram_quota: int
        :param volume_quota: 存储空间的配额。单位：GB。取值范围：实际使用的存储空间 ~ 2,147,483,646。
        :type volume_quota: int
        """
        
        

        self._enterprise_projects_id = None
        self._instance_quota = None
        self._vcpus_quota = None
        self._ram_quota = None
        self._volume_quota = None
        self.discriminator = None

        self.enterprise_projects_id = enterprise_projects_id
        if instance_quota is not None:
            self.instance_quota = instance_quota
        if vcpus_quota is not None:
            self.vcpus_quota = vcpus_quota
        if ram_quota is not None:
            self.ram_quota = ram_quota
        if volume_quota is not None:
            self.volume_quota = volume_quota

    @property
    def enterprise_projects_id(self):
        """Gets the enterprise_projects_id of this EpsQuotasOption.

        企业项目Id。

        :return: The enterprise_projects_id of this EpsQuotasOption.
        :rtype: str
        """
        return self._enterprise_projects_id

    @enterprise_projects_id.setter
    def enterprise_projects_id(self, enterprise_projects_id):
        """Sets the enterprise_projects_id of this EpsQuotasOption.

        企业项目Id。

        :param enterprise_projects_id: The enterprise_projects_id of this EpsQuotasOption.
        :type enterprise_projects_id: str
        """
        self._enterprise_projects_id = enterprise_projects_id

    @property
    def instance_quota(self):
        """Gets the instance_quota of this EpsQuotasOption.

        实例的配额。取值范围：实际创建的实例个数 ~ 100,000。

        :return: The instance_quota of this EpsQuotasOption.
        :rtype: int
        """
        return self._instance_quota

    @instance_quota.setter
    def instance_quota(self, instance_quota):
        """Sets the instance_quota of this EpsQuotasOption.

        实例的配额。取值范围：实际创建的实例个数 ~ 100,000。

        :param instance_quota: The instance_quota of this EpsQuotasOption.
        :type instance_quota: int
        """
        self._instance_quota = instance_quota

    @property
    def vcpus_quota(self):
        """Gets the vcpus_quota of this EpsQuotasOption.

        cpu的配额。取值范围：实际使用的cpu核数 ~ 2,147,483,646。

        :return: The vcpus_quota of this EpsQuotasOption.
        :rtype: int
        """
        return self._vcpus_quota

    @vcpus_quota.setter
    def vcpus_quota(self, vcpus_quota):
        """Sets the vcpus_quota of this EpsQuotasOption.

        cpu的配额。取值范围：实际使用的cpu核数 ~ 2,147,483,646。

        :param vcpus_quota: The vcpus_quota of this EpsQuotasOption.
        :type vcpus_quota: int
        """
        self._vcpus_quota = vcpus_quota

    @property
    def ram_quota(self):
        """Gets the ram_quota of this EpsQuotasOption.

        内存的配额。单位GB。取值范围：实际使用的内存 ~ 2,147,483,646。

        :return: The ram_quota of this EpsQuotasOption.
        :rtype: int
        """
        return self._ram_quota

    @ram_quota.setter
    def ram_quota(self, ram_quota):
        """Sets the ram_quota of this EpsQuotasOption.

        内存的配额。单位GB。取值范围：实际使用的内存 ~ 2,147,483,646。

        :param ram_quota: The ram_quota of this EpsQuotasOption.
        :type ram_quota: int
        """
        self._ram_quota = ram_quota

    @property
    def volume_quota(self):
        """Gets the volume_quota of this EpsQuotasOption.

        存储空间的配额。单位：GB。取值范围：实际使用的存储空间 ~ 2,147,483,646。

        :return: The volume_quota of this EpsQuotasOption.
        :rtype: int
        """
        return self._volume_quota

    @volume_quota.setter
    def volume_quota(self, volume_quota):
        """Sets the volume_quota of this EpsQuotasOption.

        存储空间的配额。单位：GB。取值范围：实际使用的存储空间 ~ 2,147,483,646。

        :param volume_quota: The volume_quota of this EpsQuotasOption.
        :type volume_quota: int
        """
        self._volume_quota = volume_quota

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
        if not isinstance(other, EpsQuotasOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
