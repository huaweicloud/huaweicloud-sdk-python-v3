# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPrrTemplateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'application_type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'name': 'name',
        'application_type': 'application_type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, name=None, application_type=None, offset=None, limit=None):
        """ListPrrTemplateRequest

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param application_type: 应用类型 core: 核心应用 non-core: 非核心应用
        :type application_type: str
        :param offset: 分页参数
        :type offset: int
        :param limit: 每页显示的条目数量
        :type limit: int
        """
        
        

        self._name = None
        self._application_type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if application_type is not None:
            self.application_type = application_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def name(self):
        """Gets the name of this ListPrrTemplateRequest.

        名称

        :return: The name of this ListPrrTemplateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPrrTemplateRequest.

        名称

        :param name: The name of this ListPrrTemplateRequest.
        :type name: str
        """
        self._name = name

    @property
    def application_type(self):
        """Gets the application_type of this ListPrrTemplateRequest.

        应用类型 core: 核心应用 non-core: 非核心应用

        :return: The application_type of this ListPrrTemplateRequest.
        :rtype: str
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        """Sets the application_type of this ListPrrTemplateRequest.

        应用类型 core: 核心应用 non-core: 非核心应用

        :param application_type: The application_type of this ListPrrTemplateRequest.
        :type application_type: str
        """
        self._application_type = application_type

    @property
    def offset(self):
        """Gets the offset of this ListPrrTemplateRequest.

        分页参数

        :return: The offset of this ListPrrTemplateRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPrrTemplateRequest.

        分页参数

        :param offset: The offset of this ListPrrTemplateRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPrrTemplateRequest.

        每页显示的条目数量

        :return: The limit of this ListPrrTemplateRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPrrTemplateRequest.

        每页显示的条目数量

        :param limit: The limit of this ListPrrTemplateRequest.
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
        if not isinstance(other, ListPrrTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
