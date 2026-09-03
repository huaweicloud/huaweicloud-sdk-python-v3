# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserInstanceListResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'das_instances': 'list[DASUserInstanceInfo]',
        'total': 'int'
    }

    attribute_map = {
        'das_instances': 'das_instances',
        'total': 'total'
    }

    def __init__(self, das_instances=None, total=None):
        r"""ListUserInstanceListResponse

        The model defined in huaweicloud sdk

        :param das_instances: 实例列表
        :type das_instances: list[:class:`huaweicloudsdkdas.v3.DASUserInstanceInfo`]
        :param total: 总数
        :type total: int
        """
        
        super().__init__()

        self._das_instances = None
        self._total = None
        self.discriminator = None

        if das_instances is not None:
            self.das_instances = das_instances
        if total is not None:
            self.total = total

    @property
    def das_instances(self):
        r"""Gets the das_instances of this ListUserInstanceListResponse.

        实例列表

        :return: The das_instances of this ListUserInstanceListResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.DASUserInstanceInfo`]
        """
        return self._das_instances

    @das_instances.setter
    def das_instances(self, das_instances):
        r"""Sets the das_instances of this ListUserInstanceListResponse.

        实例列表

        :param das_instances: The das_instances of this ListUserInstanceListResponse.
        :type das_instances: list[:class:`huaweicloudsdkdas.v3.DASUserInstanceInfo`]
        """
        self._das_instances = das_instances

    @property
    def total(self):
        r"""Gets the total of this ListUserInstanceListResponse.

        总数

        :return: The total of this ListUserInstanceListResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListUserInstanceListResponse.

        总数

        :param total: The total of this ListUserInstanceListResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListUserInstanceListResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListUserInstanceListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
