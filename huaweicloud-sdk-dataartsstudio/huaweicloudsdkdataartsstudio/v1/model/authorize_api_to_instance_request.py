# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthorizeApiToInstanceRequest:

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
        'dlm_type': 'str',
        'api_id': 'str',
        'instance_id': 'str',
        'body': 'ApiParaForAuthorizeToInstance'
    }

    attribute_map = {
        'workspace': 'workspace',
        'dlm_type': 'Dlm-Type',
        'api_id': 'api_id',
        'instance_id': 'instance_id',
        'body': 'body'
    }

    def __init__(self, workspace=None, dlm_type=None, api_id=None, instance_id=None, body=None):
        r"""AuthorizeApiToInstanceRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param dlm_type: 数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。
        :type dlm_type: str
        :param api_id: api编号。
        :type api_id: str
        :param instance_id: 集群编号。
        :type instance_id: str
        :param body: Body of the AuthorizeApiToInstanceRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.ApiParaForAuthorizeToInstance`
        """
        
        

        self._workspace = None
        self._dlm_type = None
        self._api_id = None
        self._instance_id = None
        self._body = None
        self.discriminator = None

        self.workspace = workspace
        if dlm_type is not None:
            self.dlm_type = dlm_type
        self.api_id = api_id
        self.instance_id = instance_id
        if body is not None:
            self.body = body

    @property
    def workspace(self):
        r"""Gets the workspace of this AuthorizeApiToInstanceRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this AuthorizeApiToInstanceRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this AuthorizeApiToInstanceRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this AuthorizeApiToInstanceRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def dlm_type(self):
        r"""Gets the dlm_type of this AuthorizeApiToInstanceRequest.

        数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。

        :return: The dlm_type of this AuthorizeApiToInstanceRequest.
        :rtype: str
        """
        return self._dlm_type

    @dlm_type.setter
    def dlm_type(self, dlm_type):
        r"""Sets the dlm_type of this AuthorizeApiToInstanceRequest.

        数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。

        :param dlm_type: The dlm_type of this AuthorizeApiToInstanceRequest.
        :type dlm_type: str
        """
        self._dlm_type = dlm_type

    @property
    def api_id(self):
        r"""Gets the api_id of this AuthorizeApiToInstanceRequest.

        api编号。

        :return: The api_id of this AuthorizeApiToInstanceRequest.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        r"""Sets the api_id of this AuthorizeApiToInstanceRequest.

        api编号。

        :param api_id: The api_id of this AuthorizeApiToInstanceRequest.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this AuthorizeApiToInstanceRequest.

        集群编号。

        :return: The instance_id of this AuthorizeApiToInstanceRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this AuthorizeApiToInstanceRequest.

        集群编号。

        :param instance_id: The instance_id of this AuthorizeApiToInstanceRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def body(self):
        r"""Gets the body of this AuthorizeApiToInstanceRequest.

        :return: The body of this AuthorizeApiToInstanceRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ApiParaForAuthorizeToInstance`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this AuthorizeApiToInstanceRequest.

        :param body: The body of this AuthorizeApiToInstanceRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.ApiParaForAuthorizeToInstance`
        """
        self._body = body

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
        if not isinstance(other, AuthorizeApiToInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
