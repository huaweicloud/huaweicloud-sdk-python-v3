# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAllDataSourceRequest:

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
        'type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, name=None, type=None, limit=None, offset=None):
        """ShowAllDataSourceRequest

        The model defined in huaweicloud sdk

        :param name: filter
        :type name: str
        :param type: 数据源类型, 包括：OBS、DIS、IOTDA、SMN、FUNCTION_GRAPH、MODEL_ARTS、DCS、KAFKA、API
        :type type: str
        :param limit: 每次查询返回元素的上限
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0
        :type offset: int
        """
        
        

        self._name = None
        self._type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def name(self):
        """Gets the name of this ShowAllDataSourceRequest.

        filter

        :return: The name of this ShowAllDataSourceRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowAllDataSourceRequest.

        filter

        :param name: The name of this ShowAllDataSourceRequest.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ShowAllDataSourceRequest.

        数据源类型, 包括：OBS、DIS、IOTDA、SMN、FUNCTION_GRAPH、MODEL_ARTS、DCS、KAFKA、API

        :return: The type of this ShowAllDataSourceRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowAllDataSourceRequest.

        数据源类型, 包括：OBS、DIS、IOTDA、SMN、FUNCTION_GRAPH、MODEL_ARTS、DCS、KAFKA、API

        :param type: The type of this ShowAllDataSourceRequest.
        :type type: str
        """
        self._type = type

    @property
    def limit(self):
        """Gets the limit of this ShowAllDataSourceRequest.

        每次查询返回元素的上限

        :return: The limit of this ShowAllDataSourceRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowAllDataSourceRequest.

        每次查询返回元素的上限

        :param limit: The limit of this ShowAllDataSourceRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowAllDataSourceRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0

        :return: The offset of this ShowAllDataSourceRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowAllDataSourceRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0

        :param offset: The offset of this ShowAllDataSourceRequest.
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
        if not isinstance(other, ShowAllDataSourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
