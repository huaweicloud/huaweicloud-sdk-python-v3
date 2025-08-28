# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiCloudClusterAuthInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_groups': 'str',
        'resources': 'str',
        'function': 'str',
        'is_authed': 'bool',
        'advice': 'str'
    }

    attribute_map = {
        'api_groups': 'api_groups',
        'resources': 'resources',
        'function': 'function',
        'is_authed': 'is_authed',
        'advice': 'advice'
    }

    def __init__(self, api_groups=None, resources=None, function=None, is_authed=None, advice=None):
        r"""MultiCloudClusterAuthInfo

        The model defined in huaweicloud sdk

        :param api_groups: **参数解释**： API组 **取值范围**： 字符长度1-64位 
        :type api_groups: str
        :param resources: **参数解释**： 资源 **取值范围**： 字符长度1-16位 
        :type resources: str
        :param function: **参数解释**： 所属特性 **取值范围**： 字符长度1-16位 
        :type function: str
        :param is_authed: 是否有权访问
        :type is_authed: bool
        :param advice: **参数解释**： 修复建议 **取值范围**： 字符长度1-128位 
        :type advice: str
        """
        
        

        self._api_groups = None
        self._resources = None
        self._function = None
        self._is_authed = None
        self._advice = None
        self.discriminator = None

        if api_groups is not None:
            self.api_groups = api_groups
        if resources is not None:
            self.resources = resources
        if function is not None:
            self.function = function
        if is_authed is not None:
            self.is_authed = is_authed
        if advice is not None:
            self.advice = advice

    @property
    def api_groups(self):
        r"""Gets the api_groups of this MultiCloudClusterAuthInfo.

        **参数解释**： API组 **取值范围**： 字符长度1-64位 

        :return: The api_groups of this MultiCloudClusterAuthInfo.
        :rtype: str
        """
        return self._api_groups

    @api_groups.setter
    def api_groups(self, api_groups):
        r"""Sets the api_groups of this MultiCloudClusterAuthInfo.

        **参数解释**： API组 **取值范围**： 字符长度1-64位 

        :param api_groups: The api_groups of this MultiCloudClusterAuthInfo.
        :type api_groups: str
        """
        self._api_groups = api_groups

    @property
    def resources(self):
        r"""Gets the resources of this MultiCloudClusterAuthInfo.

        **参数解释**： 资源 **取值范围**： 字符长度1-16位 

        :return: The resources of this MultiCloudClusterAuthInfo.
        :rtype: str
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this MultiCloudClusterAuthInfo.

        **参数解释**： 资源 **取值范围**： 字符长度1-16位 

        :param resources: The resources of this MultiCloudClusterAuthInfo.
        :type resources: str
        """
        self._resources = resources

    @property
    def function(self):
        r"""Gets the function of this MultiCloudClusterAuthInfo.

        **参数解释**： 所属特性 **取值范围**： 字符长度1-16位 

        :return: The function of this MultiCloudClusterAuthInfo.
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        r"""Sets the function of this MultiCloudClusterAuthInfo.

        **参数解释**： 所属特性 **取值范围**： 字符长度1-16位 

        :param function: The function of this MultiCloudClusterAuthInfo.
        :type function: str
        """
        self._function = function

    @property
    def is_authed(self):
        r"""Gets the is_authed of this MultiCloudClusterAuthInfo.

        是否有权访问

        :return: The is_authed of this MultiCloudClusterAuthInfo.
        :rtype: bool
        """
        return self._is_authed

    @is_authed.setter
    def is_authed(self, is_authed):
        r"""Sets the is_authed of this MultiCloudClusterAuthInfo.

        是否有权访问

        :param is_authed: The is_authed of this MultiCloudClusterAuthInfo.
        :type is_authed: bool
        """
        self._is_authed = is_authed

    @property
    def advice(self):
        r"""Gets the advice of this MultiCloudClusterAuthInfo.

        **参数解释**： 修复建议 **取值范围**： 字符长度1-128位 

        :return: The advice of this MultiCloudClusterAuthInfo.
        :rtype: str
        """
        return self._advice

    @advice.setter
    def advice(self, advice):
        r"""Sets the advice of this MultiCloudClusterAuthInfo.

        **参数解释**： 修复建议 **取值范围**： 字符长度1-128位 

        :param advice: The advice of this MultiCloudClusterAuthInfo.
        :type advice: str
        """
        self._advice = advice

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
        if not isinstance(other, MultiCloudClusterAuthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
