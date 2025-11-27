# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceKinds:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_groups': 'list[str]',
        'kinds': 'list[str]'
    }

    attribute_map = {
        'api_groups': 'apiGroups',
        'kinds': 'kinds'
    }

    def __init__(self, api_groups=None, kinds=None):
        r"""ResourceKinds

        The model defined in huaweicloud sdk

        :param api_groups: 资源所属的API组
        :type api_groups: list[str]
        :param kinds: 资源类型
        :type kinds: list[str]
        """
        
        

        self._api_groups = None
        self._kinds = None
        self.discriminator = None

        if api_groups is not None:
            self.api_groups = api_groups
        if kinds is not None:
            self.kinds = kinds

    @property
    def api_groups(self):
        r"""Gets the api_groups of this ResourceKinds.

        资源所属的API组

        :return: The api_groups of this ResourceKinds.
        :rtype: list[str]
        """
        return self._api_groups

    @api_groups.setter
    def api_groups(self, api_groups):
        r"""Sets the api_groups of this ResourceKinds.

        资源所属的API组

        :param api_groups: The api_groups of this ResourceKinds.
        :type api_groups: list[str]
        """
        self._api_groups = api_groups

    @property
    def kinds(self):
        r"""Gets the kinds of this ResourceKinds.

        资源类型

        :return: The kinds of this ResourceKinds.
        :rtype: list[str]
        """
        return self._kinds

    @kinds.setter
    def kinds(self, kinds):
        r"""Sets the kinds of this ResourceKinds.

        资源类型

        :param kinds: The kinds of this ResourceKinds.
        :type kinds: list[str]
        """
        self._kinds = kinds

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
        if not isinstance(other, ResourceKinds):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
