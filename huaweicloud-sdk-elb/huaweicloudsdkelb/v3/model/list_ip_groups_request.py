# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIpGroupsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'description': 'list[str]',
        'id': 'list[str]',
        'ip_list': 'list[str]',
        'limit': 'int',
        'marker': 'str',
        'name': 'list[str]',
        'page_reverse': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'ip_list': 'ip_list',
        'limit': 'limit',
        'marker': 'marker',
        'name': 'name',
        'page_reverse': 'page_reverse'
    }

    def __init__(self, description=None, id=None, ip_list=None, limit=None, marker=None, name=None, page_reverse=None):
        """ListIpGroupsRequest - a model defined in huaweicloud sdk"""
        
        

        self._description = None
        self._id = None
        self._ip_list = None
        self._limit = None
        self._marker = None
        self._name = None
        self._page_reverse = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if ip_list is not None:
            self.ip_list = ip_list
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if name is not None:
            self.name = name
        if page_reverse is not None:
            self.page_reverse = page_reverse

    @property
    def description(self):
        """Gets the description of this ListIpGroupsRequest.

        ip地址组的描述信息。

        :return: The description of this ListIpGroupsRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListIpGroupsRequest.

        ip地址组的描述信息。

        :param description: The description of this ListIpGroupsRequest.
        :type: list[str]
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this ListIpGroupsRequest.

        ip地址组的id

        :return: The id of this ListIpGroupsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListIpGroupsRequest.

        ip地址组的id

        :param id: The id of this ListIpGroupsRequest.
        :type: list[str]
        """
        self._id = id

    @property
    def ip_list(self):
        """Gets the ip_list of this ListIpGroupsRequest.

        ip地址，多个用逗号分隔

        :return: The ip_list of this ListIpGroupsRequest.
        :rtype: list[str]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        """Sets the ip_list of this ListIpGroupsRequest.

        ip地址，多个用逗号分隔

        :param ip_list: The ip_list of this ListIpGroupsRequest.
        :type: list[str]
        """
        self._ip_list = ip_list

    @property
    def limit(self):
        """Gets the limit of this ListIpGroupsRequest.

        每页返回的个数。

        :return: The limit of this ListIpGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListIpGroupsRequest.

        每页返回的个数。

        :param limit: The limit of this ListIpGroupsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListIpGroupsRequest.

        上一页最后一条记录的ID。  使用说明：  - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :return: The marker of this ListIpGroupsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListIpGroupsRequest.

        上一页最后一条记录的ID。  使用说明：  - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :param marker: The marker of this ListIpGroupsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def name(self):
        """Gets the name of this ListIpGroupsRequest.

        ip地址组的名称

        :return: The name of this ListIpGroupsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListIpGroupsRequest.

        ip地址组的名称

        :param name: The name of this ListIpGroupsRequest.
        :type: list[str]
        """
        self._name = name

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListIpGroupsRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。  使用说明：必须与limit一起使用。

        :return: The page_reverse of this ListIpGroupsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListIpGroupsRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。  使用说明：必须与limit一起使用。

        :param page_reverse: The page_reverse of this ListIpGroupsRequest.
        :type: bool
        """
        self._page_reverse = page_reverse

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
        if not isinstance(other, ListIpGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
