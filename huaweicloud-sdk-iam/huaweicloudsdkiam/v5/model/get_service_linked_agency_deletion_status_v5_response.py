# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetServiceLinkedAgencyDeletionStatusV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'DeletionTaskStatus',
        'reason': 'str',
        'agency_usage_list': 'list[AgencyUsage]'
    }

    attribute_map = {
        'status': 'status',
        'reason': 'reason',
        'agency_usage_list': 'agency_usage_list'
    }

    def __init__(self, status=None, reason=None, agency_usage_list=None):
        r"""GetServiceLinkedAgencyDeletionStatusV5Response

        The model defined in huaweicloud sdk

        :param status: 
        :type status: :class:`huaweicloudsdkiam.v5.DeletionTaskStatus`
        :param reason: 删除失败的原因。
        :type reason: str
        :param agency_usage_list: 该服务关联委托正在被使用的场景列表。
        :type agency_usage_list: list[:class:`huaweicloudsdkiam.v5.AgencyUsage`]
        """
        
        super(GetServiceLinkedAgencyDeletionStatusV5Response, self).__init__()

        self._status = None
        self._reason = None
        self._agency_usage_list = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if reason is not None:
            self.reason = reason
        if agency_usage_list is not None:
            self.agency_usage_list = agency_usage_list

    @property
    def status(self):
        r"""Gets the status of this GetServiceLinkedAgencyDeletionStatusV5Response.

        :return: The status of this GetServiceLinkedAgencyDeletionStatusV5Response.
        :rtype: :class:`huaweicloudsdkiam.v5.DeletionTaskStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this GetServiceLinkedAgencyDeletionStatusV5Response.

        :param status: The status of this GetServiceLinkedAgencyDeletionStatusV5Response.
        :type status: :class:`huaweicloudsdkiam.v5.DeletionTaskStatus`
        """
        self._status = status

    @property
    def reason(self):
        r"""Gets the reason of this GetServiceLinkedAgencyDeletionStatusV5Response.

        删除失败的原因。

        :return: The reason of this GetServiceLinkedAgencyDeletionStatusV5Response.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this GetServiceLinkedAgencyDeletionStatusV5Response.

        删除失败的原因。

        :param reason: The reason of this GetServiceLinkedAgencyDeletionStatusV5Response.
        :type reason: str
        """
        self._reason = reason

    @property
    def agency_usage_list(self):
        r"""Gets the agency_usage_list of this GetServiceLinkedAgencyDeletionStatusV5Response.

        该服务关联委托正在被使用的场景列表。

        :return: The agency_usage_list of this GetServiceLinkedAgencyDeletionStatusV5Response.
        :rtype: list[:class:`huaweicloudsdkiam.v5.AgencyUsage`]
        """
        return self._agency_usage_list

    @agency_usage_list.setter
    def agency_usage_list(self, agency_usage_list):
        r"""Sets the agency_usage_list of this GetServiceLinkedAgencyDeletionStatusV5Response.

        该服务关联委托正在被使用的场景列表。

        :param agency_usage_list: The agency_usage_list of this GetServiceLinkedAgencyDeletionStatusV5Response.
        :type agency_usage_list: list[:class:`huaweicloudsdkiam.v5.AgencyUsage`]
        """
        self._agency_usage_list = agency_usage_list

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
        if not isinstance(other, GetServiceLinkedAgencyDeletionStatusV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
