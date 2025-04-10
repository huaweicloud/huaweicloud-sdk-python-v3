# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalAccessDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'list[str]',
        'condition': 'list[FindingCondition]',
        'is_public': 'bool',
        'principal': 'FindingPrincipal',
        'sources': 'list[FindingSourceType]'
    }

    attribute_map = {
        'action': 'action',
        'condition': 'condition',
        'is_public': 'is_public',
        'principal': 'principal',
        'sources': 'sources'
    }

    def __init__(self, action=None, condition=None, is_public=None, principal=None, sources=None):
        r"""ExternalAccessDetails

        The model defined in huaweicloud sdk

        :param action: 允许外部主体使用的操作。
        :type action: list[str]
        :param condition: 分析的策略语句中导致访问分析结果的条件。
        :type condition: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingCondition`]
        :param is_public: 表示生成访问分析结果的策略是否允许公共访问资源。
        :type is_public: bool
        :param principal: 
        :type principal: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingPrincipal`
        :param sources: 访问分析结果的来源，这指示如何授予生成访问分析结果的访问权限。
        :type sources: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingSourceType`]
        """
        
        

        self._action = None
        self._condition = None
        self._is_public = None
        self._principal = None
        self._sources = None
        self.discriminator = None

        self.action = action
        self.condition = condition
        self.is_public = is_public
        self.principal = principal
        if sources is not None:
            self.sources = sources

    @property
    def action(self):
        r"""Gets the action of this ExternalAccessDetails.

        允许外部主体使用的操作。

        :return: The action of this ExternalAccessDetails.
        :rtype: list[str]
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ExternalAccessDetails.

        允许外部主体使用的操作。

        :param action: The action of this ExternalAccessDetails.
        :type action: list[str]
        """
        self._action = action

    @property
    def condition(self):
        r"""Gets the condition of this ExternalAccessDetails.

        分析的策略语句中导致访问分析结果的条件。

        :return: The condition of this ExternalAccessDetails.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingCondition`]
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this ExternalAccessDetails.

        分析的策略语句中导致访问分析结果的条件。

        :param condition: The condition of this ExternalAccessDetails.
        :type condition: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingCondition`]
        """
        self._condition = condition

    @property
    def is_public(self):
        r"""Gets the is_public of this ExternalAccessDetails.

        表示生成访问分析结果的策略是否允许公共访问资源。

        :return: The is_public of this ExternalAccessDetails.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        r"""Sets the is_public of this ExternalAccessDetails.

        表示生成访问分析结果的策略是否允许公共访问资源。

        :param is_public: The is_public of this ExternalAccessDetails.
        :type is_public: bool
        """
        self._is_public = is_public

    @property
    def principal(self):
        r"""Gets the principal of this ExternalAccessDetails.

        :return: The principal of this ExternalAccessDetails.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingPrincipal`
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        r"""Sets the principal of this ExternalAccessDetails.

        :param principal: The principal of this ExternalAccessDetails.
        :type principal: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingPrincipal`
        """
        self._principal = principal

    @property
    def sources(self):
        r"""Gets the sources of this ExternalAccessDetails.

        访问分析结果的来源，这指示如何授予生成访问分析结果的访问权限。

        :return: The sources of this ExternalAccessDetails.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingSourceType`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        r"""Sets the sources of this ExternalAccessDetails.

        访问分析结果的来源，这指示如何授予生成访问分析结果的访问权限。

        :param sources: The sources of this ExternalAccessDetails.
        :type sources: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingSourceType`]
        """
        self._sources = sources

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
        if not isinstance(other, ExternalAccessDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
