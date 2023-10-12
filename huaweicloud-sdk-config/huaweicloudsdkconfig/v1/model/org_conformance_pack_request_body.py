# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrgConformancePackRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'excluded_accounts': 'list[str]',
        'template_key': 'str',
        'template_body': 'str',
        'template_uri': 'str',
        'vars_structure': 'list[VarsStructure]'
    }

    attribute_map = {
        'name': 'name',
        'excluded_accounts': 'excluded_accounts',
        'template_key': 'template_key',
        'template_body': 'template_body',
        'template_uri': 'template_uri',
        'vars_structure': 'vars_structure'
    }

    def __init__(self, name=None, excluded_accounts=None, template_key=None, template_body=None, template_uri=None, vars_structure=None):
        """OrgConformancePackRequestBody

        The model defined in huaweicloud sdk

        :param name: 组织合规规则包名称。
        :type name: str
        :param excluded_accounts: 排除配置合规包的帐号。
        :type excluded_accounts: list[str]
        :param template_key: 预定义合规规则包模板名称。
        :type template_key: str
        :param template_body: 自定义合规规则包内容。
        :type template_body: str
        :param template_uri: 合规规则包模板OBS地址。
        :type template_uri: str
        :param vars_structure: 合规规则包参数。
        :type vars_structure: list[:class:`huaweicloudsdkconfig.v1.VarsStructure`]
        """
        
        

        self._name = None
        self._excluded_accounts = None
        self._template_key = None
        self._template_body = None
        self._template_uri = None
        self._vars_structure = None
        self.discriminator = None

        self.name = name
        if excluded_accounts is not None:
            self.excluded_accounts = excluded_accounts
        if template_key is not None:
            self.template_key = template_key
        if template_body is not None:
            self.template_body = template_body
        if template_uri is not None:
            self.template_uri = template_uri
        if vars_structure is not None:
            self.vars_structure = vars_structure

    @property
    def name(self):
        """Gets the name of this OrgConformancePackRequestBody.

        组织合规规则包名称。

        :return: The name of this OrgConformancePackRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrgConformancePackRequestBody.

        组织合规规则包名称。

        :param name: The name of this OrgConformancePackRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def excluded_accounts(self):
        """Gets the excluded_accounts of this OrgConformancePackRequestBody.

        排除配置合规包的帐号。

        :return: The excluded_accounts of this OrgConformancePackRequestBody.
        :rtype: list[str]
        """
        return self._excluded_accounts

    @excluded_accounts.setter
    def excluded_accounts(self, excluded_accounts):
        """Sets the excluded_accounts of this OrgConformancePackRequestBody.

        排除配置合规包的帐号。

        :param excluded_accounts: The excluded_accounts of this OrgConformancePackRequestBody.
        :type excluded_accounts: list[str]
        """
        self._excluded_accounts = excluded_accounts

    @property
    def template_key(self):
        """Gets the template_key of this OrgConformancePackRequestBody.

        预定义合规规则包模板名称。

        :return: The template_key of this OrgConformancePackRequestBody.
        :rtype: str
        """
        return self._template_key

    @template_key.setter
    def template_key(self, template_key):
        """Sets the template_key of this OrgConformancePackRequestBody.

        预定义合规规则包模板名称。

        :param template_key: The template_key of this OrgConformancePackRequestBody.
        :type template_key: str
        """
        self._template_key = template_key

    @property
    def template_body(self):
        """Gets the template_body of this OrgConformancePackRequestBody.

        自定义合规规则包内容。

        :return: The template_body of this OrgConformancePackRequestBody.
        :rtype: str
        """
        return self._template_body

    @template_body.setter
    def template_body(self, template_body):
        """Sets the template_body of this OrgConformancePackRequestBody.

        自定义合规规则包内容。

        :param template_body: The template_body of this OrgConformancePackRequestBody.
        :type template_body: str
        """
        self._template_body = template_body

    @property
    def template_uri(self):
        """Gets the template_uri of this OrgConformancePackRequestBody.

        合规规则包模板OBS地址。

        :return: The template_uri of this OrgConformancePackRequestBody.
        :rtype: str
        """
        return self._template_uri

    @template_uri.setter
    def template_uri(self, template_uri):
        """Sets the template_uri of this OrgConformancePackRequestBody.

        合规规则包模板OBS地址。

        :param template_uri: The template_uri of this OrgConformancePackRequestBody.
        :type template_uri: str
        """
        self._template_uri = template_uri

    @property
    def vars_structure(self):
        """Gets the vars_structure of this OrgConformancePackRequestBody.

        合规规则包参数。

        :return: The vars_structure of this OrgConformancePackRequestBody.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.VarsStructure`]
        """
        return self._vars_structure

    @vars_structure.setter
    def vars_structure(self, vars_structure):
        """Sets the vars_structure of this OrgConformancePackRequestBody.

        合规规则包参数。

        :param vars_structure: The vars_structure of this OrgConformancePackRequestBody.
        :type vars_structure: list[:class:`huaweicloudsdkconfig.v1.VarsStructure`]
        """
        self._vars_structure = vars_structure

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
        if not isinstance(other, OrgConformancePackRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
