# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClassroomsRequest:

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
        'query_type': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'query_type': 'query_type'
    }

    def __init__(self, offset=None, limit=None, query_type=None):
        """ListClassroomsRequest

        The model defined in huaweicloud sdk

        :param offset: 信息记录的起始编号
        :type offset: int
        :param limit: 每页包含的信息记录数
        :type limit: int
        :param query_type: 查询的课堂类别，默认查询所有的课堂。 取值范围： create：只查询当前用户创建的课堂。 attend：只查询当前用户加入的课堂。 all：查询当前用户所有的课堂。
        :type query_type: str
        """
        
        

        self._offset = None
        self._limit = None
        self._query_type = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if query_type is not None:
            self.query_type = query_type

    @property
    def offset(self):
        """Gets the offset of this ListClassroomsRequest.

        信息记录的起始编号

        :return: The offset of this ListClassroomsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListClassroomsRequest.

        信息记录的起始编号

        :param offset: The offset of this ListClassroomsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListClassroomsRequest.

        每页包含的信息记录数

        :return: The limit of this ListClassroomsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListClassroomsRequest.

        每页包含的信息记录数

        :param limit: The limit of this ListClassroomsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def query_type(self):
        """Gets the query_type of this ListClassroomsRequest.

        查询的课堂类别，默认查询所有的课堂。 取值范围： create：只查询当前用户创建的课堂。 attend：只查询当前用户加入的课堂。 all：查询当前用户所有的课堂。

        :return: The query_type of this ListClassroomsRequest.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this ListClassroomsRequest.

        查询的课堂类别，默认查询所有的课堂。 取值范围： create：只查询当前用户创建的课堂。 attend：只查询当前用户加入的课堂。 all：查询当前用户所有的课堂。

        :param query_type: The query_type of this ListClassroomsRequest.
        :type query_type: str
        """
        self._query_type = query_type

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
        if not isinstance(other, ListClassroomsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
