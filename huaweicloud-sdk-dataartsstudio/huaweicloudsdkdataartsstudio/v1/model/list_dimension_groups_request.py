# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDimensionGroupsRequest:

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
        'table_id': 'int',
        'biz_type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'table_id': 'table_id',
        'biz_type': 'biz_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, workspace=None, table_id=None, biz_type=None, limit=None, offset=None):
        """ListDimensionGroupsRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param table_id: 关联表id
        :type table_id: int
        :param biz_type: 按业务类型查询
        :type biz_type: str
        :param limit: 查询条数，即查询Y条数据。默认值50，取值范围[1,100]
        :type limit: int
        :param offset: 查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0
        :type offset: int
        """
        
        

        self._workspace = None
        self._table_id = None
        self._biz_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.workspace = workspace
        if table_id is not None:
            self.table_id = table_id
        if biz_type is not None:
            self.biz_type = biz_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def workspace(self):
        """Gets the workspace of this ListDimensionGroupsRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListDimensionGroupsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListDimensionGroupsRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListDimensionGroupsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def table_id(self):
        """Gets the table_id of this ListDimensionGroupsRequest.

        关联表id

        :return: The table_id of this ListDimensionGroupsRequest.
        :rtype: int
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this ListDimensionGroupsRequest.

        关联表id

        :param table_id: The table_id of this ListDimensionGroupsRequest.
        :type table_id: int
        """
        self._table_id = table_id

    @property
    def biz_type(self):
        """Gets the biz_type of this ListDimensionGroupsRequest.

        按业务类型查询

        :return: The biz_type of this ListDimensionGroupsRequest.
        :rtype: str
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        """Sets the biz_type of this ListDimensionGroupsRequest.

        按业务类型查询

        :param biz_type: The biz_type of this ListDimensionGroupsRequest.
        :type biz_type: str
        """
        self._biz_type = biz_type

    @property
    def limit(self):
        """Gets the limit of this ListDimensionGroupsRequest.

        查询条数，即查询Y条数据。默认值50，取值范围[1,100]

        :return: The limit of this ListDimensionGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDimensionGroupsRequest.

        查询条数，即查询Y条数据。默认值50，取值范围[1,100]

        :param limit: The limit of this ListDimensionGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListDimensionGroupsRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0

        :return: The offset of this ListDimensionGroupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDimensionGroupsRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0

        :param offset: The offset of this ListDimensionGroupsRequest.
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
        if not isinstance(other, ListDimensionGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
