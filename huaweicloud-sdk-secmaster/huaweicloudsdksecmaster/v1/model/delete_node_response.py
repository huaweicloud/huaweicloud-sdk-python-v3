# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteNodeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delete_fail_list': 'list[Node]',
        'delete_success_list': 'list[Node]'
    }

    attribute_map = {
        'delete_fail_list': 'delete_fail_list',
        'delete_success_list': 'delete_success_list'
    }

    def __init__(self, delete_fail_list=None, delete_success_list=None):
        r"""DeleteNodeResponse

        The model defined in huaweicloud sdk

        :param delete_fail_list: 删除失败列表
        :type delete_fail_list: list[:class:`huaweicloudsdksecmaster.v1.Node`]
        :param delete_success_list: 删除成功列表
        :type delete_success_list: list[:class:`huaweicloudsdksecmaster.v1.Node`]
        """
        
        super().__init__()

        self._delete_fail_list = None
        self._delete_success_list = None
        self.discriminator = None

        if delete_fail_list is not None:
            self.delete_fail_list = delete_fail_list
        if delete_success_list is not None:
            self.delete_success_list = delete_success_list

    @property
    def delete_fail_list(self):
        r"""Gets the delete_fail_list of this DeleteNodeResponse.

        删除失败列表

        :return: The delete_fail_list of this DeleteNodeResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.Node`]
        """
        return self._delete_fail_list

    @delete_fail_list.setter
    def delete_fail_list(self, delete_fail_list):
        r"""Sets the delete_fail_list of this DeleteNodeResponse.

        删除失败列表

        :param delete_fail_list: The delete_fail_list of this DeleteNodeResponse.
        :type delete_fail_list: list[:class:`huaweicloudsdksecmaster.v1.Node`]
        """
        self._delete_fail_list = delete_fail_list

    @property
    def delete_success_list(self):
        r"""Gets the delete_success_list of this DeleteNodeResponse.

        删除成功列表

        :return: The delete_success_list of this DeleteNodeResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.Node`]
        """
        return self._delete_success_list

    @delete_success_list.setter
    def delete_success_list(self, delete_success_list):
        r"""Sets the delete_success_list of this DeleteNodeResponse.

        删除成功列表

        :param delete_success_list: The delete_success_list of this DeleteNodeResponse.
        :type delete_success_list: list[:class:`huaweicloudsdksecmaster.v1.Node`]
        """
        self._delete_success_list = delete_success_list

    def to_dict(self):
        import warnings
        warnings.warn("DeleteNodeResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DeleteNodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
