# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchListEdgeAppsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edge_app_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'app_type': 'str',
        'function_type': 'str'
    }

    attribute_map = {
        'edge_app_id': 'edge_app_id',
        'offset': 'offset',
        'limit': 'limit',
        'app_type': 'app_type',
        'function_type': 'function_type'
    }

    def __init__(self, edge_app_id=None, offset=None, limit=None, app_type=None, function_type=None):
        """BatchListEdgeAppsRequest

        The model defined in huaweicloud sdk

        :param edge_app_id: 应用ID搜索关键字
        :type edge_app_id: str
        :param offset: 查询的起始位置，取值范围为非负整数，默认为0
        :type offset: int
        :param limit: 每页记录数，默认值为10，取值区间为1-1000
        :type limit: int
        :param app_type: 应用id搜索关键字
        :type app_type: str
        :param function_type: 功能类型
        :type function_type: str
        """
        
        

        self._edge_app_id = None
        self._offset = None
        self._limit = None
        self._app_type = None
        self._function_type = None
        self.discriminator = None

        if edge_app_id is not None:
            self.edge_app_id = edge_app_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if app_type is not None:
            self.app_type = app_type
        if function_type is not None:
            self.function_type = function_type

    @property
    def edge_app_id(self):
        """Gets the edge_app_id of this BatchListEdgeAppsRequest.

        应用ID搜索关键字

        :return: The edge_app_id of this BatchListEdgeAppsRequest.
        :rtype: str
        """
        return self._edge_app_id

    @edge_app_id.setter
    def edge_app_id(self, edge_app_id):
        """Sets the edge_app_id of this BatchListEdgeAppsRequest.

        应用ID搜索关键字

        :param edge_app_id: The edge_app_id of this BatchListEdgeAppsRequest.
        :type edge_app_id: str
        """
        self._edge_app_id = edge_app_id

    @property
    def offset(self):
        """Gets the offset of this BatchListEdgeAppsRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :return: The offset of this BatchListEdgeAppsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this BatchListEdgeAppsRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :param offset: The offset of this BatchListEdgeAppsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this BatchListEdgeAppsRequest.

        每页记录数，默认值为10，取值区间为1-1000

        :return: The limit of this BatchListEdgeAppsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this BatchListEdgeAppsRequest.

        每页记录数，默认值为10，取值区间为1-1000

        :param limit: The limit of this BatchListEdgeAppsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def app_type(self):
        """Gets the app_type of this BatchListEdgeAppsRequest.

        应用id搜索关键字

        :return: The app_type of this BatchListEdgeAppsRequest.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this BatchListEdgeAppsRequest.

        应用id搜索关键字

        :param app_type: The app_type of this BatchListEdgeAppsRequest.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def function_type(self):
        """Gets the function_type of this BatchListEdgeAppsRequest.

        功能类型

        :return: The function_type of this BatchListEdgeAppsRequest.
        :rtype: str
        """
        return self._function_type

    @function_type.setter
    def function_type(self, function_type):
        """Sets the function_type of this BatchListEdgeAppsRequest.

        功能类型

        :param function_type: The function_type of this BatchListEdgeAppsRequest.
        :type function_type: str
        """
        self._function_type = function_type

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
        if not isinstance(other, BatchListEdgeAppsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
