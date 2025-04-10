# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgencyPolicyRoleOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'display_name': 'str',
        'type': 'str',
        'description': 'str',
        'description_cn': 'str',
        'policy': 'AgencyPolicy'
    }

    attribute_map = {
        'display_name': 'display_name',
        'type': 'type',
        'description': 'description',
        'description_cn': 'description_cn',
        'policy': 'policy'
    }

    def __init__(self, display_name=None, type=None, description=None, description_cn=None, policy=None):
        r"""AgencyPolicyRoleOption

        The model defined in huaweicloud sdk

        :param display_name: 自定义策略展示名。
        :type display_name: str
        :param type: 自定义策略的显示模式。 &gt; - AX表示在domain层显示。 &gt; - XA表示在project层显示。 &gt; - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。
        :type type: str
        :param description: 自定义策略的描述信息。
        :type description: str
        :param description_cn: 自定义策略的中文描述信息。
        :type description_cn: str
        :param policy: 
        :type policy: :class:`huaweicloudsdkiam.v3.AgencyPolicy`
        """
        
        

        self._display_name = None
        self._type = None
        self._description = None
        self._description_cn = None
        self._policy = None
        self.discriminator = None

        self.display_name = display_name
        self.type = type
        self.description = description
        if description_cn is not None:
            self.description_cn = description_cn
        self.policy = policy

    @property
    def display_name(self):
        r"""Gets the display_name of this AgencyPolicyRoleOption.

        自定义策略展示名。

        :return: The display_name of this AgencyPolicyRoleOption.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this AgencyPolicyRoleOption.

        自定义策略展示名。

        :param display_name: The display_name of this AgencyPolicyRoleOption.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def type(self):
        r"""Gets the type of this AgencyPolicyRoleOption.

        自定义策略的显示模式。 > - AX表示在domain层显示。 > - XA表示在project层显示。 > - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。

        :return: The type of this AgencyPolicyRoleOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AgencyPolicyRoleOption.

        自定义策略的显示模式。 > - AX表示在domain层显示。 > - XA表示在project层显示。 > - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。

        :param type: The type of this AgencyPolicyRoleOption.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this AgencyPolicyRoleOption.

        自定义策略的描述信息。

        :return: The description of this AgencyPolicyRoleOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AgencyPolicyRoleOption.

        自定义策略的描述信息。

        :param description: The description of this AgencyPolicyRoleOption.
        :type description: str
        """
        self._description = description

    @property
    def description_cn(self):
        r"""Gets the description_cn of this AgencyPolicyRoleOption.

        自定义策略的中文描述信息。

        :return: The description_cn of this AgencyPolicyRoleOption.
        :rtype: str
        """
        return self._description_cn

    @description_cn.setter
    def description_cn(self, description_cn):
        r"""Sets the description_cn of this AgencyPolicyRoleOption.

        自定义策略的中文描述信息。

        :param description_cn: The description_cn of this AgencyPolicyRoleOption.
        :type description_cn: str
        """
        self._description_cn = description_cn

    @property
    def policy(self):
        r"""Gets the policy of this AgencyPolicyRoleOption.

        :return: The policy of this AgencyPolicyRoleOption.
        :rtype: :class:`huaweicloudsdkiam.v3.AgencyPolicy`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this AgencyPolicyRoleOption.

        :param policy: The policy of this AgencyPolicyRoleOption.
        :type policy: :class:`huaweicloudsdkiam.v3.AgencyPolicy`
        """
        self._policy = policy

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
        if not isinstance(other, AgencyPolicyRoleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
