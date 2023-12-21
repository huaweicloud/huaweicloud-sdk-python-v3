# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CBHInstances:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'specification': 'str',
        'instance_name': 'str',
        'password': 'str',
        'region': 'str',
        'availability_zone': 'str',
        'slave_availability_zone': 'str',
        'charging_mode': 'int',
        'period_type': 'int',
        'period_num': 'int',
        'is_auto_renew': 'int',
        'is_auto_pay': 'int',
        'network': 'object',
        'ipv6_enable': 'bool',
        'enterprise_project_id': 'str',
        'attach_disk_size': 'int',
        'tags': 'list[ResourceTag]'
    }

    attribute_map = {
        'specification': 'specification',
        'instance_name': 'instance_name',
        'password': 'password',
        'region': 'region',
        'availability_zone': 'availability_zone',
        'slave_availability_zone': 'slave_availability_zone',
        'charging_mode': 'charging_mode',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_renew': 'is_auto_renew',
        'is_auto_pay': 'is_auto_pay',
        'network': 'network',
        'ipv6_enable': 'ipv6_enable',
        'enterprise_project_id': 'enterprise_project_id',
        'attach_disk_size': 'attach_disk_size',
        'tags': 'tags'
    }

    def __init__(self, specification=None, instance_name=None, password=None, region=None, availability_zone=None, slave_availability_zone=None, charging_mode=None, period_type=None, period_num=None, is_auto_renew=None, is_auto_pay=None, network=None, ipv6_enable=None, enterprise_project_id=None, attach_disk_size=None, tags=None):
        """CBHInstances

        The model defined in huaweicloud sdk

        :param specification: 待创建云堡垒机规格ID，例如： - cbh.basic.50 - cbh.enhance.50  已上线的规格请参见《云堡垒机产品介绍》的[服务版本差异](https://support.huaweicloud.com/productdesc-cbh/cbh_01_0010.html)章节。
        :type specification: str
        :param instance_name: 云堡垒机实例名称，取值范围：  只能由中文字符、英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。  例如：CBH-6b8e
        :type instance_name: str
        :param password: 堡垒机实例前端登录密码。  密码规则：8-32位,不能包含amdin或nidma及其大写形式,必须包含大小写数字特殊字符四种类型中的三种。
        :type password: str
        :param region: 创建云堡垒机实例所在局点ID。   可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取。
        :type region: str
        :param availability_zone: 创建云堡垒机所在的可用分区，需要指定可用分区名称。(主备模式是作为主机可用区)  可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取。
        :type availability_zone: str
        :param slave_availability_zone: 创建云堡垒机备机所在的可用分区，需要指定可用分区名称。(只创建单机时不传此字段)。  可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取。
        :type slave_availability_zone: str
        :param charging_mode: 计费模式。 - 0 包周期计费。 - 1 按需计费，部分局点支持。
        :type charging_mode: int
        :param period_type: 订购周期类型。（包周期模式必传） - 2：月 - 3：年
        :type period_type: int
        :param period_num: 订购周期数。（包周期模式必传） - period_type&#x3D;2（周期类型为月），取值范围[1，9] - periodType&#x3D;3（周期类型为年），取值范围[1，10]
        :type period_num: int
        :param is_auto_renew: 是否自动续订。 - 1，自动续订 - 0，不自动续订  默认值为“0”
        :type is_auto_renew: int
        :param is_auto_pay: 是否自动支付，下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。 - 1：是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券) - 0：否（需要客户手动去支付，客户可以选择折扣和优惠券。）  默认值为“0”
        :type is_auto_pay: int
        :param network: 网络信息。
        :type network: object
        :param ipv6_enable: 云堡垒机实例是否支持IPV6。  默认值为“false”。
        :type ipv6_enable: bool
        :param enterprise_project_id: 企业项目ID。  默认值为“0”。
        :type enterprise_project_id: str
        :param attach_disk_size: 附加磁盘大小。单位TB  &gt; 说明： 附加磁盘和规格自带磁盘大小合起来不能超过300TB。
        :type attach_disk_size: int
        :param tags: 标签信息。
        :type tags: list[:class:`huaweicloudsdkcbh.v2.ResourceTag`]
        """
        
        

        self._specification = None
        self._instance_name = None
        self._password = None
        self._region = None
        self._availability_zone = None
        self._slave_availability_zone = None
        self._charging_mode = None
        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._is_auto_pay = None
        self._network = None
        self._ipv6_enable = None
        self._enterprise_project_id = None
        self._attach_disk_size = None
        self._tags = None
        self.discriminator = None

        self.specification = specification
        self.instance_name = instance_name
        self.password = password
        self.region = region
        self.availability_zone = availability_zone
        if slave_availability_zone is not None:
            self.slave_availability_zone = slave_availability_zone
        self.charging_mode = charging_mode
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        self.network = network
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if attach_disk_size is not None:
            self.attach_disk_size = attach_disk_size
        if tags is not None:
            self.tags = tags

    @property
    def specification(self):
        """Gets the specification of this CBHInstances.

        待创建云堡垒机规格ID，例如： - cbh.basic.50 - cbh.enhance.50  已上线的规格请参见《云堡垒机产品介绍》的[服务版本差异](https://support.huaweicloud.com/productdesc-cbh/cbh_01_0010.html)章节。

        :return: The specification of this CBHInstances.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        """Sets the specification of this CBHInstances.

        待创建云堡垒机规格ID，例如： - cbh.basic.50 - cbh.enhance.50  已上线的规格请参见《云堡垒机产品介绍》的[服务版本差异](https://support.huaweicloud.com/productdesc-cbh/cbh_01_0010.html)章节。

        :param specification: The specification of this CBHInstances.
        :type specification: str
        """
        self._specification = specification

    @property
    def instance_name(self):
        """Gets the instance_name of this CBHInstances.

        云堡垒机实例名称，取值范围：  只能由中文字符、英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。  例如：CBH-6b8e

        :return: The instance_name of this CBHInstances.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this CBHInstances.

        云堡垒机实例名称，取值范围：  只能由中文字符、英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。  例如：CBH-6b8e

        :param instance_name: The instance_name of this CBHInstances.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def password(self):
        """Gets the password of this CBHInstances.

        堡垒机实例前端登录密码。  密码规则：8-32位,不能包含amdin或nidma及其大写形式,必须包含大小写数字特殊字符四种类型中的三种。

        :return: The password of this CBHInstances.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CBHInstances.

        堡垒机实例前端登录密码。  密码规则：8-32位,不能包含amdin或nidma及其大写形式,必须包含大小写数字特殊字符四种类型中的三种。

        :param password: The password of this CBHInstances.
        :type password: str
        """
        self._password = password

    @property
    def region(self):
        """Gets the region of this CBHInstances.

        创建云堡垒机实例所在局点ID。   可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取。

        :return: The region of this CBHInstances.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CBHInstances.

        创建云堡垒机实例所在局点ID。   可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取。

        :param region: The region of this CBHInstances.
        :type region: str
        """
        self._region = region

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CBHInstances.

        创建云堡垒机所在的可用分区，需要指定可用分区名称。(主备模式是作为主机可用区)  可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取。

        :return: The availability_zone of this CBHInstances.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CBHInstances.

        创建云堡垒机所在的可用分区，需要指定可用分区名称。(主备模式是作为主机可用区)  可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取。

        :param availability_zone: The availability_zone of this CBHInstances.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def slave_availability_zone(self):
        """Gets the slave_availability_zone of this CBHInstances.

        创建云堡垒机备机所在的可用分区，需要指定可用分区名称。(只创建单机时不传此字段)。  可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取。

        :return: The slave_availability_zone of this CBHInstances.
        :rtype: str
        """
        return self._slave_availability_zone

    @slave_availability_zone.setter
    def slave_availability_zone(self, slave_availability_zone):
        """Sets the slave_availability_zone of this CBHInstances.

        创建云堡垒机备机所在的可用分区，需要指定可用分区名称。(只创建单机时不传此字段)。  可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取。

        :param slave_availability_zone: The slave_availability_zone of this CBHInstances.
        :type slave_availability_zone: str
        """
        self._slave_availability_zone = slave_availability_zone

    @property
    def charging_mode(self):
        """Gets the charging_mode of this CBHInstances.

        计费模式。 - 0 包周期计费。 - 1 按需计费，部分局点支持。

        :return: The charging_mode of this CBHInstances.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this CBHInstances.

        计费模式。 - 0 包周期计费。 - 1 按需计费，部分局点支持。

        :param charging_mode: The charging_mode of this CBHInstances.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def period_type(self):
        """Gets the period_type of this CBHInstances.

        订购周期类型。（包周期模式必传） - 2：月 - 3：年

        :return: The period_type of this CBHInstances.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this CBHInstances.

        订购周期类型。（包周期模式必传） - 2：月 - 3：年

        :param period_type: The period_type of this CBHInstances.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this CBHInstances.

        订购周期数。（包周期模式必传） - period_type=2（周期类型为月），取值范围[1，9] - periodType=3（周期类型为年），取值范围[1，10]

        :return: The period_num of this CBHInstances.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this CBHInstances.

        订购周期数。（包周期模式必传） - period_type=2（周期类型为月），取值范围[1，9] - periodType=3（周期类型为年），取值范围[1，10]

        :param period_num: The period_num of this CBHInstances.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this CBHInstances.

        是否自动续订。 - 1，自动续订 - 0，不自动续订  默认值为“0”

        :return: The is_auto_renew of this CBHInstances.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this CBHInstances.

        是否自动续订。 - 1，自动续订 - 0，不自动续订  默认值为“0”

        :param is_auto_renew: The is_auto_renew of this CBHInstances.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this CBHInstances.

        是否自动支付，下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。 - 1：是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券) - 0：否（需要客户手动去支付，客户可以选择折扣和优惠券。）  默认值为“0”

        :return: The is_auto_pay of this CBHInstances.
        :rtype: int
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this CBHInstances.

        是否自动支付，下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。 - 1：是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券) - 0：否（需要客户手动去支付，客户可以选择折扣和优惠券。）  默认值为“0”

        :param is_auto_pay: The is_auto_pay of this CBHInstances.
        :type is_auto_pay: int
        """
        self._is_auto_pay = is_auto_pay

    @property
    def network(self):
        """Gets the network of this CBHInstances.

        网络信息。

        :return: The network of this CBHInstances.
        :rtype: object
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this CBHInstances.

        网络信息。

        :param network: The network of this CBHInstances.
        :type network: object
        """
        self._network = network

    @property
    def ipv6_enable(self):
        """Gets the ipv6_enable of this CBHInstances.

        云堡垒机实例是否支持IPV6。  默认值为“false”。

        :return: The ipv6_enable of this CBHInstances.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        """Sets the ipv6_enable of this CBHInstances.

        云堡垒机实例是否支持IPV6。  默认值为“false”。

        :param ipv6_enable: The ipv6_enable of this CBHInstances.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CBHInstances.

        企业项目ID。  默认值为“0”。

        :return: The enterprise_project_id of this CBHInstances.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CBHInstances.

        企业项目ID。  默认值为“0”。

        :param enterprise_project_id: The enterprise_project_id of this CBHInstances.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def attach_disk_size(self):
        """Gets the attach_disk_size of this CBHInstances.

        附加磁盘大小。单位TB  > 说明： 附加磁盘和规格自带磁盘大小合起来不能超过300TB。

        :return: The attach_disk_size of this CBHInstances.
        :rtype: int
        """
        return self._attach_disk_size

    @attach_disk_size.setter
    def attach_disk_size(self, attach_disk_size):
        """Sets the attach_disk_size of this CBHInstances.

        附加磁盘大小。单位TB  > 说明： 附加磁盘和规格自带磁盘大小合起来不能超过300TB。

        :param attach_disk_size: The attach_disk_size of this CBHInstances.
        :type attach_disk_size: int
        """
        self._attach_disk_size = attach_disk_size

    @property
    def tags(self):
        """Gets the tags of this CBHInstances.

        标签信息。

        :return: The tags of this CBHInstances.
        :rtype: list[:class:`huaweicloudsdkcbh.v2.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CBHInstances.

        标签信息。

        :param tags: The tags of this CBHInstances.
        :type tags: list[:class:`huaweicloudsdkcbh.v2.ResourceTag`]
        """
        self._tags = tags

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
        if not isinstance(other, CBHInstances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
