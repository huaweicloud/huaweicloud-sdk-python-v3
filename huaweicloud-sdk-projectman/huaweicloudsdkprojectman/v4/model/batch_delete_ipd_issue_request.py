# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteIpdIssueRequest:

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
        'is_permanent_delete': 'bool',
        'src_project_id': 'str',
        'body': 'list[str]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'is_permanent_delete': 'is_permanent_delete',
        'src_project_id': 'src_project_id',
        'body': 'body'
    }

    def __init__(self, project_id=None, is_permanent_delete=None, src_project_id=None, body=None):
        r"""BatchDeleteIpdIssueRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。
        :type project_id: str
        :param is_permanent_delete: 是否永久删除
        :type is_permanent_delete: bool
        :param src_project_id: 工作项的提出项目ID
        :type src_project_id: str
        :param body: Body of the BatchDeleteIpdIssueRequest
        :type body: list[str]
        """
        
        

        self._project_id = None
        self._is_permanent_delete = None
        self._src_project_id = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        if is_permanent_delete is not None:
            self.is_permanent_delete = is_permanent_delete
        if src_project_id is not None:
            self.src_project_id = src_project_id
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this BatchDeleteIpdIssueRequest.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :return: The project_id of this BatchDeleteIpdIssueRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this BatchDeleteIpdIssueRequest.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :param project_id: The project_id of this BatchDeleteIpdIssueRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def is_permanent_delete(self):
        r"""Gets the is_permanent_delete of this BatchDeleteIpdIssueRequest.

        是否永久删除

        :return: The is_permanent_delete of this BatchDeleteIpdIssueRequest.
        :rtype: bool
        """
        return self._is_permanent_delete

    @is_permanent_delete.setter
    def is_permanent_delete(self, is_permanent_delete):
        r"""Sets the is_permanent_delete of this BatchDeleteIpdIssueRequest.

        是否永久删除

        :param is_permanent_delete: The is_permanent_delete of this BatchDeleteIpdIssueRequest.
        :type is_permanent_delete: bool
        """
        self._is_permanent_delete = is_permanent_delete

    @property
    def src_project_id(self):
        r"""Gets the src_project_id of this BatchDeleteIpdIssueRequest.

        工作项的提出项目ID

        :return: The src_project_id of this BatchDeleteIpdIssueRequest.
        :rtype: str
        """
        return self._src_project_id

    @src_project_id.setter
    def src_project_id(self, src_project_id):
        r"""Sets the src_project_id of this BatchDeleteIpdIssueRequest.

        工作项的提出项目ID

        :param src_project_id: The src_project_id of this BatchDeleteIpdIssueRequest.
        :type src_project_id: str
        """
        self._src_project_id = src_project_id

    @property
    def body(self):
        r"""Gets the body of this BatchDeleteIpdIssueRequest.

        :return: The body of this BatchDeleteIpdIssueRequest.
        :rtype: list[str]
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchDeleteIpdIssueRequest.

        :param body: The body of this BatchDeleteIpdIssueRequest.
        :type body: list[str]
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
        if not isinstance(other, BatchDeleteIpdIssueRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
