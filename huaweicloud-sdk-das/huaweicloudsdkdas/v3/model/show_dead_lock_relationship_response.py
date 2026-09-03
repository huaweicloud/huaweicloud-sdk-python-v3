# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeadLockRelationshipResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'process_list': 'list[DeadLockProcess]',
        'resource_list': 'list[DeadLockResource]'
    }

    attribute_map = {
        'process_list': 'process_list',
        'resource_list': 'resource_list'
    }

    def __init__(self, process_list=None, resource_list=None):
        r"""ShowDeadLockRelationshipResponse

        The model defined in huaweicloud sdk

        :param process_list: 会话列表
        :type process_list: list[:class:`huaweicloudsdkdas.v3.DeadLockProcess`]
        :param resource_list: 资源列表
        :type resource_list: list[:class:`huaweicloudsdkdas.v3.DeadLockResource`]
        """
        
        super().__init__()

        self._process_list = None
        self._resource_list = None
        self.discriminator = None

        if process_list is not None:
            self.process_list = process_list
        if resource_list is not None:
            self.resource_list = resource_list

    @property
    def process_list(self):
        r"""Gets the process_list of this ShowDeadLockRelationshipResponse.

        会话列表

        :return: The process_list of this ShowDeadLockRelationshipResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.DeadLockProcess`]
        """
        return self._process_list

    @process_list.setter
    def process_list(self, process_list):
        r"""Sets the process_list of this ShowDeadLockRelationshipResponse.

        会话列表

        :param process_list: The process_list of this ShowDeadLockRelationshipResponse.
        :type process_list: list[:class:`huaweicloudsdkdas.v3.DeadLockProcess`]
        """
        self._process_list = process_list

    @property
    def resource_list(self):
        r"""Gets the resource_list of this ShowDeadLockRelationshipResponse.

        资源列表

        :return: The resource_list of this ShowDeadLockRelationshipResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.DeadLockResource`]
        """
        return self._resource_list

    @resource_list.setter
    def resource_list(self, resource_list):
        r"""Sets the resource_list of this ShowDeadLockRelationshipResponse.

        资源列表

        :param resource_list: The resource_list of this ShowDeadLockRelationshipResponse.
        :type resource_list: list[:class:`huaweicloudsdkdas.v3.DeadLockResource`]
        """
        self._resource_list = resource_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowDeadLockRelationshipResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowDeadLockRelationshipResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
