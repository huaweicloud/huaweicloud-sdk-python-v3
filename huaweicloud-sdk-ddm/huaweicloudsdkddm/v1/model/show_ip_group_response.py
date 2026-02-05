# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIpGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'group_id': 'str',
        'enable_ipgroup': 'bool',
        'type': 'str',
        'ipgroup': 'object'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'group_id': 'group_id',
        'enable_ipgroup': 'enable_ipgroup',
        'type': 'type',
        'ipgroup': 'ipgroup'
    }

    def __init__(self, instance_id=None, group_id=None, enable_ipgroup=None, type=None, ipgroup=None):
        r"""ShowIpGroupResponse

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**：  实例ID，此参数是实例的唯一标识。  **参数范围**：  只能由英文字母、数字组成，后缀为in09，长度为36个字符。
        :type instance_id: str
        :param group_id: **参数解释**：  组ID。此参数是参数组的唯一标识。  **参数范围**：  只能由英文字母、数字组成。
        :type group_id: str
        :param enable_ipgroup: **参数解释**：  是否开启弹性负载均衡ip组。  **参数范围**：  只能由英文字母、数字组成。
        :type enable_ipgroup: bool
        :param type: **参数解释**：  弹性负载均衡ip组类型。  **参数范围**：  只能由英文字母、数字组成。
        :type type: str
        :param ipgroup: **参数解释**：  ip组信息。  **参数范围**：  只能由英文字母、数字组成。
        :type ipgroup: object
        """
        
        super().__init__()

        self._instance_id = None
        self._group_id = None
        self._enable_ipgroup = None
        self._type = None
        self._ipgroup = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if group_id is not None:
            self.group_id = group_id
        if enable_ipgroup is not None:
            self.enable_ipgroup = enable_ipgroup
        if type is not None:
            self.type = type
        if ipgroup is not None:
            self.ipgroup = ipgroup

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowIpGroupResponse.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  **参数范围**：  只能由英文字母、数字组成，后缀为in09，长度为36个字符。

        :return: The instance_id of this ShowIpGroupResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowIpGroupResponse.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  **参数范围**：  只能由英文字母、数字组成，后缀为in09，长度为36个字符。

        :param instance_id: The instance_id of this ShowIpGroupResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def group_id(self):
        r"""Gets the group_id of this ShowIpGroupResponse.

        **参数解释**：  组ID。此参数是参数组的唯一标识。  **参数范围**：  只能由英文字母、数字组成。

        :return: The group_id of this ShowIpGroupResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ShowIpGroupResponse.

        **参数解释**：  组ID。此参数是参数组的唯一标识。  **参数范围**：  只能由英文字母、数字组成。

        :param group_id: The group_id of this ShowIpGroupResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def enable_ipgroup(self):
        r"""Gets the enable_ipgroup of this ShowIpGroupResponse.

        **参数解释**：  是否开启弹性负载均衡ip组。  **参数范围**：  只能由英文字母、数字组成。

        :return: The enable_ipgroup of this ShowIpGroupResponse.
        :rtype: bool
        """
        return self._enable_ipgroup

    @enable_ipgroup.setter
    def enable_ipgroup(self, enable_ipgroup):
        r"""Sets the enable_ipgroup of this ShowIpGroupResponse.

        **参数解释**：  是否开启弹性负载均衡ip组。  **参数范围**：  只能由英文字母、数字组成。

        :param enable_ipgroup: The enable_ipgroup of this ShowIpGroupResponse.
        :type enable_ipgroup: bool
        """
        self._enable_ipgroup = enable_ipgroup

    @property
    def type(self):
        r"""Gets the type of this ShowIpGroupResponse.

        **参数解释**：  弹性负载均衡ip组类型。  **参数范围**：  只能由英文字母、数字组成。

        :return: The type of this ShowIpGroupResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowIpGroupResponse.

        **参数解释**：  弹性负载均衡ip组类型。  **参数范围**：  只能由英文字母、数字组成。

        :param type: The type of this ShowIpGroupResponse.
        :type type: str
        """
        self._type = type

    @property
    def ipgroup(self):
        r"""Gets the ipgroup of this ShowIpGroupResponse.

        **参数解释**：  ip组信息。  **参数范围**：  只能由英文字母、数字组成。

        :return: The ipgroup of this ShowIpGroupResponse.
        :rtype: object
        """
        return self._ipgroup

    @ipgroup.setter
    def ipgroup(self, ipgroup):
        r"""Sets the ipgroup of this ShowIpGroupResponse.

        **参数解释**：  ip组信息。  **参数范围**：  只能由英文字母、数字组成。

        :param ipgroup: The ipgroup of this ShowIpGroupResponse.
        :type ipgroup: object
        """
        self._ipgroup = ipgroup

    def to_dict(self):
        import warnings
        warnings.warn("ShowIpGroupResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowIpGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
