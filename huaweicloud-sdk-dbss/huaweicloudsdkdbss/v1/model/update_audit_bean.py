# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAuditBean:

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
        'comment': 'str'
    }

    attribute_map = {
        'name': 'name',
        'comment': 'comment'
    }

    def __init__(self, name=None, comment=None):
        r"""UpdateAuditBean

        The model defined in huaweicloud sdk

        :param name: 实例名称。只能由中文字符,英文字母,数字,下划线,中划线组成的字符串,长度小于等于64。不能为空字符串。
        :type name: str
        :param comment: 实例描述信息，只能由中文字符,英文字母,数字,下划线,中划线,空格组成的字符串，长度小于等于255。可以为空字符串。
        :type comment: str
        """
        
        

        self._name = None
        self._comment = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if comment is not None:
            self.comment = comment

    @property
    def name(self):
        r"""Gets the name of this UpdateAuditBean.

        实例名称。只能由中文字符,英文字母,数字,下划线,中划线组成的字符串,长度小于等于64。不能为空字符串。

        :return: The name of this UpdateAuditBean.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateAuditBean.

        实例名称。只能由中文字符,英文字母,数字,下划线,中划线组成的字符串,长度小于等于64。不能为空字符串。

        :param name: The name of this UpdateAuditBean.
        :type name: str
        """
        self._name = name

    @property
    def comment(self):
        r"""Gets the comment of this UpdateAuditBean.

        实例描述信息，只能由中文字符,英文字母,数字,下划线,中划线,空格组成的字符串，长度小于等于255。可以为空字符串。

        :return: The comment of this UpdateAuditBean.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this UpdateAuditBean.

        实例描述信息，只能由中文字符,英文字母,数字,下划线,中划线,空格组成的字符串，长度小于等于255。可以为空字符串。

        :param comment: The comment of this UpdateAuditBean.
        :type comment: str
        """
        self._comment = comment

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
        if not isinstance(other, UpdateAuditBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
