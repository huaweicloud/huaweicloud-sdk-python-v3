# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDesignOperationResultRequest:

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
        'operation_type': 'str',
        'limit': 'int',
        'offset': 'int',
        'operation_id': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'operation_type': 'operation_type',
        'limit': 'limit',
        'offset': 'offset',
        'operation_id': 'operation_id'
    }

    def __init__(self, workspace=None, x_project_id=None, operation_type=None, limit=None, offset=None, operation_id=None):
        r"""ShowDesignOperationResultRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param operation_type: 批量操作类型。 枚举值：   - ER_REVERSE_DB: 关系建模逆向数据库   - TRANSFORM_LOGIC_MODEL: 逻辑模型转物理模型 
        :type operation_type: str
        :param limit: 每页查询条数，即查询Y条数据。默认值50，取值范围[1,100]。
        :type limit: int
        :param offset: 查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整，默认值0。
        :type offset: int
        :param operation_id: 批量操作id，在逻辑模型转物理表时，填写的是逻辑模型的model_id，在逆向数据库时，填写的是目标模型的model_id。model_id可从接口[获取模型](ListWorkspaces.xml)中获取。
        :type operation_id: str
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._operation_type = None
        self._limit = None
        self._offset = None
        self._operation_id = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        self.operation_type = operation_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if operation_id is not None:
            self.operation_id = operation_id

    @property
    def workspace(self):
        r"""Gets the workspace of this ShowDesignOperationResultRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ShowDesignOperationResultRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ShowDesignOperationResultRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ShowDesignOperationResultRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this ShowDesignOperationResultRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this ShowDesignOperationResultRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this ShowDesignOperationResultRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this ShowDesignOperationResultRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def operation_type(self):
        r"""Gets the operation_type of this ShowDesignOperationResultRequest.

        批量操作类型。 枚举值：   - ER_REVERSE_DB: 关系建模逆向数据库   - TRANSFORM_LOGIC_MODEL: 逻辑模型转物理模型 

        :return: The operation_type of this ShowDesignOperationResultRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        r"""Sets the operation_type of this ShowDesignOperationResultRequest.

        批量操作类型。 枚举值：   - ER_REVERSE_DB: 关系建模逆向数据库   - TRANSFORM_LOGIC_MODEL: 逻辑模型转物理模型 

        :param operation_type: The operation_type of this ShowDesignOperationResultRequest.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def limit(self):
        r"""Gets the limit of this ShowDesignOperationResultRequest.

        每页查询条数，即查询Y条数据。默认值50，取值范围[1,100]。

        :return: The limit of this ShowDesignOperationResultRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowDesignOperationResultRequest.

        每页查询条数，即查询Y条数据。默认值50，取值范围[1,100]。

        :param limit: The limit of this ShowDesignOperationResultRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowDesignOperationResultRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整，默认值0。

        :return: The offset of this ShowDesignOperationResultRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowDesignOperationResultRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整，默认值0。

        :param offset: The offset of this ShowDesignOperationResultRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def operation_id(self):
        r"""Gets the operation_id of this ShowDesignOperationResultRequest.

        批量操作id，在逻辑模型转物理表时，填写的是逻辑模型的model_id，在逆向数据库时，填写的是目标模型的model_id。model_id可从接口[获取模型](ListWorkspaces.xml)中获取。

        :return: The operation_id of this ShowDesignOperationResultRequest.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        r"""Sets the operation_id of this ShowDesignOperationResultRequest.

        批量操作id，在逻辑模型转物理表时，填写的是逻辑模型的model_id，在逆向数据库时，填写的是目标模型的model_id。model_id可从接口[获取模型](ListWorkspaces.xml)中获取。

        :param operation_id: The operation_id of this ShowDesignOperationResultRequest.
        :type operation_id: str
        """
        self._operation_id = operation_id

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
        if not isinstance(other, ShowDesignOperationResultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
