# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckResourceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'instance_num': 'int',
        'mode': 'str',
        'availability_zone_mode': 'str',
        'node_num': 'int',
        'flavor_ref': 'str',
        'availability_zone': 'str',
        'subnet_id': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'instance_num': 'instance_num',
        'mode': 'mode',
        'availability_zone_mode': 'availability_zone_mode',
        'node_num': 'node_num',
        'flavor_ref': 'flavor_ref',
        'availability_zone': 'availability_zone',
        'subnet_id': 'subnet_id',
        'instance_id': 'instance_id'
    }

    def __init__(self, enterprise_project_id=None, instance_num=None, mode=None, availability_zone_mode=None, node_num=None, flavor_ref=None, availability_zone=None, subnet_id=None, instance_id=None):
        r"""CheckResourceInfo

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID。action为createInstance时必填。
        :type enterprise_project_id: str
        :param instance_num: 实例数量。action为createInstance时必填。
        :type instance_num: int
        :param mode: 实例类型，目前仅支持Cluster。action为createInstance时必填。
        :type mode: str
        :param availability_zone_mode: 可用区类型，单可用区single或多可用区multi。action为createInstance时必填。
        :type availability_zone_mode: str
        :param node_num: 节点数量。action为createInstance、createReadonlyNode时必填。
        :type node_num: int
        :param flavor_ref: 规格码。action为createInstance、resizeFlavor时必填。
        :type flavor_ref: str
        :param availability_zone: 可用区码。
        :type availability_zone: str
        :param subnet_id: 子网ID。action为createInstance时必填。
        :type subnet_id: str
        :param instance_id: 实例ID。action为createReadonlyNode、resizeFlavor时必填。
        :type instance_id: str
        """
        
        

        self._enterprise_project_id = None
        self._instance_num = None
        self._mode = None
        self._availability_zone_mode = None
        self._node_num = None
        self._flavor_ref = None
        self._availability_zone = None
        self._subnet_id = None
        self._instance_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if instance_num is not None:
            self.instance_num = instance_num
        if mode is not None:
            self.mode = mode
        if availability_zone_mode is not None:
            self.availability_zone_mode = availability_zone_mode
        if node_num is not None:
            self.node_num = node_num
        if flavor_ref is not None:
            self.flavor_ref = flavor_ref
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CheckResourceInfo.

        企业项目ID。action为createInstance时必填。

        :return: The enterprise_project_id of this CheckResourceInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CheckResourceInfo.

        企业项目ID。action为createInstance时必填。

        :param enterprise_project_id: The enterprise_project_id of this CheckResourceInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def instance_num(self):
        r"""Gets the instance_num of this CheckResourceInfo.

        实例数量。action为createInstance时必填。

        :return: The instance_num of this CheckResourceInfo.
        :rtype: int
        """
        return self._instance_num

    @instance_num.setter
    def instance_num(self, instance_num):
        r"""Sets the instance_num of this CheckResourceInfo.

        实例数量。action为createInstance时必填。

        :param instance_num: The instance_num of this CheckResourceInfo.
        :type instance_num: int
        """
        self._instance_num = instance_num

    @property
    def mode(self):
        r"""Gets the mode of this CheckResourceInfo.

        实例类型，目前仅支持Cluster。action为createInstance时必填。

        :return: The mode of this CheckResourceInfo.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this CheckResourceInfo.

        实例类型，目前仅支持Cluster。action为createInstance时必填。

        :param mode: The mode of this CheckResourceInfo.
        :type mode: str
        """
        self._mode = mode

    @property
    def availability_zone_mode(self):
        r"""Gets the availability_zone_mode of this CheckResourceInfo.

        可用区类型，单可用区single或多可用区multi。action为createInstance时必填。

        :return: The availability_zone_mode of this CheckResourceInfo.
        :rtype: str
        """
        return self._availability_zone_mode

    @availability_zone_mode.setter
    def availability_zone_mode(self, availability_zone_mode):
        r"""Sets the availability_zone_mode of this CheckResourceInfo.

        可用区类型，单可用区single或多可用区multi。action为createInstance时必填。

        :param availability_zone_mode: The availability_zone_mode of this CheckResourceInfo.
        :type availability_zone_mode: str
        """
        self._availability_zone_mode = availability_zone_mode

    @property
    def node_num(self):
        r"""Gets the node_num of this CheckResourceInfo.

        节点数量。action为createInstance、createReadonlyNode时必填。

        :return: The node_num of this CheckResourceInfo.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this CheckResourceInfo.

        节点数量。action为createInstance、createReadonlyNode时必填。

        :param node_num: The node_num of this CheckResourceInfo.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this CheckResourceInfo.

        规格码。action为createInstance、resizeFlavor时必填。

        :return: The flavor_ref of this CheckResourceInfo.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this CheckResourceInfo.

        规格码。action为createInstance、resizeFlavor时必填。

        :param flavor_ref: The flavor_ref of this CheckResourceInfo.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this CheckResourceInfo.

        可用区码。

        :return: The availability_zone of this CheckResourceInfo.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this CheckResourceInfo.

        可用区码。

        :param availability_zone: The availability_zone of this CheckResourceInfo.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CheckResourceInfo.

        子网ID。action为createInstance时必填。

        :return: The subnet_id of this CheckResourceInfo.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CheckResourceInfo.

        子网ID。action为createInstance时必填。

        :param subnet_id: The subnet_id of this CheckResourceInfo.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this CheckResourceInfo.

        实例ID。action为createReadonlyNode、resizeFlavor时必填。

        :return: The instance_id of this CheckResourceInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this CheckResourceInfo.

        实例ID。action为createReadonlyNode、resizeFlavor时必填。

        :param instance_id: The instance_id of this CheckResourceInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, CheckResourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
