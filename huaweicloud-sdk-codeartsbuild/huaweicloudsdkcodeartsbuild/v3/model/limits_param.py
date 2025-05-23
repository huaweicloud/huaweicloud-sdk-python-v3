# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LimitsParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disable': 'str',
        'display_name': 'str',
        'name': 'str'
    }

    attribute_map = {
        'disable': 'disable',
        'display_name': 'display_name',
        'name': 'name'
    }

    def __init__(self, disable=None, display_name=None, name=None):
        r"""LimitsParam

        The model defined in huaweicloud sdk

        :param disable: 是否生效，默认为\&quot;0\&quot;，为生效状态
        :type disable: str
        :param display_name: 参数展示的名字
        :type display_name: str
        :param name: 参数名字
        :type name: str
        """
        
        

        self._disable = None
        self._display_name = None
        self._name = None
        self.discriminator = None

        if disable is not None:
            self.disable = disable
        if display_name is not None:
            self.display_name = display_name
        if name is not None:
            self.name = name

    @property
    def disable(self):
        r"""Gets the disable of this LimitsParam.

        是否生效，默认为\"0\"，为生效状态

        :return: The disable of this LimitsParam.
        :rtype: str
        """
        return self._disable

    @disable.setter
    def disable(self, disable):
        r"""Sets the disable of this LimitsParam.

        是否生效，默认为\"0\"，为生效状态

        :param disable: The disable of this LimitsParam.
        :type disable: str
        """
        self._disable = disable

    @property
    def display_name(self):
        r"""Gets the display_name of this LimitsParam.

        参数展示的名字

        :return: The display_name of this LimitsParam.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this LimitsParam.

        参数展示的名字

        :param display_name: The display_name of this LimitsParam.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def name(self):
        r"""Gets the name of this LimitsParam.

        参数名字

        :return: The name of this LimitsParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LimitsParam.

        参数名字

        :param name: The name of this LimitsParam.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, LimitsParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
