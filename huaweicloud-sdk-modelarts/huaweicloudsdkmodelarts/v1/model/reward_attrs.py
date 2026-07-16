# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RewardAttrs:

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
        'mode': 'str',
        'regex': 'str'
    }

    attribute_map = {
        'name': 'name',
        'mode': 'mode',
        'regex': 'regex'
    }

    def __init__(self, name=None, mode=None, regex=None):
        r"""RewardAttrs

        The model defined in huaweicloud sdk

        :param name: 指标名称。
        :type name: str
        :param mode: 搜索方向。 - max指定时表示指标值越大越好； - min指定时表示指标值越小越好。
        :type mode: str
        :param regex: 指标正则表达式。
        :type regex: str
        """
        
        

        self._name = None
        self._mode = None
        self._regex = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if mode is not None:
            self.mode = mode
        if regex is not None:
            self.regex = regex

    @property
    def name(self):
        r"""Gets the name of this RewardAttrs.

        指标名称。

        :return: The name of this RewardAttrs.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RewardAttrs.

        指标名称。

        :param name: The name of this RewardAttrs.
        :type name: str
        """
        self._name = name

    @property
    def mode(self):
        r"""Gets the mode of this RewardAttrs.

        搜索方向。 - max指定时表示指标值越大越好； - min指定时表示指标值越小越好。

        :return: The mode of this RewardAttrs.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this RewardAttrs.

        搜索方向。 - max指定时表示指标值越大越好； - min指定时表示指标值越小越好。

        :param mode: The mode of this RewardAttrs.
        :type mode: str
        """
        self._mode = mode

    @property
    def regex(self):
        r"""Gets the regex of this RewardAttrs.

        指标正则表达式。

        :return: The regex of this RewardAttrs.
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        r"""Sets the regex of this RewardAttrs.

        指标正则表达式。

        :param regex: The regex of this RewardAttrs.
        :type regex: str
        """
        self._regex = regex

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
        if not isinstance(other, RewardAttrs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
