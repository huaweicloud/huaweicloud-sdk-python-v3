# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CcrulesListInfoAction:

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
        'detail': 'CcrulesListInfoActionDetail'
    }

    attribute_map = {
        'category': 'category',
        'detail': 'detail'
    }

    def __init__(self, category=None, detail=None):
        """CcrulesListInfoAction

        The model defined in huaweicloud sdk

        :param category: 动作类型：  - captcha：人机验证，阻断后用户需要输入正确的验证码，恢复正确的访问页面。  -block：阻断。   - log: 仅记录   - dynamic_block: 上一个限速周期内，请求频率超过“限速频率”将被阻断，那么在下一个限速周期内，请求频率超过“放行频率”将被阻断。注：只有当cc防护规则模式为高级模式时才支持设置dynamic_block防护动作。
        :type category: str
        :param detail: 
        :type detail: :class:`huaweicloudsdkwaf.v1.CcrulesListInfoActionDetail`
        """
        
        

        self._category = None
        self._detail = None
        self.discriminator = None

        self.category = category
        if detail is not None:
            self.detail = detail

    @property
    def category(self):
        """Gets the category of this CcrulesListInfoAction.

        动作类型：  - captcha：人机验证，阻断后用户需要输入正确的验证码，恢复正确的访问页面。  -block：阻断。   - log: 仅记录   - dynamic_block: 上一个限速周期内，请求频率超过“限速频率”将被阻断，那么在下一个限速周期内，请求频率超过“放行频率”将被阻断。注：只有当cc防护规则模式为高级模式时才支持设置dynamic_block防护动作。

        :return: The category of this CcrulesListInfoAction.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this CcrulesListInfoAction.

        动作类型：  - captcha：人机验证，阻断后用户需要输入正确的验证码，恢复正确的访问页面。  -block：阻断。   - log: 仅记录   - dynamic_block: 上一个限速周期内，请求频率超过“限速频率”将被阻断，那么在下一个限速周期内，请求频率超过“放行频率”将被阻断。注：只有当cc防护规则模式为高级模式时才支持设置dynamic_block防护动作。

        :param category: The category of this CcrulesListInfoAction.
        :type category: str
        """
        self._category = category

    @property
    def detail(self):
        """Gets the detail of this CcrulesListInfoAction.

        :return: The detail of this CcrulesListInfoAction.
        :rtype: :class:`huaweicloudsdkwaf.v1.CcrulesListInfoActionDetail`
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this CcrulesListInfoAction.

        :param detail: The detail of this CcrulesListInfoAction.
        :type detail: :class:`huaweicloudsdkwaf.v1.CcrulesListInfoActionDetail`
        """
        self._detail = detail

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
        if not isinstance(other, CcrulesListInfoAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
