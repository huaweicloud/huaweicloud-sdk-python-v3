# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoveModelConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deleted_count': 'int',
        'failed_count': 'int',
        'failed_details': 'list[ModelConfigFailedItem]'
    }

    attribute_map = {
        'deleted_count': 'deleted_count',
        'failed_count': 'failed_count',
        'failed_details': 'failed_details'
    }

    def __init__(self, deleted_count=None, failed_count=None, failed_details=None):
        r"""RemoveModelConfigResponse

        The model defined in huaweicloud sdk

        :param deleted_count: 删除数量。
        :type deleted_count: int
        :param failed_count: 失败数量。
        :type failed_count: int
        :param failed_details: 失败详情列表。
        :type failed_details: list[:class:`huaweicloudsdkworkspace.v2.ModelConfigFailedItem`]
        """
        
        super().__init__()

        self._deleted_count = None
        self._failed_count = None
        self._failed_details = None
        self.discriminator = None

        if deleted_count is not None:
            self.deleted_count = deleted_count
        if failed_count is not None:
            self.failed_count = failed_count
        if failed_details is not None:
            self.failed_details = failed_details

    @property
    def deleted_count(self):
        r"""Gets the deleted_count of this RemoveModelConfigResponse.

        删除数量。

        :return: The deleted_count of this RemoveModelConfigResponse.
        :rtype: int
        """
        return self._deleted_count

    @deleted_count.setter
    def deleted_count(self, deleted_count):
        r"""Sets the deleted_count of this RemoveModelConfigResponse.

        删除数量。

        :param deleted_count: The deleted_count of this RemoveModelConfigResponse.
        :type deleted_count: int
        """
        self._deleted_count = deleted_count

    @property
    def failed_count(self):
        r"""Gets the failed_count of this RemoveModelConfigResponse.

        失败数量。

        :return: The failed_count of this RemoveModelConfigResponse.
        :rtype: int
        """
        return self._failed_count

    @failed_count.setter
    def failed_count(self, failed_count):
        r"""Sets the failed_count of this RemoveModelConfigResponse.

        失败数量。

        :param failed_count: The failed_count of this RemoveModelConfigResponse.
        :type failed_count: int
        """
        self._failed_count = failed_count

    @property
    def failed_details(self):
        r"""Gets the failed_details of this RemoveModelConfigResponse.

        失败详情列表。

        :return: The failed_details of this RemoveModelConfigResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ModelConfigFailedItem`]
        """
        return self._failed_details

    @failed_details.setter
    def failed_details(self, failed_details):
        r"""Sets the failed_details of this RemoveModelConfigResponse.

        失败详情列表。

        :param failed_details: The failed_details of this RemoveModelConfigResponse.
        :type failed_details: list[:class:`huaweicloudsdkworkspace.v2.ModelConfigFailedItem`]
        """
        self._failed_details = failed_details

    def to_dict(self):
        import warnings
        warnings.warn("RemoveModelConfigResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, RemoveModelConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
