# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NamedContext:

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
        r"""NamedContext

        The model defined in huaweicloud sdk

        :param name: 上下文的名称
        :type name: str
        :param context: 
        :type context: :class:`huaweicloudsdkucs.v1.Context`
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
        r"""Gets the name of this NamedContext.

        上下文的名称

        :return: The name of this NamedContext.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NamedContext.

        上下文的名称

        :param name: The name of this NamedContext.
        :type name: str
        """
        self._name = name

    @property
    def context(self):
        r"""Gets the context of this NamedContext.

        :return: The context of this NamedContext.
        :rtype: :class:`huaweicloudsdkucs.v1.Context`
        """
        return self._context

    @context.setter
    def context(self, context):
        r"""Sets the context of this NamedContext.

        :param context: The context of this NamedContext.
        :type context: :class:`huaweicloudsdkucs.v1.Context`
        """
        self._context = context

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NamedContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
