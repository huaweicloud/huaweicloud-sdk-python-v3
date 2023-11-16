# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PackageResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'package_id': 'str',
        'package_name': 'str',
        'region_id': 'str',
        'protection_type': 'int',
        'instance_type': 'str',
        'resource_id': 'str',
        'count_down_code': 'str',
        'count_down_infos': 'str',
        'count_down_tips': 'str',
        'order_id': 'str',
        'subscription_id': 'str',
        'ip_num': 'int',
        'ip_num_now': 'int',
        'protection_num_now': 'int',
        'protection_num': 'int',
        'basic_bandwidth': 'int',
        'elastic_bandwidth': 'int',
        'service_bandwidth': 'int',
        'clean_bandwidth': 'int',
        'policy_num': 'int',
        'is_old': 'bool',
        'new_flag': 'bool',
        'create_time': 'int'
    }

    attribute_map = {
        'package_id': 'package_id',
        'package_name': 'package_name',
        'region_id': 'region_id',
        'protection_type': 'protection_type',
        'instance_type': 'instance_type',
        'resource_id': 'resource_id',
        'count_down_code': 'count_down_code',
        'count_down_infos': 'count_down_infos',
        'count_down_tips': 'count_down_tips',
        'order_id': 'order_id',
        'subscription_id': 'subscription_id',
        'ip_num': 'ip_num',
        'ip_num_now': 'ip_num_now',
        'protection_num_now': 'protection_num_now',
        'protection_num': 'protection_num',
        'basic_bandwidth': 'basic_bandwidth',
        'elastic_bandwidth': 'elastic_bandwidth',
        'service_bandwidth': 'service_bandwidth',
        'clean_bandwidth': 'clean_bandwidth',
        'policy_num': 'policy_num',
        'is_old': 'is_old',
        'new_flag': 'new_flag',
        'create_time': 'create_time'
    }

    def __init__(self, package_id=None, package_name=None, region_id=None, protection_type=None, instance_type=None, resource_id=None, count_down_code=None, count_down_infos=None, count_down_tips=None, order_id=None, subscription_id=None, ip_num=None, ip_num_now=None, protection_num_now=None, protection_num=None, basic_bandwidth=None, elastic_bandwidth=None, service_bandwidth=None, clean_bandwidth=None, policy_num=None, is_old=None, new_flag=None, create_time=None):
        """PackageResponse

        The model defined in huaweicloud sdk

        :param package_id: 防护包id
        :type package_id: str
        :param package_name: 防护包名
        :type package_name: str
        :param region_id: 资源所属region
        :type region_id: str
        :param protection_type: 防护类型
        :type protection_type: int
        :param instance_type: 防护包类型。cnad_pro：专业版；cnad_ip：标准版；cnad_ep：铂金版；cnad_full_high：全力防高级版；cnad_vic：按需版；cnad_intl_ep：国际站铂金版
        :type instance_type: str
        :param resource_id: 资源id
        :type resource_id: str
        :param count_down_code: 倒计时相关信息
        :type count_down_code: str
        :param count_down_infos: 倒计时相关信息
        :type count_down_infos: str
        :param count_down_tips: 倒计时相关信息
        :type count_down_tips: str
        :param order_id: 订单id
        :type order_id: str
        :param subscription_id: 续费用的id
        :type subscription_id: str
        :param ip_num: ip数
        :type ip_num: int
        :param ip_num_now: 当前IP数
        :type ip_num_now: int
        :param protection_num_now: 当前防护次数
        :type protection_num_now: int
        :param protection_num: 防护次数，9999为无限次
        :type protection_num: int
        :param basic_bandwidth: 保底带宽
        :type basic_bandwidth: int
        :param elastic_bandwidth: 弹性带宽
        :type elastic_bandwidth: int
        :param service_bandwidth: 业务带宽
        :type service_bandwidth: int
        :param clean_bandwidth: 回源带宽
        :type clean_bandwidth: int
        :param policy_num: 策略模板数
        :type policy_num: int
        :param is_old: 是否旧防护包（旧防护包不支持升级规格）,默认不传为否
        :type is_old: bool
        :param new_flag: 专业版铂金版合并之后购买的专业版和铂金版均标识为true
        :type new_flag: bool
        :param create_time: 创建时间
        :type create_time: int
        """
        
        

        self._package_id = None
        self._package_name = None
        self._region_id = None
        self._protection_type = None
        self._instance_type = None
        self._resource_id = None
        self._count_down_code = None
        self._count_down_infos = None
        self._count_down_tips = None
        self._order_id = None
        self._subscription_id = None
        self._ip_num = None
        self._ip_num_now = None
        self._protection_num_now = None
        self._protection_num = None
        self._basic_bandwidth = None
        self._elastic_bandwidth = None
        self._service_bandwidth = None
        self._clean_bandwidth = None
        self._policy_num = None
        self._is_old = None
        self._new_flag = None
        self._create_time = None
        self.discriminator = None

        self.package_id = package_id
        self.package_name = package_name
        self.region_id = region_id
        self.protection_type = protection_type
        self.instance_type = instance_type
        self.resource_id = resource_id
        if count_down_code is not None:
            self.count_down_code = count_down_code
        if count_down_infos is not None:
            self.count_down_infos = count_down_infos
        if count_down_tips is not None:
            self.count_down_tips = count_down_tips
        if order_id is not None:
            self.order_id = order_id
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if ip_num is not None:
            self.ip_num = ip_num
        if ip_num_now is not None:
            self.ip_num_now = ip_num_now
        if protection_num_now is not None:
            self.protection_num_now = protection_num_now
        if protection_num is not None:
            self.protection_num = protection_num
        if basic_bandwidth is not None:
            self.basic_bandwidth = basic_bandwidth
        if elastic_bandwidth is not None:
            self.elastic_bandwidth = elastic_bandwidth
        if service_bandwidth is not None:
            self.service_bandwidth = service_bandwidth
        if clean_bandwidth is not None:
            self.clean_bandwidth = clean_bandwidth
        self.policy_num = policy_num
        if is_old is not None:
            self.is_old = is_old
        if new_flag is not None:
            self.new_flag = new_flag
        self.create_time = create_time

    @property
    def package_id(self):
        """Gets the package_id of this PackageResponse.

        防护包id

        :return: The package_id of this PackageResponse.
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """Sets the package_id of this PackageResponse.

        防护包id

        :param package_id: The package_id of this PackageResponse.
        :type package_id: str
        """
        self._package_id = package_id

    @property
    def package_name(self):
        """Gets the package_name of this PackageResponse.

        防护包名

        :return: The package_name of this PackageResponse.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this PackageResponse.

        防护包名

        :param package_name: The package_name of this PackageResponse.
        :type package_name: str
        """
        self._package_name = package_name

    @property
    def region_id(self):
        """Gets the region_id of this PackageResponse.

        资源所属region

        :return: The region_id of this PackageResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this PackageResponse.

        资源所属region

        :param region_id: The region_id of this PackageResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def protection_type(self):
        """Gets the protection_type of this PackageResponse.

        防护类型

        :return: The protection_type of this PackageResponse.
        :rtype: int
        """
        return self._protection_type

    @protection_type.setter
    def protection_type(self, protection_type):
        """Sets the protection_type of this PackageResponse.

        防护类型

        :param protection_type: The protection_type of this PackageResponse.
        :type protection_type: int
        """
        self._protection_type = protection_type

    @property
    def instance_type(self):
        """Gets the instance_type of this PackageResponse.

        防护包类型。cnad_pro：专业版；cnad_ip：标准版；cnad_ep：铂金版；cnad_full_high：全力防高级版；cnad_vic：按需版；cnad_intl_ep：国际站铂金版

        :return: The instance_type of this PackageResponse.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this PackageResponse.

        防护包类型。cnad_pro：专业版；cnad_ip：标准版；cnad_ep：铂金版；cnad_full_high：全力防高级版；cnad_vic：按需版；cnad_intl_ep：国际站铂金版

        :param instance_type: The instance_type of this PackageResponse.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def resource_id(self):
        """Gets the resource_id of this PackageResponse.

        资源id

        :return: The resource_id of this PackageResponse.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this PackageResponse.

        资源id

        :param resource_id: The resource_id of this PackageResponse.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def count_down_code(self):
        """Gets the count_down_code of this PackageResponse.

        倒计时相关信息

        :return: The count_down_code of this PackageResponse.
        :rtype: str
        """
        return self._count_down_code

    @count_down_code.setter
    def count_down_code(self, count_down_code):
        """Sets the count_down_code of this PackageResponse.

        倒计时相关信息

        :param count_down_code: The count_down_code of this PackageResponse.
        :type count_down_code: str
        """
        self._count_down_code = count_down_code

    @property
    def count_down_infos(self):
        """Gets the count_down_infos of this PackageResponse.

        倒计时相关信息

        :return: The count_down_infos of this PackageResponse.
        :rtype: str
        """
        return self._count_down_infos

    @count_down_infos.setter
    def count_down_infos(self, count_down_infos):
        """Sets the count_down_infos of this PackageResponse.

        倒计时相关信息

        :param count_down_infos: The count_down_infos of this PackageResponse.
        :type count_down_infos: str
        """
        self._count_down_infos = count_down_infos

    @property
    def count_down_tips(self):
        """Gets the count_down_tips of this PackageResponse.

        倒计时相关信息

        :return: The count_down_tips of this PackageResponse.
        :rtype: str
        """
        return self._count_down_tips

    @count_down_tips.setter
    def count_down_tips(self, count_down_tips):
        """Sets the count_down_tips of this PackageResponse.

        倒计时相关信息

        :param count_down_tips: The count_down_tips of this PackageResponse.
        :type count_down_tips: str
        """
        self._count_down_tips = count_down_tips

    @property
    def order_id(self):
        """Gets the order_id of this PackageResponse.

        订单id

        :return: The order_id of this PackageResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this PackageResponse.

        订单id

        :param order_id: The order_id of this PackageResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this PackageResponse.

        续费用的id

        :return: The subscription_id of this PackageResponse.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this PackageResponse.

        续费用的id

        :param subscription_id: The subscription_id of this PackageResponse.
        :type subscription_id: str
        """
        self._subscription_id = subscription_id

    @property
    def ip_num(self):
        """Gets the ip_num of this PackageResponse.

        ip数

        :return: The ip_num of this PackageResponse.
        :rtype: int
        """
        return self._ip_num

    @ip_num.setter
    def ip_num(self, ip_num):
        """Sets the ip_num of this PackageResponse.

        ip数

        :param ip_num: The ip_num of this PackageResponse.
        :type ip_num: int
        """
        self._ip_num = ip_num

    @property
    def ip_num_now(self):
        """Gets the ip_num_now of this PackageResponse.

        当前IP数

        :return: The ip_num_now of this PackageResponse.
        :rtype: int
        """
        return self._ip_num_now

    @ip_num_now.setter
    def ip_num_now(self, ip_num_now):
        """Sets the ip_num_now of this PackageResponse.

        当前IP数

        :param ip_num_now: The ip_num_now of this PackageResponse.
        :type ip_num_now: int
        """
        self._ip_num_now = ip_num_now

    @property
    def protection_num_now(self):
        """Gets the protection_num_now of this PackageResponse.

        当前防护次数

        :return: The protection_num_now of this PackageResponse.
        :rtype: int
        """
        return self._protection_num_now

    @protection_num_now.setter
    def protection_num_now(self, protection_num_now):
        """Sets the protection_num_now of this PackageResponse.

        当前防护次数

        :param protection_num_now: The protection_num_now of this PackageResponse.
        :type protection_num_now: int
        """
        self._protection_num_now = protection_num_now

    @property
    def protection_num(self):
        """Gets the protection_num of this PackageResponse.

        防护次数，9999为无限次

        :return: The protection_num of this PackageResponse.
        :rtype: int
        """
        return self._protection_num

    @protection_num.setter
    def protection_num(self, protection_num):
        """Sets the protection_num of this PackageResponse.

        防护次数，9999为无限次

        :param protection_num: The protection_num of this PackageResponse.
        :type protection_num: int
        """
        self._protection_num = protection_num

    @property
    def basic_bandwidth(self):
        """Gets the basic_bandwidth of this PackageResponse.

        保底带宽

        :return: The basic_bandwidth of this PackageResponse.
        :rtype: int
        """
        return self._basic_bandwidth

    @basic_bandwidth.setter
    def basic_bandwidth(self, basic_bandwidth):
        """Sets the basic_bandwidth of this PackageResponse.

        保底带宽

        :param basic_bandwidth: The basic_bandwidth of this PackageResponse.
        :type basic_bandwidth: int
        """
        self._basic_bandwidth = basic_bandwidth

    @property
    def elastic_bandwidth(self):
        """Gets the elastic_bandwidth of this PackageResponse.

        弹性带宽

        :return: The elastic_bandwidth of this PackageResponse.
        :rtype: int
        """
        return self._elastic_bandwidth

    @elastic_bandwidth.setter
    def elastic_bandwidth(self, elastic_bandwidth):
        """Sets the elastic_bandwidth of this PackageResponse.

        弹性带宽

        :param elastic_bandwidth: The elastic_bandwidth of this PackageResponse.
        :type elastic_bandwidth: int
        """
        self._elastic_bandwidth = elastic_bandwidth

    @property
    def service_bandwidth(self):
        """Gets the service_bandwidth of this PackageResponse.

        业务带宽

        :return: The service_bandwidth of this PackageResponse.
        :rtype: int
        """
        return self._service_bandwidth

    @service_bandwidth.setter
    def service_bandwidth(self, service_bandwidth):
        """Sets the service_bandwidth of this PackageResponse.

        业务带宽

        :param service_bandwidth: The service_bandwidth of this PackageResponse.
        :type service_bandwidth: int
        """
        self._service_bandwidth = service_bandwidth

    @property
    def clean_bandwidth(self):
        """Gets the clean_bandwidth of this PackageResponse.

        回源带宽

        :return: The clean_bandwidth of this PackageResponse.
        :rtype: int
        """
        return self._clean_bandwidth

    @clean_bandwidth.setter
    def clean_bandwidth(self, clean_bandwidth):
        """Sets the clean_bandwidth of this PackageResponse.

        回源带宽

        :param clean_bandwidth: The clean_bandwidth of this PackageResponse.
        :type clean_bandwidth: int
        """
        self._clean_bandwidth = clean_bandwidth

    @property
    def policy_num(self):
        """Gets the policy_num of this PackageResponse.

        策略模板数

        :return: The policy_num of this PackageResponse.
        :rtype: int
        """
        return self._policy_num

    @policy_num.setter
    def policy_num(self, policy_num):
        """Sets the policy_num of this PackageResponse.

        策略模板数

        :param policy_num: The policy_num of this PackageResponse.
        :type policy_num: int
        """
        self._policy_num = policy_num

    @property
    def is_old(self):
        """Gets the is_old of this PackageResponse.

        是否旧防护包（旧防护包不支持升级规格）,默认不传为否

        :return: The is_old of this PackageResponse.
        :rtype: bool
        """
        return self._is_old

    @is_old.setter
    def is_old(self, is_old):
        """Sets the is_old of this PackageResponse.

        是否旧防护包（旧防护包不支持升级规格）,默认不传为否

        :param is_old: The is_old of this PackageResponse.
        :type is_old: bool
        """
        self._is_old = is_old

    @property
    def new_flag(self):
        """Gets the new_flag of this PackageResponse.

        专业版铂金版合并之后购买的专业版和铂金版均标识为true

        :return: The new_flag of this PackageResponse.
        :rtype: bool
        """
        return self._new_flag

    @new_flag.setter
    def new_flag(self, new_flag):
        """Sets the new_flag of this PackageResponse.

        专业版铂金版合并之后购买的专业版和铂金版均标识为true

        :param new_flag: The new_flag of this PackageResponse.
        :type new_flag: bool
        """
        self._new_flag = new_flag

    @property
    def create_time(self):
        """Gets the create_time of this PackageResponse.

        创建时间

        :return: The create_time of this PackageResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this PackageResponse.

        创建时间

        :param create_time: The create_time of this PackageResponse.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, PackageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
