# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnlargeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_id': 'str',
        'node_number': 'int',
        'group_id': 'str',
        'is_auto_pay': 'bool',
        'available_zones': 'list[str]'
    }

    attribute_map = {
        'flavor_id': 'flavor_id',
        'node_number': 'node_number',
        'group_id': 'group_id',
        'is_auto_pay': 'is_auto_pay',
        'available_zones': 'available_zones'
    }

    def __init__(self, flavor_id=None, node_number=None, group_id=None, is_auto_pay=None, available_zones=None):
        r"""EnlargeRequest

        The model defined in huaweicloud sdk

        :param flavor_id: 当前进行节点扩容的DDM实例底层虚机规格id
        :type flavor_id: str
        :param node_number: 需要扩容的节点个数
        :type node_number: int
        :param group_id: 组id，指定当前进行节点扩容的组。当实例的组&gt;1时，必填。
        :type group_id: str
        :param is_auto_pay: 变更包年包月实例规格时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。true，表示自动从账户中支付。false，表示手动从账户中支付，默认为该方式。
        :type is_auto_pay: bool
        :param available_zones: 可用区Code，仅包年包月实例传递该参数，个数需与node_number一致。请参见地区和终端节点(https://developer.huaweicloud.com/endpoint?DDM)。
        :type available_zones: list[str]
        """
        
        

        self._flavor_id = None
        self._node_number = None
        self._group_id = None
        self._is_auto_pay = None
        self._available_zones = None
        self.discriminator = None

        self.flavor_id = flavor_id
        self.node_number = node_number
        if group_id is not None:
            self.group_id = group_id
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if available_zones is not None:
            self.available_zones = available_zones

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this EnlargeRequest.

        当前进行节点扩容的DDM实例底层虚机规格id

        :return: The flavor_id of this EnlargeRequest.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this EnlargeRequest.

        当前进行节点扩容的DDM实例底层虚机规格id

        :param flavor_id: The flavor_id of this EnlargeRequest.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def node_number(self):
        r"""Gets the node_number of this EnlargeRequest.

        需要扩容的节点个数

        :return: The node_number of this EnlargeRequest.
        :rtype: int
        """
        return self._node_number

    @node_number.setter
    def node_number(self, node_number):
        r"""Sets the node_number of this EnlargeRequest.

        需要扩容的节点个数

        :param node_number: The node_number of this EnlargeRequest.
        :type node_number: int
        """
        self._node_number = node_number

    @property
    def group_id(self):
        r"""Gets the group_id of this EnlargeRequest.

        组id，指定当前进行节点扩容的组。当实例的组>1时，必填。

        :return: The group_id of this EnlargeRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this EnlargeRequest.

        组id，指定当前进行节点扩容的组。当实例的组>1时，必填。

        :param group_id: The group_id of this EnlargeRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this EnlargeRequest.

        变更包年包月实例规格时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。true，表示自动从账户中支付。false，表示手动从账户中支付，默认为该方式。

        :return: The is_auto_pay of this EnlargeRequest.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this EnlargeRequest.

        变更包年包月实例规格时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。true，表示自动从账户中支付。false，表示手动从账户中支付，默认为该方式。

        :param is_auto_pay: The is_auto_pay of this EnlargeRequest.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

    @property
    def available_zones(self):
        r"""Gets the available_zones of this EnlargeRequest.

        可用区Code，仅包年包月实例传递该参数，个数需与node_number一致。请参见地区和终端节点(https://developer.huaweicloud.com/endpoint?DDM)。

        :return: The available_zones of this EnlargeRequest.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this EnlargeRequest.

        可用区Code，仅包年包月实例传递该参数，个数需与node_number一致。请参见地区和终端节点(https://developer.huaweicloud.com/endpoint?DDM)。

        :param available_zones: The available_zones of this EnlargeRequest.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

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
        if not isinstance(other, EnlargeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
