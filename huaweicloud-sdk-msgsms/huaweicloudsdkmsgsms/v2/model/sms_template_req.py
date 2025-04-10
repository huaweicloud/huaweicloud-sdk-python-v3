# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmsTemplateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'brackets': 'str',
        'region': 'str',
        'send_country': 'list[int]',
        'sign_id': 'str',
        'template_content': 'str',
        'template_desc': 'str',
        'template_name': 'str',
        'template_type': 'str',
        'universal_template': 'int',
        'variable_attributes': 'list[SmsTemplateVariableAttrReq]',
        'flow_status': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'brackets': 'brackets',
        'region': 'region',
        'send_country': 'send_country',
        'sign_id': 'sign_id',
        'template_content': 'template_content',
        'template_desc': 'template_desc',
        'template_name': 'template_name',
        'template_type': 'template_type',
        'universal_template': 'universal_template',
        'variable_attributes': 'variable_attributes',
        'flow_status': 'flow_status'
    }

    def __init__(self, app_id=None, brackets=None, region=None, send_country=None, sign_id=None, template_content=None, template_desc=None, template_name=None, template_type=None, universal_template=None, variable_attributes=None, flow_status=None):
        r"""SmsTemplateReq

        The model defined in huaweicloud sdk

        :param app_id: 应用主键ID
        :type app_id: str
        :param brackets: 中括号类型。支持枚举值： 1. CN: 中文类型 2. GB: 英文类型
        :type brackets: str
        :param region: 地域 1. cn：国内 2. intl：
        :type region: str
        :param send_country: 发送国家id列表，只有地域为国际时，该字段有效
        :type send_country: list[int]
        :param sign_id: 签名主键ID，只有地域为国内时，该字段有效
        :type sign_id: str
        :param template_content: 模板内容
        :type template_content: str
        :param template_desc: 模板描述
        :type template_desc: str
        :param template_name: 模板名称
        :type template_name: str
        :param template_type: 模板类型。只有地域为国内时，该字段有效。支持枚举值： 1. VERIFY_CODE_TYPE: 验证码类 2. PROMOTION_TYPE: 推广类 3. NOTIFY_TYPE: 通知类
        :type template_type: str
        :param universal_template: 是否为通用模板 1. 0: 非通用模板 2. 1: 通用模板
        :type universal_template: int
        :param variable_attributes: 模板参数
        :type variable_attributes: list[:class:`huaweicloudsdkmsgsms.v2.SmsTemplateVariableAttrReq`]
        :param flow_status: 流程状态 1. Pending: 待提交 2. Reviewing: 待审核 3. Disable：停用
        :type flow_status: str
        """
        
        

        self._app_id = None
        self._brackets = None
        self._region = None
        self._send_country = None
        self._sign_id = None
        self._template_content = None
        self._template_desc = None
        self._template_name = None
        self._template_type = None
        self._universal_template = None
        self._variable_attributes = None
        self._flow_status = None
        self.discriminator = None

        self.app_id = app_id
        if brackets is not None:
            self.brackets = brackets
        self.region = region
        if send_country is not None:
            self.send_country = send_country
        if sign_id is not None:
            self.sign_id = sign_id
        self.template_content = template_content
        if template_desc is not None:
            self.template_desc = template_desc
        self.template_name = template_name
        self.template_type = template_type
        if universal_template is not None:
            self.universal_template = universal_template
        if variable_attributes is not None:
            self.variable_attributes = variable_attributes
        if flow_status is not None:
            self.flow_status = flow_status

    @property
    def app_id(self):
        r"""Gets the app_id of this SmsTemplateReq.

        应用主键ID

        :return: The app_id of this SmsTemplateReq.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this SmsTemplateReq.

        应用主键ID

        :param app_id: The app_id of this SmsTemplateReq.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def brackets(self):
        r"""Gets the brackets of this SmsTemplateReq.

        中括号类型。支持枚举值： 1. CN: 中文类型 2. GB: 英文类型

        :return: The brackets of this SmsTemplateReq.
        :rtype: str
        """
        return self._brackets

    @brackets.setter
    def brackets(self, brackets):
        r"""Sets the brackets of this SmsTemplateReq.

        中括号类型。支持枚举值： 1. CN: 中文类型 2. GB: 英文类型

        :param brackets: The brackets of this SmsTemplateReq.
        :type brackets: str
        """
        self._brackets = brackets

    @property
    def region(self):
        r"""Gets the region of this SmsTemplateReq.

        地域 1. cn：国内 2. intl：

        :return: The region of this SmsTemplateReq.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this SmsTemplateReq.

        地域 1. cn：国内 2. intl：

        :param region: The region of this SmsTemplateReq.
        :type region: str
        """
        self._region = region

    @property
    def send_country(self):
        r"""Gets the send_country of this SmsTemplateReq.

        发送国家id列表，只有地域为国际时，该字段有效

        :return: The send_country of this SmsTemplateReq.
        :rtype: list[int]
        """
        return self._send_country

    @send_country.setter
    def send_country(self, send_country):
        r"""Sets the send_country of this SmsTemplateReq.

        发送国家id列表，只有地域为国际时，该字段有效

        :param send_country: The send_country of this SmsTemplateReq.
        :type send_country: list[int]
        """
        self._send_country = send_country

    @property
    def sign_id(self):
        r"""Gets the sign_id of this SmsTemplateReq.

        签名主键ID，只有地域为国内时，该字段有效

        :return: The sign_id of this SmsTemplateReq.
        :rtype: str
        """
        return self._sign_id

    @sign_id.setter
    def sign_id(self, sign_id):
        r"""Sets the sign_id of this SmsTemplateReq.

        签名主键ID，只有地域为国内时，该字段有效

        :param sign_id: The sign_id of this SmsTemplateReq.
        :type sign_id: str
        """
        self._sign_id = sign_id

    @property
    def template_content(self):
        r"""Gets the template_content of this SmsTemplateReq.

        模板内容

        :return: The template_content of this SmsTemplateReq.
        :rtype: str
        """
        return self._template_content

    @template_content.setter
    def template_content(self, template_content):
        r"""Sets the template_content of this SmsTemplateReq.

        模板内容

        :param template_content: The template_content of this SmsTemplateReq.
        :type template_content: str
        """
        self._template_content = template_content

    @property
    def template_desc(self):
        r"""Gets the template_desc of this SmsTemplateReq.

        模板描述

        :return: The template_desc of this SmsTemplateReq.
        :rtype: str
        """
        return self._template_desc

    @template_desc.setter
    def template_desc(self, template_desc):
        r"""Sets the template_desc of this SmsTemplateReq.

        模板描述

        :param template_desc: The template_desc of this SmsTemplateReq.
        :type template_desc: str
        """
        self._template_desc = template_desc

    @property
    def template_name(self):
        r"""Gets the template_name of this SmsTemplateReq.

        模板名称

        :return: The template_name of this SmsTemplateReq.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this SmsTemplateReq.

        模板名称

        :param template_name: The template_name of this SmsTemplateReq.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_type(self):
        r"""Gets the template_type of this SmsTemplateReq.

        模板类型。只有地域为国内时，该字段有效。支持枚举值： 1. VERIFY_CODE_TYPE: 验证码类 2. PROMOTION_TYPE: 推广类 3. NOTIFY_TYPE: 通知类

        :return: The template_type of this SmsTemplateReq.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        r"""Sets the template_type of this SmsTemplateReq.

        模板类型。只有地域为国内时，该字段有效。支持枚举值： 1. VERIFY_CODE_TYPE: 验证码类 2. PROMOTION_TYPE: 推广类 3. NOTIFY_TYPE: 通知类

        :param template_type: The template_type of this SmsTemplateReq.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def universal_template(self):
        r"""Gets the universal_template of this SmsTemplateReq.

        是否为通用模板 1. 0: 非通用模板 2. 1: 通用模板

        :return: The universal_template of this SmsTemplateReq.
        :rtype: int
        """
        return self._universal_template

    @universal_template.setter
    def universal_template(self, universal_template):
        r"""Sets the universal_template of this SmsTemplateReq.

        是否为通用模板 1. 0: 非通用模板 2. 1: 通用模板

        :param universal_template: The universal_template of this SmsTemplateReq.
        :type universal_template: int
        """
        self._universal_template = universal_template

    @property
    def variable_attributes(self):
        r"""Gets the variable_attributes of this SmsTemplateReq.

        模板参数

        :return: The variable_attributes of this SmsTemplateReq.
        :rtype: list[:class:`huaweicloudsdkmsgsms.v2.SmsTemplateVariableAttrReq`]
        """
        return self._variable_attributes

    @variable_attributes.setter
    def variable_attributes(self, variable_attributes):
        r"""Sets the variable_attributes of this SmsTemplateReq.

        模板参数

        :param variable_attributes: The variable_attributes of this SmsTemplateReq.
        :type variable_attributes: list[:class:`huaweicloudsdkmsgsms.v2.SmsTemplateVariableAttrReq`]
        """
        self._variable_attributes = variable_attributes

    @property
    def flow_status(self):
        r"""Gets the flow_status of this SmsTemplateReq.

        流程状态 1. Pending: 待提交 2. Reviewing: 待审核 3. Disable：停用

        :return: The flow_status of this SmsTemplateReq.
        :rtype: str
        """
        return self._flow_status

    @flow_status.setter
    def flow_status(self, flow_status):
        r"""Sets the flow_status of this SmsTemplateReq.

        流程状态 1. Pending: 待提交 2. Reviewing: 待审核 3. Disable：停用

        :param flow_status: The flow_status of this SmsTemplateReq.
        :type flow_status: str
        """
        self._flow_status = flow_status

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
        if not isinstance(other, SmsTemplateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
