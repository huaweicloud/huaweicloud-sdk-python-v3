# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailableTag:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mode': 'str',
        'alias': 'str',
        'public_border_group': 'str'
    }

    attribute_map = {
        'mode': 'mode',
        'alias': 'alias',
        'public_border_group': 'public_border_group'
    }

    def __init__(self, mode=None, alias=None, public_border_group=None):
        r"""AvailableTag

        The model defined in huaweicloud sdk

        :param mode: 可用区计费模式，分为专属dedicated和共享shard
        :type mode: str
        :param alias: az的别名
        :type alias: str
        :param public_border_group: 所属group。默认为”center”
        :type public_border_group: str
        """
        
        

        self._mode = None
        self._alias = None
        self._public_border_group = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode
        if alias is not None:
            self.alias = alias
        if public_border_group is not None:
            self.public_border_group = public_border_group

    @property
    def mode(self):
        r"""Gets the mode of this AvailableTag.

        可用区计费模式，分为专属dedicated和共享shard

        :return: The mode of this AvailableTag.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this AvailableTag.

        可用区计费模式，分为专属dedicated和共享shard

        :param mode: The mode of this AvailableTag.
        :type mode: str
        """
        self._mode = mode

    @property
    def alias(self):
        r"""Gets the alias of this AvailableTag.

        az的别名

        :return: The alias of this AvailableTag.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this AvailableTag.

        az的别名

        :param alias: The alias of this AvailableTag.
        :type alias: str
        """
        self._alias = alias

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this AvailableTag.

        所属group。默认为”center”

        :return: The public_border_group of this AvailableTag.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this AvailableTag.

        所属group。默认为”center”

        :param public_border_group: The public_border_group of this AvailableTag.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

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
        if not isinstance(other, AvailableTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
