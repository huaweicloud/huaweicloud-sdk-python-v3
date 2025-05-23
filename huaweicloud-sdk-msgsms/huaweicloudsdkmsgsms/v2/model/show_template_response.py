# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'customer_id': 'str',
        'tenant': 'TenantBasic',
        'template_name': 'str',
        'template_id': 'str',
        'template_type': 'str',
        'app_name': 'str',
        'app_key': 'str',
        'sign_id': 'str',
        'template_content': 'str',
        'has_variable': 'str',
        'template_desc': 'str',
        'review_desc': 'str',
        'review_order': 'str',
        'flow_status': 'str',
        'universal_template': 'int',
        'status': 'str',
        'region': 'str',
        'brackets': 'str',
        'site': 'str',
        'urge_status': 'str',
        'urge_time': 'str',
        'urge_desc': 'str',
        'send_country1': 'int',
        'send_country2': 'int',
        'send_country3': 'int',
        'is_support_multiomp': 'bool',
        'country_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'customer_id': 'customer_id',
        'tenant': 'tenant',
        'template_name': 'template_name',
        'template_id': 'template_id',
        'template_type': 'template_type',
        'app_name': 'app_name',
        'app_key': 'app_key',
        'sign_id': 'sign_id',
        'template_content': 'template_content',
        'has_variable': 'has_variable',
        'template_desc': 'template_desc',
        'review_desc': 'review_desc',
        'review_order': 'review_order',
        'flow_status': 'flow_status',
        'universal_template': 'universal_template',
        'status': 'status',
        'region': 'region',
        'brackets': 'brackets',
        'site': 'site',
        'urge_status': 'urge_status',
        'urge_time': 'urge_time',
        'urge_desc': 'urge_desc',
        'send_country1': 'send_country1',
        'send_country2': 'send_country2',
        'send_country3': 'send_country3',
        'is_support_multiomp': 'is_support_multiomp',
        'country_name': 'country_name'
    }

    def __init__(self, id=None, create_time=None, update_time=None, customer_id=None, tenant=None, template_name=None, template_id=None, template_type=None, app_name=None, app_key=None, sign_id=None, template_content=None, has_variable=None, template_desc=None, review_desc=None, review_order=None, flow_status=None, universal_template=None, status=None, region=None, brackets=None, site=None, urge_status=None, urge_time=None, urge_desc=None, send_country1=None, send_country2=None, send_country3=None, is_support_multiomp=None, country_name=None):
        r"""ShowTemplateResponse

        The model defined in huaweicloud sdk

        :param id: 模板主键ID，用于获取、修改、删除模板以及查询模板变量的唯一标识
        :type id: str
        :param create_time: 创建时间[yyyy-MM-dd HH:mm:ss]
        :type create_time: str
        :param update_time: 更新时间[yyyy-MM-dd HH:mm:ss]
        :type update_time: str
        :param customer_id: 租户customer id
        :type customer_id: str
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkmsgsms.v2.TenantBasic`
        :param template_name: 模板名称
        :type template_name: str
        :param template_id: 模板ID
        :type template_id: str
        :param template_type: 模板类型
        :type template_type: str
        :param app_name: 应用名称
        :type app_name: str
        :param app_key: 应用key
        :type app_key: str
        :param sign_id: 签名主键id
        :type sign_id: str
        :param template_content: 模板内容
        :type template_content: str
        :param has_variable: 是否有变量
        :type has_variable: str
        :param template_desc: 申请描述
        :type template_desc: str
        :param review_desc: 审核意见
        :type review_desc: str
        :param review_order: 审核人账号
        :type review_order: str
        :param flow_status: 流程状态
        :type flow_status: str
        :param universal_template: 是否是通用模板
        :type universal_template: int
        :param status: 模板状态
        :type status: str
        :param region: 地域 1. cn：国内 2. intl：国际
        :type region: str
        :param brackets: 中括号类型 支持枚举值：  CN: 中文类型  GB: 英文类型
        :type brackets: str
        :param site: 站点
        :type site: str
        :param urge_status: 催审状态
        :type urge_status: str
        :param urge_time: 催审时间
        :type urge_time: str
        :param urge_desc: 催审描述
        :type urge_desc: str
        :param send_country1: 发送国家1
        :type send_country1: int
        :param send_country2: 发送国家2
        :type send_country2: int
        :param send_country3: 发送国家3
        :type send_country3: int
        :param is_support_multiomp: 是否支持多OMP
        :type is_support_multiomp: bool
        :param country_name: 国家名称列表，返回发送国家前三名的国家名称，国家名称间以\&quot;~\&quot;分隔
        :type country_name: str
        """
        
        super(ShowTemplateResponse, self).__init__()

        self._id = None
        self._create_time = None
        self._update_time = None
        self._customer_id = None
        self._tenant = None
        self._template_name = None
        self._template_id = None
        self._template_type = None
        self._app_name = None
        self._app_key = None
        self._sign_id = None
        self._template_content = None
        self._has_variable = None
        self._template_desc = None
        self._review_desc = None
        self._review_order = None
        self._flow_status = None
        self._universal_template = None
        self._status = None
        self._region = None
        self._brackets = None
        self._site = None
        self._urge_status = None
        self._urge_time = None
        self._urge_desc = None
        self._send_country1 = None
        self._send_country2 = None
        self._send_country3 = None
        self._is_support_multiomp = None
        self._country_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if customer_id is not None:
            self.customer_id = customer_id
        if tenant is not None:
            self.tenant = tenant
        if template_name is not None:
            self.template_name = template_name
        if template_id is not None:
            self.template_id = template_id
        if template_type is not None:
            self.template_type = template_type
        if app_name is not None:
            self.app_name = app_name
        if app_key is not None:
            self.app_key = app_key
        if sign_id is not None:
            self.sign_id = sign_id
        if template_content is not None:
            self.template_content = template_content
        if has_variable is not None:
            self.has_variable = has_variable
        if template_desc is not None:
            self.template_desc = template_desc
        if review_desc is not None:
            self.review_desc = review_desc
        if review_order is not None:
            self.review_order = review_order
        if flow_status is not None:
            self.flow_status = flow_status
        if universal_template is not None:
            self.universal_template = universal_template
        if status is not None:
            self.status = status
        if region is not None:
            self.region = region
        if brackets is not None:
            self.brackets = brackets
        if site is not None:
            self.site = site
        if urge_status is not None:
            self.urge_status = urge_status
        if urge_time is not None:
            self.urge_time = urge_time
        if urge_desc is not None:
            self.urge_desc = urge_desc
        if send_country1 is not None:
            self.send_country1 = send_country1
        if send_country2 is not None:
            self.send_country2 = send_country2
        if send_country3 is not None:
            self.send_country3 = send_country3
        if is_support_multiomp is not None:
            self.is_support_multiomp = is_support_multiomp
        if country_name is not None:
            self.country_name = country_name

    @property
    def id(self):
        r"""Gets the id of this ShowTemplateResponse.

        模板主键ID，用于获取、修改、删除模板以及查询模板变量的唯一标识

        :return: The id of this ShowTemplateResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowTemplateResponse.

        模板主键ID，用于获取、修改、删除模板以及查询模板变量的唯一标识

        :param id: The id of this ShowTemplateResponse.
        :type id: str
        """
        self._id = id

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowTemplateResponse.

        创建时间[yyyy-MM-dd HH:mm:ss]

        :return: The create_time of this ShowTemplateResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowTemplateResponse.

        创建时间[yyyy-MM-dd HH:mm:ss]

        :param create_time: The create_time of this ShowTemplateResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowTemplateResponse.

        更新时间[yyyy-MM-dd HH:mm:ss]

        :return: The update_time of this ShowTemplateResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowTemplateResponse.

        更新时间[yyyy-MM-dd HH:mm:ss]

        :param update_time: The update_time of this ShowTemplateResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def customer_id(self):
        r"""Gets the customer_id of this ShowTemplateResponse.

        租户customer id

        :return: The customer_id of this ShowTemplateResponse.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this ShowTemplateResponse.

        租户customer id

        :param customer_id: The customer_id of this ShowTemplateResponse.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def tenant(self):
        r"""Gets the tenant of this ShowTemplateResponse.

        :return: The tenant of this ShowTemplateResponse.
        :rtype: :class:`huaweicloudsdkmsgsms.v2.TenantBasic`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        r"""Sets the tenant of this ShowTemplateResponse.

        :param tenant: The tenant of this ShowTemplateResponse.
        :type tenant: :class:`huaweicloudsdkmsgsms.v2.TenantBasic`
        """
        self._tenant = tenant

    @property
    def template_name(self):
        r"""Gets the template_name of this ShowTemplateResponse.

        模板名称

        :return: The template_name of this ShowTemplateResponse.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this ShowTemplateResponse.

        模板名称

        :param template_name: The template_name of this ShowTemplateResponse.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_id(self):
        r"""Gets the template_id of this ShowTemplateResponse.

        模板ID

        :return: The template_id of this ShowTemplateResponse.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ShowTemplateResponse.

        模板ID

        :param template_id: The template_id of this ShowTemplateResponse.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_type(self):
        r"""Gets the template_type of this ShowTemplateResponse.

        模板类型

        :return: The template_type of this ShowTemplateResponse.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        r"""Sets the template_type of this ShowTemplateResponse.

        模板类型

        :param template_type: The template_type of this ShowTemplateResponse.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def app_name(self):
        r"""Gets the app_name of this ShowTemplateResponse.

        应用名称

        :return: The app_name of this ShowTemplateResponse.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ShowTemplateResponse.

        应用名称

        :param app_name: The app_name of this ShowTemplateResponse.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_key(self):
        r"""Gets the app_key of this ShowTemplateResponse.

        应用key

        :return: The app_key of this ShowTemplateResponse.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        r"""Sets the app_key of this ShowTemplateResponse.

        应用key

        :param app_key: The app_key of this ShowTemplateResponse.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def sign_id(self):
        r"""Gets the sign_id of this ShowTemplateResponse.

        签名主键id

        :return: The sign_id of this ShowTemplateResponse.
        :rtype: str
        """
        return self._sign_id

    @sign_id.setter
    def sign_id(self, sign_id):
        r"""Sets the sign_id of this ShowTemplateResponse.

        签名主键id

        :param sign_id: The sign_id of this ShowTemplateResponse.
        :type sign_id: str
        """
        self._sign_id = sign_id

    @property
    def template_content(self):
        r"""Gets the template_content of this ShowTemplateResponse.

        模板内容

        :return: The template_content of this ShowTemplateResponse.
        :rtype: str
        """
        return self._template_content

    @template_content.setter
    def template_content(self, template_content):
        r"""Sets the template_content of this ShowTemplateResponse.

        模板内容

        :param template_content: The template_content of this ShowTemplateResponse.
        :type template_content: str
        """
        self._template_content = template_content

    @property
    def has_variable(self):
        r"""Gets the has_variable of this ShowTemplateResponse.

        是否有变量

        :return: The has_variable of this ShowTemplateResponse.
        :rtype: str
        """
        return self._has_variable

    @has_variable.setter
    def has_variable(self, has_variable):
        r"""Sets the has_variable of this ShowTemplateResponse.

        是否有变量

        :param has_variable: The has_variable of this ShowTemplateResponse.
        :type has_variable: str
        """
        self._has_variable = has_variable

    @property
    def template_desc(self):
        r"""Gets the template_desc of this ShowTemplateResponse.

        申请描述

        :return: The template_desc of this ShowTemplateResponse.
        :rtype: str
        """
        return self._template_desc

    @template_desc.setter
    def template_desc(self, template_desc):
        r"""Sets the template_desc of this ShowTemplateResponse.

        申请描述

        :param template_desc: The template_desc of this ShowTemplateResponse.
        :type template_desc: str
        """
        self._template_desc = template_desc

    @property
    def review_desc(self):
        r"""Gets the review_desc of this ShowTemplateResponse.

        审核意见

        :return: The review_desc of this ShowTemplateResponse.
        :rtype: str
        """
        return self._review_desc

    @review_desc.setter
    def review_desc(self, review_desc):
        r"""Sets the review_desc of this ShowTemplateResponse.

        审核意见

        :param review_desc: The review_desc of this ShowTemplateResponse.
        :type review_desc: str
        """
        self._review_desc = review_desc

    @property
    def review_order(self):
        r"""Gets the review_order of this ShowTemplateResponse.

        审核人账号

        :return: The review_order of this ShowTemplateResponse.
        :rtype: str
        """
        return self._review_order

    @review_order.setter
    def review_order(self, review_order):
        r"""Sets the review_order of this ShowTemplateResponse.

        审核人账号

        :param review_order: The review_order of this ShowTemplateResponse.
        :type review_order: str
        """
        self._review_order = review_order

    @property
    def flow_status(self):
        r"""Gets the flow_status of this ShowTemplateResponse.

        流程状态

        :return: The flow_status of this ShowTemplateResponse.
        :rtype: str
        """
        return self._flow_status

    @flow_status.setter
    def flow_status(self, flow_status):
        r"""Sets the flow_status of this ShowTemplateResponse.

        流程状态

        :param flow_status: The flow_status of this ShowTemplateResponse.
        :type flow_status: str
        """
        self._flow_status = flow_status

    @property
    def universal_template(self):
        r"""Gets the universal_template of this ShowTemplateResponse.

        是否是通用模板

        :return: The universal_template of this ShowTemplateResponse.
        :rtype: int
        """
        return self._universal_template

    @universal_template.setter
    def universal_template(self, universal_template):
        r"""Sets the universal_template of this ShowTemplateResponse.

        是否是通用模板

        :param universal_template: The universal_template of this ShowTemplateResponse.
        :type universal_template: int
        """
        self._universal_template = universal_template

    @property
    def status(self):
        r"""Gets the status of this ShowTemplateResponse.

        模板状态

        :return: The status of this ShowTemplateResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowTemplateResponse.

        模板状态

        :param status: The status of this ShowTemplateResponse.
        :type status: str
        """
        self._status = status

    @property
    def region(self):
        r"""Gets the region of this ShowTemplateResponse.

        地域 1. cn：国内 2. intl：国际

        :return: The region of this ShowTemplateResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ShowTemplateResponse.

        地域 1. cn：国内 2. intl：国际

        :param region: The region of this ShowTemplateResponse.
        :type region: str
        """
        self._region = region

    @property
    def brackets(self):
        r"""Gets the brackets of this ShowTemplateResponse.

        中括号类型 支持枚举值：  CN: 中文类型  GB: 英文类型

        :return: The brackets of this ShowTemplateResponse.
        :rtype: str
        """
        return self._brackets

    @brackets.setter
    def brackets(self, brackets):
        r"""Sets the brackets of this ShowTemplateResponse.

        中括号类型 支持枚举值：  CN: 中文类型  GB: 英文类型

        :param brackets: The brackets of this ShowTemplateResponse.
        :type brackets: str
        """
        self._brackets = brackets

    @property
    def site(self):
        r"""Gets the site of this ShowTemplateResponse.

        站点

        :return: The site of this ShowTemplateResponse.
        :rtype: str
        """
        return self._site

    @site.setter
    def site(self, site):
        r"""Sets the site of this ShowTemplateResponse.

        站点

        :param site: The site of this ShowTemplateResponse.
        :type site: str
        """
        self._site = site

    @property
    def urge_status(self):
        r"""Gets the urge_status of this ShowTemplateResponse.

        催审状态

        :return: The urge_status of this ShowTemplateResponse.
        :rtype: str
        """
        return self._urge_status

    @urge_status.setter
    def urge_status(self, urge_status):
        r"""Sets the urge_status of this ShowTemplateResponse.

        催审状态

        :param urge_status: The urge_status of this ShowTemplateResponse.
        :type urge_status: str
        """
        self._urge_status = urge_status

    @property
    def urge_time(self):
        r"""Gets the urge_time of this ShowTemplateResponse.

        催审时间

        :return: The urge_time of this ShowTemplateResponse.
        :rtype: str
        """
        return self._urge_time

    @urge_time.setter
    def urge_time(self, urge_time):
        r"""Sets the urge_time of this ShowTemplateResponse.

        催审时间

        :param urge_time: The urge_time of this ShowTemplateResponse.
        :type urge_time: str
        """
        self._urge_time = urge_time

    @property
    def urge_desc(self):
        r"""Gets the urge_desc of this ShowTemplateResponse.

        催审描述

        :return: The urge_desc of this ShowTemplateResponse.
        :rtype: str
        """
        return self._urge_desc

    @urge_desc.setter
    def urge_desc(self, urge_desc):
        r"""Sets the urge_desc of this ShowTemplateResponse.

        催审描述

        :param urge_desc: The urge_desc of this ShowTemplateResponse.
        :type urge_desc: str
        """
        self._urge_desc = urge_desc

    @property
    def send_country1(self):
        r"""Gets the send_country1 of this ShowTemplateResponse.

        发送国家1

        :return: The send_country1 of this ShowTemplateResponse.
        :rtype: int
        """
        return self._send_country1

    @send_country1.setter
    def send_country1(self, send_country1):
        r"""Sets the send_country1 of this ShowTemplateResponse.

        发送国家1

        :param send_country1: The send_country1 of this ShowTemplateResponse.
        :type send_country1: int
        """
        self._send_country1 = send_country1

    @property
    def send_country2(self):
        r"""Gets the send_country2 of this ShowTemplateResponse.

        发送国家2

        :return: The send_country2 of this ShowTemplateResponse.
        :rtype: int
        """
        return self._send_country2

    @send_country2.setter
    def send_country2(self, send_country2):
        r"""Sets the send_country2 of this ShowTemplateResponse.

        发送国家2

        :param send_country2: The send_country2 of this ShowTemplateResponse.
        :type send_country2: int
        """
        self._send_country2 = send_country2

    @property
    def send_country3(self):
        r"""Gets the send_country3 of this ShowTemplateResponse.

        发送国家3

        :return: The send_country3 of this ShowTemplateResponse.
        :rtype: int
        """
        return self._send_country3

    @send_country3.setter
    def send_country3(self, send_country3):
        r"""Sets the send_country3 of this ShowTemplateResponse.

        发送国家3

        :param send_country3: The send_country3 of this ShowTemplateResponse.
        :type send_country3: int
        """
        self._send_country3 = send_country3

    @property
    def is_support_multiomp(self):
        r"""Gets the is_support_multiomp of this ShowTemplateResponse.

        是否支持多OMP

        :return: The is_support_multiomp of this ShowTemplateResponse.
        :rtype: bool
        """
        return self._is_support_multiomp

    @is_support_multiomp.setter
    def is_support_multiomp(self, is_support_multiomp):
        r"""Sets the is_support_multiomp of this ShowTemplateResponse.

        是否支持多OMP

        :param is_support_multiomp: The is_support_multiomp of this ShowTemplateResponse.
        :type is_support_multiomp: bool
        """
        self._is_support_multiomp = is_support_multiomp

    @property
    def country_name(self):
        r"""Gets the country_name of this ShowTemplateResponse.

        国家名称列表，返回发送国家前三名的国家名称，国家名称间以\"~\"分隔

        :return: The country_name of this ShowTemplateResponse.
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        r"""Sets the country_name of this ShowTemplateResponse.

        国家名称列表，返回发送国家前三名的国家名称，国家名称间以\"~\"分隔

        :param country_name: The country_name of this ShowTemplateResponse.
        :type country_name: str
        """
        self._country_name = country_name

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
        if not isinstance(other, ShowTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
