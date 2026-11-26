# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataServiceApproversResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_records': 'str',
        'size': 'int',
        'total_pages': 'int',
        'approvers': 'list[ApproverListApprovers]'
    }

    attribute_map = {
        'total_records': 'total_records',
        'size': 'size',
        'total_pages': 'total_pages',
        'approvers': 'approvers'
    }

    def __init__(self, total_records=None, size=None, total_pages=None, approvers=None):
        r"""ListDataServiceApproversResponse

        The model defined in huaweicloud sdk

        :param total_records: 总记录数
        :type total_records: str
        :param size: 单页记录数
        :type size: int
        :param total_pages: 总页数
        :type total_pages: int
        :param approvers: 审批人列表信息
        :type approvers: list[:class:`huaweicloudsdkdataartsstudio.v1.ApproverListApprovers`]
        """
        
        super().__init__()

        self._total_records = None
        self._size = None
        self._total_pages = None
        self._approvers = None
        self.discriminator = None

        if total_records is not None:
            self.total_records = total_records
        if size is not None:
            self.size = size
        if total_pages is not None:
            self.total_pages = total_pages
        if approvers is not None:
            self.approvers = approvers

    @property
    def total_records(self):
        r"""Gets the total_records of this ListDataServiceApproversResponse.

        总记录数

        :return: The total_records of this ListDataServiceApproversResponse.
        :rtype: str
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        r"""Sets the total_records of this ListDataServiceApproversResponse.

        总记录数

        :param total_records: The total_records of this ListDataServiceApproversResponse.
        :type total_records: str
        """
        self._total_records = total_records

    @property
    def size(self):
        r"""Gets the size of this ListDataServiceApproversResponse.

        单页记录数

        :return: The size of this ListDataServiceApproversResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListDataServiceApproversResponse.

        单页记录数

        :param size: The size of this ListDataServiceApproversResponse.
        :type size: int
        """
        self._size = size

    @property
    def total_pages(self):
        r"""Gets the total_pages of this ListDataServiceApproversResponse.

        总页数

        :return: The total_pages of this ListDataServiceApproversResponse.
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        r"""Sets the total_pages of this ListDataServiceApproversResponse.

        总页数

        :param total_pages: The total_pages of this ListDataServiceApproversResponse.
        :type total_pages: int
        """
        self._total_pages = total_pages

    @property
    def approvers(self):
        r"""Gets the approvers of this ListDataServiceApproversResponse.

        审批人列表信息

        :return: The approvers of this ListDataServiceApproversResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ApproverListApprovers`]
        """
        return self._approvers

    @approvers.setter
    def approvers(self, approvers):
        r"""Sets the approvers of this ListDataServiceApproversResponse.

        审批人列表信息

        :param approvers: The approvers of this ListDataServiceApproversResponse.
        :type approvers: list[:class:`huaweicloudsdkdataartsstudio.v1.ApproverListApprovers`]
        """
        self._approvers = approvers

    def to_dict(self):
        import warnings
        warnings.warn("ListDataServiceApproversResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListDataServiceApproversResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
