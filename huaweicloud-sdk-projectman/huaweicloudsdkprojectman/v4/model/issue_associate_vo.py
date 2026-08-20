# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueAssociateVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'associated_ids': 'str',
        'operation_flag': 'int',
        'associate_issue_type': 'str',
        'source_issue_type': 'str',
        'is_replace': 'bool',
        'link_field_code': 'str'
    }

    attribute_map = {
        'associated_ids': 'associated_ids',
        'operation_flag': 'operation_flag',
        'associate_issue_type': 'associate_issue_type',
        'source_issue_type': 'source_issue_type',
        'is_replace': 'is_replace',
        'link_field_code': 'link_field_code'
    }

    def __init__(self, associated_ids=None, operation_flag=None, associate_issue_type=None, source_issue_type=None, is_replace=None, link_field_code=None):
        r"""IssueAssociateVO

        The model defined in huaweicloud sdk

        :param associated_ids: 关联的工作项ID，多个ID使用逗号分割。可以通过查询工作项列表或者查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。 当link_field_code&#x3D;link时，最多支持关联500个工作项ID，其他场景最多支持50个工作项ID。
        :type associated_ids: str
        :param operation_flag: 操作类型标记位。
        :type operation_flag: int
        :param associate_issue_type: 关联项类型编码。
        :type associate_issue_type: str
        :param source_issue_type: 当前工作项类型编码。
        :type source_issue_type: str
        :param is_replace: 是否使用替换模式。默认为false，追加关联项。如果为true，则会删除原有的关联项，替换为本次关联的工作项。
        :type is_replace: bool
        :param link_field_code: 关联字段的字段编码。
        :type link_field_code: str
        """
        
        

        self._associated_ids = None
        self._operation_flag = None
        self._associate_issue_type = None
        self._source_issue_type = None
        self._is_replace = None
        self._link_field_code = None
        self.discriminator = None

        self.associated_ids = associated_ids
        self.operation_flag = operation_flag
        self.associate_issue_type = associate_issue_type
        self.source_issue_type = source_issue_type
        if is_replace is not None:
            self.is_replace = is_replace
        if link_field_code is not None:
            self.link_field_code = link_field_code

    @property
    def associated_ids(self):
        r"""Gets the associated_ids of this IssueAssociateVO.

        关联的工作项ID，多个ID使用逗号分割。可以通过查询工作项列表或者查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。 当link_field_code=link时，最多支持关联500个工作项ID，其他场景最多支持50个工作项ID。

        :return: The associated_ids of this IssueAssociateVO.
        :rtype: str
        """
        return self._associated_ids

    @associated_ids.setter
    def associated_ids(self, associated_ids):
        r"""Sets the associated_ids of this IssueAssociateVO.

        关联的工作项ID，多个ID使用逗号分割。可以通过查询工作项列表或者查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。 当link_field_code=link时，最多支持关联500个工作项ID，其他场景最多支持50个工作项ID。

        :param associated_ids: The associated_ids of this IssueAssociateVO.
        :type associated_ids: str
        """
        self._associated_ids = associated_ids

    @property
    def operation_flag(self):
        r"""Gets the operation_flag of this IssueAssociateVO.

        操作类型标记位。

        :return: The operation_flag of this IssueAssociateVO.
        :rtype: int
        """
        return self._operation_flag

    @operation_flag.setter
    def operation_flag(self, operation_flag):
        r"""Sets the operation_flag of this IssueAssociateVO.

        操作类型标记位。

        :param operation_flag: The operation_flag of this IssueAssociateVO.
        :type operation_flag: int
        """
        self._operation_flag = operation_flag

    @property
    def associate_issue_type(self):
        r"""Gets the associate_issue_type of this IssueAssociateVO.

        关联项类型编码。

        :return: The associate_issue_type of this IssueAssociateVO.
        :rtype: str
        """
        return self._associate_issue_type

    @associate_issue_type.setter
    def associate_issue_type(self, associate_issue_type):
        r"""Sets the associate_issue_type of this IssueAssociateVO.

        关联项类型编码。

        :param associate_issue_type: The associate_issue_type of this IssueAssociateVO.
        :type associate_issue_type: str
        """
        self._associate_issue_type = associate_issue_type

    @property
    def source_issue_type(self):
        r"""Gets the source_issue_type of this IssueAssociateVO.

        当前工作项类型编码。

        :return: The source_issue_type of this IssueAssociateVO.
        :rtype: str
        """
        return self._source_issue_type

    @source_issue_type.setter
    def source_issue_type(self, source_issue_type):
        r"""Sets the source_issue_type of this IssueAssociateVO.

        当前工作项类型编码。

        :param source_issue_type: The source_issue_type of this IssueAssociateVO.
        :type source_issue_type: str
        """
        self._source_issue_type = source_issue_type

    @property
    def is_replace(self):
        r"""Gets the is_replace of this IssueAssociateVO.

        是否使用替换模式。默认为false，追加关联项。如果为true，则会删除原有的关联项，替换为本次关联的工作项。

        :return: The is_replace of this IssueAssociateVO.
        :rtype: bool
        """
        return self._is_replace

    @is_replace.setter
    def is_replace(self, is_replace):
        r"""Sets the is_replace of this IssueAssociateVO.

        是否使用替换模式。默认为false，追加关联项。如果为true，则会删除原有的关联项，替换为本次关联的工作项。

        :param is_replace: The is_replace of this IssueAssociateVO.
        :type is_replace: bool
        """
        self._is_replace = is_replace

    @property
    def link_field_code(self):
        r"""Gets the link_field_code of this IssueAssociateVO.

        关联字段的字段编码。

        :return: The link_field_code of this IssueAssociateVO.
        :rtype: str
        """
        return self._link_field_code

    @link_field_code.setter
    def link_field_code(self, link_field_code):
        r"""Sets the link_field_code of this IssueAssociateVO.

        关联字段的字段编码。

        :param link_field_code: The link_field_code of this IssueAssociateVO.
        :type link_field_code: str
        """
        self._link_field_code = link_field_code

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
        if not isinstance(other, IssueAssociateVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
