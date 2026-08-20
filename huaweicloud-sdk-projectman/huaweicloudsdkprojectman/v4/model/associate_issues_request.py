# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateIssuesRequest:

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
        'issue_id': 'str',
        'dst_domain_id': 'str',
        'body': 'IssueAssociateVO'
    }

    attribute_map = {
        'project_id': 'project_id',
        'issue_id': 'issue_id',
        'dst_domain_id': 'dst_domain_id',
        'body': 'body'
    }

    def __init__(self, project_id=None, issue_id=None, dst_domain_id=None, body=None):
        r"""AssociateIssuesRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。
        :type project_id: str
        :param issue_id: 工作项唯一ID。可以通过查询工作项列表或者查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。
        :type issue_id: str
        :param dst_domain_id: 目标项目的32位UUID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。非跨项目场景，与请求路径中的project_id一致。
        :type dst_domain_id: str
        :param body: Body of the AssociateIssuesRequest
        :type body: :class:`huaweicloudsdkprojectman.v4.IssueAssociateVO`
        """
        
        

        self._project_id = None
        self._issue_id = None
        self._dst_domain_id = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.issue_id = issue_id
        self.dst_domain_id = dst_domain_id
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this AssociateIssuesRequest.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :return: The project_id of this AssociateIssuesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AssociateIssuesRequest.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :param project_id: The project_id of this AssociateIssuesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def issue_id(self):
        r"""Gets the issue_id of this AssociateIssuesRequest.

        工作项唯一ID。可以通过查询工作项列表或者查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。

        :return: The issue_id of this AssociateIssuesRequest.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this AssociateIssuesRequest.

        工作项唯一ID。可以通过查询工作项列表或者查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。

        :param issue_id: The issue_id of this AssociateIssuesRequest.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def dst_domain_id(self):
        r"""Gets the dst_domain_id of this AssociateIssuesRequest.

        目标项目的32位UUID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。非跨项目场景，与请求路径中的project_id一致。

        :return: The dst_domain_id of this AssociateIssuesRequest.
        :rtype: str
        """
        return self._dst_domain_id

    @dst_domain_id.setter
    def dst_domain_id(self, dst_domain_id):
        r"""Sets the dst_domain_id of this AssociateIssuesRequest.

        目标项目的32位UUID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。非跨项目场景，与请求路径中的project_id一致。

        :param dst_domain_id: The dst_domain_id of this AssociateIssuesRequest.
        :type dst_domain_id: str
        """
        self._dst_domain_id = dst_domain_id

    @property
    def body(self):
        r"""Gets the body of this AssociateIssuesRequest.

        :return: The body of this AssociateIssuesRequest.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueAssociateVO`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this AssociateIssuesRequest.

        :param body: The body of this AssociateIssuesRequest.
        :type body: :class:`huaweicloudsdkprojectman.v4.IssueAssociateVO`
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
        if not isinstance(other, AssociateIssuesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
