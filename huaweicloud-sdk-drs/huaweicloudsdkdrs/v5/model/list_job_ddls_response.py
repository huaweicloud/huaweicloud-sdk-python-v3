# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobDdlsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ddl_list': 'list[DdlAlarmResp]',
        'count': 'int'
    }

    attribute_map = {
        'ddl_list': 'ddl_list',
        'count': 'count'
    }

    def __init__(self, ddl_list=None, count=None):
        r"""ListJobDdlsResponse

        The model defined in huaweicloud sdk

        :param ddl_list: DDL告警信息列表。
        :type ddl_list: list[:class:`huaweicloudsdkdrs.v5.DdlAlarmResp`]
        :param count: 列表中的项目总数，与分页无关。
        :type count: int
        """
        
        super(ListJobDdlsResponse, self).__init__()

        self._ddl_list = None
        self._count = None
        self.discriminator = None

        if ddl_list is not None:
            self.ddl_list = ddl_list
        if count is not None:
            self.count = count

    @property
    def ddl_list(self):
        r"""Gets the ddl_list of this ListJobDdlsResponse.

        DDL告警信息列表。

        :return: The ddl_list of this ListJobDdlsResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.DdlAlarmResp`]
        """
        return self._ddl_list

    @ddl_list.setter
    def ddl_list(self, ddl_list):
        r"""Sets the ddl_list of this ListJobDdlsResponse.

        DDL告警信息列表。

        :param ddl_list: The ddl_list of this ListJobDdlsResponse.
        :type ddl_list: list[:class:`huaweicloudsdkdrs.v5.DdlAlarmResp`]
        """
        self._ddl_list = ddl_list

    @property
    def count(self):
        r"""Gets the count of this ListJobDdlsResponse.

        列表中的项目总数，与分页无关。

        :return: The count of this ListJobDdlsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListJobDdlsResponse.

        列表中的项目总数，与分页无关。

        :param count: The count of this ListJobDdlsResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListJobDdlsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
