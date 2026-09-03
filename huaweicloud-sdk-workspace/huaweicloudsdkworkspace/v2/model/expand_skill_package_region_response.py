# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExpandSkillPackageRegionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'success_count': 'int',
        'failed_count': 'int',
        'failed_details': 'list[RegionFailedDetail]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'total': 'total',
        'success_count': 'success_count',
        'failed_count': 'failed_count',
        'failed_details': 'failed_details',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, total=None, success_count=None, failed_count=None, failed_details=None, x_request_id=None):
        r"""ExpandSkillPackageRegionResponse

        The model defined in huaweicloud sdk

        :param total: 请求总数。
        :type total: int
        :param success_count: 成功数量。
        :type success_count: int
        :param failed_count: 失败数量。
        :type failed_count: int
        :param failed_details: 失败详情列表。
        :type failed_details: list[:class:`huaweicloudsdkworkspace.v2.RegionFailedDetail`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._total = None
        self._success_count = None
        self._failed_count = None
        self._failed_details = None
        self._x_request_id = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if success_count is not None:
            self.success_count = success_count
        if failed_count is not None:
            self.failed_count = failed_count
        if failed_details is not None:
            self.failed_details = failed_details
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def total(self):
        r"""Gets the total of this ExpandSkillPackageRegionResponse.

        请求总数。

        :return: The total of this ExpandSkillPackageRegionResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ExpandSkillPackageRegionResponse.

        请求总数。

        :param total: The total of this ExpandSkillPackageRegionResponse.
        :type total: int
        """
        self._total = total

    @property
    def success_count(self):
        r"""Gets the success_count of this ExpandSkillPackageRegionResponse.

        成功数量。

        :return: The success_count of this ExpandSkillPackageRegionResponse.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        r"""Sets the success_count of this ExpandSkillPackageRegionResponse.

        成功数量。

        :param success_count: The success_count of this ExpandSkillPackageRegionResponse.
        :type success_count: int
        """
        self._success_count = success_count

    @property
    def failed_count(self):
        r"""Gets the failed_count of this ExpandSkillPackageRegionResponse.

        失败数量。

        :return: The failed_count of this ExpandSkillPackageRegionResponse.
        :rtype: int
        """
        return self._failed_count

    @failed_count.setter
    def failed_count(self, failed_count):
        r"""Sets the failed_count of this ExpandSkillPackageRegionResponse.

        失败数量。

        :param failed_count: The failed_count of this ExpandSkillPackageRegionResponse.
        :type failed_count: int
        """
        self._failed_count = failed_count

    @property
    def failed_details(self):
        r"""Gets the failed_details of this ExpandSkillPackageRegionResponse.

        失败详情列表。

        :return: The failed_details of this ExpandSkillPackageRegionResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.RegionFailedDetail`]
        """
        return self._failed_details

    @failed_details.setter
    def failed_details(self, failed_details):
        r"""Sets the failed_details of this ExpandSkillPackageRegionResponse.

        失败详情列表。

        :param failed_details: The failed_details of this ExpandSkillPackageRegionResponse.
        :type failed_details: list[:class:`huaweicloudsdkworkspace.v2.RegionFailedDetail`]
        """
        self._failed_details = failed_details

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ExpandSkillPackageRegionResponse.

        :return: The x_request_id of this ExpandSkillPackageRegionResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ExpandSkillPackageRegionResponse.

        :param x_request_id: The x_request_id of this ExpandSkillPackageRegionResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ExpandSkillPackageRegionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ExpandSkillPackageRegionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
