# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourcesCount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'business_type': 'str',
        'count': 'float',
        'charging_mode': 'str',
        'resource_source': 'str'
    }

    attribute_map = {
        'business_type': 'business_type',
        'count': 'count',
        'charging_mode': 'charging_mode',
        'resource_source': 'resource_source'
    }

    def __init__(self, business_type=None, count=None, charging_mode=None, resource_source=None):
        r"""ResourcesCount

        The model defined in huaweicloud sdk

        :param business_type: 业务类型。
        :type business_type: str
        :param count: 资源总数。
        :type count: float
        :param charging_mode: 计费类型。 * PERIODIC: 包周期 * ONE_TIME：一次性 * ON_DEMAND：按需
        :type charging_mode: str
        :param resource_source: 资源来源。 * PURCHASED: 购买 * SP_ALLOCATED：SP分配 * ADMIN_ALLOCATED：系统管理员分配
        :type resource_source: str
        """
        
        

        self._business_type = None
        self._count = None
        self._charging_mode = None
        self._resource_source = None
        self.discriminator = None

        if business_type is not None:
            self.business_type = business_type
        if count is not None:
            self.count = count
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if resource_source is not None:
            self.resource_source = resource_source

    @property
    def business_type(self):
        r"""Gets the business_type of this ResourcesCount.

        业务类型。

        :return: The business_type of this ResourcesCount.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        r"""Sets the business_type of this ResourcesCount.

        业务类型。

        :param business_type: The business_type of this ResourcesCount.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def count(self):
        r"""Gets the count of this ResourcesCount.

        资源总数。

        :return: The count of this ResourcesCount.
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ResourcesCount.

        资源总数。

        :param count: The count of this ResourcesCount.
        :type count: float
        """
        self._count = count

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ResourcesCount.

        计费类型。 * PERIODIC: 包周期 * ONE_TIME：一次性 * ON_DEMAND：按需

        :return: The charging_mode of this ResourcesCount.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ResourcesCount.

        计费类型。 * PERIODIC: 包周期 * ONE_TIME：一次性 * ON_DEMAND：按需

        :param charging_mode: The charging_mode of this ResourcesCount.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def resource_source(self):
        r"""Gets the resource_source of this ResourcesCount.

        资源来源。 * PURCHASED: 购买 * SP_ALLOCATED：SP分配 * ADMIN_ALLOCATED：系统管理员分配

        :return: The resource_source of this ResourcesCount.
        :rtype: str
        """
        return self._resource_source

    @resource_source.setter
    def resource_source(self, resource_source):
        r"""Sets the resource_source of this ResourcesCount.

        资源来源。 * PURCHASED: 购买 * SP_ALLOCATED：SP分配 * ADMIN_ALLOCATED：系统管理员分配

        :param resource_source: The resource_source of this ResourcesCount.
        :type resource_source: str
        """
        self._resource_source = resource_source

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
        if not isinstance(other, ResourcesCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
