# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pool_id': 'str',
        'flavor_id': 'str',
        'flavor_name': 'str',
        'max_num': 'int',
        'flavor_type': 'str',
        'billing': 'BillingInfo',
        'flavor_info': 'FlavorInfoResponse',
        'attributes': 'dict(str, str)'
    }

    attribute_map = {
        'pool_id': 'pool_id',
        'flavor_id': 'flavor_id',
        'flavor_name': 'flavor_name',
        'max_num': 'max_num',
        'flavor_type': 'flavor_type',
        'billing': 'billing',
        'flavor_info': 'flavor_info',
        'attributes': 'attributes'
    }

    def __init__(self, pool_id=None, flavor_id=None, flavor_name=None, max_num=None, flavor_type=None, billing=None, flavor_info=None, attributes=None):
        r"""FlavorResponse

        The model defined in huaweicloud sdk

        :param pool_id: **参数解释**：训练作业选择的资源池ID。 **取值范围**：不涉及。
        :type pool_id: str
        :param flavor_id: 资源规格的ID。
        :type flavor_id: str
        :param flavor_name: 资源规格的名称。
        :type flavor_name: str
        :param max_num: 资源规格的最大节点数。
        :type max_num: int
        :param flavor_type: 资源规格的类型。可选值如下： - CPU - GPU - [Ascend](tag:hc,hk,fcs_super)
        :type flavor_type: str
        :param billing: 
        :type billing: :class:`huaweicloudsdkmodelarts.v1.BillingInfo`
        :param flavor_info: 
        :type flavor_info: :class:`huaweicloudsdkmodelarts.v1.FlavorInfoResponse`
        :param attributes: 其他规格属性。
        :type attributes: dict(str, str)
        """
        
        

        self._pool_id = None
        self._flavor_id = None
        self._flavor_name = None
        self._max_num = None
        self._flavor_type = None
        self._billing = None
        self._flavor_info = None
        self._attributes = None
        self.discriminator = None

        if pool_id is not None:
            self.pool_id = pool_id
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if flavor_name is not None:
            self.flavor_name = flavor_name
        if max_num is not None:
            self.max_num = max_num
        if flavor_type is not None:
            self.flavor_type = flavor_type
        if billing is not None:
            self.billing = billing
        if flavor_info is not None:
            self.flavor_info = flavor_info
        if attributes is not None:
            self.attributes = attributes

    @property
    def pool_id(self):
        r"""Gets the pool_id of this FlavorResponse.

        **参数解释**：训练作业选择的资源池ID。 **取值范围**：不涉及。

        :return: The pool_id of this FlavorResponse.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this FlavorResponse.

        **参数解释**：训练作业选择的资源池ID。 **取值范围**：不涉及。

        :param pool_id: The pool_id of this FlavorResponse.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this FlavorResponse.

        资源规格的ID。

        :return: The flavor_id of this FlavorResponse.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this FlavorResponse.

        资源规格的ID。

        :param flavor_id: The flavor_id of this FlavorResponse.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def flavor_name(self):
        r"""Gets the flavor_name of this FlavorResponse.

        资源规格的名称。

        :return: The flavor_name of this FlavorResponse.
        :rtype: str
        """
        return self._flavor_name

    @flavor_name.setter
    def flavor_name(self, flavor_name):
        r"""Sets the flavor_name of this FlavorResponse.

        资源规格的名称。

        :param flavor_name: The flavor_name of this FlavorResponse.
        :type flavor_name: str
        """
        self._flavor_name = flavor_name

    @property
    def max_num(self):
        r"""Gets the max_num of this FlavorResponse.

        资源规格的最大节点数。

        :return: The max_num of this FlavorResponse.
        :rtype: int
        """
        return self._max_num

    @max_num.setter
    def max_num(self, max_num):
        r"""Sets the max_num of this FlavorResponse.

        资源规格的最大节点数。

        :param max_num: The max_num of this FlavorResponse.
        :type max_num: int
        """
        self._max_num = max_num

    @property
    def flavor_type(self):
        r"""Gets the flavor_type of this FlavorResponse.

        资源规格的类型。可选值如下： - CPU - GPU - [Ascend](tag:hc,hk,fcs_super)

        :return: The flavor_type of this FlavorResponse.
        :rtype: str
        """
        return self._flavor_type

    @flavor_type.setter
    def flavor_type(self, flavor_type):
        r"""Sets the flavor_type of this FlavorResponse.

        资源规格的类型。可选值如下： - CPU - GPU - [Ascend](tag:hc,hk,fcs_super)

        :param flavor_type: The flavor_type of this FlavorResponse.
        :type flavor_type: str
        """
        self._flavor_type = flavor_type

    @property
    def billing(self):
        r"""Gets the billing of this FlavorResponse.

        :return: The billing of this FlavorResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BillingInfo`
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        r"""Sets the billing of this FlavorResponse.

        :param billing: The billing of this FlavorResponse.
        :type billing: :class:`huaweicloudsdkmodelarts.v1.BillingInfo`
        """
        self._billing = billing

    @property
    def flavor_info(self):
        r"""Gets the flavor_info of this FlavorResponse.

        :return: The flavor_info of this FlavorResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.FlavorInfoResponse`
        """
        return self._flavor_info

    @flavor_info.setter
    def flavor_info(self, flavor_info):
        r"""Sets the flavor_info of this FlavorResponse.

        :param flavor_info: The flavor_info of this FlavorResponse.
        :type flavor_info: :class:`huaweicloudsdkmodelarts.v1.FlavorInfoResponse`
        """
        self._flavor_info = flavor_info

    @property
    def attributes(self):
        r"""Gets the attributes of this FlavorResponse.

        其他规格属性。

        :return: The attributes of this FlavorResponse.
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        r"""Sets the attributes of this FlavorResponse.

        其他规格属性。

        :param attributes: The attributes of this FlavorResponse.
        :type attributes: dict(str, str)
        """
        self._attributes = attributes

    def to_dict(self):
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
        if not isinstance(other, FlavorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
