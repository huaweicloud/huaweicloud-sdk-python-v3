# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAggregationLogicTableByIdRequest:

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
        'id': 'str',
        'latest': 'bool'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'id': 'id',
        'latest': 'latest'
    }

    def __init__(self, workspace=None, x_project_id=None, id=None, latest=None):
        r"""ShowAggregationLogicTableByIdRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param id: 实体ID，ID字符串。
        :type id: str
        :param latest: 是否查询最新的。
        :type latest: bool
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._id = None
        self._latest = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        self.id = id
        if latest is not None:
            self.latest = latest

    @property
    def workspace(self):
        r"""Gets the workspace of this ShowAggregationLogicTableByIdRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ShowAggregationLogicTableByIdRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ShowAggregationLogicTableByIdRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ShowAggregationLogicTableByIdRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this ShowAggregationLogicTableByIdRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this ShowAggregationLogicTableByIdRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this ShowAggregationLogicTableByIdRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this ShowAggregationLogicTableByIdRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def id(self):
        r"""Gets the id of this ShowAggregationLogicTableByIdRequest.

        实体ID，ID字符串。

        :return: The id of this ShowAggregationLogicTableByIdRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowAggregationLogicTableByIdRequest.

        实体ID，ID字符串。

        :param id: The id of this ShowAggregationLogicTableByIdRequest.
        :type id: str
        """
        self._id = id

    @property
    def latest(self):
        r"""Gets the latest of this ShowAggregationLogicTableByIdRequest.

        是否查询最新的。

        :return: The latest of this ShowAggregationLogicTableByIdRequest.
        :rtype: bool
        """
        return self._latest

    @latest.setter
    def latest(self, latest):
        r"""Sets the latest of this ShowAggregationLogicTableByIdRequest.

        是否查询最新的。

        :param latest: The latest of this ShowAggregationLogicTableByIdRequest.
        :type latest: bool
        """
        self._latest = latest

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
        if not isinstance(other, ShowAggregationLogicTableByIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
