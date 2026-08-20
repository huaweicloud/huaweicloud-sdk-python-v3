# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIpdProcessInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'operate_type': 'str',
        'domain_id': 'str',
        'body': 'CreateProcessInstanceReq'
    }

    attribute_map = {
        'project_id': 'project_id',
        'operate_type': 'operate_type',
        'domain_id': 'domain_id',
        'body': 'body'
    }

    def __init__(self, project_id=None, operate_type=None, domain_id=None, body=None):
        r"""CreateIpdProcessInstanceRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。
        :type project_id: str
        :param operate_type: 操作类型
        :type operate_type: str
        :param domain_id: 提出项目的domainId
        :type domain_id: str
        :param body: Body of the CreateIpdProcessInstanceRequest
        :type body: :class:`huaweicloudsdkprojectman.v4.CreateProcessInstanceReq`
        """
        
        

        self._project_id = None
        self._operate_type = None
        self._domain_id = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        if operate_type is not None:
            self.operate_type = operate_type
        if domain_id is not None:
            self.domain_id = domain_id
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateIpdProcessInstanceRequest.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :return: The project_id of this CreateIpdProcessInstanceRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateIpdProcessInstanceRequest.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :param project_id: The project_id of this CreateIpdProcessInstanceRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def operate_type(self):
        r"""Gets the operate_type of this CreateIpdProcessInstanceRequest.

        操作类型

        :return: The operate_type of this CreateIpdProcessInstanceRequest.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this CreateIpdProcessInstanceRequest.

        操作类型

        :param operate_type: The operate_type of this CreateIpdProcessInstanceRequest.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CreateIpdProcessInstanceRequest.

        提出项目的domainId

        :return: The domain_id of this CreateIpdProcessInstanceRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CreateIpdProcessInstanceRequest.

        提出项目的domainId

        :param domain_id: The domain_id of this CreateIpdProcessInstanceRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def body(self):
        r"""Gets the body of this CreateIpdProcessInstanceRequest.

        :return: The body of this CreateIpdProcessInstanceRequest.
        :rtype: :class:`huaweicloudsdkprojectman.v4.CreateProcessInstanceReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateIpdProcessInstanceRequest.

        :param body: The body of this CreateIpdProcessInstanceRequest.
        :type body: :class:`huaweicloudsdkprojectman.v4.CreateProcessInstanceReq`
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
        if not isinstance(other, CreateIpdProcessInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
