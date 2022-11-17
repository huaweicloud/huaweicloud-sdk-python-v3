# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOrgInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_temporary': 'bool',
        'limit': 'int',
        'offset': 'int',
        'org_id': 'str',
        'search': 'str'
    }

    attribute_map = {
        'is_temporary': 'is_temporary',
        'limit': 'limit',
        'offset': 'offset',
        'org_id': 'org_id',
        'search': 'search'
    }

    def __init__(self, is_temporary=None, limit=None, offset=None, org_id=None, search=None):
        """ListOrgInstancesRequest

        The model defined in huaweicloud sdk

        :param is_temporary: 是否页面显示（以标签配置为准）
        :type is_temporary: bool
        :param limit: 每页显示的条目数量 10/15/30
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询
        :type offset: int
        :param org_id: 租户id（对应华为云帐号的domainId）
        :type org_id: str
        :param search: 关键字查询(根据实例名，描述模糊查询)
        :type search: str
        """
        
        

        self._is_temporary = None
        self._limit = None
        self._offset = None
        self._org_id = None
        self._search = None
        self.discriminator = None

        if is_temporary is not None:
            self.is_temporary = is_temporary
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.org_id = org_id
        if search is not None:
            self.search = search

    @property
    def is_temporary(self):
        """Gets the is_temporary of this ListOrgInstancesRequest.

        是否页面显示（以标签配置为准）

        :return: The is_temporary of this ListOrgInstancesRequest.
        :rtype: bool
        """
        return self._is_temporary

    @is_temporary.setter
    def is_temporary(self, is_temporary):
        """Sets the is_temporary of this ListOrgInstancesRequest.

        是否页面显示（以标签配置为准）

        :param is_temporary: The is_temporary of this ListOrgInstancesRequest.
        :type is_temporary: bool
        """
        self._is_temporary = is_temporary

    @property
    def limit(self):
        """Gets the limit of this ListOrgInstancesRequest.

        每页显示的条目数量 10/15/30

        :return: The limit of this ListOrgInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListOrgInstancesRequest.

        每页显示的条目数量 10/15/30

        :param limit: The limit of this ListOrgInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListOrgInstancesRequest.

        偏移量，表示从此偏移量开始查询

        :return: The offset of this ListOrgInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListOrgInstancesRequest.

        偏移量，表示从此偏移量开始查询

        :param offset: The offset of this ListOrgInstancesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def org_id(self):
        """Gets the org_id of this ListOrgInstancesRequest.

        租户id（对应华为云帐号的domainId）

        :return: The org_id of this ListOrgInstancesRequest.
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this ListOrgInstancesRequest.

        租户id（对应华为云帐号的domainId）

        :param org_id: The org_id of this ListOrgInstancesRequest.
        :type org_id: str
        """
        self._org_id = org_id

    @property
    def search(self):
        """Gets the search of this ListOrgInstancesRequest.

        关键字查询(根据实例名，描述模糊查询)

        :return: The search of this ListOrgInstancesRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this ListOrgInstancesRequest.

        关键字查询(根据实例名，描述模糊查询)

        :param search: The search of this ListOrgInstancesRequest.
        :type search: str
        """
        self._search = search

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
        if not isinstance(other, ListOrgInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
