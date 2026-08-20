# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryIssueAssociatedItemRequest:

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
        'issue_type': 'str',
        'domain_id': 'str',
        'target_project_id': 'str',
        'link_field_code': 'str',
        'page_no': 'str',
        'page_size': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'issue_id': 'issue_id',
        'issue_type': 'issue_type',
        'domain_id': 'domain_id',
        'target_project_id': 'target_project_id',
        'link_field_code': 'link_field_code',
        'page_no': 'page_no',
        'page_size': 'page_size'
    }

    def __init__(self, project_id=None, issue_id=None, issue_type=None, domain_id=None, target_project_id=None, link_field_code=None, page_no=None, page_size=None):
        r"""QueryIssueAssociatedItemRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。
        :type project_id: str
        :param issue_id: 工作项唯一ID。可以通过查询工作项列表或者查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。
        :type issue_id: str
        :param issue_type: 工作项类型。
        :type issue_type: str
        :param domain_id: 项目空间ID，可以通过查询IPD项目列表接口获取，响应消息体中的domain_id字段的值就是项目空间ID。
        :type domain_id: str
        :param target_project_id: 目标项目的32位uuid，项目唯一标识，通过查询IPD项目列表获取，响应消息体中的project_id字段的值就是项目ID。
        :type target_project_id: str
        :param link_field_code: 关联字段的字段编码。
        :type link_field_code: str
        :param page_no: 分页参数，当前页。
        :type page_no: str
        :param page_size: 分页参数，页长。
        :type page_size: str
        """
        
        

        self._project_id = None
        self._issue_id = None
        self._issue_type = None
        self._domain_id = None
        self._target_project_id = None
        self._link_field_code = None
        self._page_no = None
        self._page_size = None
        self.discriminator = None

        self.project_id = project_id
        self.issue_id = issue_id
        self.issue_type = issue_type
        if domain_id is not None:
            self.domain_id = domain_id
        if target_project_id is not None:
            self.target_project_id = target_project_id
        if link_field_code is not None:
            self.link_field_code = link_field_code
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size

    @property
    def project_id(self):
        r"""Gets the project_id of this QueryIssueAssociatedItemRequest.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :return: The project_id of this QueryIssueAssociatedItemRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this QueryIssueAssociatedItemRequest.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :param project_id: The project_id of this QueryIssueAssociatedItemRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def issue_id(self):
        r"""Gets the issue_id of this QueryIssueAssociatedItemRequest.

        工作项唯一ID。可以通过查询工作项列表或者查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。

        :return: The issue_id of this QueryIssueAssociatedItemRequest.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this QueryIssueAssociatedItemRequest.

        工作项唯一ID。可以通过查询工作项列表或者查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。

        :param issue_id: The issue_id of this QueryIssueAssociatedItemRequest.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def issue_type(self):
        r"""Gets the issue_type of this QueryIssueAssociatedItemRequest.

        工作项类型。

        :return: The issue_type of this QueryIssueAssociatedItemRequest.
        :rtype: str
        """
        return self._issue_type

    @issue_type.setter
    def issue_type(self, issue_type):
        r"""Sets the issue_type of this QueryIssueAssociatedItemRequest.

        工作项类型。

        :param issue_type: The issue_type of this QueryIssueAssociatedItemRequest.
        :type issue_type: str
        """
        self._issue_type = issue_type

    @property
    def domain_id(self):
        r"""Gets the domain_id of this QueryIssueAssociatedItemRequest.

        项目空间ID，可以通过查询IPD项目列表接口获取，响应消息体中的domain_id字段的值就是项目空间ID。

        :return: The domain_id of this QueryIssueAssociatedItemRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this QueryIssueAssociatedItemRequest.

        项目空间ID，可以通过查询IPD项目列表接口获取，响应消息体中的domain_id字段的值就是项目空间ID。

        :param domain_id: The domain_id of this QueryIssueAssociatedItemRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def target_project_id(self):
        r"""Gets the target_project_id of this QueryIssueAssociatedItemRequest.

        目标项目的32位uuid，项目唯一标识，通过查询IPD项目列表获取，响应消息体中的project_id字段的值就是项目ID。

        :return: The target_project_id of this QueryIssueAssociatedItemRequest.
        :rtype: str
        """
        return self._target_project_id

    @target_project_id.setter
    def target_project_id(self, target_project_id):
        r"""Sets the target_project_id of this QueryIssueAssociatedItemRequest.

        目标项目的32位uuid，项目唯一标识，通过查询IPD项目列表获取，响应消息体中的project_id字段的值就是项目ID。

        :param target_project_id: The target_project_id of this QueryIssueAssociatedItemRequest.
        :type target_project_id: str
        """
        self._target_project_id = target_project_id

    @property
    def link_field_code(self):
        r"""Gets the link_field_code of this QueryIssueAssociatedItemRequest.

        关联字段的字段编码。

        :return: The link_field_code of this QueryIssueAssociatedItemRequest.
        :rtype: str
        """
        return self._link_field_code

    @link_field_code.setter
    def link_field_code(self, link_field_code):
        r"""Sets the link_field_code of this QueryIssueAssociatedItemRequest.

        关联字段的字段编码。

        :param link_field_code: The link_field_code of this QueryIssueAssociatedItemRequest.
        :type link_field_code: str
        """
        self._link_field_code = link_field_code

    @property
    def page_no(self):
        r"""Gets the page_no of this QueryIssueAssociatedItemRequest.

        分页参数，当前页。

        :return: The page_no of this QueryIssueAssociatedItemRequest.
        :rtype: str
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this QueryIssueAssociatedItemRequest.

        分页参数，当前页。

        :param page_no: The page_no of this QueryIssueAssociatedItemRequest.
        :type page_no: str
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this QueryIssueAssociatedItemRequest.

        分页参数，页长。

        :return: The page_size of this QueryIssueAssociatedItemRequest.
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this QueryIssueAssociatedItemRequest.

        分页参数，页长。

        :param page_size: The page_size of this QueryIssueAssociatedItemRequest.
        :type page_size: str
        """
        self._page_size = page_size

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
        if not isinstance(other, QueryIssueAssociatedItemRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
