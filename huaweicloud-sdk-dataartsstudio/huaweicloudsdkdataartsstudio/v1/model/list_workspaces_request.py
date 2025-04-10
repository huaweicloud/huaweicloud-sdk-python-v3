# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkspacesRequest:

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
        'x_project_id': 'str',
        'workspace_type': 'str',
        'limit': 'int',
        'offset': 'int',
        'dw_type': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'workspace_type': 'workspace_type',
        'limit': 'limit',
        'offset': 'offset',
        'dw_type': 'dw_type'
    }

    def __init__(self, workspace=None, x_project_id=None, workspace_type=None, limit=None, offset=None, dw_type=None):
        r"""ListWorkspacesRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param workspace_type: 模型工作区类型枚举。 枚举值：   - THIRD_NF: 关系建模   - DIMENSION: 维度建模 
        :type workspace_type: str
        :param limit: 每页查询条数，即查询Y条数据。默认值50，取值范围[1,100]。
        :type limit: int
        :param offset: 查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整，默认值0。
        :type offset: int
        :param dw_type: 数据连接类型
        :type dw_type: str
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._workspace_type = None
        self._limit = None
        self._offset = None
        self._dw_type = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        if workspace_type is not None:
            self.workspace_type = workspace_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if dw_type is not None:
            self.dw_type = dw_type

    @property
    def workspace(self):
        r"""Gets the workspace of this ListWorkspacesRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ListWorkspacesRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListWorkspacesRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ListWorkspacesRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this ListWorkspacesRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this ListWorkspacesRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this ListWorkspacesRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this ListWorkspacesRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def workspace_type(self):
        r"""Gets the workspace_type of this ListWorkspacesRequest.

        模型工作区类型枚举。 枚举值：   - THIRD_NF: 关系建模   - DIMENSION: 维度建模 

        :return: The workspace_type of this ListWorkspacesRequest.
        :rtype: str
        """
        return self._workspace_type

    @workspace_type.setter
    def workspace_type(self, workspace_type):
        r"""Sets the workspace_type of this ListWorkspacesRequest.

        模型工作区类型枚举。 枚举值：   - THIRD_NF: 关系建模   - DIMENSION: 维度建模 

        :param workspace_type: The workspace_type of this ListWorkspacesRequest.
        :type workspace_type: str
        """
        self._workspace_type = workspace_type

    @property
    def limit(self):
        r"""Gets the limit of this ListWorkspacesRequest.

        每页查询条数，即查询Y条数据。默认值50，取值范围[1,100]。

        :return: The limit of this ListWorkspacesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWorkspacesRequest.

        每页查询条数，即查询Y条数据。默认值50，取值范围[1,100]。

        :param limit: The limit of this ListWorkspacesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListWorkspacesRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整，默认值0。

        :return: The offset of this ListWorkspacesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWorkspacesRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整，默认值0。

        :param offset: The offset of this ListWorkspacesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def dw_type(self):
        r"""Gets the dw_type of this ListWorkspacesRequest.

        数据连接类型

        :return: The dw_type of this ListWorkspacesRequest.
        :rtype: str
        """
        return self._dw_type

    @dw_type.setter
    def dw_type(self, dw_type):
        r"""Sets the dw_type of this ListWorkspacesRequest.

        数据连接类型

        :param dw_type: The dw_type of this ListWorkspacesRequest.
        :type dw_type: str
        """
        self._dw_type = dw_type

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
        if not isinstance(other, ListWorkspacesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
