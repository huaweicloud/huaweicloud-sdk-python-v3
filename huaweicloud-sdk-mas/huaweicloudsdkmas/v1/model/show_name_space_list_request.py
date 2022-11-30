# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNameSpaceListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'str',
        'limit': 'str',
        'name': 'str',
        'type': 'str',
        'is_used': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'type': 'type',
        'is_used': 'is_used',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, offset=None, limit=None, name=None, type=None, is_used=None, enterprise_project_id=None):
        """ShowNameSpaceListRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量
        :type offset: str
        :param limit: 每页显示的条目数量
        :type limit: str
        :param name: 命名空间名称
        :type name: str
        :param type: 多活类型，1：同城多活，2：异地多活
        :type type: str
        :param is_used: 是否已被使用   true  ：是   false  ：否
        :type is_used: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        """
        
        

        self._offset = None
        self._limit = None
        self._name = None
        self._type = None
        self._is_used = None
        self._enterprise_project_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if is_used is not None:
            self.is_used = is_used
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        """Gets the offset of this ShowNameSpaceListRequest.

        偏移量

        :return: The offset of this ShowNameSpaceListRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowNameSpaceListRequest.

        偏移量

        :param offset: The offset of this ShowNameSpaceListRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowNameSpaceListRequest.

        每页显示的条目数量

        :return: The limit of this ShowNameSpaceListRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowNameSpaceListRequest.

        每页显示的条目数量

        :param limit: The limit of this ShowNameSpaceListRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ShowNameSpaceListRequest.

        命名空间名称

        :return: The name of this ShowNameSpaceListRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowNameSpaceListRequest.

        命名空间名称

        :param name: The name of this ShowNameSpaceListRequest.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ShowNameSpaceListRequest.

        多活类型，1：同城多活，2：异地多活

        :return: The type of this ShowNameSpaceListRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowNameSpaceListRequest.

        多活类型，1：同城多活，2：异地多活

        :param type: The type of this ShowNameSpaceListRequest.
        :type type: str
        """
        self._type = type

    @property
    def is_used(self):
        """Gets the is_used of this ShowNameSpaceListRequest.

        是否已被使用   true  ：是   false  ：否

        :return: The is_used of this ShowNameSpaceListRequest.
        :rtype: str
        """
        return self._is_used

    @is_used.setter
    def is_used(self, is_used):
        """Sets the is_used of this ShowNameSpaceListRequest.

        是否已被使用   true  ：是   false  ：否

        :param is_used: The is_used of this ShowNameSpaceListRequest.
        :type is_used: str
        """
        self._is_used = is_used

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowNameSpaceListRequest.

        企业项目ID

        :return: The enterprise_project_id of this ShowNameSpaceListRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowNameSpaceListRequest.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ShowNameSpaceListRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ShowNameSpaceListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
