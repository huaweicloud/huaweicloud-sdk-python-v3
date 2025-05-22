# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChatResourceConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'count_resource': 'int',
        'resource_source': 'str',
        'charge_mode': 'str',
        'resource_nums': 'int',
        'resource_available_nums': 'int',
        'status': 'str',
        'expire_time': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'count_resource': 'count_resource',
        'resource_source': 'resource_source',
        'charge_mode': 'charge_mode',
        'resource_nums': 'resource_nums',
        'resource_available_nums': 'resource_available_nums',
        'status': 'status',
        'expire_time': 'expire_time'
    }

    def __init__(self, resource_id=None, count_resource=None, resource_source=None, charge_mode=None, resource_nums=None, resource_available_nums=None, status=None, expire_time=None):
        r"""ChatResourceConfigInfo

        The model defined in huaweicloud sdk

        :param resource_id: 资源id
        :type resource_id: str
        :param count_resource: 资源数量
        :type count_resource: int
        :param resource_source: 资源来源。 * PURCHASED: 购买 * SP_ALLOCATED：SP分配 * ADMIN_ALLOCATED：系统管理员分配 &gt; * 开通按需；购买按需套餐包、一次性资源、包周期等都属于PURCHASED。
        :type resource_source: str
        :param charge_mode: 资源计费类型。 * PERIODIC: 包周期 * ONE_TIME：一次性计费 * ON_DEMAND: 按需计费 &gt; * 一次性计费包括：租户订购的一次性资源，SP管理员分配给租户的一次性资源，SP管理员分配给租户的按需套餐包资源，系统管理员分配的资源（分钟数等）。
        :type charge_mode: str
        :param resource_nums: 资源数量。智能交互并发路数。
        :type resource_nums: int
        :param resource_available_nums: 可用资源数量。智能交互并发路数。
        :type resource_available_nums: int
        :param status: 资源状态。 * ACTIVE: 正常 * FREEZE：冻结 * DELETED：退订或过期
        :type status: str
        :param expire_time: 资源过期时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;
        :type expire_time: str
        """
        
        

        self._resource_id = None
        self._count_resource = None
        self._resource_source = None
        self._charge_mode = None
        self._resource_nums = None
        self._resource_available_nums = None
        self._status = None
        self._expire_time = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if count_resource is not None:
            self.count_resource = count_resource
        if resource_source is not None:
            self.resource_source = resource_source
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if resource_nums is not None:
            self.resource_nums = resource_nums
        if resource_available_nums is not None:
            self.resource_available_nums = resource_available_nums
        if status is not None:
            self.status = status
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ChatResourceConfigInfo.

        资源id

        :return: The resource_id of this ChatResourceConfigInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ChatResourceConfigInfo.

        资源id

        :param resource_id: The resource_id of this ChatResourceConfigInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def count_resource(self):
        r"""Gets the count_resource of this ChatResourceConfigInfo.

        资源数量

        :return: The count_resource of this ChatResourceConfigInfo.
        :rtype: int
        """
        return self._count_resource

    @count_resource.setter
    def count_resource(self, count_resource):
        r"""Sets the count_resource of this ChatResourceConfigInfo.

        资源数量

        :param count_resource: The count_resource of this ChatResourceConfigInfo.
        :type count_resource: int
        """
        self._count_resource = count_resource

    @property
    def resource_source(self):
        r"""Gets the resource_source of this ChatResourceConfigInfo.

        资源来源。 * PURCHASED: 购买 * SP_ALLOCATED：SP分配 * ADMIN_ALLOCATED：系统管理员分配 > * 开通按需；购买按需套餐包、一次性资源、包周期等都属于PURCHASED。

        :return: The resource_source of this ChatResourceConfigInfo.
        :rtype: str
        """
        return self._resource_source

    @resource_source.setter
    def resource_source(self, resource_source):
        r"""Sets the resource_source of this ChatResourceConfigInfo.

        资源来源。 * PURCHASED: 购买 * SP_ALLOCATED：SP分配 * ADMIN_ALLOCATED：系统管理员分配 > * 开通按需；购买按需套餐包、一次性资源、包周期等都属于PURCHASED。

        :param resource_source: The resource_source of this ChatResourceConfigInfo.
        :type resource_source: str
        """
        self._resource_source = resource_source

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this ChatResourceConfigInfo.

        资源计费类型。 * PERIODIC: 包周期 * ONE_TIME：一次性计费 * ON_DEMAND: 按需计费 > * 一次性计费包括：租户订购的一次性资源，SP管理员分配给租户的一次性资源，SP管理员分配给租户的按需套餐包资源，系统管理员分配的资源（分钟数等）。

        :return: The charge_mode of this ChatResourceConfigInfo.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this ChatResourceConfigInfo.

        资源计费类型。 * PERIODIC: 包周期 * ONE_TIME：一次性计费 * ON_DEMAND: 按需计费 > * 一次性计费包括：租户订购的一次性资源，SP管理员分配给租户的一次性资源，SP管理员分配给租户的按需套餐包资源，系统管理员分配的资源（分钟数等）。

        :param charge_mode: The charge_mode of this ChatResourceConfigInfo.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def resource_nums(self):
        r"""Gets the resource_nums of this ChatResourceConfigInfo.

        资源数量。智能交互并发路数。

        :return: The resource_nums of this ChatResourceConfigInfo.
        :rtype: int
        """
        return self._resource_nums

    @resource_nums.setter
    def resource_nums(self, resource_nums):
        r"""Sets the resource_nums of this ChatResourceConfigInfo.

        资源数量。智能交互并发路数。

        :param resource_nums: The resource_nums of this ChatResourceConfigInfo.
        :type resource_nums: int
        """
        self._resource_nums = resource_nums

    @property
    def resource_available_nums(self):
        r"""Gets the resource_available_nums of this ChatResourceConfigInfo.

        可用资源数量。智能交互并发路数。

        :return: The resource_available_nums of this ChatResourceConfigInfo.
        :rtype: int
        """
        return self._resource_available_nums

    @resource_available_nums.setter
    def resource_available_nums(self, resource_available_nums):
        r"""Sets the resource_available_nums of this ChatResourceConfigInfo.

        可用资源数量。智能交互并发路数。

        :param resource_available_nums: The resource_available_nums of this ChatResourceConfigInfo.
        :type resource_available_nums: int
        """
        self._resource_available_nums = resource_available_nums

    @property
    def status(self):
        r"""Gets the status of this ChatResourceConfigInfo.

        资源状态。 * ACTIVE: 正常 * FREEZE：冻结 * DELETED：退订或过期

        :return: The status of this ChatResourceConfigInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ChatResourceConfigInfo.

        资源状态。 * ACTIVE: 正常 * FREEZE：冻结 * DELETED：退订或过期

        :param status: The status of this ChatResourceConfigInfo.
        :type status: str
        """
        self._status = status

    @property
    def expire_time(self):
        r"""Gets the expire_time of this ChatResourceConfigInfo.

        资源过期时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :return: The expire_time of this ChatResourceConfigInfo.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this ChatResourceConfigInfo.

        资源过期时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :param expire_time: The expire_time of this ChatResourceConfigInfo.
        :type expire_time: str
        """
        self._expire_time = expire_time

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
        if not isinstance(other, ChatResourceConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
