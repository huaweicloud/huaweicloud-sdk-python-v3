# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceGroupResponse(SdkResponse):

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
        'instance_group_list': 'list[InstanceGroup]'
    }

    attribute_map = {
        'total': 'total',
        'instance_group_list': 'instance_group_list'
    }

    def __init__(self, total=None, instance_group_list=None):
        r"""ListInstanceGroupResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param instance_group_list: 实例组列表
        :type instance_group_list: list[:class:`huaweicloudsdkdas.v3.InstanceGroup`]
        """
        
        super().__init__()

        self._total = None
        self._instance_group_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if instance_group_list is not None:
            self.instance_group_list = instance_group_list

    @property
    def total(self):
        r"""Gets the total of this ListInstanceGroupResponse.

        总数

        :return: The total of this ListInstanceGroupResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInstanceGroupResponse.

        总数

        :param total: The total of this ListInstanceGroupResponse.
        :type total: int
        """
        self._total = total

    @property
    def instance_group_list(self):
        r"""Gets the instance_group_list of this ListInstanceGroupResponse.

        实例组列表

        :return: The instance_group_list of this ListInstanceGroupResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.InstanceGroup`]
        """
        return self._instance_group_list

    @instance_group_list.setter
    def instance_group_list(self, instance_group_list):
        r"""Sets the instance_group_list of this ListInstanceGroupResponse.

        实例组列表

        :param instance_group_list: The instance_group_list of this ListInstanceGroupResponse.
        :type instance_group_list: list[:class:`huaweicloudsdkdas.v3.InstanceGroup`]
        """
        self._instance_group_list = instance_group_list

    def to_dict(self):
        import warnings
        warnings.warn("ListInstanceGroupResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListInstanceGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
