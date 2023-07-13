# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTableModelRelationsRequest:

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
        'model_id': 'str',
        'table_ids': 'str',
        'biz_type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'model_id': 'model_id',
        'table_ids': 'table_ids',
        'biz_type': 'biz_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, workspace=None, model_id=None, table_ids=None, biz_type=None, limit=None, offset=None):
        """ListTableModelRelationsRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param model_id: 依据workspace id查工作区
        :type model_id: str
        :param table_ids: 表模型ids
        :type table_ids: str
        :param biz_type: 表类型
        :type biz_type: str
        :param limit: 查询条数，即查询Y条数据。默认值50，取值范围[1,100]
        :type limit: int
        :param offset: 查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0
        :type offset: int
        """
        
        

        self._workspace = None
        self._model_id = None
        self._table_ids = None
        self._biz_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.workspace = workspace
        self.model_id = model_id
        if table_ids is not None:
            self.table_ids = table_ids
        if biz_type is not None:
            self.biz_type = biz_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def workspace(self):
        """Gets the workspace of this ListTableModelRelationsRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListTableModelRelationsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListTableModelRelationsRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListTableModelRelationsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def model_id(self):
        """Gets the model_id of this ListTableModelRelationsRequest.

        依据workspace id查工作区

        :return: The model_id of this ListTableModelRelationsRequest.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this ListTableModelRelationsRequest.

        依据workspace id查工作区

        :param model_id: The model_id of this ListTableModelRelationsRequest.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def table_ids(self):
        """Gets the table_ids of this ListTableModelRelationsRequest.

        表模型ids

        :return: The table_ids of this ListTableModelRelationsRequest.
        :rtype: str
        """
        return self._table_ids

    @table_ids.setter
    def table_ids(self, table_ids):
        """Sets the table_ids of this ListTableModelRelationsRequest.

        表模型ids

        :param table_ids: The table_ids of this ListTableModelRelationsRequest.
        :type table_ids: str
        """
        self._table_ids = table_ids

    @property
    def biz_type(self):
        """Gets the biz_type of this ListTableModelRelationsRequest.

        表类型

        :return: The biz_type of this ListTableModelRelationsRequest.
        :rtype: str
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        """Sets the biz_type of this ListTableModelRelationsRequest.

        表类型

        :param biz_type: The biz_type of this ListTableModelRelationsRequest.
        :type biz_type: str
        """
        self._biz_type = biz_type

    @property
    def limit(self):
        """Gets the limit of this ListTableModelRelationsRequest.

        查询条数，即查询Y条数据。默认值50，取值范围[1,100]

        :return: The limit of this ListTableModelRelationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTableModelRelationsRequest.

        查询条数，即查询Y条数据。默认值50，取值范围[1,100]

        :param limit: The limit of this ListTableModelRelationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListTableModelRelationsRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0

        :return: The offset of this ListTableModelRelationsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTableModelRelationsRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0

        :param offset: The offset of this ListTableModelRelationsRequest.
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
        if not isinstance(other, ListTableModelRelationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
