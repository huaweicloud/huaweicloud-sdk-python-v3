# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddInstanceToGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'bool',
        'success_instance_ids': 'list[str]',
        'failed_instance_ids': 'list[str]'
    }

    attribute_map = {
        'success': 'success',
        'success_instance_ids': 'success_instance_ids',
        'failed_instance_ids': 'failed_instance_ids'
    }

    def __init__(self, success=None, success_instance_ids=None, failed_instance_ids=None):
        r"""AddInstanceToGroupResponse

        The model defined in huaweicloud sdk

        :param success: 是否成功
        :type success: bool
        :param success_instance_ids: 成功的实例ID列表
        :type success_instance_ids: list[str]
        :param failed_instance_ids: 失败的实例ID列表
        :type failed_instance_ids: list[str]
        """
        
        super().__init__()

        self._success = None
        self._success_instance_ids = None
        self._failed_instance_ids = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if success_instance_ids is not None:
            self.success_instance_ids = success_instance_ids
        if failed_instance_ids is not None:
            self.failed_instance_ids = failed_instance_ids

    @property
    def success(self):
        r"""Gets the success of this AddInstanceToGroupResponse.

        是否成功

        :return: The success of this AddInstanceToGroupResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this AddInstanceToGroupResponse.

        是否成功

        :param success: The success of this AddInstanceToGroupResponse.
        :type success: bool
        """
        self._success = success

    @property
    def success_instance_ids(self):
        r"""Gets the success_instance_ids of this AddInstanceToGroupResponse.

        成功的实例ID列表

        :return: The success_instance_ids of this AddInstanceToGroupResponse.
        :rtype: list[str]
        """
        return self._success_instance_ids

    @success_instance_ids.setter
    def success_instance_ids(self, success_instance_ids):
        r"""Sets the success_instance_ids of this AddInstanceToGroupResponse.

        成功的实例ID列表

        :param success_instance_ids: The success_instance_ids of this AddInstanceToGroupResponse.
        :type success_instance_ids: list[str]
        """
        self._success_instance_ids = success_instance_ids

    @property
    def failed_instance_ids(self):
        r"""Gets the failed_instance_ids of this AddInstanceToGroupResponse.

        失败的实例ID列表

        :return: The failed_instance_ids of this AddInstanceToGroupResponse.
        :rtype: list[str]
        """
        return self._failed_instance_ids

    @failed_instance_ids.setter
    def failed_instance_ids(self, failed_instance_ids):
        r"""Sets the failed_instance_ids of this AddInstanceToGroupResponse.

        失败的实例ID列表

        :param failed_instance_ids: The failed_instance_ids of this AddInstanceToGroupResponse.
        :type failed_instance_ids: list[str]
        """
        self._failed_instance_ids = failed_instance_ids

    def to_dict(self):
        import warnings
        warnings.warn("AddInstanceToGroupResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, AddInstanceToGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
