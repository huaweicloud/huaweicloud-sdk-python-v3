# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetQuota:

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
        'instance_quota': 'int',
        'vcpus_quota': 'int',
        'ram_quota': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'instance_quota': 'instance_quota',
        'vcpus_quota': 'vcpus_quota',
        'ram_quota': 'ram_quota'
    }

    def __init__(self, enterprise_project_id=None, instance_quota=None, vcpus_quota=None, ram_quota=None):
        """SetQuota

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param instance_quota: 实例个数配额。取值范围0~100000。(如果已经存在实例，应该大于已经存在的实例个数)
        :type instance_quota: int
        :param vcpus_quota: CPU核数配额。取值范围0~2147483646。(如果已经存在实例，应该大于已经占用的cpu个数)
        :type vcpus_quota: int
        :param ram_quota: 内存使用配额，单位为GB。取值范围0~2147483646。(如果已经存在实例，应该大于已经占用的内存数)
        :type ram_quota: int
        """
        
        

        self._enterprise_project_id = None
        self._instance_quota = None
        self._vcpus_quota = None
        self._ram_quota = None
        self.discriminator = None

        self.enterprise_project_id = enterprise_project_id
        self.instance_quota = instance_quota
        self.vcpus_quota = vcpus_quota
        self.ram_quota = ram_quota

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this SetQuota.

        企业项目ID。

        :return: The enterprise_project_id of this SetQuota.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this SetQuota.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this SetQuota.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def instance_quota(self):
        """Gets the instance_quota of this SetQuota.

        实例个数配额。取值范围0~100000。(如果已经存在实例，应该大于已经存在的实例个数)

        :return: The instance_quota of this SetQuota.
        :rtype: int
        """
        return self._instance_quota

    @instance_quota.setter
    def instance_quota(self, instance_quota):
        """Sets the instance_quota of this SetQuota.

        实例个数配额。取值范围0~100000。(如果已经存在实例，应该大于已经存在的实例个数)

        :param instance_quota: The instance_quota of this SetQuota.
        :type instance_quota: int
        """
        self._instance_quota = instance_quota

    @property
    def vcpus_quota(self):
        """Gets the vcpus_quota of this SetQuota.

        CPU核数配额。取值范围0~2147483646。(如果已经存在实例，应该大于已经占用的cpu个数)

        :return: The vcpus_quota of this SetQuota.
        :rtype: int
        """
        return self._vcpus_quota

    @vcpus_quota.setter
    def vcpus_quota(self, vcpus_quota):
        """Sets the vcpus_quota of this SetQuota.

        CPU核数配额。取值范围0~2147483646。(如果已经存在实例，应该大于已经占用的cpu个数)

        :param vcpus_quota: The vcpus_quota of this SetQuota.
        :type vcpus_quota: int
        """
        self._vcpus_quota = vcpus_quota

    @property
    def ram_quota(self):
        """Gets the ram_quota of this SetQuota.

        内存使用配额，单位为GB。取值范围0~2147483646。(如果已经存在实例，应该大于已经占用的内存数)

        :return: The ram_quota of this SetQuota.
        :rtype: int
        """
        return self._ram_quota

    @ram_quota.setter
    def ram_quota(self, ram_quota):
        """Sets the ram_quota of this SetQuota.

        内存使用配额，单位为GB。取值范围0~2147483646。(如果已经存在实例，应该大于已经占用的内存数)

        :param ram_quota: The ram_quota of this SetQuota.
        :type ram_quota: int
        """
        self._ram_quota = ram_quota

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
        if not isinstance(other, SetQuota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
