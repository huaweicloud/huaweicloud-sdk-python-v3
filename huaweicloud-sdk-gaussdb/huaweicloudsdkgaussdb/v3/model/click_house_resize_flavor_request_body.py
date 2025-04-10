# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClickHouseResizeFlavorRequestBody:

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
        'delay': 'bool',
        'instance_id': 'str'
    }

    attribute_map = {
        'flavor_ref': 'flavor_ref',
        'delay': 'delay',
        'instance_id': 'instance_id'
    }

    def __init__(self, flavor_ref=None, delay=None, instance_id=None):
        r"""ClickHouseResizeFlavorRequestBody

        The model defined in huaweicloud sdk

        :param flavor_ref: 规格ID。可通过“查询规格信息”接口获取。  仅允许使用对应数据库，和对应实例类型的规格ID。
        :type flavor_ref: str
        :param delay: 是否延迟变更。默认false。
        :type delay: bool
        :param instance_id: 实例ID，严格匹配UUID规则。
        :type instance_id: str
        """
        
        

        self._flavor_ref = None
        self._delay = None
        self._instance_id = None
        self.discriminator = None

        self.flavor_ref = flavor_ref
        self.delay = delay
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this ClickHouseResizeFlavorRequestBody.

        规格ID。可通过“查询规格信息”接口获取。  仅允许使用对应数据库，和对应实例类型的规格ID。

        :return: The flavor_ref of this ClickHouseResizeFlavorRequestBody.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this ClickHouseResizeFlavorRequestBody.

        规格ID。可通过“查询规格信息”接口获取。  仅允许使用对应数据库，和对应实例类型的规格ID。

        :param flavor_ref: The flavor_ref of this ClickHouseResizeFlavorRequestBody.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def delay(self):
        r"""Gets the delay of this ClickHouseResizeFlavorRequestBody.

        是否延迟变更。默认false。

        :return: The delay of this ClickHouseResizeFlavorRequestBody.
        :rtype: bool
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this ClickHouseResizeFlavorRequestBody.

        是否延迟变更。默认false。

        :param delay: The delay of this ClickHouseResizeFlavorRequestBody.
        :type delay: bool
        """
        self._delay = delay

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ClickHouseResizeFlavorRequestBody.

        实例ID，严格匹配UUID规则。

        :return: The instance_id of this ClickHouseResizeFlavorRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ClickHouseResizeFlavorRequestBody.

        实例ID，严格匹配UUID规则。

        :param instance_id: The instance_id of this ClickHouseResizeFlavorRequestBody.
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
        if not isinstance(other, ClickHouseResizeFlavorRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
