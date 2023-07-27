# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTestCaseHistoriesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'version_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'version_id': 'version_id'
    }

    def __init__(self, offset=None, limit=None, version_id=None):
        """ListTestCaseHistoriesRequestBody

        The model defined in huaweicloud sdk

        :param offset: 起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于20000
        :type offset: int
        :param limit: 每页显示的条目数量,最大支持200条
        :type limit: int
        :param version_id: 版本ID（分支ID或测试计划ID），长度11-34位字符（字母和数字）。
        :type version_id: str
        """
        
        

        self._offset = None
        self._limit = None
        self._version_id = None
        self.discriminator = None

        self.offset = offset
        self.limit = limit
        self.version_id = version_id

    @property
    def offset(self):
        """Gets the offset of this ListTestCaseHistoriesRequestBody.

        起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于20000

        :return: The offset of this ListTestCaseHistoriesRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTestCaseHistoriesRequestBody.

        起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于20000

        :param offset: The offset of this ListTestCaseHistoriesRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListTestCaseHistoriesRequestBody.

        每页显示的条目数量,最大支持200条

        :return: The limit of this ListTestCaseHistoriesRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTestCaseHistoriesRequestBody.

        每页显示的条目数量,最大支持200条

        :param limit: The limit of this ListTestCaseHistoriesRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def version_id(self):
        """Gets the version_id of this ListTestCaseHistoriesRequestBody.

        版本ID（分支ID或测试计划ID），长度11-34位字符（字母和数字）。

        :return: The version_id of this ListTestCaseHistoriesRequestBody.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this ListTestCaseHistoriesRequestBody.

        版本ID（分支ID或测试计划ID），长度11-34位字符（字母和数字）。

        :param version_id: The version_id of this ListTestCaseHistoriesRequestBody.
        :type version_id: str
        """
        self._version_id = version_id

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
        if not isinstance(other, ListTestCaseHistoriesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
