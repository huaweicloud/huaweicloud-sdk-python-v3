# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDesktopNamePolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_name_policy_infos': 'list[DesktopNamePolicyInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'desktop_name_policy_infos': 'desktop_name_policy_infos',
        'total_count': 'total_count'
    }

    def __init__(self, desktop_name_policy_infos=None, total_count=None):
        r"""ListDesktopNamePolicyResponse

        The model defined in huaweicloud sdk

        :param desktop_name_policy_infos: 桌面名称策略信息。
        :type desktop_name_policy_infos: list[:class:`huaweicloudsdkworkspace.v2.DesktopNamePolicyInfo`]
        :param total_count: 查询返回总条数。
        :type total_count: int
        """
        
        super(ListDesktopNamePolicyResponse, self).__init__()

        self._desktop_name_policy_infos = None
        self._total_count = None
        self.discriminator = None

        if desktop_name_policy_infos is not None:
            self.desktop_name_policy_infos = desktop_name_policy_infos
        if total_count is not None:
            self.total_count = total_count

    @property
    def desktop_name_policy_infos(self):
        r"""Gets the desktop_name_policy_infos of this ListDesktopNamePolicyResponse.

        桌面名称策略信息。

        :return: The desktop_name_policy_infos of this ListDesktopNamePolicyResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.DesktopNamePolicyInfo`]
        """
        return self._desktop_name_policy_infos

    @desktop_name_policy_infos.setter
    def desktop_name_policy_infos(self, desktop_name_policy_infos):
        r"""Sets the desktop_name_policy_infos of this ListDesktopNamePolicyResponse.

        桌面名称策略信息。

        :param desktop_name_policy_infos: The desktop_name_policy_infos of this ListDesktopNamePolicyResponse.
        :type desktop_name_policy_infos: list[:class:`huaweicloudsdkworkspace.v2.DesktopNamePolicyInfo`]
        """
        self._desktop_name_policy_infos = desktop_name_policy_infos

    @property
    def total_count(self):
        r"""Gets the total_count of this ListDesktopNamePolicyResponse.

        查询返回总条数。

        :return: The total_count of this ListDesktopNamePolicyResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListDesktopNamePolicyResponse.

        查询返回总条数。

        :param total_count: The total_count of this ListDesktopNamePolicyResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListDesktopNamePolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
