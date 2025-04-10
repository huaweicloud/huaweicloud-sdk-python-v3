# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResizeOrderRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_open_security_group_rule': 'bool',
        'execute_immediately': 'bool',
        'new_capacity': 'float',
        'password': 'str',
        'spec_code': 'str'
    }

    attribute_map = {
        'auto_open_security_group_rule': 'auto_open_security_group_rule',
        'execute_immediately': 'execute_immediately',
        'new_capacity': 'new_capacity',
        'password': 'password',
        'spec_code': 'spec_code'
    }

    def __init__(self, auto_open_security_group_rule=None, execute_immediately=None, new_capacity=None, password=None, spec_code=None):
        r"""CreateResizeOrderRequestBody

        The model defined in huaweicloud sdk

        :param auto_open_security_group_rule: 自动开启安全组规则
        :type auto_open_security_group_rule: bool
        :param execute_immediately: 启动迅速
        :type execute_immediately: bool
        :param new_capacity: 新的容量，单位是GB
        :type new_capacity: float
        :param password: 密码
        :type password: str
        :param spec_code: 区域代码
        :type spec_code: str
        """
        
        

        self._auto_open_security_group_rule = None
        self._execute_immediately = None
        self._new_capacity = None
        self._password = None
        self._spec_code = None
        self.discriminator = None

        if auto_open_security_group_rule is not None:
            self.auto_open_security_group_rule = auto_open_security_group_rule
        if execute_immediately is not None:
            self.execute_immediately = execute_immediately
        if new_capacity is not None:
            self.new_capacity = new_capacity
        if password is not None:
            self.password = password
        if spec_code is not None:
            self.spec_code = spec_code

    @property
    def auto_open_security_group_rule(self):
        r"""Gets the auto_open_security_group_rule of this CreateResizeOrderRequestBody.

        自动开启安全组规则

        :return: The auto_open_security_group_rule of this CreateResizeOrderRequestBody.
        :rtype: bool
        """
        return self._auto_open_security_group_rule

    @auto_open_security_group_rule.setter
    def auto_open_security_group_rule(self, auto_open_security_group_rule):
        r"""Sets the auto_open_security_group_rule of this CreateResizeOrderRequestBody.

        自动开启安全组规则

        :param auto_open_security_group_rule: The auto_open_security_group_rule of this CreateResizeOrderRequestBody.
        :type auto_open_security_group_rule: bool
        """
        self._auto_open_security_group_rule = auto_open_security_group_rule

    @property
    def execute_immediately(self):
        r"""Gets the execute_immediately of this CreateResizeOrderRequestBody.

        启动迅速

        :return: The execute_immediately of this CreateResizeOrderRequestBody.
        :rtype: bool
        """
        return self._execute_immediately

    @execute_immediately.setter
    def execute_immediately(self, execute_immediately):
        r"""Sets the execute_immediately of this CreateResizeOrderRequestBody.

        启动迅速

        :param execute_immediately: The execute_immediately of this CreateResizeOrderRequestBody.
        :type execute_immediately: bool
        """
        self._execute_immediately = execute_immediately

    @property
    def new_capacity(self):
        r"""Gets the new_capacity of this CreateResizeOrderRequestBody.

        新的容量，单位是GB

        :return: The new_capacity of this CreateResizeOrderRequestBody.
        :rtype: float
        """
        return self._new_capacity

    @new_capacity.setter
    def new_capacity(self, new_capacity):
        r"""Sets the new_capacity of this CreateResizeOrderRequestBody.

        新的容量，单位是GB

        :param new_capacity: The new_capacity of this CreateResizeOrderRequestBody.
        :type new_capacity: float
        """
        self._new_capacity = new_capacity

    @property
    def password(self):
        r"""Gets the password of this CreateResizeOrderRequestBody.

        密码

        :return: The password of this CreateResizeOrderRequestBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this CreateResizeOrderRequestBody.

        密码

        :param password: The password of this CreateResizeOrderRequestBody.
        :type password: str
        """
        self._password = password

    @property
    def spec_code(self):
        r"""Gets the spec_code of this CreateResizeOrderRequestBody.

        区域代码

        :return: The spec_code of this CreateResizeOrderRequestBody.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this CreateResizeOrderRequestBody.

        区域代码

        :param spec_code: The spec_code of this CreateResizeOrderRequestBody.
        :type spec_code: str
        """
        self._spec_code = spec_code

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
        if not isinstance(other, CreateResizeOrderRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
