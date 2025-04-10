# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identify_condition': 'str',
        'publisher': 'str',
        'product_name': 'str',
        'process_name': 'str',
        'support_os': 'str',
        'version': 'str',
        'product_version': 'str'
    }

    attribute_map = {
        'identify_condition': 'identify_condition',
        'publisher': 'publisher',
        'product_name': 'product_name',
        'process_name': 'process_name',
        'support_os': 'support_os',
        'version': 'version',
        'product_version': 'product_version'
    }

    def __init__(self, identify_condition=None, publisher=None, product_name=None, process_name=None, support_os=None, version=None, product_version=None):
        r"""ProductRule

        The model defined in huaweicloud sdk

        :param identify_condition: 识别条件。
        :type identify_condition: str
        :param publisher: 发布者名称： 1. 名称允许可见字符或空格，不可为全空格。 2. 长度0~1024个字符。 3. 为空或者*号表示任意匹配。
        :type publisher: str
        :param product_name: 产品名称： 1. 名称允许可见字符或空格，不可为全空格。 2. 长度0~128个字符。 3. 为空或者*号表示任意匹配。
        :type product_name: str
        :param process_name: 进程名称： 1. 名称允许可见字符或空格，不可为全空格。 2. 长度0~128个字符。 3. 为空或者*号表示任意匹配。
        :type process_name: str
        :param support_os: 操作系统类型，仅内置规则存在该字段。 1. 名称允许可见字符或空格，不可为全空格。 2. 长度0~128个字符。
        :type support_os: str
        :param version: 版本号： 1. 名称允许可见字符或空格，不可为全空格。 2. 长度0~128个字符。 3. 为空或者*号表示任意匹配。
        :type version: str
        :param product_version: 产品版本号： 1. 允许可见字符。 2. 长度0~128个字符。
        :type product_version: str
        """
        
        

        self._identify_condition = None
        self._publisher = None
        self._product_name = None
        self._process_name = None
        self._support_os = None
        self._version = None
        self._product_version = None
        self.discriminator = None

        if identify_condition is not None:
            self.identify_condition = identify_condition
        if publisher is not None:
            self.publisher = publisher
        if product_name is not None:
            self.product_name = product_name
        if process_name is not None:
            self.process_name = process_name
        if support_os is not None:
            self.support_os = support_os
        if version is not None:
            self.version = version
        if product_version is not None:
            self.product_version = product_version

    @property
    def identify_condition(self):
        r"""Gets the identify_condition of this ProductRule.

        识别条件。

        :return: The identify_condition of this ProductRule.
        :rtype: str
        """
        return self._identify_condition

    @identify_condition.setter
    def identify_condition(self, identify_condition):
        r"""Sets the identify_condition of this ProductRule.

        识别条件。

        :param identify_condition: The identify_condition of this ProductRule.
        :type identify_condition: str
        """
        self._identify_condition = identify_condition

    @property
    def publisher(self):
        r"""Gets the publisher of this ProductRule.

        发布者名称： 1. 名称允许可见字符或空格，不可为全空格。 2. 长度0~1024个字符。 3. 为空或者*号表示任意匹配。

        :return: The publisher of this ProductRule.
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        r"""Sets the publisher of this ProductRule.

        发布者名称： 1. 名称允许可见字符或空格，不可为全空格。 2. 长度0~1024个字符。 3. 为空或者*号表示任意匹配。

        :param publisher: The publisher of this ProductRule.
        :type publisher: str
        """
        self._publisher = publisher

    @property
    def product_name(self):
        r"""Gets the product_name of this ProductRule.

        产品名称： 1. 名称允许可见字符或空格，不可为全空格。 2. 长度0~128个字符。 3. 为空或者*号表示任意匹配。

        :return: The product_name of this ProductRule.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this ProductRule.

        产品名称： 1. 名称允许可见字符或空格，不可为全空格。 2. 长度0~128个字符。 3. 为空或者*号表示任意匹配。

        :param product_name: The product_name of this ProductRule.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def process_name(self):
        r"""Gets the process_name of this ProductRule.

        进程名称： 1. 名称允许可见字符或空格，不可为全空格。 2. 长度0~128个字符。 3. 为空或者*号表示任意匹配。

        :return: The process_name of this ProductRule.
        :rtype: str
        """
        return self._process_name

    @process_name.setter
    def process_name(self, process_name):
        r"""Sets the process_name of this ProductRule.

        进程名称： 1. 名称允许可见字符或空格，不可为全空格。 2. 长度0~128个字符。 3. 为空或者*号表示任意匹配。

        :param process_name: The process_name of this ProductRule.
        :type process_name: str
        """
        self._process_name = process_name

    @property
    def support_os(self):
        r"""Gets the support_os of this ProductRule.

        操作系统类型，仅内置规则存在该字段。 1. 名称允许可见字符或空格，不可为全空格。 2. 长度0~128个字符。

        :return: The support_os of this ProductRule.
        :rtype: str
        """
        return self._support_os

    @support_os.setter
    def support_os(self, support_os):
        r"""Sets the support_os of this ProductRule.

        操作系统类型，仅内置规则存在该字段。 1. 名称允许可见字符或空格，不可为全空格。 2. 长度0~128个字符。

        :param support_os: The support_os of this ProductRule.
        :type support_os: str
        """
        self._support_os = support_os

    @property
    def version(self):
        r"""Gets the version of this ProductRule.

        版本号： 1. 名称允许可见字符或空格，不可为全空格。 2. 长度0~128个字符。 3. 为空或者*号表示任意匹配。

        :return: The version of this ProductRule.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ProductRule.

        版本号： 1. 名称允许可见字符或空格，不可为全空格。 2. 长度0~128个字符。 3. 为空或者*号表示任意匹配。

        :param version: The version of this ProductRule.
        :type version: str
        """
        self._version = version

    @property
    def product_version(self):
        r"""Gets the product_version of this ProductRule.

        产品版本号： 1. 允许可见字符。 2. 长度0~128个字符。

        :return: The product_version of this ProductRule.
        :rtype: str
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        r"""Sets the product_version of this ProductRule.

        产品版本号： 1. 允许可见字符。 2. 长度0~128个字符。

        :param product_version: The product_version of this ProductRule.
        :type product_version: str
        """
        self._product_version = product_version

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
        if not isinstance(other, ProductRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
