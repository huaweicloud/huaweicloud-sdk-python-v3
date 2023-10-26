# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnableAutoRollbackPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_auto_rollback': 'bool'
    }

    attribute_map = {
        'enable_auto_rollback': 'enable_auto_rollback'
    }

    def __init__(self, enable_auto_rollback=None):
        """EnableAutoRollbackPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param enable_auto_rollback: 自动回滚的标识位，如果不传默认为false，即默认不开启资源栈自动回滚（自动回滚开启后，如果部署失败，则会自动回滚，并返回上一个稳定状态）  *在UpdateStack API中，若该参数未在RequestBody中给予，则不会对资源栈的自动回滚属性进行更新* *该属性与使用模板导入资源功能互斥，如果堆栈的自动回滚设置为true，则不允许部署包含导入资源的模板*
        :type enable_auto_rollback: bool
        """
        
        

        self._enable_auto_rollback = None
        self.discriminator = None

        if enable_auto_rollback is not None:
            self.enable_auto_rollback = enable_auto_rollback

    @property
    def enable_auto_rollback(self):
        """Gets the enable_auto_rollback of this EnableAutoRollbackPrimitiveTypeHolder.

        自动回滚的标识位，如果不传默认为false，即默认不开启资源栈自动回滚（自动回滚开启后，如果部署失败，则会自动回滚，并返回上一个稳定状态）  *在UpdateStack API中，若该参数未在RequestBody中给予，则不会对资源栈的自动回滚属性进行更新* *该属性与使用模板导入资源功能互斥，如果堆栈的自动回滚设置为true，则不允许部署包含导入资源的模板*

        :return: The enable_auto_rollback of this EnableAutoRollbackPrimitiveTypeHolder.
        :rtype: bool
        """
        return self._enable_auto_rollback

    @enable_auto_rollback.setter
    def enable_auto_rollback(self, enable_auto_rollback):
        """Sets the enable_auto_rollback of this EnableAutoRollbackPrimitiveTypeHolder.

        自动回滚的标识位，如果不传默认为false，即默认不开启资源栈自动回滚（自动回滚开启后，如果部署失败，则会自动回滚，并返回上一个稳定状态）  *在UpdateStack API中，若该参数未在RequestBody中给予，则不会对资源栈的自动回滚属性进行更新* *该属性与使用模板导入资源功能互斥，如果堆栈的自动回滚设置为true，则不允许部署包含导入资源的模板*

        :param enable_auto_rollback: The enable_auto_rollback of this EnableAutoRollbackPrimitiveTypeHolder.
        :type enable_auto_rollback: bool
        """
        self._enable_auto_rollback = enable_auto_rollback

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
        if not isinstance(other, EnableAutoRollbackPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
