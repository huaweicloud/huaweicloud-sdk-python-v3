# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConformancePackRequestBody:

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
        'agency_name': 'str',
        'template_key': 'str',
        'template_body': 'str',
        'template_uri': 'str',
        'vars_structure': 'list[VarsStructure]'
    }

    attribute_map = {
        'name': 'name',
        'agency_name': 'agency_name',
        'template_key': 'template_key',
        'template_body': 'template_body',
        'template_uri': 'template_uri',
        'vars_structure': 'vars_structure'
    }

    def __init__(self, name=None, agency_name=None, template_key=None, template_body=None, template_uri=None, vars_structure=None):
        r"""ConformancePackRequestBody

        The model defined in huaweicloud sdk

        :param name: 合规规则包名称。
        :type name: str
        :param agency_name: 委托名称，该委托需要授权云服务ResourceFormation调用Config服务的合规规则的创建、更新、删除接口。
        :type agency_name: str
        :param template_key: 预定义合规包模板名称。
        :type template_key: str
        :param template_body: 自定义合规包内容。
        :type template_body: str
        :param template_uri: 合规包模板OBS地址。
        :type template_uri: str
        :param vars_structure: 合规规则包参数。
        :type vars_structure: list[:class:`huaweicloudsdkconfig.v1.VarsStructure`]
        """
        
        

        self._name = None
        self._agency_name = None
        self._template_key = None
        self._template_body = None
        self._template_uri = None
        self._vars_structure = None
        self.discriminator = None

        self.name = name
        if agency_name is not None:
            self.agency_name = agency_name
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
        r"""Gets the name of this ConformancePackRequestBody.

        合规规则包名称。

        :return: The name of this ConformancePackRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ConformancePackRequestBody.

        合规规则包名称。

        :param name: The name of this ConformancePackRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def agency_name(self):
        r"""Gets the agency_name of this ConformancePackRequestBody.

        委托名称，该委托需要授权云服务ResourceFormation调用Config服务的合规规则的创建、更新、删除接口。

        :return: The agency_name of this ConformancePackRequestBody.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this ConformancePackRequestBody.

        委托名称，该委托需要授权云服务ResourceFormation调用Config服务的合规规则的创建、更新、删除接口。

        :param agency_name: The agency_name of this ConformancePackRequestBody.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def template_key(self):
        r"""Gets the template_key of this ConformancePackRequestBody.

        预定义合规包模板名称。

        :return: The template_key of this ConformancePackRequestBody.
        :rtype: str
        """
        return self._template_key

    @template_key.setter
    def template_key(self, template_key):
        r"""Sets the template_key of this ConformancePackRequestBody.

        预定义合规包模板名称。

        :param template_key: The template_key of this ConformancePackRequestBody.
        :type template_key: str
        """
        self._template_key = template_key

    @property
    def template_body(self):
        r"""Gets the template_body of this ConformancePackRequestBody.

        自定义合规包内容。

        :return: The template_body of this ConformancePackRequestBody.
        :rtype: str
        """
        return self._template_body

    @template_body.setter
    def template_body(self, template_body):
        r"""Sets the template_body of this ConformancePackRequestBody.

        自定义合规包内容。

        :param template_body: The template_body of this ConformancePackRequestBody.
        :type template_body: str
        """
        self._template_body = template_body

    @property
    def template_uri(self):
        r"""Gets the template_uri of this ConformancePackRequestBody.

        合规包模板OBS地址。

        :return: The template_uri of this ConformancePackRequestBody.
        :rtype: str
        """
        return self._template_uri

    @template_uri.setter
    def template_uri(self, template_uri):
        r"""Sets the template_uri of this ConformancePackRequestBody.

        合规包模板OBS地址。

        :param template_uri: The template_uri of this ConformancePackRequestBody.
        :type template_uri: str
        """
        self._template_uri = template_uri

    @property
    def vars_structure(self):
        r"""Gets the vars_structure of this ConformancePackRequestBody.

        合规规则包参数。

        :return: The vars_structure of this ConformancePackRequestBody.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.VarsStructure`]
        """
        return self._vars_structure

    @vars_structure.setter
    def vars_structure(self, vars_structure):
        r"""Sets the vars_structure of this ConformancePackRequestBody.

        合规规则包参数。

        :param vars_structure: The vars_structure of this ConformancePackRequestBody.
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
        if not isinstance(other, ConformancePackRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
