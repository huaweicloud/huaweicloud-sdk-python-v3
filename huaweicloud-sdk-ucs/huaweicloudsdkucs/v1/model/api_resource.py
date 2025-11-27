# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class APIResource:

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
        'kind': 'str'
    }

    attribute_map = {
        'name': 'name',
        'kind': 'kind'
    }

    def __init__(self, name=None, kind=None):
        r"""APIResource

        The model defined in huaweicloud sdk

        :param name: 资源名
        :type name: str
        :param kind: 资源类别
        :type kind: str
        """
        
        

        self._name = None
        self._kind = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if kind is not None:
            self.kind = kind

    @property
    def name(self):
        r"""Gets the name of this APIResource.

        资源名

        :return: The name of this APIResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this APIResource.

        资源名

        :param name: The name of this APIResource.
        :type name: str
        """
        self._name = name

    @property
    def kind(self):
        r"""Gets the kind of this APIResource.

        资源类别

        :return: The kind of this APIResource.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this APIResource.

        资源类别

        :param kind: The kind of this APIResource.
        :type kind: str
        """
        self._kind = kind

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
        if not isinstance(other, APIResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
