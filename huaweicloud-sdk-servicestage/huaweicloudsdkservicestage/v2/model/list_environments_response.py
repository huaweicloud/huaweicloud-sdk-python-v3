# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnvironmentsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'environments': 'list[Environment]'
    }

    attribute_map = {
        'count': 'count',
        'environments': 'environments'
    }

    def __init__(self, count=None, environments=None):
        r"""ListEnvironmentsResponse

        The model defined in huaweicloud sdk

        :param count: 环境总数。
        :type count: int
        :param environments: 环境列表。
        :type environments: list[:class:`huaweicloudsdkservicestage.v2.Environment`]
        """
        
        super().__init__()

        self._count = None
        self._environments = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if environments is not None:
            self.environments = environments

    @property
    def count(self):
        r"""Gets the count of this ListEnvironmentsResponse.

        环境总数。

        :return: The count of this ListEnvironmentsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListEnvironmentsResponse.

        环境总数。

        :param count: The count of this ListEnvironmentsResponse.
        :type count: int
        """
        self._count = count

    @property
    def environments(self):
        r"""Gets the environments of this ListEnvironmentsResponse.

        环境列表。

        :return: The environments of this ListEnvironmentsResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.Environment`]
        """
        return self._environments

    @environments.setter
    def environments(self, environments):
        r"""Sets the environments of this ListEnvironmentsResponse.

        环境列表。

        :param environments: The environments of this ListEnvironmentsResponse.
        :type environments: list[:class:`huaweicloudsdkservicestage.v2.Environment`]
        """
        self._environments = environments

    def to_dict(self):
        import warnings
        warnings.warn("ListEnvironmentsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListEnvironmentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
