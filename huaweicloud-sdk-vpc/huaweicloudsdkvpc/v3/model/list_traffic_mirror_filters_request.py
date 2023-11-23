# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTrafficMirrorFiltersRequest:

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
        'name': 'str',
        'description': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, id=None, name=None, description=None, created_at=None, updated_at=None, limit=None, marker=None):
        """ListTrafficMirrorFiltersRequest

        The model defined in huaweicloud sdk

        :param id: 使用ID过滤查询或排序
        :type id: str
        :param name: 使用name过滤或排序
        :type name: str
        :param description: 使用description过滤查询
        :type description: str
        :param created_at: 使用创建时间戳排序
        :type created_at: str
        :param updated_at: 使用更新时间戳排序
        :type updated_at: str
        :param limit: 功能说明：每页返回的个数 取值范围：0-2000
        :type limit: int
        :param marker: 分页查询起始的资源ID，为空时查询第一页
        :type marker: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def id(self):
        """Gets the id of this ListTrafficMirrorFiltersRequest.

        使用ID过滤查询或排序

        :return: The id of this ListTrafficMirrorFiltersRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListTrafficMirrorFiltersRequest.

        使用ID过滤查询或排序

        :param id: The id of this ListTrafficMirrorFiltersRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListTrafficMirrorFiltersRequest.

        使用name过滤或排序

        :return: The name of this ListTrafficMirrorFiltersRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListTrafficMirrorFiltersRequest.

        使用name过滤或排序

        :param name: The name of this ListTrafficMirrorFiltersRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ListTrafficMirrorFiltersRequest.

        使用description过滤查询

        :return: The description of this ListTrafficMirrorFiltersRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListTrafficMirrorFiltersRequest.

        使用description过滤查询

        :param description: The description of this ListTrafficMirrorFiltersRequest.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this ListTrafficMirrorFiltersRequest.

        使用创建时间戳排序

        :return: The created_at of this ListTrafficMirrorFiltersRequest.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ListTrafficMirrorFiltersRequest.

        使用创建时间戳排序

        :param created_at: The created_at of this ListTrafficMirrorFiltersRequest.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ListTrafficMirrorFiltersRequest.

        使用更新时间戳排序

        :return: The updated_at of this ListTrafficMirrorFiltersRequest.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ListTrafficMirrorFiltersRequest.

        使用更新时间戳排序

        :param updated_at: The updated_at of this ListTrafficMirrorFiltersRequest.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def limit(self):
        """Gets the limit of this ListTrafficMirrorFiltersRequest.

        功能说明：每页返回的个数 取值范围：0-2000

        :return: The limit of this ListTrafficMirrorFiltersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTrafficMirrorFiltersRequest.

        功能说明：每页返回的个数 取值范围：0-2000

        :param limit: The limit of this ListTrafficMirrorFiltersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListTrafficMirrorFiltersRequest.

        分页查询起始的资源ID，为空时查询第一页

        :return: The marker of this ListTrafficMirrorFiltersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListTrafficMirrorFiltersRequest.

        分页查询起始的资源ID，为空时查询第一页

        :param marker: The marker of this ListTrafficMirrorFiltersRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListTrafficMirrorFiltersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
