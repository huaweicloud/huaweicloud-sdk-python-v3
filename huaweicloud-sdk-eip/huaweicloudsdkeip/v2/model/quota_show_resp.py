# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaShowResp:

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
        'used': 'int',
        'quota': 'int',
        'min': 'int'
    }

    attribute_map = {
        'type': 'type',
        'used': 'used',
        'quota': 'quota',
        'min': 'min'
    }

    def __init__(self, type=None, used=None, quota=None, min=None):
        """QuotaShowResp

        The model defined in huaweicloud sdk

        :param type: 功能说明：根据type过滤查询指定类型的配额 取值范围：vpc，subnet，securityGroup，securityGroupRule，publicIp，vpn，vpngw，vpcPeer，firewall，shareBandwidth，shareBandwidthIP
        :type type: str
        :param used: 功能说明：已创建的资源个数 取值范围：0~quota数
        :type used: int
        :param quota: 功能说明：资源的最大配额数 取值范围：各类型资源默认配额数~Integer最大值 约束：资源的默认配额数可以修改，而且配额需要提前在底层配置，参考默认配置为：vpc默认5，子网默认100，安全组默认100，安全组规则默认5000，弹性公网IP默认10，vpn默认5，vpngw默认2，vpcPeer默认50，firewall默认200，shareBandwidth默认5，shareBandwidthIP默认20
        :type quota: int
        :param min: 允许修改的配额最小值
        :type min: int
        """
        
        

        self._type = None
        self._used = None
        self._quota = None
        self._min = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if used is not None:
            self.used = used
        if quota is not None:
            self.quota = quota
        if min is not None:
            self.min = min

    @property
    def type(self):
        """Gets the type of this QuotaShowResp.

        功能说明：根据type过滤查询指定类型的配额 取值范围：vpc，subnet，securityGroup，securityGroupRule，publicIp，vpn，vpngw，vpcPeer，firewall，shareBandwidth，shareBandwidthIP

        :return: The type of this QuotaShowResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QuotaShowResp.

        功能说明：根据type过滤查询指定类型的配额 取值范围：vpc，subnet，securityGroup，securityGroupRule，publicIp，vpn，vpngw，vpcPeer，firewall，shareBandwidth，shareBandwidthIP

        :param type: The type of this QuotaShowResp.
        :type type: str
        """
        self._type = type

    @property
    def used(self):
        """Gets the used of this QuotaShowResp.

        功能说明：已创建的资源个数 取值范围：0~quota数

        :return: The used of this QuotaShowResp.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this QuotaShowResp.

        功能说明：已创建的资源个数 取值范围：0~quota数

        :param used: The used of this QuotaShowResp.
        :type used: int
        """
        self._used = used

    @property
    def quota(self):
        """Gets the quota of this QuotaShowResp.

        功能说明：资源的最大配额数 取值范围：各类型资源默认配额数~Integer最大值 约束：资源的默认配额数可以修改，而且配额需要提前在底层配置，参考默认配置为：vpc默认5，子网默认100，安全组默认100，安全组规则默认5000，弹性公网IP默认10，vpn默认5，vpngw默认2，vpcPeer默认50，firewall默认200，shareBandwidth默认5，shareBandwidthIP默认20

        :return: The quota of this QuotaShowResp.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this QuotaShowResp.

        功能说明：资源的最大配额数 取值范围：各类型资源默认配额数~Integer最大值 约束：资源的默认配额数可以修改，而且配额需要提前在底层配置，参考默认配置为：vpc默认5，子网默认100，安全组默认100，安全组规则默认5000，弹性公网IP默认10，vpn默认5，vpngw默认2，vpcPeer默认50，firewall默认200，shareBandwidth默认5，shareBandwidthIP默认20

        :param quota: The quota of this QuotaShowResp.
        :type quota: int
        """
        self._quota = quota

    @property
    def min(self):
        """Gets the min of this QuotaShowResp.

        允许修改的配额最小值

        :return: The min of this QuotaShowResp.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this QuotaShowResp.

        允许修改的配额最小值

        :param min: The min of this QuotaShowResp.
        :type min: int
        """
        self._min = min

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
        if not isinstance(other, QuotaShowResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
