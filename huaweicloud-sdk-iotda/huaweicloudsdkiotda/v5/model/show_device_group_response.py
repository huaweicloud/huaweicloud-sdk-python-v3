# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeviceGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'name': 'str',
        'description': 'str',
        'super_group_id': 'str',
        'group_type': 'str',
        'dynamic_group_rule': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'name': 'name',
        'description': 'description',
        'super_group_id': 'super_group_id',
        'group_type': 'group_type',
        'dynamic_group_rule': 'dynamic_group_rule'
    }

    def __init__(self, group_id=None, name=None, description=None, super_group_id=None, group_type=None, dynamic_group_rule=None):
        r"""ShowDeviceGroupResponse

        The model defined in huaweicloud sdk

        :param group_id: 设备组ID，用于唯一标识一个设备组，在创建设备组时由物联网平台分配。
        :type group_id: str
        :param name: 设备组名称，单个资源空间下不可重复。
        :type name: str
        :param description: 设备组描述。
        :type description: str
        :param super_group_id: 父设备组ID，该设备组的父设备组ID。
        :type super_group_id: str
        :param group_type: 设备组类型，分为动态设备组和静态设备组两种
        :type group_type: str
        :param dynamic_group_rule: 动态设备组规则
        :type dynamic_group_rule: str
        """
        
        super(ShowDeviceGroupResponse, self).__init__()

        self._group_id = None
        self._name = None
        self._description = None
        self._super_group_id = None
        self._group_type = None
        self._dynamic_group_rule = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if super_group_id is not None:
            self.super_group_id = super_group_id
        if group_type is not None:
            self.group_type = group_type
        if dynamic_group_rule is not None:
            self.dynamic_group_rule = dynamic_group_rule

    @property
    def group_id(self):
        r"""Gets the group_id of this ShowDeviceGroupResponse.

        设备组ID，用于唯一标识一个设备组，在创建设备组时由物联网平台分配。

        :return: The group_id of this ShowDeviceGroupResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ShowDeviceGroupResponse.

        设备组ID，用于唯一标识一个设备组，在创建设备组时由物联网平台分配。

        :param group_id: The group_id of this ShowDeviceGroupResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def name(self):
        r"""Gets the name of this ShowDeviceGroupResponse.

        设备组名称，单个资源空间下不可重复。

        :return: The name of this ShowDeviceGroupResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowDeviceGroupResponse.

        设备组名称，单个资源空间下不可重复。

        :param name: The name of this ShowDeviceGroupResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowDeviceGroupResponse.

        设备组描述。

        :return: The description of this ShowDeviceGroupResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowDeviceGroupResponse.

        设备组描述。

        :param description: The description of this ShowDeviceGroupResponse.
        :type description: str
        """
        self._description = description

    @property
    def super_group_id(self):
        r"""Gets the super_group_id of this ShowDeviceGroupResponse.

        父设备组ID，该设备组的父设备组ID。

        :return: The super_group_id of this ShowDeviceGroupResponse.
        :rtype: str
        """
        return self._super_group_id

    @super_group_id.setter
    def super_group_id(self, super_group_id):
        r"""Sets the super_group_id of this ShowDeviceGroupResponse.

        父设备组ID，该设备组的父设备组ID。

        :param super_group_id: The super_group_id of this ShowDeviceGroupResponse.
        :type super_group_id: str
        """
        self._super_group_id = super_group_id

    @property
    def group_type(self):
        r"""Gets the group_type of this ShowDeviceGroupResponse.

        设备组类型，分为动态设备组和静态设备组两种

        :return: The group_type of this ShowDeviceGroupResponse.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        r"""Sets the group_type of this ShowDeviceGroupResponse.

        设备组类型，分为动态设备组和静态设备组两种

        :param group_type: The group_type of this ShowDeviceGroupResponse.
        :type group_type: str
        """
        self._group_type = group_type

    @property
    def dynamic_group_rule(self):
        r"""Gets the dynamic_group_rule of this ShowDeviceGroupResponse.

        动态设备组规则

        :return: The dynamic_group_rule of this ShowDeviceGroupResponse.
        :rtype: str
        """
        return self._dynamic_group_rule

    @dynamic_group_rule.setter
    def dynamic_group_rule(self, dynamic_group_rule):
        r"""Sets the dynamic_group_rule of this ShowDeviceGroupResponse.

        动态设备组规则

        :param dynamic_group_rule: The dynamic_group_rule of this ShowDeviceGroupResponse.
        :type dynamic_group_rule: str
        """
        self._dynamic_group_rule = dynamic_group_rule

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowDeviceGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
