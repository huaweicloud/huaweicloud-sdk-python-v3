# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRoutetablesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'limit': 'int',
        'name': 'str',
        'offset': 'int',
        'vpc_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'limit': 'limit',
        'name': 'name',
        'offset': 'offset',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, id=None, limit=None, name=None, offset=None, vpc_id=None):
        """ListRoutetablesRequest

        The model defined in huaweicloud sdk

        :param id: 路由表ID
        :type id: str
        :param limit: 每页的最大数
        :type limit: int
        :param name: 路由表名称。
        :type name: str
        :param offset: 偏移量
        :type offset: int
        :param vpc_id: vpc的ID
        :type vpc_id: str
        """
        
        

        self._id = None
        self._limit = None
        self._name = None
        self._offset = None
        self._vpc_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def id(self):
        """Gets the id of this ListRoutetablesRequest.

        路由表ID

        :return: The id of this ListRoutetablesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListRoutetablesRequest.

        路由表ID

        :param id: The id of this ListRoutetablesRequest.
        :type id: str
        """
        self._id = id

    @property
    def limit(self):
        """Gets the limit of this ListRoutetablesRequest.

        每页的最大数

        :return: The limit of this ListRoutetablesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRoutetablesRequest.

        每页的最大数

        :param limit: The limit of this ListRoutetablesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListRoutetablesRequest.

        路由表名称。

        :return: The name of this ListRoutetablesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListRoutetablesRequest.

        路由表名称。

        :param name: The name of this ListRoutetablesRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ListRoutetablesRequest.

        偏移量

        :return: The offset of this ListRoutetablesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRoutetablesRequest.

        偏移量

        :param offset: The offset of this ListRoutetablesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListRoutetablesRequest.

        vpc的ID

        :return: The vpc_id of this ListRoutetablesRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListRoutetablesRequest.

        vpc的ID

        :param vpc_id: The vpc_id of this ListRoutetablesRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, ListRoutetablesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
