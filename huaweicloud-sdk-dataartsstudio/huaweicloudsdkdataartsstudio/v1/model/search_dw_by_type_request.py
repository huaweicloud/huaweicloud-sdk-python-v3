# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchDwByTypeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'force_refresh': 'bool',
        'dw_type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'force_refresh': 'force_refresh',
        'dw_type': 'dw_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, workspace=None, force_refresh=None, dw_type=None, limit=None, offset=None):
        """SearchDwByTypeRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param force_refresh: 是否查询最新的
        :type force_refresh: bool
        :param dw_type: 数据连接类型
        :type dw_type: str
        :param limit: limit
        :type limit: int
        :param offset: limit
        :type offset: int
        """
        
        

        self._workspace = None
        self._force_refresh = None
        self._dw_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.workspace = workspace
        if force_refresh is not None:
            self.force_refresh = force_refresh
        self.dw_type = dw_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def workspace(self):
        """Gets the workspace of this SearchDwByTypeRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this SearchDwByTypeRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this SearchDwByTypeRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this SearchDwByTypeRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def force_refresh(self):
        """Gets the force_refresh of this SearchDwByTypeRequest.

        是否查询最新的

        :return: The force_refresh of this SearchDwByTypeRequest.
        :rtype: bool
        """
        return self._force_refresh

    @force_refresh.setter
    def force_refresh(self, force_refresh):
        """Sets the force_refresh of this SearchDwByTypeRequest.

        是否查询最新的

        :param force_refresh: The force_refresh of this SearchDwByTypeRequest.
        :type force_refresh: bool
        """
        self._force_refresh = force_refresh

    @property
    def dw_type(self):
        """Gets the dw_type of this SearchDwByTypeRequest.

        数据连接类型

        :return: The dw_type of this SearchDwByTypeRequest.
        :rtype: str
        """
        return self._dw_type

    @dw_type.setter
    def dw_type(self, dw_type):
        """Sets the dw_type of this SearchDwByTypeRequest.

        数据连接类型

        :param dw_type: The dw_type of this SearchDwByTypeRequest.
        :type dw_type: str
        """
        self._dw_type = dw_type

    @property
    def limit(self):
        """Gets the limit of this SearchDwByTypeRequest.

        limit

        :return: The limit of this SearchDwByTypeRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchDwByTypeRequest.

        limit

        :param limit: The limit of this SearchDwByTypeRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this SearchDwByTypeRequest.

        limit

        :return: The offset of this SearchDwByTypeRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchDwByTypeRequest.

        limit

        :param offset: The offset of this SearchDwByTypeRequest.
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
        if not isinstance(other, SearchDwByTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
