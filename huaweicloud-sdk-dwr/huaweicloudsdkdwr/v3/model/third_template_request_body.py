# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThirdTemplateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'inputs': 'list[Input]',
        'dynamic_source_definition': 'dict(str, object)',
        'need_policy': 'list[Policy]',
        'func_provider': 'dict(str, str)',
        'func_name': 'dict(str, str)',
        'func_description': 'dict(str, str)',
        'func_link': 'dict(str, str)',
        'app_urn': 'str',
        'bill_value': 'float',
        'agency': 'str',
        'register_status': 'str'
    }

    attribute_map = {
        'category': 'category',
        'inputs': 'inputs',
        'dynamic_source_definition': 'dynamic_source_definition',
        'need_policy': 'need_policy',
        'func_provider': 'func_provider',
        'func_name': 'func_name',
        'func_description': 'func_description',
        'func_link': 'func_link',
        'app_urn': 'app_urn',
        'bill_value': 'bill_value',
        'agency': 'agency',
        'register_status': 'register_status'
    }

    def __init__(self, category=None, inputs=None, dynamic_source_definition=None, need_policy=None, func_provider=None, func_name=None, func_description=None, func_link=None, app_urn=None, bill_value=None, agency=None, register_status=None):
        r"""ThirdTemplateRequestBody

        The model defined in huaweicloud sdk

        :param category: 必须以字母或数字开头，只能由字母、数字、下划线和中划线组成，长度小于等于64个字符。
        :type category: str
        :param inputs: Inputs参数
        :type inputs: list[:class:`huaweicloudsdkdwr.v3.Input`]
        :param dynamic_source_definition: 根据DWR自定义的函数模板创建属于用户的function，并指定该参数设置的参数值。
        :type dynamic_source_definition: dict(str, object)
        :param need_policy: 算子执行时需要的权限信息。
        :type need_policy: list[:class:`huaweicloudsdkdwr.v3.Policy`]
        :param func_provider: 算子提供方。 英文：必须以字母或数字开头，只能由字母、数字、下划线和中划线组成，长度小于等于32个字符。 中文：只能由中文、字母、数字、下划线和中划线组成，长度小于等于32个字符。
        :type func_provider: dict(str, str)
        :param func_name: 算子名称。 英文：必须以字母或数字开头，只能由字母、数字、下划线和中划线组成，长度小于等于50个字符。 中文：只能由中文、字母、数字、下划线和中划线组成，长度小于等于50个字符。
        :type func_name: dict(str, str)
        :param func_description: 算子描述。 英文：长度最小为0，最长为256，可以是数字、大小写字母以及英文的逗号，句号，冒号，中划线,，下划线，空格。 中文：长度最小为0，最长为256，可以是中文、数字、大小写字母以及中英文的逗号，句号，冒号，中划线，下划线，空格。
        :type func_description: dict(str, str)
        :param func_link: 云市场链接。 需要包含中文， 长度最小为0，最长为512，须遵守http协议中定义的规则。
        :type func_link: dict(str, str)
        :param app_urn: serverless算子应用程序urn
        :type app_urn: str
        :param bill_value: Serverless计费单价
        :type bill_value: float
        :param agency: serverless所需要委托名
        :type agency: str
        :param register_status: 算子状态。初始创建时为init_created。申请提交时传入submit_approve。 算子状态。申请提交时传入submit_approve。
        :type register_status: str
        """
        
        

        self._category = None
        self._inputs = None
        self._dynamic_source_definition = None
        self._need_policy = None
        self._func_provider = None
        self._func_name = None
        self._func_description = None
        self._func_link = None
        self._app_urn = None
        self._bill_value = None
        self._agency = None
        self._register_status = None
        self.discriminator = None

        self.category = category
        if inputs is not None:
            self.inputs = inputs
        if dynamic_source_definition is not None:
            self.dynamic_source_definition = dynamic_source_definition
        if need_policy is not None:
            self.need_policy = need_policy
        self.func_provider = func_provider
        self.func_name = func_name
        self.func_description = func_description
        if func_link is not None:
            self.func_link = func_link
        if app_urn is not None:
            self.app_urn = app_urn
        if bill_value is not None:
            self.bill_value = bill_value
        if agency is not None:
            self.agency = agency
        if register_status is not None:
            self.register_status = register_status

    @property
    def category(self):
        r"""Gets the category of this ThirdTemplateRequestBody.

        必须以字母或数字开头，只能由字母、数字、下划线和中划线组成，长度小于等于64个字符。

        :return: The category of this ThirdTemplateRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ThirdTemplateRequestBody.

        必须以字母或数字开头，只能由字母、数字、下划线和中划线组成，长度小于等于64个字符。

        :param category: The category of this ThirdTemplateRequestBody.
        :type category: str
        """
        self._category = category

    @property
    def inputs(self):
        r"""Gets the inputs of this ThirdTemplateRequestBody.

        Inputs参数

        :return: The inputs of this ThirdTemplateRequestBody.
        :rtype: list[:class:`huaweicloudsdkdwr.v3.Input`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this ThirdTemplateRequestBody.

        Inputs参数

        :param inputs: The inputs of this ThirdTemplateRequestBody.
        :type inputs: list[:class:`huaweicloudsdkdwr.v3.Input`]
        """
        self._inputs = inputs

    @property
    def dynamic_source_definition(self):
        r"""Gets the dynamic_source_definition of this ThirdTemplateRequestBody.

        根据DWR自定义的函数模板创建属于用户的function，并指定该参数设置的参数值。

        :return: The dynamic_source_definition of this ThirdTemplateRequestBody.
        :rtype: dict(str, object)
        """
        return self._dynamic_source_definition

    @dynamic_source_definition.setter
    def dynamic_source_definition(self, dynamic_source_definition):
        r"""Sets the dynamic_source_definition of this ThirdTemplateRequestBody.

        根据DWR自定义的函数模板创建属于用户的function，并指定该参数设置的参数值。

        :param dynamic_source_definition: The dynamic_source_definition of this ThirdTemplateRequestBody.
        :type dynamic_source_definition: dict(str, object)
        """
        self._dynamic_source_definition = dynamic_source_definition

    @property
    def need_policy(self):
        r"""Gets the need_policy of this ThirdTemplateRequestBody.

        算子执行时需要的权限信息。

        :return: The need_policy of this ThirdTemplateRequestBody.
        :rtype: list[:class:`huaweicloudsdkdwr.v3.Policy`]
        """
        return self._need_policy

    @need_policy.setter
    def need_policy(self, need_policy):
        r"""Sets the need_policy of this ThirdTemplateRequestBody.

        算子执行时需要的权限信息。

        :param need_policy: The need_policy of this ThirdTemplateRequestBody.
        :type need_policy: list[:class:`huaweicloudsdkdwr.v3.Policy`]
        """
        self._need_policy = need_policy

    @property
    def func_provider(self):
        r"""Gets the func_provider of this ThirdTemplateRequestBody.

        算子提供方。 英文：必须以字母或数字开头，只能由字母、数字、下划线和中划线组成，长度小于等于32个字符。 中文：只能由中文、字母、数字、下划线和中划线组成，长度小于等于32个字符。

        :return: The func_provider of this ThirdTemplateRequestBody.
        :rtype: dict(str, str)
        """
        return self._func_provider

    @func_provider.setter
    def func_provider(self, func_provider):
        r"""Sets the func_provider of this ThirdTemplateRequestBody.

        算子提供方。 英文：必须以字母或数字开头，只能由字母、数字、下划线和中划线组成，长度小于等于32个字符。 中文：只能由中文、字母、数字、下划线和中划线组成，长度小于等于32个字符。

        :param func_provider: The func_provider of this ThirdTemplateRequestBody.
        :type func_provider: dict(str, str)
        """
        self._func_provider = func_provider

    @property
    def func_name(self):
        r"""Gets the func_name of this ThirdTemplateRequestBody.

        算子名称。 英文：必须以字母或数字开头，只能由字母、数字、下划线和中划线组成，长度小于等于50个字符。 中文：只能由中文、字母、数字、下划线和中划线组成，长度小于等于50个字符。

        :return: The func_name of this ThirdTemplateRequestBody.
        :rtype: dict(str, str)
        """
        return self._func_name

    @func_name.setter
    def func_name(self, func_name):
        r"""Sets the func_name of this ThirdTemplateRequestBody.

        算子名称。 英文：必须以字母或数字开头，只能由字母、数字、下划线和中划线组成，长度小于等于50个字符。 中文：只能由中文、字母、数字、下划线和中划线组成，长度小于等于50个字符。

        :param func_name: The func_name of this ThirdTemplateRequestBody.
        :type func_name: dict(str, str)
        """
        self._func_name = func_name

    @property
    def func_description(self):
        r"""Gets the func_description of this ThirdTemplateRequestBody.

        算子描述。 英文：长度最小为0，最长为256，可以是数字、大小写字母以及英文的逗号，句号，冒号，中划线,，下划线，空格。 中文：长度最小为0，最长为256，可以是中文、数字、大小写字母以及中英文的逗号，句号，冒号，中划线，下划线，空格。

        :return: The func_description of this ThirdTemplateRequestBody.
        :rtype: dict(str, str)
        """
        return self._func_description

    @func_description.setter
    def func_description(self, func_description):
        r"""Sets the func_description of this ThirdTemplateRequestBody.

        算子描述。 英文：长度最小为0，最长为256，可以是数字、大小写字母以及英文的逗号，句号，冒号，中划线,，下划线，空格。 中文：长度最小为0，最长为256，可以是中文、数字、大小写字母以及中英文的逗号，句号，冒号，中划线，下划线，空格。

        :param func_description: The func_description of this ThirdTemplateRequestBody.
        :type func_description: dict(str, str)
        """
        self._func_description = func_description

    @property
    def func_link(self):
        r"""Gets the func_link of this ThirdTemplateRequestBody.

        云市场链接。 需要包含中文， 长度最小为0，最长为512，须遵守http协议中定义的规则。

        :return: The func_link of this ThirdTemplateRequestBody.
        :rtype: dict(str, str)
        """
        return self._func_link

    @func_link.setter
    def func_link(self, func_link):
        r"""Sets the func_link of this ThirdTemplateRequestBody.

        云市场链接。 需要包含中文， 长度最小为0，最长为512，须遵守http协议中定义的规则。

        :param func_link: The func_link of this ThirdTemplateRequestBody.
        :type func_link: dict(str, str)
        """
        self._func_link = func_link

    @property
    def app_urn(self):
        r"""Gets the app_urn of this ThirdTemplateRequestBody.

        serverless算子应用程序urn

        :return: The app_urn of this ThirdTemplateRequestBody.
        :rtype: str
        """
        return self._app_urn

    @app_urn.setter
    def app_urn(self, app_urn):
        r"""Sets the app_urn of this ThirdTemplateRequestBody.

        serverless算子应用程序urn

        :param app_urn: The app_urn of this ThirdTemplateRequestBody.
        :type app_urn: str
        """
        self._app_urn = app_urn

    @property
    def bill_value(self):
        r"""Gets the bill_value of this ThirdTemplateRequestBody.

        Serverless计费单价

        :return: The bill_value of this ThirdTemplateRequestBody.
        :rtype: float
        """
        return self._bill_value

    @bill_value.setter
    def bill_value(self, bill_value):
        r"""Sets the bill_value of this ThirdTemplateRequestBody.

        Serverless计费单价

        :param bill_value: The bill_value of this ThirdTemplateRequestBody.
        :type bill_value: float
        """
        self._bill_value = bill_value

    @property
    def agency(self):
        r"""Gets the agency of this ThirdTemplateRequestBody.

        serverless所需要委托名

        :return: The agency of this ThirdTemplateRequestBody.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        r"""Sets the agency of this ThirdTemplateRequestBody.

        serverless所需要委托名

        :param agency: The agency of this ThirdTemplateRequestBody.
        :type agency: str
        """
        self._agency = agency

    @property
    def register_status(self):
        r"""Gets the register_status of this ThirdTemplateRequestBody.

        算子状态。初始创建时为init_created。申请提交时传入submit_approve。 算子状态。申请提交时传入submit_approve。

        :return: The register_status of this ThirdTemplateRequestBody.
        :rtype: str
        """
        return self._register_status

    @register_status.setter
    def register_status(self, register_status):
        r"""Sets the register_status of this ThirdTemplateRequestBody.

        算子状态。初始创建时为init_created。申请提交时传入submit_approve。 算子状态。申请提交时传入submit_approve。

        :param register_status: The register_status of this ThirdTemplateRequestBody.
        :type register_status: str
        """
        self._register_status = register_status

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
        if not isinstance(other, ThirdTemplateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
