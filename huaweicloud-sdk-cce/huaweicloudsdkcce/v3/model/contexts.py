# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Contexts:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'context': 'Context'
    }

    attribute_map = {
        'name': 'name',
        'context': 'context'
    }

    def __init__(self, name=None, context=None):
        """Contexts

        The model defined in huaweicloud sdk

        :param name: 上下文的名称。 - 若不存在publicIp（虚拟机弹性IP），则集群列表的集群数量为1，该字段值为“internal”。 - 若存在publicIp，则集群列表的集群数量大于1，所有扩展的context的name的值为“external”。 
        :type name: str
        :param context: 
        :type context: :class:`huaweicloudsdkcce.v3.Context`
        """
        
        

        self._name = None
        self._context = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if context is not None:
            self.context = context

    @property
    def name(self):
        """Gets the name of this Contexts.

        上下文的名称。 - 若不存在publicIp（虚拟机弹性IP），则集群列表的集群数量为1，该字段值为“internal”。 - 若存在publicIp，则集群列表的集群数量大于1，所有扩展的context的name的值为“external”。 

        :return: The name of this Contexts.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Contexts.

        上下文的名称。 - 若不存在publicIp（虚拟机弹性IP），则集群列表的集群数量为1，该字段值为“internal”。 - 若存在publicIp，则集群列表的集群数量大于1，所有扩展的context的name的值为“external”。 

        :param name: The name of this Contexts.
        :type name: str
        """
        self._name = name

    @property
    def context(self):
        """Gets the context of this Contexts.

        :return: The context of this Contexts.
        :rtype: :class:`huaweicloudsdkcce.v3.Context`
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this Contexts.

        :param context: The context of this Contexts.
        :type context: :class:`huaweicloudsdkcce.v3.Context`
        """
        self._context = context

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
        if not isinstance(other, Contexts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
