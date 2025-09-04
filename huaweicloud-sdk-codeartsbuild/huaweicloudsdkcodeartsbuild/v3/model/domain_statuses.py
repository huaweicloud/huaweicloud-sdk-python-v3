# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainStatuses:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_name': 'str',
        'domain_id': 'str',
        'domain_name': 'str',
        'free_quota': 'bool',
        'free_package_quota': 'bool',
        'status': 'int',
        'is_federation': 'int',
        'is_whitelist': 'int',
        'region': 'str',
        'package_type': 'str',
        'domain_type': 'int',
        'domain_business_type': 'str',
        'domain_malicious_docker_args': 'str',
        'allow_custom_env': 'int',
        'spec_threshold': 'str'
    }

    attribute_map = {
        'service_name': 'service_name',
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'free_quota': 'free_quota',
        'free_package_quota': 'free_package_quota',
        'status': 'status',
        'is_federation': 'is_federation',
        'is_whitelist': 'is_whitelist',
        'region': 'region',
        'package_type': 'package_type',
        'domain_type': 'domain_type',
        'domain_business_type': 'domain_business_type',
        'domain_malicious_docker_args': 'domain_malicious_docker_args',
        'allow_custom_env': 'allow_custom_env',
        'spec_threshold': 'spec_threshold'
    }

    def __init__(self, service_name=None, domain_id=None, domain_name=None, free_quota=None, free_package_quota=None, status=None, is_federation=None, is_whitelist=None, region=None, package_type=None, domain_type=None, domain_business_type=None, domain_malicious_docker_args=None, allow_custom_env=None, spec_threshold=None):
        r"""DomainStatuses

        The model defined in huaweicloud sdk

        :param service_name: **参数解释**： 服务名。 **约束限制**： 不涉及。 **取值范围**： 默认CodeCI。
        :type service_name: str
        :param domain_id: **参数解释**： 租户id。 **约束限制**： 不涉及。 **取值范围**： 不涉及。
        :type domain_id: str
        :param domain_name: **参数解释**： 租户名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。
        :type domain_name: str
        :param free_quota: **参数解释**： freeQuota。 **约束限制**： 不涉及。 **取值范围**： true或false。
        :type free_quota: bool
        :param free_package_quota: **参数解释**： freePackageQuota。 **约束限制**： 不涉及。 **取值范围**： true或false。
        :type free_package_quota: bool
        :param status: **参数解释**： 状态。 **约束限制**： 不涉及。 **取值范围**： 不涉及。
        :type status: int
        :param is_federation: **参数解释**： isFederation。 **约束限制**： 不涉及。 **取值范围**： 不涉及。
        :type is_federation: int
        :param is_whitelist: **参数解释**： 白名单标识。 **约束限制**： 不涉及。 **取值范围**： 不涉及。
        :type is_whitelist: int
        :param region: **参数解释**： 地区。 **约束限制**： 不涉及。 **取值范围**： 不涉及。
        :type region: str
        :param package_type: **参数解释**： 包类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。
        :type package_type: str
        :param domain_type: **参数解释**： 租户类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。
        :type domain_type: int
        :param domain_business_type: **参数解释**： 租户业务类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。
        :type domain_business_type: str
        :param domain_malicious_docker_args: **参数解释**： domainMaliciousDockerArgs。 **约束限制**： 不涉及。 **取值范围**： 不涉及。
        :type domain_malicious_docker_args: str
        :param allow_custom_env: **参数解释**： 允许自定义环境数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。
        :type allow_custom_env: int
        :param spec_threshold: **参数解释**： 默认的加速阈值注入。 **约束限制**： 不涉及。 **取值范围**： 不涉及。
        :type spec_threshold: str
        """
        
        

        self._service_name = None
        self._domain_id = None
        self._domain_name = None
        self._free_quota = None
        self._free_package_quota = None
        self._status = None
        self._is_federation = None
        self._is_whitelist = None
        self._region = None
        self._package_type = None
        self._domain_type = None
        self._domain_business_type = None
        self._domain_malicious_docker_args = None
        self._allow_custom_env = None
        self._spec_threshold = None
        self.discriminator = None

        if service_name is not None:
            self.service_name = service_name
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if free_quota is not None:
            self.free_quota = free_quota
        if free_package_quota is not None:
            self.free_package_quota = free_package_quota
        if status is not None:
            self.status = status
        if is_federation is not None:
            self.is_federation = is_federation
        if is_whitelist is not None:
            self.is_whitelist = is_whitelist
        if region is not None:
            self.region = region
        if package_type is not None:
            self.package_type = package_type
        if domain_type is not None:
            self.domain_type = domain_type
        if domain_business_type is not None:
            self.domain_business_type = domain_business_type
        if domain_malicious_docker_args is not None:
            self.domain_malicious_docker_args = domain_malicious_docker_args
        if allow_custom_env is not None:
            self.allow_custom_env = allow_custom_env
        if spec_threshold is not None:
            self.spec_threshold = spec_threshold

    @property
    def service_name(self):
        r"""Gets the service_name of this DomainStatuses.

        **参数解释**： 服务名。 **约束限制**： 不涉及。 **取值范围**： 默认CodeCI。

        :return: The service_name of this DomainStatuses.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this DomainStatuses.

        **参数解释**： 服务名。 **约束限制**： 不涉及。 **取值范围**： 默认CodeCI。

        :param service_name: The service_name of this DomainStatuses.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this DomainStatuses.

        **参数解释**： 租户id。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :return: The domain_id of this DomainStatuses.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this DomainStatuses.

        **参数解释**： 租户id。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :param domain_id: The domain_id of this DomainStatuses.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this DomainStatuses.

        **参数解释**： 租户名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :return: The domain_name of this DomainStatuses.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this DomainStatuses.

        **参数解释**： 租户名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :param domain_name: The domain_name of this DomainStatuses.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def free_quota(self):
        r"""Gets the free_quota of this DomainStatuses.

        **参数解释**： freeQuota。 **约束限制**： 不涉及。 **取值范围**： true或false。

        :return: The free_quota of this DomainStatuses.
        :rtype: bool
        """
        return self._free_quota

    @free_quota.setter
    def free_quota(self, free_quota):
        r"""Sets the free_quota of this DomainStatuses.

        **参数解释**： freeQuota。 **约束限制**： 不涉及。 **取值范围**： true或false。

        :param free_quota: The free_quota of this DomainStatuses.
        :type free_quota: bool
        """
        self._free_quota = free_quota

    @property
    def free_package_quota(self):
        r"""Gets the free_package_quota of this DomainStatuses.

        **参数解释**： freePackageQuota。 **约束限制**： 不涉及。 **取值范围**： true或false。

        :return: The free_package_quota of this DomainStatuses.
        :rtype: bool
        """
        return self._free_package_quota

    @free_package_quota.setter
    def free_package_quota(self, free_package_quota):
        r"""Sets the free_package_quota of this DomainStatuses.

        **参数解释**： freePackageQuota。 **约束限制**： 不涉及。 **取值范围**： true或false。

        :param free_package_quota: The free_package_quota of this DomainStatuses.
        :type free_package_quota: bool
        """
        self._free_package_quota = free_package_quota

    @property
    def status(self):
        r"""Gets the status of this DomainStatuses.

        **参数解释**： 状态。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :return: The status of this DomainStatuses.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DomainStatuses.

        **参数解释**： 状态。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :param status: The status of this DomainStatuses.
        :type status: int
        """
        self._status = status

    @property
    def is_federation(self):
        r"""Gets the is_federation of this DomainStatuses.

        **参数解释**： isFederation。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :return: The is_federation of this DomainStatuses.
        :rtype: int
        """
        return self._is_federation

    @is_federation.setter
    def is_federation(self, is_federation):
        r"""Sets the is_federation of this DomainStatuses.

        **参数解释**： isFederation。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :param is_federation: The is_federation of this DomainStatuses.
        :type is_federation: int
        """
        self._is_federation = is_federation

    @property
    def is_whitelist(self):
        r"""Gets the is_whitelist of this DomainStatuses.

        **参数解释**： 白名单标识。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :return: The is_whitelist of this DomainStatuses.
        :rtype: int
        """
        return self._is_whitelist

    @is_whitelist.setter
    def is_whitelist(self, is_whitelist):
        r"""Sets the is_whitelist of this DomainStatuses.

        **参数解释**： 白名单标识。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :param is_whitelist: The is_whitelist of this DomainStatuses.
        :type is_whitelist: int
        """
        self._is_whitelist = is_whitelist

    @property
    def region(self):
        r"""Gets the region of this DomainStatuses.

        **参数解释**： 地区。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :return: The region of this DomainStatuses.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this DomainStatuses.

        **参数解释**： 地区。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :param region: The region of this DomainStatuses.
        :type region: str
        """
        self._region = region

    @property
    def package_type(self):
        r"""Gets the package_type of this DomainStatuses.

        **参数解释**： 包类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :return: The package_type of this DomainStatuses.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        r"""Sets the package_type of this DomainStatuses.

        **参数解释**： 包类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :param package_type: The package_type of this DomainStatuses.
        :type package_type: str
        """
        self._package_type = package_type

    @property
    def domain_type(self):
        r"""Gets the domain_type of this DomainStatuses.

        **参数解释**： 租户类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :return: The domain_type of this DomainStatuses.
        :rtype: int
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        r"""Sets the domain_type of this DomainStatuses.

        **参数解释**： 租户类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :param domain_type: The domain_type of this DomainStatuses.
        :type domain_type: int
        """
        self._domain_type = domain_type

    @property
    def domain_business_type(self):
        r"""Gets the domain_business_type of this DomainStatuses.

        **参数解释**： 租户业务类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :return: The domain_business_type of this DomainStatuses.
        :rtype: str
        """
        return self._domain_business_type

    @domain_business_type.setter
    def domain_business_type(self, domain_business_type):
        r"""Sets the domain_business_type of this DomainStatuses.

        **参数解释**： 租户业务类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :param domain_business_type: The domain_business_type of this DomainStatuses.
        :type domain_business_type: str
        """
        self._domain_business_type = domain_business_type

    @property
    def domain_malicious_docker_args(self):
        r"""Gets the domain_malicious_docker_args of this DomainStatuses.

        **参数解释**： domainMaliciousDockerArgs。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :return: The domain_malicious_docker_args of this DomainStatuses.
        :rtype: str
        """
        return self._domain_malicious_docker_args

    @domain_malicious_docker_args.setter
    def domain_malicious_docker_args(self, domain_malicious_docker_args):
        r"""Sets the domain_malicious_docker_args of this DomainStatuses.

        **参数解释**： domainMaliciousDockerArgs。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :param domain_malicious_docker_args: The domain_malicious_docker_args of this DomainStatuses.
        :type domain_malicious_docker_args: str
        """
        self._domain_malicious_docker_args = domain_malicious_docker_args

    @property
    def allow_custom_env(self):
        r"""Gets the allow_custom_env of this DomainStatuses.

        **参数解释**： 允许自定义环境数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :return: The allow_custom_env of this DomainStatuses.
        :rtype: int
        """
        return self._allow_custom_env

    @allow_custom_env.setter
    def allow_custom_env(self, allow_custom_env):
        r"""Sets the allow_custom_env of this DomainStatuses.

        **参数解释**： 允许自定义环境数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :param allow_custom_env: The allow_custom_env of this DomainStatuses.
        :type allow_custom_env: int
        """
        self._allow_custom_env = allow_custom_env

    @property
    def spec_threshold(self):
        r"""Gets the spec_threshold of this DomainStatuses.

        **参数解释**： 默认的加速阈值注入。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :return: The spec_threshold of this DomainStatuses.
        :rtype: str
        """
        return self._spec_threshold

    @spec_threshold.setter
    def spec_threshold(self, spec_threshold):
        r"""Sets the spec_threshold of this DomainStatuses.

        **参数解释**： 默认的加速阈值注入。 **约束限制**： 不涉及。 **取值范围**： 不涉及。

        :param spec_threshold: The spec_threshold of this DomainStatuses.
        :type spec_threshold: str
        """
        self._spec_threshold = spec_threshold

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
        if not isinstance(other, DomainStatuses):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
