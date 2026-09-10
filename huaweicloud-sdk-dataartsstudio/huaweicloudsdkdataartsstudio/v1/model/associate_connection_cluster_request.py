# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateConnectionClusterRequest:

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
        'connection_id': 'str',
        'body': 'AssociateConnectionClusterReq'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'connection_id': 'connection_id',
        'body': 'body'
    }

    def __init__(self, workspace=None, x_project_id=None, connection_id=None, body=None):
        r"""AssociateConnectionClusterRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param connection_id: 连接ID，用于标识资源组网络连接的UUID。
        :type connection_id: str
        :param body: Body of the AssociateConnectionClusterRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.AssociateConnectionClusterReq`
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._connection_id = None
        self._body = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        self.connection_id = connection_id
        if body is not None:
            self.body = body

    @property
    def workspace(self):
        r"""Gets the workspace of this AssociateConnectionClusterRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this AssociateConnectionClusterRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this AssociateConnectionClusterRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this AssociateConnectionClusterRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this AssociateConnectionClusterRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this AssociateConnectionClusterRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this AssociateConnectionClusterRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this AssociateConnectionClusterRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def connection_id(self):
        r"""Gets the connection_id of this AssociateConnectionClusterRequest.

        连接ID，用于标识资源组网络连接的UUID。

        :return: The connection_id of this AssociateConnectionClusterRequest.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this AssociateConnectionClusterRequest.

        连接ID，用于标识资源组网络连接的UUID。

        :param connection_id: The connection_id of this AssociateConnectionClusterRequest.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def body(self):
        r"""Gets the body of this AssociateConnectionClusterRequest.

        :return: The body of this AssociateConnectionClusterRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.AssociateConnectionClusterReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this AssociateConnectionClusterRequest.

        :param body: The body of this AssociateConnectionClusterRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.AssociateConnectionClusterReq`
        """
        self._body = body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AssociateConnectionClusterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
