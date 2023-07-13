# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DbParamInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'common': 'list[DbParam]',
        'performance': 'list[DbParam]'
    }

    attribute_map = {
        'common': 'common',
        'performance': 'performance'
    }

    def __init__(self, common=None, performance=None):
        """DbParamInfo

        The model defined in huaweicloud sdk

        :param common: 常规参数。只有对比结果为不一致的目标库参数能被修改。
        :type common: list[:class:`huaweicloudsdkdrs.v5.DbParam`]
        :param performance: 性能参数。对比结果一致也可以修改目标库的值。
        :type performance: list[:class:`huaweicloudsdkdrs.v5.DbParam`]
        """
        
        

        self._common = None
        self._performance = None
        self.discriminator = None

        if common is not None:
            self.common = common
        if performance is not None:
            self.performance = performance

    @property
    def common(self):
        """Gets the common of this DbParamInfo.

        常规参数。只有对比结果为不一致的目标库参数能被修改。

        :return: The common of this DbParamInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.DbParam`]
        """
        return self._common

    @common.setter
    def common(self, common):
        """Sets the common of this DbParamInfo.

        常规参数。只有对比结果为不一致的目标库参数能被修改。

        :param common: The common of this DbParamInfo.
        :type common: list[:class:`huaweicloudsdkdrs.v5.DbParam`]
        """
        self._common = common

    @property
    def performance(self):
        """Gets the performance of this DbParamInfo.

        性能参数。对比结果一致也可以修改目标库的值。

        :return: The performance of this DbParamInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.DbParam`]
        """
        return self._performance

    @performance.setter
    def performance(self, performance):
        """Sets the performance of this DbParamInfo.

        性能参数。对比结果一致也可以修改目标库的值。

        :param performance: The performance of this DbParamInfo.
        :type performance: list[:class:`huaweicloudsdkdrs.v5.DbParam`]
        """
        self._performance = performance

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
        if not isinstance(other, DbParamInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
