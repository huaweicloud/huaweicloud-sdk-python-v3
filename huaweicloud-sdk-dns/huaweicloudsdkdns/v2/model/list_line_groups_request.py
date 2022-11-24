# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLineGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'line_id': 'str',
        'name': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'line_id': 'line_id',
        'name': 'name',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, line_id=None, name=None, limit=None, offset=None):
        """ListLineGroupsRequest

        The model defined in huaweicloud sdk

        :param line_id: 线路分组ID。 模糊匹配。
        :type line_id: str
        :param name: 线路分组名称。 模糊匹配。
        :type name: str
        :param limit: 每页返回的资源个数。 当查询详细信息时：取值范围：0~100取值一般为10，20，50默认为100。 当查询概要信息时：取值范围：0~3000默认为3000。
        :type limit: int
        :param offset: 取值范围：0~2147483647 分页查询起始页码，起始值为0。
        :type offset: int
        """
        
        

        self._line_id = None
        self._name = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if line_id is not None:
            self.line_id = line_id
        if name is not None:
            self.name = name
        self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def line_id(self):
        """Gets the line_id of this ListLineGroupsRequest.

        线路分组ID。 模糊匹配。

        :return: The line_id of this ListLineGroupsRequest.
        :rtype: str
        """
        return self._line_id

    @line_id.setter
    def line_id(self, line_id):
        """Sets the line_id of this ListLineGroupsRequest.

        线路分组ID。 模糊匹配。

        :param line_id: The line_id of this ListLineGroupsRequest.
        :type line_id: str
        """
        self._line_id = line_id

    @property
    def name(self):
        """Gets the name of this ListLineGroupsRequest.

        线路分组名称。 模糊匹配。

        :return: The name of this ListLineGroupsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListLineGroupsRequest.

        线路分组名称。 模糊匹配。

        :param name: The name of this ListLineGroupsRequest.
        :type name: str
        """
        self._name = name

    @property
    def limit(self):
        """Gets the limit of this ListLineGroupsRequest.

        每页返回的资源个数。 当查询详细信息时：取值范围：0~100取值一般为10，20，50默认为100。 当查询概要信息时：取值范围：0~3000默认为3000。

        :return: The limit of this ListLineGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListLineGroupsRequest.

        每页返回的资源个数。 当查询详细信息时：取值范围：0~100取值一般为10，20，50默认为100。 当查询概要信息时：取值范围：0~3000默认为3000。

        :param limit: The limit of this ListLineGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListLineGroupsRequest.

        取值范围：0~2147483647 分页查询起始页码，起始值为0。

        :return: The offset of this ListLineGroupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListLineGroupsRequest.

        取值范围：0~2147483647 分页查询起始页码，起始值为0。

        :param offset: The offset of this ListLineGroupsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListLineGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
