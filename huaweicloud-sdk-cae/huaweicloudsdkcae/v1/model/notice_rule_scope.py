# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NoticeRuleScope:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'environments': 'list[str]',
        'applications': 'list[str]',
        'components': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'environments': 'environments',
        'applications': 'applications',
        'components': 'components'
    }

    def __init__(self, type=None, environments=None, applications=None, components=None):
        r"""NoticeRuleScope

        The model defined in huaweicloud sdk

        :param type: 生效范围的类型。包括environments（对指定环境下所有组件生效），applications（对指定应用下所有组件生效），components（对指定的组件生效）。
        :type type: str
        :param environments: 生效的环境id列表。
        :type environments: list[str]
        :param applications: 生效的应用id列表。
        :type applications: list[str]
        :param components: 生效的组件id列表。
        :type components: list[str]
        """
        
        

        self._type = None
        self._environments = None
        self._applications = None
        self._components = None
        self.discriminator = None

        self.type = type
        if environments is not None:
            self.environments = environments
        if applications is not None:
            self.applications = applications
        if components is not None:
            self.components = components

    @property
    def type(self):
        r"""Gets the type of this NoticeRuleScope.

        生效范围的类型。包括environments（对指定环境下所有组件生效），applications（对指定应用下所有组件生效），components（对指定的组件生效）。

        :return: The type of this NoticeRuleScope.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this NoticeRuleScope.

        生效范围的类型。包括environments（对指定环境下所有组件生效），applications（对指定应用下所有组件生效），components（对指定的组件生效）。

        :param type: The type of this NoticeRuleScope.
        :type type: str
        """
        self._type = type

    @property
    def environments(self):
        r"""Gets the environments of this NoticeRuleScope.

        生效的环境id列表。

        :return: The environments of this NoticeRuleScope.
        :rtype: list[str]
        """
        return self._environments

    @environments.setter
    def environments(self, environments):
        r"""Sets the environments of this NoticeRuleScope.

        生效的环境id列表。

        :param environments: The environments of this NoticeRuleScope.
        :type environments: list[str]
        """
        self._environments = environments

    @property
    def applications(self):
        r"""Gets the applications of this NoticeRuleScope.

        生效的应用id列表。

        :return: The applications of this NoticeRuleScope.
        :rtype: list[str]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        r"""Sets the applications of this NoticeRuleScope.

        生效的应用id列表。

        :param applications: The applications of this NoticeRuleScope.
        :type applications: list[str]
        """
        self._applications = applications

    @property
    def components(self):
        r"""Gets the components of this NoticeRuleScope.

        生效的组件id列表。

        :return: The components of this NoticeRuleScope.
        :rtype: list[str]
        """
        return self._components

    @components.setter
    def components(self, components):
        r"""Sets the components of this NoticeRuleScope.

        生效的组件id列表。

        :param components: The components of this NoticeRuleScope.
        :type components: list[str]
        """
        self._components = components

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
        if not isinstance(other, NoticeRuleScope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
