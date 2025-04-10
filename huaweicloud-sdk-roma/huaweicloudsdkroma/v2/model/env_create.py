# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnvCreate:

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
        'remark': 'str'
    }

    attribute_map = {
        'name': 'name',
        'remark': 'remark'
    }

    def __init__(self, name=None, remark=None):
        r"""EnvCreate

        The model defined in huaweicloud sdk

        :param name: 环境的名称，支持英文，数字，下划线，且只能以英文字母开头。
        :type name: str
        :param remark: 描述信息 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type remark: str
        """
        
        

        self._name = None
        self._remark = None
        self.discriminator = None

        self.name = name
        if remark is not None:
            self.remark = remark

    @property
    def name(self):
        r"""Gets the name of this EnvCreate.

        环境的名称，支持英文，数字，下划线，且只能以英文字母开头。

        :return: The name of this EnvCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EnvCreate.

        环境的名称，支持英文，数字，下划线，且只能以英文字母开头。

        :param name: The name of this EnvCreate.
        :type name: str
        """
        self._name = name

    @property
    def remark(self):
        r"""Gets the remark of this EnvCreate.

        描述信息 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this EnvCreate.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this EnvCreate.

        描述信息 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this EnvCreate.
        :type remark: str
        """
        self._remark = remark

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
        if not isinstance(other, EnvCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
