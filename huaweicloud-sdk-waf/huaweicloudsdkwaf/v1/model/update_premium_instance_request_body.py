# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePremiumInstanceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'params': 'list[str]'
    }

    attribute_map = {
        'action': 'action',
        'params': 'params'
    }

    def __init__(self, action=None, params=None):
        r"""UpdatePremiumInstanceRequestBody

        The model defined in huaweicloud sdk

        :param action: **参数解释：** 独享引擎操作名称，目前支持 upgrade（升级） ，rollback（升级后回滚），security_groups（切换安全组） **取值范围：** 不涉及
        :type action: str
        :param params: **参数解释：**  具体的请求参数，操作为upgrade（升级） ，rollback（升级后回滚）时无需填写，操作位 security_groups（切换安全组）时，参数为安全组的ip数组 **取值范围：** 不涉及
        :type params: list[str]
        """
        
        

        self._action = None
        self._params = None
        self.discriminator = None

        self.action = action
        if params is not None:
            self.params = params

    @property
    def action(self):
        r"""Gets the action of this UpdatePremiumInstanceRequestBody.

        **参数解释：** 独享引擎操作名称，目前支持 upgrade（升级） ，rollback（升级后回滚），security_groups（切换安全组） **取值范围：** 不涉及

        :return: The action of this UpdatePremiumInstanceRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this UpdatePremiumInstanceRequestBody.

        **参数解释：** 独享引擎操作名称，目前支持 upgrade（升级） ，rollback（升级后回滚），security_groups（切换安全组） **取值范围：** 不涉及

        :param action: The action of this UpdatePremiumInstanceRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def params(self):
        r"""Gets the params of this UpdatePremiumInstanceRequestBody.

        **参数解释：**  具体的请求参数，操作为upgrade（升级） ，rollback（升级后回滚）时无需填写，操作位 security_groups（切换安全组）时，参数为安全组的ip数组 **取值范围：** 不涉及

        :return: The params of this UpdatePremiumInstanceRequestBody.
        :rtype: list[str]
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this UpdatePremiumInstanceRequestBody.

        **参数解释：**  具体的请求参数，操作为upgrade（升级） ，rollback（升级后回滚）时无需填写，操作位 security_groups（切换安全组）时，参数为安全组的ip数组 **取值范围：** 不涉及

        :param params: The params of this UpdatePremiumInstanceRequestBody.
        :type params: list[str]
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
        if not isinstance(other, UpdatePremiumInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
