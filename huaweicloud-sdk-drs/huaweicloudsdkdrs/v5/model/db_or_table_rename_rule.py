# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DbOrTableRenameRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'prefix_name': 'str',
        'suffix_name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'prefix_name': 'prefix_name',
        'suffix_name': 'suffix_name',
        'type': 'type'
    }

    def __init__(self, prefix_name=None, suffix_name=None, type=None):
        r"""DbOrTableRenameRule

        The model defined in huaweicloud sdk

        :param prefix_name: 前缀名称 当type为prefixAndSuffix， 填写prefix_name，库表名称仅增加前缀，若同时也填写suffix_name, 库表名称增加前后缀
        :type prefix_name: str
        :param suffix_name: 后缀名称 当type为prefixAndSuffix， 填写suffix_name，库表名称仅增加后缀，若同时也填写prefix_name, 库表名称同时增加前后缀
        :type suffix_name: str
        :param type: 库表映射类型 prefixAndSuffix:前缀、后缀或者前后缀
        :type type: str
        """
        
        

        self._prefix_name = None
        self._suffix_name = None
        self._type = None
        self.discriminator = None

        if prefix_name is not None:
            self.prefix_name = prefix_name
        if suffix_name is not None:
            self.suffix_name = suffix_name
        if type is not None:
            self.type = type

    @property
    def prefix_name(self):
        r"""Gets the prefix_name of this DbOrTableRenameRule.

        前缀名称 当type为prefixAndSuffix， 填写prefix_name，库表名称仅增加前缀，若同时也填写suffix_name, 库表名称增加前后缀

        :return: The prefix_name of this DbOrTableRenameRule.
        :rtype: str
        """
        return self._prefix_name

    @prefix_name.setter
    def prefix_name(self, prefix_name):
        r"""Sets the prefix_name of this DbOrTableRenameRule.

        前缀名称 当type为prefixAndSuffix， 填写prefix_name，库表名称仅增加前缀，若同时也填写suffix_name, 库表名称增加前后缀

        :param prefix_name: The prefix_name of this DbOrTableRenameRule.
        :type prefix_name: str
        """
        self._prefix_name = prefix_name

    @property
    def suffix_name(self):
        r"""Gets the suffix_name of this DbOrTableRenameRule.

        后缀名称 当type为prefixAndSuffix， 填写suffix_name，库表名称仅增加后缀，若同时也填写prefix_name, 库表名称同时增加前后缀

        :return: The suffix_name of this DbOrTableRenameRule.
        :rtype: str
        """
        return self._suffix_name

    @suffix_name.setter
    def suffix_name(self, suffix_name):
        r"""Sets the suffix_name of this DbOrTableRenameRule.

        后缀名称 当type为prefixAndSuffix， 填写suffix_name，库表名称仅增加后缀，若同时也填写prefix_name, 库表名称同时增加前后缀

        :param suffix_name: The suffix_name of this DbOrTableRenameRule.
        :type suffix_name: str
        """
        self._suffix_name = suffix_name

    @property
    def type(self):
        r"""Gets the type of this DbOrTableRenameRule.

        库表映射类型 prefixAndSuffix:前缀、后缀或者前后缀

        :return: The type of this DbOrTableRenameRule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DbOrTableRenameRule.

        库表映射类型 prefixAndSuffix:前缀、后缀或者前后缀

        :param type: The type of this DbOrTableRenameRule.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, DbOrTableRenameRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
