# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterRolesBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_ref': 'str',
        'volume': 'CreateClusterInstanceVolumeBody',
        'type': 'str',
        'instance_num': 'int'
    }

    attribute_map = {
        'flavor_ref': 'flavorRef',
        'volume': 'volume',
        'type': 'type',
        'instance_num': 'instanceNum'
    }

    def __init__(self, flavor_ref=None, volume=None, type=None, instance_num=None):
        """CreateClusterRolesBody

        The model defined in huaweicloud sdk

        :param flavor_ref: 实例规格名称。可以使用[获取实例规格列表](ListFlavors.xml)的name属性确认当前拥有的规格信息。
        :type flavor_ref: str
        :param volume: 
        :type volume: :class:`huaweicloudsdkcss.v2.CreateClusterInstanceVolumeBody`
        :param type: 实例类型(选择实例类型时应至少选择一个ess类型)。例如，  - ess-master对应Master节点。 - ess-client对应clinet节点。 - ess-cold对应冷数据节点。 - ess对应数据节点。
        :type type: str
        :param instance_num: 实例个数。 - ess节点，选择范围：1~32个节点数量。   - 若同时选择ess和ess-master时，可以选择1~200个节点数量。    - 若同时选择ess和ess-client时，可以选择1~32个节点数量。    - 若同时选择ess和ess-cold时，可以选择1~32个节点数量。 - ess-master节点，选择范围：3~10内的奇数个节点数量。 - ess-client节点，选择范围：1~32个节点数量。 - ess-cold节点，选择范围：1~32个节点数量。
        :type instance_num: int
        """
        
        

        self._flavor_ref = None
        self._volume = None
        self._type = None
        self._instance_num = None
        self.discriminator = None

        self.flavor_ref = flavor_ref
        self.volume = volume
        self.type = type
        self.instance_num = instance_num

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this CreateClusterRolesBody.

        实例规格名称。可以使用[获取实例规格列表](ListFlavors.xml)的name属性确认当前拥有的规格信息。

        :return: The flavor_ref of this CreateClusterRolesBody.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this CreateClusterRolesBody.

        实例规格名称。可以使用[获取实例规格列表](ListFlavors.xml)的name属性确认当前拥有的规格信息。

        :param flavor_ref: The flavor_ref of this CreateClusterRolesBody.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def volume(self):
        """Gets the volume of this CreateClusterRolesBody.

        :return: The volume of this CreateClusterRolesBody.
        :rtype: :class:`huaweicloudsdkcss.v2.CreateClusterInstanceVolumeBody`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this CreateClusterRolesBody.

        :param volume: The volume of this CreateClusterRolesBody.
        :type volume: :class:`huaweicloudsdkcss.v2.CreateClusterInstanceVolumeBody`
        """
        self._volume = volume

    @property
    def type(self):
        """Gets the type of this CreateClusterRolesBody.

        实例类型(选择实例类型时应至少选择一个ess类型)。例如，  - ess-master对应Master节点。 - ess-client对应clinet节点。 - ess-cold对应冷数据节点。 - ess对应数据节点。

        :return: The type of this CreateClusterRolesBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateClusterRolesBody.

        实例类型(选择实例类型时应至少选择一个ess类型)。例如，  - ess-master对应Master节点。 - ess-client对应clinet节点。 - ess-cold对应冷数据节点。 - ess对应数据节点。

        :param type: The type of this CreateClusterRolesBody.
        :type type: str
        """
        self._type = type

    @property
    def instance_num(self):
        """Gets the instance_num of this CreateClusterRolesBody.

        实例个数。 - ess节点，选择范围：1~32个节点数量。   - 若同时选择ess和ess-master时，可以选择1~200个节点数量。    - 若同时选择ess和ess-client时，可以选择1~32个节点数量。    - 若同时选择ess和ess-cold时，可以选择1~32个节点数量。 - ess-master节点，选择范围：3~10内的奇数个节点数量。 - ess-client节点，选择范围：1~32个节点数量。 - ess-cold节点，选择范围：1~32个节点数量。

        :return: The instance_num of this CreateClusterRolesBody.
        :rtype: int
        """
        return self._instance_num

    @instance_num.setter
    def instance_num(self, instance_num):
        """Sets the instance_num of this CreateClusterRolesBody.

        实例个数。 - ess节点，选择范围：1~32个节点数量。   - 若同时选择ess和ess-master时，可以选择1~200个节点数量。    - 若同时选择ess和ess-client时，可以选择1~32个节点数量。    - 若同时选择ess和ess-cold时，可以选择1~32个节点数量。 - ess-master节点，选择范围：3~10内的奇数个节点数量。 - ess-client节点，选择范围：1~32个节点数量。 - ess-cold节点，选择范围：1~32个节点数量。

        :param instance_num: The instance_num of this CreateClusterRolesBody.
        :type instance_num: int
        """
        self._instance_num = instance_num

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
        if not isinstance(other, CreateClusterRolesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
