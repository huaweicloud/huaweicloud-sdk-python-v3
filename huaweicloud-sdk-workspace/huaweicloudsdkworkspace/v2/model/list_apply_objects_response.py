# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplyObjectsResponse(SdkResponse):

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
        'apply_objects': 'list[ApplyObjectDetailInfo]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'apply_objects': 'apply_objects'
    }

    def __init__(self, total_count=None, apply_objects=None):
        r"""ListApplyObjectsResponse

        The model defined in huaweicloud sdk

        :param total_count: 总数量
        :type total_count: int
        :param apply_objects: 应用对象列表
        :type apply_objects: list[:class:`huaweicloudsdkworkspace.v2.ApplyObjectDetailInfo`]
        """
        
        super().__init__()

        self._total_count = None
        self._apply_objects = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if apply_objects is not None:
            self.apply_objects = apply_objects

    @property
    def total_count(self):
        r"""Gets the total_count of this ListApplyObjectsResponse.

        总数量

        :return: The total_count of this ListApplyObjectsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListApplyObjectsResponse.

        总数量

        :param total_count: The total_count of this ListApplyObjectsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def apply_objects(self):
        r"""Gets the apply_objects of this ListApplyObjectsResponse.

        应用对象列表

        :return: The apply_objects of this ListApplyObjectsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ApplyObjectDetailInfo`]
        """
        return self._apply_objects

    @apply_objects.setter
    def apply_objects(self, apply_objects):
        r"""Sets the apply_objects of this ListApplyObjectsResponse.

        应用对象列表

        :param apply_objects: The apply_objects of this ListApplyObjectsResponse.
        :type apply_objects: list[:class:`huaweicloudsdkworkspace.v2.ApplyObjectDetailInfo`]
        """
        self._apply_objects = apply_objects

    def to_dict(self):
        import warnings
        warnings.warn("ListApplyObjectsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListApplyObjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
