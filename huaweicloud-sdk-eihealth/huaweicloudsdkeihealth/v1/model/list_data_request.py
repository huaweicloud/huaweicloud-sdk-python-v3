# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eihealth_project_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'path': 'str',
        'search_key': 'str',
        'sort_dir': 'str',
        'sort_key': 'str',
        'marker': 'str'
    }

    attribute_map = {
        'eihealth_project_id': 'eihealth_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'path': 'path',
        'search_key': 'search_key',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'marker': 'marker'
    }

    def __init__(self, eihealth_project_id=None, limit=None, offset=None, path=None, search_key=None, sort_dir=None, sort_key=None, marker=None):
        """ListDataRequest

        The model defined in huaweicloud sdk

        :param eihealth_project_id: 医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        :param limit: 限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]
        :type limit: int
        :param offset: 偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]
        :type offset: int
        :param path: 指定文件夹（项目名称:/路径）
        :type path: str
        :param search_key: 查询关键词
        :type search_key: str
        :param sort_dir: 降序或升序（分别对应desc和asc，默认为desc）
        :type sort_dir: str
        :param sort_key: 排序字段（支持type，create_time）
        :type sort_key: str
        :param marker: 开始标签
        :type marker: str
        """
        
        

        self._eihealth_project_id = None
        self._limit = None
        self._offset = None
        self._path = None
        self._search_key = None
        self._sort_dir = None
        self._sort_key = None
        self._marker = None
        self.discriminator = None

        self.eihealth_project_id = eihealth_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if path is not None:
            self.path = path
        if search_key is not None:
            self.search_key = search_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if marker is not None:
            self.marker = marker

    @property
    def eihealth_project_id(self):
        """Gets the eihealth_project_id of this ListDataRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this ListDataRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        """Sets the eihealth_project_id of this ListDataRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this ListDataRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def limit(self):
        """Gets the limit of this ListDataRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]

        :return: The limit of this ListDataRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDataRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]

        :param limit: The limit of this ListDataRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListDataRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]

        :return: The offset of this ListDataRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDataRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]

        :param offset: The offset of this ListDataRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def path(self):
        """Gets the path of this ListDataRequest.

        指定文件夹（项目名称:/路径）

        :return: The path of this ListDataRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ListDataRequest.

        指定文件夹（项目名称:/路径）

        :param path: The path of this ListDataRequest.
        :type path: str
        """
        self._path = path

    @property
    def search_key(self):
        """Gets the search_key of this ListDataRequest.

        查询关键词

        :return: The search_key of this ListDataRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this ListDataRequest.

        查询关键词

        :param search_key: The search_key of this ListDataRequest.
        :type search_key: str
        """
        self._search_key = search_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListDataRequest.

        降序或升序（分别对应desc和asc，默认为desc）

        :return: The sort_dir of this ListDataRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListDataRequest.

        降序或升序（分别对应desc和asc，默认为desc）

        :param sort_dir: The sort_dir of this ListDataRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        """Gets the sort_key of this ListDataRequest.

        排序字段（支持type，create_time）

        :return: The sort_key of this ListDataRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListDataRequest.

        排序字段（支持type，create_time）

        :param sort_key: The sort_key of this ListDataRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def marker(self):
        """Gets the marker of this ListDataRequest.

        开始标签

        :return: The marker of this ListDataRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListDataRequest.

        开始标签

        :param marker: The marker of this ListDataRequest.
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
        if not isinstance(other, ListDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
