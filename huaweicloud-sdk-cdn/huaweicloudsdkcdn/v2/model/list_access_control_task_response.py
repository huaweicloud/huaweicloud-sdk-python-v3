# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccessControlTaskResponse(SdkResponse):

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
        'access_control_tasks': 'list[AccessControlTask]'
    }

    attribute_map = {
        'total': 'total',
        'access_control_tasks': 'access_control_tasks'
    }

    def __init__(self, total=None, access_control_tasks=None):
        r"""ListAccessControlTaskResponse

        The model defined in huaweicloud sdk

        :param total: 查询结果总数。
        :type total: int
        :param access_control_tasks: 封禁或解禁URL任务信息。
        :type access_control_tasks: list[:class:`huaweicloudsdkcdn.v2.AccessControlTask`]
        """
        
        super().__init__()

        self._total = None
        self._access_control_tasks = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if access_control_tasks is not None:
            self.access_control_tasks = access_control_tasks

    @property
    def total(self):
        r"""Gets the total of this ListAccessControlTaskResponse.

        查询结果总数。

        :return: The total of this ListAccessControlTaskResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListAccessControlTaskResponse.

        查询结果总数。

        :param total: The total of this ListAccessControlTaskResponse.
        :type total: int
        """
        self._total = total

    @property
    def access_control_tasks(self):
        r"""Gets the access_control_tasks of this ListAccessControlTaskResponse.

        封禁或解禁URL任务信息。

        :return: The access_control_tasks of this ListAccessControlTaskResponse.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.AccessControlTask`]
        """
        return self._access_control_tasks

    @access_control_tasks.setter
    def access_control_tasks(self, access_control_tasks):
        r"""Sets the access_control_tasks of this ListAccessControlTaskResponse.

        封禁或解禁URL任务信息。

        :param access_control_tasks: The access_control_tasks of this ListAccessControlTaskResponse.
        :type access_control_tasks: list[:class:`huaweicloudsdkcdn.v2.AccessControlTask`]
        """
        self._access_control_tasks = access_control_tasks

    def to_dict(self):
        import warnings
        warnings.warn("ListAccessControlTaskResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAccessControlTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
