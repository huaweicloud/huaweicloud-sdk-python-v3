# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserStatisticsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'enterprise_project_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'user_name': 'user_name',
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, user_name=None, enterprise_project_id=None, limit=None, offset=None):
        """ListUserStatisticsRequest

        The model defined in huaweicloud sdk

        :param user_name: 账号名称，参考windows文件命名规则，支持字母、数字、下划线、中文，特殊字符!@.-等，不包括中文标点符号
        :type user_name: str
        :param enterprise_project_id: 企业项目
        :type enterprise_project_id: str
        :param limit: 默认10
        :type limit: int
        :param offset: 默认是0
        :type offset: int
        """
        
        

        self._user_name = None
        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def user_name(self):
        """Gets the user_name of this ListUserStatisticsRequest.

        账号名称，参考windows文件命名规则，支持字母、数字、下划线、中文，特殊字符!@.-等，不包括中文标点符号

        :return: The user_name of this ListUserStatisticsRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ListUserStatisticsRequest.

        账号名称，参考windows文件命名规则，支持字母、数字、下划线、中文，特殊字符!@.-等，不包括中文标点符号

        :param user_name: The user_name of this ListUserStatisticsRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListUserStatisticsRequest.

        企业项目

        :return: The enterprise_project_id of this ListUserStatisticsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListUserStatisticsRequest.

        企业项目

        :param enterprise_project_id: The enterprise_project_id of this ListUserStatisticsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        """Gets the limit of this ListUserStatisticsRequest.

        默认10

        :return: The limit of this ListUserStatisticsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListUserStatisticsRequest.

        默认10

        :param limit: The limit of this ListUserStatisticsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListUserStatisticsRequest.

        默认是0

        :return: The offset of this ListUserStatisticsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListUserStatisticsRequest.

        默认是0

        :param offset: The offset of this ListUserStatisticsRequest.
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
        if not isinstance(other, ListUserStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
