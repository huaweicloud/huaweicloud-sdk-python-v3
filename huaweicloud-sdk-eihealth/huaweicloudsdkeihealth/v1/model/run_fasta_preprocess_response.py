# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunFastaPreprocessResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'has_more': 'bool'
    }

    attribute_map = {
        'count': 'count',
        'has_more': 'has_more'
    }

    def __init__(self, count=None, has_more=None):
        r"""RunFastaPreprocessResponse

        The model defined in huaweicloud sdk

        :param count: 已知的蛋白序列数量
        :type count: int
        :param has_more: 文件中是否还有更多氨基酸序列没有处理
        :type has_more: bool
        """
        
        super(RunFastaPreprocessResponse, self).__init__()

        self._count = None
        self._has_more = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if has_more is not None:
            self.has_more = has_more

    @property
    def count(self):
        r"""Gets the count of this RunFastaPreprocessResponse.

        已知的蛋白序列数量

        :return: The count of this RunFastaPreprocessResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this RunFastaPreprocessResponse.

        已知的蛋白序列数量

        :param count: The count of this RunFastaPreprocessResponse.
        :type count: int
        """
        self._count = count

    @property
    def has_more(self):
        r"""Gets the has_more of this RunFastaPreprocessResponse.

        文件中是否还有更多氨基酸序列没有处理

        :return: The has_more of this RunFastaPreprocessResponse.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        r"""Sets the has_more of this RunFastaPreprocessResponse.

        文件中是否还有更多氨基酸序列没有处理

        :param has_more: The has_more of this RunFastaPreprocessResponse.
        :type has_more: bool
        """
        self._has_more = has_more

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
        if not isinstance(other, RunFastaPreprocessResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
