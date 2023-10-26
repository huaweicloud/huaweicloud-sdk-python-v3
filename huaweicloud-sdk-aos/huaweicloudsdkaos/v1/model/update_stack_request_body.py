# coding: utf-8

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
        'description': 'str',
        'stack_id': 'str',
        'enable_deletion_protection': 'bool',
        'enable_auto_rollback': 'bool',
        'agencies': 'list[Agency]'
    }

    attribute_map = {
        'description': 'description',
        'stack_id': 'stack_id',
        'enable_deletion_protection': 'enable_deletion_protection',
        'enable_auto_rollback': 'enable_auto_rollback',
        'agencies': 'agencies'
    }

    def __init__(self, description=None, stack_id=None, enable_deletion_protection=None, enable_auto_rollback=None, agencies=None):
        """UpdateStackRequestBody

        The model defined in huaweicloud sdk

        :param description: 资源栈的描述。可用于客户识别自己的资源栈。
        :type description: str
        :param stack_id: 资源栈（stack）的唯一ID。  此ID由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给与的stack_id和当前资源栈的ID不一致，则返回400
        :type stack_id: str
        :param enable_deletion_protection: 删除保护的标识位，如果不传默认为false，即默认不开启资源栈删除保护（删除保护开启后资源栈不允许被删除）  *在UpdateStack API中，若该参数未在RequestBody中给予，则不会对资源栈的删除保护属性进行更新*
        :type enable_deletion_protection: bool
        :param enable_auto_rollback: 自动回滚的标识位，如果不传默认为false，即默认不开启资源栈自动回滚（自动回滚开启后，如果部署失败，则会自动回滚，并返回上一个稳定状态）  *在UpdateStack API中，若该参数未在RequestBody中给予，则不会对资源栈的自动回滚属性进行更新* *该属性与使用模板导入资源功能互斥，如果堆栈的自动回滚设置为true，则不允许部署包含导入资源的模板*
        :type enable_auto_rollback: bool
        :param agencies: 委托授权的信息。  RFS仅在创建资源栈（触发部署）、创建执行计划、部署资源栈、删除资源栈等涉及资源操作的请求中使用委托，且该委托仅作用于与之绑定的Provider对资源的操作中。若委托中提供的权限不足，有可能导致相关资源操作失败。  [创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)
        :type agencies: list[:class:`huaweicloudsdkaos.v1.Agency`]
        """
        
        

        self._description = None
        self._stack_id = None
        self._enable_deletion_protection = None
        self._enable_auto_rollback = None
        self._agencies = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if stack_id is not None:
            self.stack_id = stack_id
        if enable_deletion_protection is not None:
            self.enable_deletion_protection = enable_deletion_protection
        if enable_auto_rollback is not None:
            self.enable_auto_rollback = enable_auto_rollback
        if agencies is not None:
            self.agencies = agencies

    @property
    def description(self):
        """Gets the description of this UpdateStackRequestBody.

        资源栈的描述。可用于客户识别自己的资源栈。

        :return: The description of this UpdateStackRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateStackRequestBody.

        资源栈的描述。可用于客户识别自己的资源栈。

        :param description: The description of this UpdateStackRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def stack_id(self):
        """Gets the stack_id of this UpdateStackRequestBody.

        资源栈（stack）的唯一ID。  此ID由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给与的stack_id和当前资源栈的ID不一致，则返回400

        :return: The stack_id of this UpdateStackRequestBody.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this UpdateStackRequestBody.

        资源栈（stack）的唯一ID。  此ID由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给与的stack_id和当前资源栈的ID不一致，则返回400

        :param stack_id: The stack_id of this UpdateStackRequestBody.
        :type stack_id: str
        """
        self._stack_id = stack_id

    @property
    def enable_deletion_protection(self):
        """Gets the enable_deletion_protection of this UpdateStackRequestBody.

        删除保护的标识位，如果不传默认为false，即默认不开启资源栈删除保护（删除保护开启后资源栈不允许被删除）  *在UpdateStack API中，若该参数未在RequestBody中给予，则不会对资源栈的删除保护属性进行更新*

        :return: The enable_deletion_protection of this UpdateStackRequestBody.
        :rtype: bool
        """
        return self._enable_deletion_protection

    @enable_deletion_protection.setter
    def enable_deletion_protection(self, enable_deletion_protection):
        """Sets the enable_deletion_protection of this UpdateStackRequestBody.

        删除保护的标识位，如果不传默认为false，即默认不开启资源栈删除保护（删除保护开启后资源栈不允许被删除）  *在UpdateStack API中，若该参数未在RequestBody中给予，则不会对资源栈的删除保护属性进行更新*

        :param enable_deletion_protection: The enable_deletion_protection of this UpdateStackRequestBody.
        :type enable_deletion_protection: bool
        """
        self._enable_deletion_protection = enable_deletion_protection

    @property
    def enable_auto_rollback(self):
        """Gets the enable_auto_rollback of this UpdateStackRequestBody.

        自动回滚的标识位，如果不传默认为false，即默认不开启资源栈自动回滚（自动回滚开启后，如果部署失败，则会自动回滚，并返回上一个稳定状态）  *在UpdateStack API中，若该参数未在RequestBody中给予，则不会对资源栈的自动回滚属性进行更新* *该属性与使用模板导入资源功能互斥，如果堆栈的自动回滚设置为true，则不允许部署包含导入资源的模板*

        :return: The enable_auto_rollback of this UpdateStackRequestBody.
        :rtype: bool
        """
        return self._enable_auto_rollback

    @enable_auto_rollback.setter
    def enable_auto_rollback(self, enable_auto_rollback):
        """Sets the enable_auto_rollback of this UpdateStackRequestBody.

        自动回滚的标识位，如果不传默认为false，即默认不开启资源栈自动回滚（自动回滚开启后，如果部署失败，则会自动回滚，并返回上一个稳定状态）  *在UpdateStack API中，若该参数未在RequestBody中给予，则不会对资源栈的自动回滚属性进行更新* *该属性与使用模板导入资源功能互斥，如果堆栈的自动回滚设置为true，则不允许部署包含导入资源的模板*

        :param enable_auto_rollback: The enable_auto_rollback of this UpdateStackRequestBody.
        :type enable_auto_rollback: bool
        """
        self._enable_auto_rollback = enable_auto_rollback

    @property
    def agencies(self):
        """Gets the agencies of this UpdateStackRequestBody.

        委托授权的信息。  RFS仅在创建资源栈（触发部署）、创建执行计划、部署资源栈、删除资源栈等涉及资源操作的请求中使用委托，且该委托仅作用于与之绑定的Provider对资源的操作中。若委托中提供的权限不足，有可能导致相关资源操作失败。  [创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)

        :return: The agencies of this UpdateStackRequestBody.
        :rtype: list[:class:`huaweicloudsdkaos.v1.Agency`]
        """
        return self._agencies

    @agencies.setter
    def agencies(self, agencies):
        """Sets the agencies of this UpdateStackRequestBody.

        委托授权的信息。  RFS仅在创建资源栈（触发部署）、创建执行计划、部署资源栈、删除资源栈等涉及资源操作的请求中使用委托，且该委托仅作用于与之绑定的Provider对资源的操作中。若委托中提供的权限不足，有可能导致相关资源操作失败。  [创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)

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
