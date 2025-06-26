# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLtsLogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_status': 'str',
        'lts_access_list': 'list[LtslogInfo]',
        'count': 'int'
    }

    attribute_map = {
        'access_status': 'access_status',
        'lts_access_list': 'lts_access_list',
        'count': 'count'
    }

    def __init__(self, access_status=None, lts_access_list=None, count=None):
        r"""ListLtsLogsResponse

        The model defined in huaweicloud sdk

        :param access_status: **参数解释**： 日志开启状态。 **取值范围**： 不涉及。
        :type access_status: str
        :param lts_access_list: **参数解释**： LTS日志列表。 **取值范围**： 不涉及。
        :type lts_access_list: list[:class:`huaweicloudsdkdws.v2.LtslogInfo`]
        :param count: **参数解释**： 总数量。 **取值范围**： 大于等于0。
        :type count: int
        """
        
        super(ListLtsLogsResponse, self).__init__()

        self._access_status = None
        self._lts_access_list = None
        self._count = None
        self.discriminator = None

        if access_status is not None:
            self.access_status = access_status
        if lts_access_list is not None:
            self.lts_access_list = lts_access_list
        if count is not None:
            self.count = count

    @property
    def access_status(self):
        r"""Gets the access_status of this ListLtsLogsResponse.

        **参数解释**： 日志开启状态。 **取值范围**： 不涉及。

        :return: The access_status of this ListLtsLogsResponse.
        :rtype: str
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        r"""Sets the access_status of this ListLtsLogsResponse.

        **参数解释**： 日志开启状态。 **取值范围**： 不涉及。

        :param access_status: The access_status of this ListLtsLogsResponse.
        :type access_status: str
        """
        self._access_status = access_status

    @property
    def lts_access_list(self):
        r"""Gets the lts_access_list of this ListLtsLogsResponse.

        **参数解释**： LTS日志列表。 **取值范围**： 不涉及。

        :return: The lts_access_list of this ListLtsLogsResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.LtslogInfo`]
        """
        return self._lts_access_list

    @lts_access_list.setter
    def lts_access_list(self, lts_access_list):
        r"""Sets the lts_access_list of this ListLtsLogsResponse.

        **参数解释**： LTS日志列表。 **取值范围**： 不涉及。

        :param lts_access_list: The lts_access_list of this ListLtsLogsResponse.
        :type lts_access_list: list[:class:`huaweicloudsdkdws.v2.LtslogInfo`]
        """
        self._lts_access_list = lts_access_list

    @property
    def count(self):
        r"""Gets the count of this ListLtsLogsResponse.

        **参数解释**： 总数量。 **取值范围**： 大于等于0。

        :return: The count of this ListLtsLogsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListLtsLogsResponse.

        **参数解释**： 总数量。 **取值范围**： 大于等于0。

        :param count: The count of this ListLtsLogsResponse.
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
        if not isinstance(other, ListLtsLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
