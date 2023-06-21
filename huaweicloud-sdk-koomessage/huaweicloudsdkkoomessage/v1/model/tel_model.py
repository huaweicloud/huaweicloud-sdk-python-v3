# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TelModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tel': 'str',
        'usage': 'str'
    }

    attribute_map = {
        'tel': 'tel',
        'usage': 'usage'
    }

    def __init__(self, tel=None, usage=None):
        """TelModel

        The model defined in huaweicloud sdk

        :param tel: 电话号码（只能包含数字和”-“，且开头和结尾必须为数字）。
        :type tel: str
        :param usage: 号码用途。  &gt; 号码用途长度范围为1-30个字符，中文占2个字符，英文占1个字符。 
        :type usage: str
        """
        
        

        self._tel = None
        self._usage = None
        self.discriminator = None

        self.tel = tel
        self.usage = usage

    @property
    def tel(self):
        """Gets the tel of this TelModel.

        电话号码（只能包含数字和”-“，且开头和结尾必须为数字）。

        :return: The tel of this TelModel.
        :rtype: str
        """
        return self._tel

    @tel.setter
    def tel(self, tel):
        """Sets the tel of this TelModel.

        电话号码（只能包含数字和”-“，且开头和结尾必须为数字）。

        :param tel: The tel of this TelModel.
        :type tel: str
        """
        self._tel = tel

    @property
    def usage(self):
        """Gets the usage of this TelModel.

        号码用途。  > 号码用途长度范围为1-30个字符，中文占2个字符，英文占1个字符。 

        :return: The usage of this TelModel.
        :rtype: str
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this TelModel.

        号码用途。  > 号码用途长度范围为1-30个字符，中文占2个字符，英文占1个字符。 

        :param usage: The usage of this TelModel.
        :type usage: str
        """
        self._usage = usage

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
        if not isinstance(other, TelModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
