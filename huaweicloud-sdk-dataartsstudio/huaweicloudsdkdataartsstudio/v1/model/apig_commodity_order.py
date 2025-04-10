# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApigCommodityOrder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'order_id': 'str',
        'region_id': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'subscription_id': 'str',
        'resource_type': 'str',
        'resource_spec_code': 'str',
        'product_id': 'str',
        'order_type': 'str',
        'charge_type': 'str',
        'is_auto_renew': 'int',
        'status': 'int',
        'vpc_id': 'str',
        'security_group_id': 'str',
        'eps_id': 'str',
        'effective_time': 'float',
        'expire_days': 'str',
        'expire_time': 'float',
        'lock_check_endpoint': 'str',
        'create_user': 'str',
        'create_time': 'float',
        'domain_id': 'str',
        'is_trial_order': 'int',
        'work_space_mode': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'order_id': 'order_id',
        'region_id': 'region_id',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'subscription_id': 'subscription_id',
        'resource_type': 'resource_type',
        'resource_spec_code': 'resource_spec_code',
        'product_id': 'product_id',
        'order_type': 'order_type',
        'charge_type': 'charge_type',
        'is_auto_renew': 'is_auto_renew',
        'status': 'status',
        'vpc_id': 'vpc_id',
        'security_group_id': 'security_group_id',
        'eps_id': 'eps_id',
        'effective_time': 'effective_time',
        'expire_days': 'expire_days',
        'expire_time': 'expire_time',
        'lock_check_endpoint': 'lock_check_endpoint',
        'create_user': 'create_user',
        'create_time': 'create_time',
        'domain_id': 'domain_id',
        'is_trial_order': 'is_trial_order',
        'work_space_mode': 'work_space_mode'
    }

    def __init__(self, project_id=None, order_id=None, region_id=None, resource_id=None, resource_name=None, subscription_id=None, resource_type=None, resource_spec_code=None, product_id=None, order_type=None, charge_type=None, is_auto_renew=None, status=None, vpc_id=None, security_group_id=None, eps_id=None, effective_time=None, expire_days=None, expire_time=None, lock_check_endpoint=None, create_user=None, create_time=None, domain_id=None, is_trial_order=None, work_space_mode=None):
        r"""ApigCommodityOrder

        The model defined in huaweicloud sdk

        :param project_id: 实例所属项目id
        :type project_id: str
        :param order_id: CBC订单id
        :type order_id: str
        :param region_id: 当前所属region Id
        :type region_id: str
        :param resource_id: 实例id
        :type resource_id: str
        :param resource_name: 实例名称
        :type resource_name: str
        :param subscription_id: CBC订购id
        :type subscription_id: str
        :param resource_type: 资源类型，hws.resource.type.dayu
        :type resource_type: str
        :param resource_spec_code: 产品规格编码，例如dayu.starter，dayu.basic，dayu.advanced等
        :type resource_spec_code: str
        :param product_id: CBC产品id，未安装CBC的环境无需这个值
        :type product_id: str
        :param order_type: 订单类型标识符
        :type order_type: str
        :param charge_type: 支付选项，留空
        :type charge_type: str
        :param is_auto_renew: 自动续费标识，当前实例为按需支付时必填，0代表不续费，1代表自动续费
        :type is_auto_renew: int
        :param status: 实例状态,1未生效2生效中3已删除&#x3D;退订4保留期&#x3D;冻结5宽限期6删除中
        :type status: int
        :param vpc_id: 虚拟私有云id
        :type vpc_id: str
        :param security_group_id: 安全组id
        :type security_group_id: str
        :param eps_id: 企业项目id，如果当前为公有云，且用户开启企业项目，则必选
        :type eps_id: str
        :param effective_time: 生效时间点，包周期实例有效
        :type effective_time: float
        :param expire_days: 过期时间天数，包周期实例有效
        :type expire_days: str
        :param expire_time: 过期时间点，包周期有效
        :type expire_time: float
        :param lock_check_endpoint: CBC锁定节点
        :type lock_check_endpoint: str
        :param create_user: 创建用户
        :type create_user: str
        :param create_time: 创建时间点
        :type create_time: float
        :param domain_id: 用户domain id
        :type domain_id: str
        :param is_trial_order: 是否试用订单
        :type is_trial_order: int
        :param work_space_mode: 工作空间模式说明
        :type work_space_mode: str
        """
        
        

        self._project_id = None
        self._order_id = None
        self._region_id = None
        self._resource_id = None
        self._resource_name = None
        self._subscription_id = None
        self._resource_type = None
        self._resource_spec_code = None
        self._product_id = None
        self._order_type = None
        self._charge_type = None
        self._is_auto_renew = None
        self._status = None
        self._vpc_id = None
        self._security_group_id = None
        self._eps_id = None
        self._effective_time = None
        self._expire_days = None
        self._expire_time = None
        self._lock_check_endpoint = None
        self._create_user = None
        self._create_time = None
        self._domain_id = None
        self._is_trial_order = None
        self._work_space_mode = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if order_id is not None:
            self.order_id = order_id
        if region_id is not None:
            self.region_id = region_id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if product_id is not None:
            self.product_id = product_id
        if order_type is not None:
            self.order_type = order_type
        if charge_type is not None:
            self.charge_type = charge_type
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if status is not None:
            self.status = status
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if eps_id is not None:
            self.eps_id = eps_id
        if effective_time is not None:
            self.effective_time = effective_time
        if expire_days is not None:
            self.expire_days = expire_days
        if expire_time is not None:
            self.expire_time = expire_time
        if lock_check_endpoint is not None:
            self.lock_check_endpoint = lock_check_endpoint
        if create_user is not None:
            self.create_user = create_user
        if create_time is not None:
            self.create_time = create_time
        if domain_id is not None:
            self.domain_id = domain_id
        if is_trial_order is not None:
            self.is_trial_order = is_trial_order
        if work_space_mode is not None:
            self.work_space_mode = work_space_mode

    @property
    def project_id(self):
        r"""Gets the project_id of this ApigCommodityOrder.

        实例所属项目id

        :return: The project_id of this ApigCommodityOrder.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ApigCommodityOrder.

        实例所属项目id

        :param project_id: The project_id of this ApigCommodityOrder.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def order_id(self):
        r"""Gets the order_id of this ApigCommodityOrder.

        CBC订单id

        :return: The order_id of this ApigCommodityOrder.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ApigCommodityOrder.

        CBC订单id

        :param order_id: The order_id of this ApigCommodityOrder.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ApigCommodityOrder.

        当前所属region Id

        :return: The region_id of this ApigCommodityOrder.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ApigCommodityOrder.

        当前所属region Id

        :param region_id: The region_id of this ApigCommodityOrder.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ApigCommodityOrder.

        实例id

        :return: The resource_id of this ApigCommodityOrder.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ApigCommodityOrder.

        实例id

        :param resource_id: The resource_id of this ApigCommodityOrder.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ApigCommodityOrder.

        实例名称

        :return: The resource_name of this ApigCommodityOrder.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ApigCommodityOrder.

        实例名称

        :param resource_name: The resource_name of this ApigCommodityOrder.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def subscription_id(self):
        r"""Gets the subscription_id of this ApigCommodityOrder.

        CBC订购id

        :return: The subscription_id of this ApigCommodityOrder.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        r"""Sets the subscription_id of this ApigCommodityOrder.

        CBC订购id

        :param subscription_id: The subscription_id of this ApigCommodityOrder.
        :type subscription_id: str
        """
        self._subscription_id = subscription_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ApigCommodityOrder.

        资源类型，hws.resource.type.dayu

        :return: The resource_type of this ApigCommodityOrder.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ApigCommodityOrder.

        资源类型，hws.resource.type.dayu

        :param resource_type: The resource_type of this ApigCommodityOrder.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this ApigCommodityOrder.

        产品规格编码，例如dayu.starter，dayu.basic，dayu.advanced等

        :return: The resource_spec_code of this ApigCommodityOrder.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this ApigCommodityOrder.

        产品规格编码，例如dayu.starter，dayu.basic，dayu.advanced等

        :param resource_spec_code: The resource_spec_code of this ApigCommodityOrder.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def product_id(self):
        r"""Gets the product_id of this ApigCommodityOrder.

        CBC产品id，未安装CBC的环境无需这个值

        :return: The product_id of this ApigCommodityOrder.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ApigCommodityOrder.

        CBC产品id，未安装CBC的环境无需这个值

        :param product_id: The product_id of this ApigCommodityOrder.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def order_type(self):
        r"""Gets the order_type of this ApigCommodityOrder.

        订单类型标识符

        :return: The order_type of this ApigCommodityOrder.
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        r"""Sets the order_type of this ApigCommodityOrder.

        订单类型标识符

        :param order_type: The order_type of this ApigCommodityOrder.
        :type order_type: str
        """
        self._order_type = order_type

    @property
    def charge_type(self):
        r"""Gets the charge_type of this ApigCommodityOrder.

        支付选项，留空

        :return: The charge_type of this ApigCommodityOrder.
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        r"""Sets the charge_type of this ApigCommodityOrder.

        支付选项，留空

        :param charge_type: The charge_type of this ApigCommodityOrder.
        :type charge_type: str
        """
        self._charge_type = charge_type

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this ApigCommodityOrder.

        自动续费标识，当前实例为按需支付时必填，0代表不续费，1代表自动续费

        :return: The is_auto_renew of this ApigCommodityOrder.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this ApigCommodityOrder.

        自动续费标识，当前实例为按需支付时必填，0代表不续费，1代表自动续费

        :param is_auto_renew: The is_auto_renew of this ApigCommodityOrder.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

    @property
    def status(self):
        r"""Gets the status of this ApigCommodityOrder.

        实例状态,1未生效2生效中3已删除=退订4保留期=冻结5宽限期6删除中

        :return: The status of this ApigCommodityOrder.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ApigCommodityOrder.

        实例状态,1未生效2生效中3已删除=退订4保留期=冻结5宽限期6删除中

        :param status: The status of this ApigCommodityOrder.
        :type status: int
        """
        self._status = status

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ApigCommodityOrder.

        虚拟私有云id

        :return: The vpc_id of this ApigCommodityOrder.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ApigCommodityOrder.

        虚拟私有云id

        :param vpc_id: The vpc_id of this ApigCommodityOrder.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this ApigCommodityOrder.

        安全组id

        :return: The security_group_id of this ApigCommodityOrder.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this ApigCommodityOrder.

        安全组id

        :param security_group_id: The security_group_id of this ApigCommodityOrder.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def eps_id(self):
        r"""Gets the eps_id of this ApigCommodityOrder.

        企业项目id，如果当前为公有云，且用户开启企业项目，则必选

        :return: The eps_id of this ApigCommodityOrder.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        r"""Sets the eps_id of this ApigCommodityOrder.

        企业项目id，如果当前为公有云，且用户开启企业项目，则必选

        :param eps_id: The eps_id of this ApigCommodityOrder.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def effective_time(self):
        r"""Gets the effective_time of this ApigCommodityOrder.

        生效时间点，包周期实例有效

        :return: The effective_time of this ApigCommodityOrder.
        :rtype: float
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        r"""Sets the effective_time of this ApigCommodityOrder.

        生效时间点，包周期实例有效

        :param effective_time: The effective_time of this ApigCommodityOrder.
        :type effective_time: float
        """
        self._effective_time = effective_time

    @property
    def expire_days(self):
        r"""Gets the expire_days of this ApigCommodityOrder.

        过期时间天数，包周期实例有效

        :return: The expire_days of this ApigCommodityOrder.
        :rtype: str
        """
        return self._expire_days

    @expire_days.setter
    def expire_days(self, expire_days):
        r"""Sets the expire_days of this ApigCommodityOrder.

        过期时间天数，包周期实例有效

        :param expire_days: The expire_days of this ApigCommodityOrder.
        :type expire_days: str
        """
        self._expire_days = expire_days

    @property
    def expire_time(self):
        r"""Gets the expire_time of this ApigCommodityOrder.

        过期时间点，包周期有效

        :return: The expire_time of this ApigCommodityOrder.
        :rtype: float
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this ApigCommodityOrder.

        过期时间点，包周期有效

        :param expire_time: The expire_time of this ApigCommodityOrder.
        :type expire_time: float
        """
        self._expire_time = expire_time

    @property
    def lock_check_endpoint(self):
        r"""Gets the lock_check_endpoint of this ApigCommodityOrder.

        CBC锁定节点

        :return: The lock_check_endpoint of this ApigCommodityOrder.
        :rtype: str
        """
        return self._lock_check_endpoint

    @lock_check_endpoint.setter
    def lock_check_endpoint(self, lock_check_endpoint):
        r"""Sets the lock_check_endpoint of this ApigCommodityOrder.

        CBC锁定节点

        :param lock_check_endpoint: The lock_check_endpoint of this ApigCommodityOrder.
        :type lock_check_endpoint: str
        """
        self._lock_check_endpoint = lock_check_endpoint

    @property
    def create_user(self):
        r"""Gets the create_user of this ApigCommodityOrder.

        创建用户

        :return: The create_user of this ApigCommodityOrder.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ApigCommodityOrder.

        创建用户

        :param create_user: The create_user of this ApigCommodityOrder.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def create_time(self):
        r"""Gets the create_time of this ApigCommodityOrder.

        创建时间点

        :return: The create_time of this ApigCommodityOrder.
        :rtype: float
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ApigCommodityOrder.

        创建时间点

        :param create_time: The create_time of this ApigCommodityOrder.
        :type create_time: float
        """
        self._create_time = create_time

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ApigCommodityOrder.

        用户domain id

        :return: The domain_id of this ApigCommodityOrder.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ApigCommodityOrder.

        用户domain id

        :param domain_id: The domain_id of this ApigCommodityOrder.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def is_trial_order(self):
        r"""Gets the is_trial_order of this ApigCommodityOrder.

        是否试用订单

        :return: The is_trial_order of this ApigCommodityOrder.
        :rtype: int
        """
        return self._is_trial_order

    @is_trial_order.setter
    def is_trial_order(self, is_trial_order):
        r"""Sets the is_trial_order of this ApigCommodityOrder.

        是否试用订单

        :param is_trial_order: The is_trial_order of this ApigCommodityOrder.
        :type is_trial_order: int
        """
        self._is_trial_order = is_trial_order

    @property
    def work_space_mode(self):
        r"""Gets the work_space_mode of this ApigCommodityOrder.

        工作空间模式说明

        :return: The work_space_mode of this ApigCommodityOrder.
        :rtype: str
        """
        return self._work_space_mode

    @work_space_mode.setter
    def work_space_mode(self, work_space_mode):
        r"""Sets the work_space_mode of this ApigCommodityOrder.

        工作空间模式说明

        :param work_space_mode: The work_space_mode of this ApigCommodityOrder.
        :type work_space_mode: str
        """
        self._work_space_mode = work_space_mode

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
        if not isinstance(other, ApigCommodityOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
