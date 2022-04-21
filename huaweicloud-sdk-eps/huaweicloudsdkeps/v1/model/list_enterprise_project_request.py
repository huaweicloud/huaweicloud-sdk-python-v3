# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnterpriseProjectRequest:

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
        'sort_dir': 'str',
        'sort_key': 'str',
        'status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'limit': 'limit',
        'name': 'name',
        'offset': 'offset',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'status': 'status'
    }

    def __init__(self, id=None, limit=None, name=None, offset=None, sort_dir=None, sort_key=None, status=None):
        """ListEnterpriseProjectRequest

        The model defined in huaweicloud sdk

        :param id: 企业项目ID，0表示默认企业项目
        :type id: str
        :param limit: 查询记录数默认为1000，limit最多为1000, 最小值为1
        :type limit: int
        :param name: 企业项目名称，支持模糊搜索
        :type name: str
        :param offset: 索引位置，从offset指定的下一条数据开始查询，必须为数字，不能为负数，默认为0
        :type offset: int
        :param sort_dir: 降序或升序,默认为“desc” 。desc表示降序 。asc 表示升序
        :type sort_dir: str
        :param sort_key: 返回结果按该关键字排序（支持updated_at等关键字，默认为“created_at”）
        :type sort_key: str
        :param status: 企业项目状态。 1--启用，2--停用
        :type status: int
        """
        
        

        self._id = None
        self._limit = None
        self._name = None
        self._offset = None
        self._sort_dir = None
        self._sort_key = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this ListEnterpriseProjectRequest.

        企业项目ID，0表示默认企业项目

        :return: The id of this ListEnterpriseProjectRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListEnterpriseProjectRequest.

        企业项目ID，0表示默认企业项目

        :param id: The id of this ListEnterpriseProjectRequest.
        :type id: str
        """
        self._id = id

    @property
    def limit(self):
        """Gets the limit of this ListEnterpriseProjectRequest.

        查询记录数默认为1000，limit最多为1000, 最小值为1

        :return: The limit of this ListEnterpriseProjectRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEnterpriseProjectRequest.

        查询记录数默认为1000，limit最多为1000, 最小值为1

        :param limit: The limit of this ListEnterpriseProjectRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListEnterpriseProjectRequest.

        企业项目名称，支持模糊搜索

        :return: The name of this ListEnterpriseProjectRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListEnterpriseProjectRequest.

        企业项目名称，支持模糊搜索

        :param name: The name of this ListEnterpriseProjectRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ListEnterpriseProjectRequest.

        索引位置，从offset指定的下一条数据开始查询，必须为数字，不能为负数，默认为0

        :return: The offset of this ListEnterpriseProjectRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEnterpriseProjectRequest.

        索引位置，从offset指定的下一条数据开始查询，必须为数字，不能为负数，默认为0

        :param offset: The offset of this ListEnterpriseProjectRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListEnterpriseProjectRequest.

        降序或升序,默认为“desc” 。desc表示降序 。asc 表示升序

        :return: The sort_dir of this ListEnterpriseProjectRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListEnterpriseProjectRequest.

        降序或升序,默认为“desc” 。desc表示降序 。asc 表示升序

        :param sort_dir: The sort_dir of this ListEnterpriseProjectRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        """Gets the sort_key of this ListEnterpriseProjectRequest.

        返回结果按该关键字排序（支持updated_at等关键字，默认为“created_at”）

        :return: The sort_key of this ListEnterpriseProjectRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListEnterpriseProjectRequest.

        返回结果按该关键字排序（支持updated_at等关键字，默认为“created_at”）

        :param sort_key: The sort_key of this ListEnterpriseProjectRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def status(self):
        """Gets the status of this ListEnterpriseProjectRequest.

        企业项目状态。 1--启用，2--停用

        :return: The status of this ListEnterpriseProjectRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListEnterpriseProjectRequest.

        企业项目状态。 1--启用，2--停用

        :param status: The status of this ListEnterpriseProjectRequest.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, ListEnterpriseProjectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
