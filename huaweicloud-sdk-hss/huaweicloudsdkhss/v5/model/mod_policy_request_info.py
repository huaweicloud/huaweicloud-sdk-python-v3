# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModPolicyRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'policy_id': 'str',
        'template_id': 'str',
        'policy_description': 'str',
        'content': 'PolicyContent',
        'white_image_list': 'list[WhiteImageInfo]',
        'resources': 'list[PolicyProtectScope]',
        'parameters': 'str'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'policy_id': 'policy_id',
        'template_id': 'template_id',
        'policy_description': 'policy_description',
        'content': 'content',
        'white_image_list': 'white_image_list',
        'resources': 'resources',
        'parameters': 'parameters'
    }

    def __init__(self, policy_name=None, policy_id=None, template_id=None, policy_description=None, content=None, white_image_list=None, resources=None, parameters=None):
        r"""ModPolicyRequestInfo

        The model defined in huaweicloud sdk

        :param policy_name: 策略名称
        :type policy_name: str
        :param policy_id: 策略ID
        :type policy_id: str
        :param template_id: 模板ID
        :type template_id: str
        :param policy_description: 策略描述
        :type policy_description: str
        :param content: 
        :type content: :class:`huaweicloudsdkhss.v5.PolicyContent`
        :param white_image_list: 白名单镜像
        :type white_image_list: list[:class:`huaweicloudsdkhss.v5.WhiteImageInfo`]
        :param resources: 防护的资源信息
        :type resources: list[:class:`huaweicloudsdkhss.v5.PolicyProtectScope`]
        :param parameters: 策略参数值
        :type parameters: str
        """
        
        

        self._policy_name = None
        self._policy_id = None
        self._template_id = None
        self._policy_description = None
        self._content = None
        self._white_image_list = None
        self._resources = None
        self._parameters = None
        self.discriminator = None

        self.policy_name = policy_name
        self.policy_id = policy_id
        self.template_id = template_id
        self.policy_description = policy_description
        self.content = content
        self.white_image_list = white_image_list
        self.resources = resources
        self.parameters = parameters

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ModPolicyRequestInfo.

        策略名称

        :return: The policy_name of this ModPolicyRequestInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ModPolicyRequestInfo.

        策略名称

        :param policy_name: The policy_name of this ModPolicyRequestInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ModPolicyRequestInfo.

        策略ID

        :return: The policy_id of this ModPolicyRequestInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ModPolicyRequestInfo.

        策略ID

        :param policy_id: The policy_id of this ModPolicyRequestInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def template_id(self):
        r"""Gets the template_id of this ModPolicyRequestInfo.

        模板ID

        :return: The template_id of this ModPolicyRequestInfo.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ModPolicyRequestInfo.

        模板ID

        :param template_id: The template_id of this ModPolicyRequestInfo.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def policy_description(self):
        r"""Gets the policy_description of this ModPolicyRequestInfo.

        策略描述

        :return: The policy_description of this ModPolicyRequestInfo.
        :rtype: str
        """
        return self._policy_description

    @policy_description.setter
    def policy_description(self, policy_description):
        r"""Sets the policy_description of this ModPolicyRequestInfo.

        策略描述

        :param policy_description: The policy_description of this ModPolicyRequestInfo.
        :type policy_description: str
        """
        self._policy_description = policy_description

    @property
    def content(self):
        r"""Gets the content of this ModPolicyRequestInfo.

        :return: The content of this ModPolicyRequestInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.PolicyContent`
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ModPolicyRequestInfo.

        :param content: The content of this ModPolicyRequestInfo.
        :type content: :class:`huaweicloudsdkhss.v5.PolicyContent`
        """
        self._content = content

    @property
    def white_image_list(self):
        r"""Gets the white_image_list of this ModPolicyRequestInfo.

        白名单镜像

        :return: The white_image_list of this ModPolicyRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.WhiteImageInfo`]
        """
        return self._white_image_list

    @white_image_list.setter
    def white_image_list(self, white_image_list):
        r"""Sets the white_image_list of this ModPolicyRequestInfo.

        白名单镜像

        :param white_image_list: The white_image_list of this ModPolicyRequestInfo.
        :type white_image_list: list[:class:`huaweicloudsdkhss.v5.WhiteImageInfo`]
        """
        self._white_image_list = white_image_list

    @property
    def resources(self):
        r"""Gets the resources of this ModPolicyRequestInfo.

        防护的资源信息

        :return: The resources of this ModPolicyRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.PolicyProtectScope`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ModPolicyRequestInfo.

        防护的资源信息

        :param resources: The resources of this ModPolicyRequestInfo.
        :type resources: list[:class:`huaweicloudsdkhss.v5.PolicyProtectScope`]
        """
        self._resources = resources

    @property
    def parameters(self):
        r"""Gets the parameters of this ModPolicyRequestInfo.

        策略参数值

        :return: The parameters of this ModPolicyRequestInfo.
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this ModPolicyRequestInfo.

        策略参数值

        :param parameters: The parameters of this ModPolicyRequestInfo.
        :type parameters: str
        """
        self._parameters = parameters

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
        if not isinstance(other, ModPolicyRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
