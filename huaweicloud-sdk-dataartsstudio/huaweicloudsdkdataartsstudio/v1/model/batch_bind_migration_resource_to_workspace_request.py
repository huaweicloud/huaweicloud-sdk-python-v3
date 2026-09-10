# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchBindMigrationResourceToWorkspaceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_project_id': 'str',
        'instance_id': 'str',
        'body': 'BatchBindMigrationResourceToWorkspaceRequestBody'
    }

    attribute_map = {
        'x_project_id': 'X-Project-Id',
        'instance_id': 'instance_id',
        'body': 'body'
    }

    def __init__(self, x_project_id=None, instance_id=None, body=None):
        r"""BatchBindMigrationResourceToWorkspaceRequest

        The model defined in huaweicloud sdk

        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param instance_id: DataArts Studio实例ID。
        :type instance_id: str
        :param body: Body of the BatchBindMigrationResourceToWorkspaceRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.BatchBindMigrationResourceToWorkspaceRequestBody`
        """
        
        

        self._x_project_id = None
        self._instance_id = None
        self._body = None
        self.discriminator = None

        if x_project_id is not None:
            self.x_project_id = x_project_id
        self.instance_id = instance_id
        if body is not None:
            self.body = body

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this BatchBindMigrationResourceToWorkspaceRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this BatchBindMigrationResourceToWorkspaceRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this BatchBindMigrationResourceToWorkspaceRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this BatchBindMigrationResourceToWorkspaceRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BatchBindMigrationResourceToWorkspaceRequest.

        DataArts Studio实例ID。

        :return: The instance_id of this BatchBindMigrationResourceToWorkspaceRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BatchBindMigrationResourceToWorkspaceRequest.

        DataArts Studio实例ID。

        :param instance_id: The instance_id of this BatchBindMigrationResourceToWorkspaceRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def body(self):
        r"""Gets the body of this BatchBindMigrationResourceToWorkspaceRequest.

        :return: The body of this BatchBindMigrationResourceToWorkspaceRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BatchBindMigrationResourceToWorkspaceRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchBindMigrationResourceToWorkspaceRequest.

        :param body: The body of this BatchBindMigrationResourceToWorkspaceRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.BatchBindMigrationResourceToWorkspaceRequestBody`
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
        if not isinstance(other, BatchBindMigrationResourceToWorkspaceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
