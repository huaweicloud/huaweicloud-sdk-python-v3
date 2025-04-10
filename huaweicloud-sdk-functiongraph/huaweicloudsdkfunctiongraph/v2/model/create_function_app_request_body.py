# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFunctionAppRequestBody:

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
        'template_id': 'str',
        'description': 'str',
        'enterprise_project_id': 'str',
        'agency_name': 'str',
        'params': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'template_id': 'template_id',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'agency_name': 'agency_name',
        'params': 'params'
    }

    def __init__(self, name=None, template_id=None, description=None, enterprise_project_id=None, agency_name=None, params=None):
        r"""CreateFunctionAppRequestBody

        The model defined in huaweicloud sdk

        :param name: 应用名称
        :type name: str
        :param template_id: 应用使用的模板ID
        :type template_id: str
        :param description: 应用描述
        :type description: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param agency_name: 委托名称
        :type agency_name: str
        :param params: 模板参数
        :type params: dict(str, str)
        """
        
        

        self._name = None
        self._template_id = None
        self._description = None
        self._enterprise_project_id = None
        self._agency_name = None
        self._params = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if template_id is not None:
            self.template_id = template_id
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if agency_name is not None:
            self.agency_name = agency_name
        if params is not None:
            self.params = params

    @property
    def name(self):
        r"""Gets the name of this CreateFunctionAppRequestBody.

        应用名称

        :return: The name of this CreateFunctionAppRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateFunctionAppRequestBody.

        应用名称

        :param name: The name of this CreateFunctionAppRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def template_id(self):
        r"""Gets the template_id of this CreateFunctionAppRequestBody.

        应用使用的模板ID

        :return: The template_id of this CreateFunctionAppRequestBody.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this CreateFunctionAppRequestBody.

        应用使用的模板ID

        :param template_id: The template_id of this CreateFunctionAppRequestBody.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def description(self):
        r"""Gets the description of this CreateFunctionAppRequestBody.

        应用描述

        :return: The description of this CreateFunctionAppRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateFunctionAppRequestBody.

        应用描述

        :param description: The description of this CreateFunctionAppRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateFunctionAppRequestBody.

        企业项目ID

        :return: The enterprise_project_id of this CreateFunctionAppRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateFunctionAppRequestBody.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this CreateFunctionAppRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def agency_name(self):
        r"""Gets the agency_name of this CreateFunctionAppRequestBody.

        委托名称

        :return: The agency_name of this CreateFunctionAppRequestBody.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this CreateFunctionAppRequestBody.

        委托名称

        :param agency_name: The agency_name of this CreateFunctionAppRequestBody.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def params(self):
        r"""Gets the params of this CreateFunctionAppRequestBody.

        模板参数

        :return: The params of this CreateFunctionAppRequestBody.
        :rtype: dict(str, str)
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this CreateFunctionAppRequestBody.

        模板参数

        :param params: The params of this CreateFunctionAppRequestBody.
        :type params: dict(str, str)
        """
        self._params = params

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
        if not isinstance(other, CreateFunctionAppRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
