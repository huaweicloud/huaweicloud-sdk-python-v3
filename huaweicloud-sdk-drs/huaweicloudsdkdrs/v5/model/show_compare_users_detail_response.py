# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCompareUsersDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'user_compare_info': 'list[CompareUserInfo]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'user_compare_info': 'user_compare_info'
    }

    def __init__(self, total_count=None, user_compare_info=None):
        r"""ShowCompareUsersDetailResponse

        The model defined in huaweicloud sdk

        :param total_count: 用户对比信息的总数
        :type total_count: int
        :param user_compare_info: 用户对比信息
        :type user_compare_info: list[:class:`huaweicloudsdkdrs.v5.CompareUserInfo`]
        """
        
        super().__init__()

        self._total_count = None
        self._user_compare_info = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if user_compare_info is not None:
            self.user_compare_info = user_compare_info

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowCompareUsersDetailResponse.

        用户对比信息的总数

        :return: The total_count of this ShowCompareUsersDetailResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowCompareUsersDetailResponse.

        用户对比信息的总数

        :param total_count: The total_count of this ShowCompareUsersDetailResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def user_compare_info(self):
        r"""Gets the user_compare_info of this ShowCompareUsersDetailResponse.

        用户对比信息

        :return: The user_compare_info of this ShowCompareUsersDetailResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.CompareUserInfo`]
        """
        return self._user_compare_info

    @user_compare_info.setter
    def user_compare_info(self, user_compare_info):
        r"""Sets the user_compare_info of this ShowCompareUsersDetailResponse.

        用户对比信息

        :param user_compare_info: The user_compare_info of this ShowCompareUsersDetailResponse.
        :type user_compare_info: list[:class:`huaweicloudsdkdrs.v5.CompareUserInfo`]
        """
        self._user_compare_info = user_compare_info

    def to_dict(self):
        import warnings
        warnings.warn("ShowCompareUsersDetailResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowCompareUsersDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
