# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplicationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id_list': 'list[str]',
        'parent_id': 'str',
        'name_like': 'str',
        'code': 'str',
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'id_list': 'id_list',
        'parent_id': 'parent_id',
        'name_like': 'name_like',
        'code': 'code',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, id_list=None, parent_id=None, name_like=None, code=None, marker=None, limit=None):
        """ListApplicationsRequest

        The model defined in huaweicloud sdk

        :param id_list: id列表
        :type id_list: list[str]
        :param parent_id: parent id
        :type parent_id: str
        :param name_like: 应用名称模糊匹配
        :type name_like: str
        :param code: 应用code
        :type code: str
        :param marker: 分页参数，上一页请求最后一个id
        :type marker: str
        :param limit: 最大的返回数量
        :type limit: int
        """
        
        

        self._id_list = None
        self._parent_id = None
        self._name_like = None
        self._code = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        if id_list is not None:
            self.id_list = id_list
        if parent_id is not None:
            self.parent_id = parent_id
        if name_like is not None:
            self.name_like = name_like
        if code is not None:
            self.code = code
        if marker is not None:
            self.marker = marker
        self.limit = limit

    @property
    def id_list(self):
        """Gets the id_list of this ListApplicationsRequest.

        id列表

        :return: The id_list of this ListApplicationsRequest.
        :rtype: list[str]
        """
        return self._id_list

    @id_list.setter
    def id_list(self, id_list):
        """Sets the id_list of this ListApplicationsRequest.

        id列表

        :param id_list: The id_list of this ListApplicationsRequest.
        :type id_list: list[str]
        """
        self._id_list = id_list

    @property
    def parent_id(self):
        """Gets the parent_id of this ListApplicationsRequest.

        parent id

        :return: The parent_id of this ListApplicationsRequest.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this ListApplicationsRequest.

        parent id

        :param parent_id: The parent_id of this ListApplicationsRequest.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def name_like(self):
        """Gets the name_like of this ListApplicationsRequest.

        应用名称模糊匹配

        :return: The name_like of this ListApplicationsRequest.
        :rtype: str
        """
        return self._name_like

    @name_like.setter
    def name_like(self, name_like):
        """Sets the name_like of this ListApplicationsRequest.

        应用名称模糊匹配

        :param name_like: The name_like of this ListApplicationsRequest.
        :type name_like: str
        """
        self._name_like = name_like

    @property
    def code(self):
        """Gets the code of this ListApplicationsRequest.

        应用code

        :return: The code of this ListApplicationsRequest.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ListApplicationsRequest.

        应用code

        :param code: The code of this ListApplicationsRequest.
        :type code: str
        """
        self._code = code

    @property
    def marker(self):
        """Gets the marker of this ListApplicationsRequest.

        分页参数，上一页请求最后一个id

        :return: The marker of this ListApplicationsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListApplicationsRequest.

        分页参数，上一页请求最后一个id

        :param marker: The marker of this ListApplicationsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListApplicationsRequest.

        最大的返回数量

        :return: The limit of this ListApplicationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListApplicationsRequest.

        最大的返回数量

        :param limit: The limit of this ListApplicationsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListApplicationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
