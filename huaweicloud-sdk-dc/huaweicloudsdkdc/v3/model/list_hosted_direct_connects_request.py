# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostedDirectConnectsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'fields': 'list[str]',
        'sort_dir': 'list[str]',
        'sort_key': 'str',
        'hosting_id': 'list[str]',
        'id': 'list[str]',
        'name': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'fields': 'fields',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'hosting_id': 'hosting_id',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, limit=None, marker=None, fields=None, sort_dir=None, sort_key=None, hosting_id=None, id=None, name=None):
        """ListHostedDirectConnectsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~2000。
        :type limit: int
        :param marker: 上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。
        :type marker: str
        :param fields: 显示字段列表
        :type fields: list[str]
        :param sort_dir: 返回结果按照升序(asc)或降序(desc)排列，默认为asc
        :type sort_dir: list[str]
        :param sort_key: 排序字段。
        :type sort_key: str
        :param hosting_id: 根椐运营专线ID过滤托管专线列表
        :type hosting_id: list[str]
        :param id: 根据资源ID过滤实例
        :type id: list[str]
        :param name: 根据名字过滤查询，可查询多个名字。
        :type name: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._fields = None
        self._sort_dir = None
        self._sort_key = None
        self._hosting_id = None
        self._id = None
        self._name = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if fields is not None:
            self.fields = fields
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if hosting_id is not None:
            self.hosting_id = hosting_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def limit(self):
        """Gets the limit of this ListHostedDirectConnectsRequest.

        每页返回的个数。 取值范围：1~2000。

        :return: The limit of this ListHostedDirectConnectsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListHostedDirectConnectsRequest.

        每页返回的个数。 取值范围：1~2000。

        :param limit: The limit of this ListHostedDirectConnectsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListHostedDirectConnectsRequest.

        上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :return: The marker of this ListHostedDirectConnectsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListHostedDirectConnectsRequest.

        上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :param marker: The marker of this ListHostedDirectConnectsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def fields(self):
        """Gets the fields of this ListHostedDirectConnectsRequest.

        显示字段列表

        :return: The fields of this ListHostedDirectConnectsRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ListHostedDirectConnectsRequest.

        显示字段列表

        :param fields: The fields of this ListHostedDirectConnectsRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListHostedDirectConnectsRequest.

        返回结果按照升序(asc)或降序(desc)排列，默认为asc

        :return: The sort_dir of this ListHostedDirectConnectsRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListHostedDirectConnectsRequest.

        返回结果按照升序(asc)或降序(desc)排列，默认为asc

        :param sort_dir: The sort_dir of this ListHostedDirectConnectsRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        """Gets the sort_key of this ListHostedDirectConnectsRequest.

        排序字段。

        :return: The sort_key of this ListHostedDirectConnectsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListHostedDirectConnectsRequest.

        排序字段。

        :param sort_key: The sort_key of this ListHostedDirectConnectsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def hosting_id(self):
        """Gets the hosting_id of this ListHostedDirectConnectsRequest.

        根椐运营专线ID过滤托管专线列表

        :return: The hosting_id of this ListHostedDirectConnectsRequest.
        :rtype: list[str]
        """
        return self._hosting_id

    @hosting_id.setter
    def hosting_id(self, hosting_id):
        """Sets the hosting_id of this ListHostedDirectConnectsRequest.

        根椐运营专线ID过滤托管专线列表

        :param hosting_id: The hosting_id of this ListHostedDirectConnectsRequest.
        :type hosting_id: list[str]
        """
        self._hosting_id = hosting_id

    @property
    def id(self):
        """Gets the id of this ListHostedDirectConnectsRequest.

        根据资源ID过滤实例

        :return: The id of this ListHostedDirectConnectsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListHostedDirectConnectsRequest.

        根据资源ID过滤实例

        :param id: The id of this ListHostedDirectConnectsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListHostedDirectConnectsRequest.

        根据名字过滤查询，可查询多个名字。

        :return: The name of this ListHostedDirectConnectsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListHostedDirectConnectsRequest.

        根据名字过滤查询，可查询多个名字。

        :param name: The name of this ListHostedDirectConnectsRequest.
        :type name: list[str]
        """
        self._name = name

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
        if not isinstance(other, ListHostedDirectConnectsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
