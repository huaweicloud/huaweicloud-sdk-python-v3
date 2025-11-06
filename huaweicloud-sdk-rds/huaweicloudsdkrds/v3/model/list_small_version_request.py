# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSmallVersionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_name': 'str',
        'version': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'database_name': 'database_name',
        'version': 'version',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, database_name=None, version=None, offset=None, limit=None):
        r"""ListSmallVersionRequest

        The model defined in huaweicloud sdk

        :param database_name: 数据库引擎名。 取值范围： 支持的引擎如下，不区分大小写： PostgreSQL
        :type database_name: str
        :param version: 数据库版本号。（可输入小版本号）
        :type version: str
        :param offset: 参数解释： 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 约束限制：必须为数字，不能为负数。 取值范围：大于等于0的整数。 默认取值：0
        :type offset: int
        :param limit: 参数解释： 查询记录数。 约束限制：不涉及。 取值范围：默认为100，不能为负数，最小值为1，最大值为100。 默认取值：100
        :type limit: int
        """
        
        

        self._database_name = None
        self._version = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.database_name = database_name
        self.version = version
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def database_name(self):
        r"""Gets the database_name of this ListSmallVersionRequest.

        数据库引擎名。 取值范围： 支持的引擎如下，不区分大小写： PostgreSQL

        :return: The database_name of this ListSmallVersionRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ListSmallVersionRequest.

        数据库引擎名。 取值范围： 支持的引擎如下，不区分大小写： PostgreSQL

        :param database_name: The database_name of this ListSmallVersionRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def version(self):
        r"""Gets the version of this ListSmallVersionRequest.

        数据库版本号。（可输入小版本号）

        :return: The version of this ListSmallVersionRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListSmallVersionRequest.

        数据库版本号。（可输入小版本号）

        :param version: The version of this ListSmallVersionRequest.
        :type version: str
        """
        self._version = version

    @property
    def offset(self):
        r"""Gets the offset of this ListSmallVersionRequest.

        参数解释： 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 约束限制：必须为数字，不能为负数。 取值范围：大于等于0的整数。 默认取值：0

        :return: The offset of this ListSmallVersionRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSmallVersionRequest.

        参数解释： 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 约束限制：必须为数字，不能为负数。 取值范围：大于等于0的整数。 默认取值：0

        :param offset: The offset of this ListSmallVersionRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSmallVersionRequest.

        参数解释： 查询记录数。 约束限制：不涉及。 取值范围：默认为100，不能为负数，最小值为1，最大值为100。 默认取值：100

        :return: The limit of this ListSmallVersionRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSmallVersionRequest.

        参数解释： 查询记录数。 约束限制：不涉及。 取值范围：默认为100，不能为负数，最小值为1，最大值为100。 默认取值：100

        :param limit: The limit of this ListSmallVersionRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListSmallVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
