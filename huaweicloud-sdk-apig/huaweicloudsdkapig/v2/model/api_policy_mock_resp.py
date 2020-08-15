# coding: utf-8

import pprint
import re

import six





class ApiPolicyMockResp:


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
        'effect_mode': 'str',
        'name': 'str',
        'backend_params': 'list[BackendParam]',
        'conditions': 'list[CoditionResp]',
        'authorizer_id': 'str',
        'result_content': 'str'
    }

    attribute_map = {
        'id': 'id',
        'effect_mode': 'effect_mode',
        'name': 'name',
        'backend_params': 'backend_params',
        'conditions': 'conditions',
        'authorizer_id': 'authorizer_id',
        'result_content': 'result_content'
    }

    def __init__(self, id=None, effect_mode=None, name=None, backend_params=None, conditions=None, authorizer_id=None, result_content=None):
        """ApiPolicyMockResp - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._effect_mode = None
        self._name = None
        self._backend_params = None
        self._conditions = None
        self._authorizer_id = None
        self._result_content = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.effect_mode = effect_mode
        self.name = name
        if backend_params is not None:
            self.backend_params = backend_params
        self.conditions = conditions
        if authorizer_id is not None:
            self.authorizer_id = authorizer_id
        if result_content is not None:
            self.result_content = result_content

    @property
    def id(self):
        """Gets the id of this ApiPolicyMockResp.

        编号

        :return: The id of this ApiPolicyMockResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiPolicyMockResp.

        编号

        :param id: The id of this ApiPolicyMockResp.
        :type: str
        """
        self._id = id

    @property
    def effect_mode(self):
        """Gets the effect_mode of this ApiPolicyMockResp.

        关联的策略组合模式： - ALL：满足全部条件 - ANY：满足任一条件

        :return: The effect_mode of this ApiPolicyMockResp.
        :rtype: str
        """
        return self._effect_mode

    @effect_mode.setter
    def effect_mode(self, effect_mode):
        """Sets the effect_mode of this ApiPolicyMockResp.

        关联的策略组合模式： - ALL：满足全部条件 - ANY：满足任一条件

        :param effect_mode: The effect_mode of this ApiPolicyMockResp.
        :type: str
        """
        self._effect_mode = effect_mode

    @property
    def name(self):
        """Gets the name of this ApiPolicyMockResp.

        策略后端名称。字符串由中文、英文字母、数字、下划线组成，且只能以中文或英文开头。

        :return: The name of this ApiPolicyMockResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiPolicyMockResp.

        策略后端名称。字符串由中文、英文字母、数字、下划线组成，且只能以中文或英文开头。

        :param name: The name of this ApiPolicyMockResp.
        :type: str
        """
        self._name = name

    @property
    def backend_params(self):
        """Gets the backend_params of this ApiPolicyMockResp.

        后端参数列表

        :return: The backend_params of this ApiPolicyMockResp.
        :rtype: list[BackendParam]
        """
        return self._backend_params

    @backend_params.setter
    def backend_params(self, backend_params):
        """Sets the backend_params of this ApiPolicyMockResp.

        后端参数列表

        :param backend_params: The backend_params of this ApiPolicyMockResp.
        :type: list[BackendParam]
        """
        self._backend_params = backend_params

    @property
    def conditions(self):
        """Gets the conditions of this ApiPolicyMockResp.

        策略条件列表

        :return: The conditions of this ApiPolicyMockResp.
        :rtype: list[CoditionResp]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this ApiPolicyMockResp.

        策略条件列表

        :param conditions: The conditions of this ApiPolicyMockResp.
        :type: list[CoditionResp]
        """
        self._conditions = conditions

    @property
    def authorizer_id(self):
        """Gets the authorizer_id of this ApiPolicyMockResp.

        后端自定义认证对象的ID

        :return: The authorizer_id of this ApiPolicyMockResp.
        :rtype: str
        """
        return self._authorizer_id

    @authorizer_id.setter
    def authorizer_id(self, authorizer_id):
        """Sets the authorizer_id of this ApiPolicyMockResp.

        后端自定义认证对象的ID

        :param authorizer_id: The authorizer_id of this ApiPolicyMockResp.
        :type: str
        """
        self._authorizer_id = authorizer_id

    @property
    def result_content(self):
        """Gets the result_content of this ApiPolicyMockResp.

        返回结果

        :return: The result_content of this ApiPolicyMockResp.
        :rtype: str
        """
        return self._result_content

    @result_content.setter
    def result_content(self, result_content):
        """Sets the result_content of this ApiPolicyMockResp.

        返回结果

        :param result_content: The result_content of this ApiPolicyMockResp.
        :type: str
        """
        self._result_content = result_content

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiPolicyMockResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
