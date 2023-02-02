# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateStackRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stack_id': 'str',
        'description': 'str',
        'enable_deletion_protection': 'bool',
        'enable_auto_rollback': 'bool',
        'agencies': 'list[Agency]'
    }

    attribute_map = {
        'stack_id': 'stack_id',
        'description': 'description',
        'enable_deletion_protection': 'enable_deletion_protection',
        'enable_auto_rollback': 'enable_auto_rollback',
        'agencies': 'agencies'
    }

    def __init__(self, stack_id=None, description=None, enable_deletion_protection=None, enable_auto_rollback=None, agencies=None):
        """UpdateStackRequestBody

        The model defined in huaweicloud sdk

        :param stack_id: 资源栈Id
        :type stack_id: str
        :param description: 资源栈的描述
        :type description: str
        :param enable_deletion_protection: 是否开启删除保护
        :type enable_deletion_protection: bool
        :param enable_auto_rollback: 是否开启自动回滚
        :type enable_auto_rollback: bool
        :param agencies: 委托列表
        :type agencies: list[:class:`huaweicloudsdkaos.v1.Agency`]
        """
        
        

        self._stack_id = None
        self._description = None
        self._enable_deletion_protection = None
        self._enable_auto_rollback = None
        self._agencies = None
        self.discriminator = None

        if stack_id is not None:
            self.stack_id = stack_id
        if description is not None:
            self.description = description
        if enable_deletion_protection is not None:
            self.enable_deletion_protection = enable_deletion_protection
        if enable_auto_rollback is not None:
            self.enable_auto_rollback = enable_auto_rollback
        if agencies is not None:
            self.agencies = agencies

    @property
    def stack_id(self):
        """Gets the stack_id of this UpdateStackRequestBody.

        资源栈Id

        :return: The stack_id of this UpdateStackRequestBody.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this UpdateStackRequestBody.

        资源栈Id

        :param stack_id: The stack_id of this UpdateStackRequestBody.
        :type stack_id: str
        """
        self._stack_id = stack_id

    @property
    def description(self):
        """Gets the description of this UpdateStackRequestBody.

        资源栈的描述

        :return: The description of this UpdateStackRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateStackRequestBody.

        资源栈的描述

        :param description: The description of this UpdateStackRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def enable_deletion_protection(self):
        """Gets the enable_deletion_protection of this UpdateStackRequestBody.

        是否开启删除保护

        :return: The enable_deletion_protection of this UpdateStackRequestBody.
        :rtype: bool
        """
        return self._enable_deletion_protection

    @enable_deletion_protection.setter
    def enable_deletion_protection(self, enable_deletion_protection):
        """Sets the enable_deletion_protection of this UpdateStackRequestBody.

        是否开启删除保护

        :param enable_deletion_protection: The enable_deletion_protection of this UpdateStackRequestBody.
        :type enable_deletion_protection: bool
        """
        self._enable_deletion_protection = enable_deletion_protection

    @property
    def enable_auto_rollback(self):
        """Gets the enable_auto_rollback of this UpdateStackRequestBody.

        是否开启自动回滚

        :return: The enable_auto_rollback of this UpdateStackRequestBody.
        :rtype: bool
        """
        return self._enable_auto_rollback

    @enable_auto_rollback.setter
    def enable_auto_rollback(self, enable_auto_rollback):
        """Sets the enable_auto_rollback of this UpdateStackRequestBody.

        是否开启自动回滚

        :param enable_auto_rollback: The enable_auto_rollback of this UpdateStackRequestBody.
        :type enable_auto_rollback: bool
        """
        self._enable_auto_rollback = enable_auto_rollback

    @property
    def agencies(self):
        """Gets the agencies of this UpdateStackRequestBody.

        委托列表

        :return: The agencies of this UpdateStackRequestBody.
        :rtype: list[:class:`huaweicloudsdkaos.v1.Agency`]
        """
        return self._agencies

    @agencies.setter
    def agencies(self, agencies):
        """Sets the agencies of this UpdateStackRequestBody.

        委托列表

        :param agencies: The agencies of this UpdateStackRequestBody.
        :type agencies: list[:class:`huaweicloudsdkaos.v1.Agency`]
        """
        self._agencies = agencies

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
        if not isinstance(other, UpdateStackRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
