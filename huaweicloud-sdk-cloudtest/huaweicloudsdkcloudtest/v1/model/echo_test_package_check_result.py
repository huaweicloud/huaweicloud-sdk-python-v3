# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EchoTestPackageCheckResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'expiration_time': 'datetime',
        'has_license': 'bool',
        'original_amount': 'float',
        'package_user': 'bool',
        'resource_id': 'str',
        'resource_status': 'str',
        'resource_used': 'float',
        'spec_code': 'str',
        'start_time': 'datetime',
        'tenant_id': 'str'
    }

    attribute_map = {
        'expiration_time': 'expiration_time',
        'has_license': 'has_license',
        'original_amount': 'original_amount',
        'package_user': 'package_user',
        'resource_id': 'resource_id',
        'resource_status': 'resource_status',
        'resource_used': 'resource_used',
        'spec_code': 'spec_code',
        'start_time': 'start_time',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, expiration_time=None, has_license=None, original_amount=None, package_user=None, resource_id=None, resource_status=None, resource_used=None, spec_code=None, start_time=None, tenant_id=None):
        """EchoTestPackageCheckResult

        The model defined in huaweicloud sdk

        :param expiration_time: 到期时间
        :type expiration_time: datetime
        :param has_license: 是否拥有license
        :type has_license: bool
        :param original_amount: 总量
        :type original_amount: float
        :param package_user: 是否跨租户
        :type package_user: bool
        :param resource_id: 资源记录id
        :type resource_id: str
        :param resource_status: 套餐状态
        :type resource_status: str
        :param resource_used: 用量使用量
        :type resource_used: float
        :param spec_code: 套餐名称
        :type spec_code: str
        :param start_time: 开始时间
        :type start_time: datetime
        :param tenant_id: 租户id
        :type tenant_id: str
        """
        
        

        self._expiration_time = None
        self._has_license = None
        self._original_amount = None
        self._package_user = None
        self._resource_id = None
        self._resource_status = None
        self._resource_used = None
        self._spec_code = None
        self._start_time = None
        self._tenant_id = None
        self.discriminator = None

        if expiration_time is not None:
            self.expiration_time = expiration_time
        if has_license is not None:
            self.has_license = has_license
        if original_amount is not None:
            self.original_amount = original_amount
        if package_user is not None:
            self.package_user = package_user
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_status is not None:
            self.resource_status = resource_status
        if resource_used is not None:
            self.resource_used = resource_used
        if spec_code is not None:
            self.spec_code = spec_code
        if start_time is not None:
            self.start_time = start_time
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def expiration_time(self):
        """Gets the expiration_time of this EchoTestPackageCheckResult.

        到期时间

        :return: The expiration_time of this EchoTestPackageCheckResult.
        :rtype: datetime
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this EchoTestPackageCheckResult.

        到期时间

        :param expiration_time: The expiration_time of this EchoTestPackageCheckResult.
        :type expiration_time: datetime
        """
        self._expiration_time = expiration_time

    @property
    def has_license(self):
        """Gets the has_license of this EchoTestPackageCheckResult.

        是否拥有license

        :return: The has_license of this EchoTestPackageCheckResult.
        :rtype: bool
        """
        return self._has_license

    @has_license.setter
    def has_license(self, has_license):
        """Sets the has_license of this EchoTestPackageCheckResult.

        是否拥有license

        :param has_license: The has_license of this EchoTestPackageCheckResult.
        :type has_license: bool
        """
        self._has_license = has_license

    @property
    def original_amount(self):
        """Gets the original_amount of this EchoTestPackageCheckResult.

        总量

        :return: The original_amount of this EchoTestPackageCheckResult.
        :rtype: float
        """
        return self._original_amount

    @original_amount.setter
    def original_amount(self, original_amount):
        """Sets the original_amount of this EchoTestPackageCheckResult.

        总量

        :param original_amount: The original_amount of this EchoTestPackageCheckResult.
        :type original_amount: float
        """
        self._original_amount = original_amount

    @property
    def package_user(self):
        """Gets the package_user of this EchoTestPackageCheckResult.

        是否跨租户

        :return: The package_user of this EchoTestPackageCheckResult.
        :rtype: bool
        """
        return self._package_user

    @package_user.setter
    def package_user(self, package_user):
        """Sets the package_user of this EchoTestPackageCheckResult.

        是否跨租户

        :param package_user: The package_user of this EchoTestPackageCheckResult.
        :type package_user: bool
        """
        self._package_user = package_user

    @property
    def resource_id(self):
        """Gets the resource_id of this EchoTestPackageCheckResult.

        资源记录id

        :return: The resource_id of this EchoTestPackageCheckResult.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this EchoTestPackageCheckResult.

        资源记录id

        :param resource_id: The resource_id of this EchoTestPackageCheckResult.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_status(self):
        """Gets the resource_status of this EchoTestPackageCheckResult.

        套餐状态

        :return: The resource_status of this EchoTestPackageCheckResult.
        :rtype: str
        """
        return self._resource_status

    @resource_status.setter
    def resource_status(self, resource_status):
        """Sets the resource_status of this EchoTestPackageCheckResult.

        套餐状态

        :param resource_status: The resource_status of this EchoTestPackageCheckResult.
        :type resource_status: str
        """
        self._resource_status = resource_status

    @property
    def resource_used(self):
        """Gets the resource_used of this EchoTestPackageCheckResult.

        用量使用量

        :return: The resource_used of this EchoTestPackageCheckResult.
        :rtype: float
        """
        return self._resource_used

    @resource_used.setter
    def resource_used(self, resource_used):
        """Sets the resource_used of this EchoTestPackageCheckResult.

        用量使用量

        :param resource_used: The resource_used of this EchoTestPackageCheckResult.
        :type resource_used: float
        """
        self._resource_used = resource_used

    @property
    def spec_code(self):
        """Gets the spec_code of this EchoTestPackageCheckResult.

        套餐名称

        :return: The spec_code of this EchoTestPackageCheckResult.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this EchoTestPackageCheckResult.

        套餐名称

        :param spec_code: The spec_code of this EchoTestPackageCheckResult.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def start_time(self):
        """Gets the start_time of this EchoTestPackageCheckResult.

        开始时间

        :return: The start_time of this EchoTestPackageCheckResult.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this EchoTestPackageCheckResult.

        开始时间

        :param start_time: The start_time of this EchoTestPackageCheckResult.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this EchoTestPackageCheckResult.

        租户id

        :return: The tenant_id of this EchoTestPackageCheckResult.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this EchoTestPackageCheckResult.

        租户id

        :param tenant_id: The tenant_id of this EchoTestPackageCheckResult.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

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
        if not isinstance(other, EchoTestPackageCheckResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
