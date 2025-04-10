# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyTableAuthorityRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'approver': 'TableApprover',
        'table_info': 'ListTableApproversRequestBody',
        'proposers': 'list[TableProposers]',
        'reason': 'str'
    }

    attribute_map = {
        'approver': 'approver',
        'table_info': 'table_info',
        'proposers': 'proposers',
        'reason': 'reason'
    }

    def __init__(self, approver=None, table_info=None, proposers=None, reason=None):
        r"""ApplyTableAuthorityRequestBody

        The model defined in huaweicloud sdk

        :param approver: 
        :type approver: :class:`huaweicloudsdkdataartsstudio.v1.TableApprover`
        :param table_info: 
        :type table_info: :class:`huaweicloudsdkdataartsstudio.v1.ListTableApproversRequestBody`
        :param proposers: 申请人列表
        :type proposers: list[:class:`huaweicloudsdkdataartsstudio.v1.TableProposers`]
        :param reason: 申请理由
        :type reason: str
        """
        
        

        self._approver = None
        self._table_info = None
        self._proposers = None
        self._reason = None
        self.discriminator = None

        if approver is not None:
            self.approver = approver
        if table_info is not None:
            self.table_info = table_info
        if proposers is not None:
            self.proposers = proposers
        if reason is not None:
            self.reason = reason

    @property
    def approver(self):
        r"""Gets the approver of this ApplyTableAuthorityRequestBody.

        :return: The approver of this ApplyTableAuthorityRequestBody.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.TableApprover`
        """
        return self._approver

    @approver.setter
    def approver(self, approver):
        r"""Sets the approver of this ApplyTableAuthorityRequestBody.

        :param approver: The approver of this ApplyTableAuthorityRequestBody.
        :type approver: :class:`huaweicloudsdkdataartsstudio.v1.TableApprover`
        """
        self._approver = approver

    @property
    def table_info(self):
        r"""Gets the table_info of this ApplyTableAuthorityRequestBody.

        :return: The table_info of this ApplyTableAuthorityRequestBody.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListTableApproversRequestBody`
        """
        return self._table_info

    @table_info.setter
    def table_info(self, table_info):
        r"""Sets the table_info of this ApplyTableAuthorityRequestBody.

        :param table_info: The table_info of this ApplyTableAuthorityRequestBody.
        :type table_info: :class:`huaweicloudsdkdataartsstudio.v1.ListTableApproversRequestBody`
        """
        self._table_info = table_info

    @property
    def proposers(self):
        r"""Gets the proposers of this ApplyTableAuthorityRequestBody.

        申请人列表

        :return: The proposers of this ApplyTableAuthorityRequestBody.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TableProposers`]
        """
        return self._proposers

    @proposers.setter
    def proposers(self, proposers):
        r"""Sets the proposers of this ApplyTableAuthorityRequestBody.

        申请人列表

        :param proposers: The proposers of this ApplyTableAuthorityRequestBody.
        :type proposers: list[:class:`huaweicloudsdkdataartsstudio.v1.TableProposers`]
        """
        self._proposers = proposers

    @property
    def reason(self):
        r"""Gets the reason of this ApplyTableAuthorityRequestBody.

        申请理由

        :return: The reason of this ApplyTableAuthorityRequestBody.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this ApplyTableAuthorityRequestBody.

        申请理由

        :param reason: The reason of this ApplyTableAuthorityRequestBody.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, ApplyTableAuthorityRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
