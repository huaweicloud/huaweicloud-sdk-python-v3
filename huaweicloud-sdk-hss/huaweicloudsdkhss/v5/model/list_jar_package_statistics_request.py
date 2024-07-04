# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJarPackageStatisticsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'file_name': 'str',
        'category': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'file_name': 'file_name',
        'category': 'category',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, enterprise_project_id=None, file_name=None, category=None, limit=None, offset=None):
        """ListJarPackageStatisticsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param file_name: jar包名称
        :type file_name: str
        :param category: 类别，包含如下:   - host : 主机   - container : 容器
        :type category: str
        :param limit: 每页显示数量
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        """
        
        

        self._enterprise_project_id = None
        self._file_name = None
        self._category = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if file_name is not None:
            self.file_name = file_name
        if category is not None:
            self.category = category
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListJarPackageStatisticsRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListJarPackageStatisticsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListJarPackageStatisticsRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListJarPackageStatisticsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def file_name(self):
        """Gets the file_name of this ListJarPackageStatisticsRequest.

        jar包名称

        :return: The file_name of this ListJarPackageStatisticsRequest.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ListJarPackageStatisticsRequest.

        jar包名称

        :param file_name: The file_name of this ListJarPackageStatisticsRequest.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def category(self):
        """Gets the category of this ListJarPackageStatisticsRequest.

        类别，包含如下:   - host : 主机   - container : 容器

        :return: The category of this ListJarPackageStatisticsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ListJarPackageStatisticsRequest.

        类别，包含如下:   - host : 主机   - container : 容器

        :param category: The category of this ListJarPackageStatisticsRequest.
        :type category: str
        """
        self._category = category

    @property
    def limit(self):
        """Gets the limit of this ListJarPackageStatisticsRequest.

        每页显示数量

        :return: The limit of this ListJarPackageStatisticsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListJarPackageStatisticsRequest.

        每页显示数量

        :param limit: The limit of this ListJarPackageStatisticsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListJarPackageStatisticsRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListJarPackageStatisticsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListJarPackageStatisticsRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListJarPackageStatisticsRequest.
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
        if not isinstance(other, ListJarPackageStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
