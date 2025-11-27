# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Match:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kinds': 'list[ResourceKinds]',
        'namespaces': 'list[str]'
    }

    attribute_map = {
        'kinds': 'kinds',
        'namespaces': 'namespaces'
    }

    def __init__(self, kinds=None, namespaces=None):
        r"""Match

        The model defined in huaweicloud sdk

        :param kinds: 生效类型，当前预置，填写不会生效
        :type kinds: list[:class:`huaweicloudsdkucs.v1.ResourceKinds`]
        :param namespaces: 生效的命名空间
        :type namespaces: list[str]
        """
        
        

        self._kinds = None
        self._namespaces = None
        self.discriminator = None

        if kinds is not None:
            self.kinds = kinds
        if namespaces is not None:
            self.namespaces = namespaces

    @property
    def kinds(self):
        r"""Gets the kinds of this Match.

        生效类型，当前预置，填写不会生效

        :return: The kinds of this Match.
        :rtype: list[:class:`huaweicloudsdkucs.v1.ResourceKinds`]
        """
        return self._kinds

    @kinds.setter
    def kinds(self, kinds):
        r"""Sets the kinds of this Match.

        生效类型，当前预置，填写不会生效

        :param kinds: The kinds of this Match.
        :type kinds: list[:class:`huaweicloudsdkucs.v1.ResourceKinds`]
        """
        self._kinds = kinds

    @property
    def namespaces(self):
        r"""Gets the namespaces of this Match.

        生效的命名空间

        :return: The namespaces of this Match.
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        r"""Sets the namespaces of this Match.

        生效的命名空间

        :param namespaces: The namespaces of this Match.
        :type namespaces: list[str]
        """
        self._namespaces = namespaces

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
        if not isinstance(other, Match):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
