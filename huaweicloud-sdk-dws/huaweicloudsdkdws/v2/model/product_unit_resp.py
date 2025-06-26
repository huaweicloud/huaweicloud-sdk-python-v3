# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductUnitResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'code': 'str',
        'default_capacity': 'str',
        'classify': 'str',
        'scenario': 'str',
        'version': 'str',
        'status': 'str',
        'attribute': 'list[ProductExtendResp]',
        'duplicate': 'int',
        'default_node': 'int',
        'min_node': 'int',
        'max_node': 'int',
        'product_version_list': 'list[ProductVersionResp]',
        'flavor_id': 'str',
        'flavor_code': 'str',
        'volume_num': 'int',
        'volume_used': 'ProductVolumeUsedResp'
    }

    attribute_map = {
        'id': 'id',
        'code': 'code',
        'default_capacity': 'default_capacity',
        'classify': 'classify',
        'scenario': 'scenario',
        'version': 'version',
        'status': 'status',
        'attribute': 'attribute',
        'duplicate': 'duplicate',
        'default_node': 'default_node',
        'min_node': 'min_node',
        'max_node': 'max_node',
        'product_version_list': 'product_version_list',
        'flavor_id': 'flavor_id',
        'flavor_code': 'flavor_code',
        'volume_num': 'volume_num',
        'volume_used': 'volume_used'
    }

    def __init__(self, id=None, code=None, default_capacity=None, classify=None, scenario=None, version=None, status=None, attribute=None, duplicate=None, default_node=None, min_node=None, max_node=None, product_version_list=None, flavor_id=None, flavor_code=None, volume_num=None, volume_used=None):
        r"""ProductUnitResp

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 规格ID。 **取值范围**： 不涉及。
        :type id: str
        :param code: **参数解释**： 规格编码。 **取值范围**： 不涉及。
        :type code: str
        :param default_capacity: **参数解释**： 规格默认容量。 **取值范围**： 不涉及。
        :type default_capacity: str
        :param classify: **参数解释**： 规格类型。 **取值范围**： 不涉及。
        :type classify: str
        :param scenario: **参数解释**： 规格适用场景。 **取值范围**： 不涉及。
        :type scenario: str
        :param version: **参数解释**： 规格版本信息。 **取值范围**： v1.0：一代规格。 v2.0：二代规格。
        :type version: str
        :param status: **参数解释**： 规格状态。 **取值范围**： 不涉及。
        :type status: str
        :param attribute: **参数解释**： 扩展信息。 **取值范围**： 不涉及。
        :type attribute: list[:class:`huaweicloudsdkdws.v2.ProductExtendResp`]
        :param duplicate: **参数解释**： 规格使用副本数量。 **取值范围**： 不涉及。
        :type duplicate: int
        :param default_node: **参数解释**： 默认节点数量。 **取值范围**： 不涉及。
        :type default_node: int
        :param min_node: **参数解释**： 最小节点数。 **取值范围**： 不涉及。
        :type min_node: int
        :param max_node: **参数解释**： 最大节点数。 **取值范围**： 不涉及。
        :type max_node: int
        :param product_version_list: **参数解释**： 版本信息。 **取值范围**： 不涉及。
        :type product_version_list: list[:class:`huaweicloudsdkdws.v2.ProductVersionResp`]
        :param flavor_id: **参数解释**： 底层规格ID。有别于id字段，一般不会用到。 **取值范围**： 不涉及。
        :type flavor_id: str
        :param flavor_code: **参数解释**： 规格的底层规格编码。 **取值范围**： 不涉及。
        :type flavor_code: str
        :param volume_num: **参数解释**： 规格的磁盘数。 **取值范围**： 不涉及。
        :type volume_num: int
        :param volume_used: 
        :type volume_used: :class:`huaweicloudsdkdws.v2.ProductVolumeUsedResp`
        """
        
        

        self._id = None
        self._code = None
        self._default_capacity = None
        self._classify = None
        self._scenario = None
        self._version = None
        self._status = None
        self._attribute = None
        self._duplicate = None
        self._default_node = None
        self._min_node = None
        self._max_node = None
        self._product_version_list = None
        self._flavor_id = None
        self._flavor_code = None
        self._volume_num = None
        self._volume_used = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if default_capacity is not None:
            self.default_capacity = default_capacity
        if classify is not None:
            self.classify = classify
        if scenario is not None:
            self.scenario = scenario
        if version is not None:
            self.version = version
        if status is not None:
            self.status = status
        if attribute is not None:
            self.attribute = attribute
        if duplicate is not None:
            self.duplicate = duplicate
        if default_node is not None:
            self.default_node = default_node
        if min_node is not None:
            self.min_node = min_node
        if max_node is not None:
            self.max_node = max_node
        if product_version_list is not None:
            self.product_version_list = product_version_list
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if flavor_code is not None:
            self.flavor_code = flavor_code
        if volume_num is not None:
            self.volume_num = volume_num
        if volume_used is not None:
            self.volume_used = volume_used

    @property
    def id(self):
        r"""Gets the id of this ProductUnitResp.

        **参数解释**： 规格ID。 **取值范围**： 不涉及。

        :return: The id of this ProductUnitResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProductUnitResp.

        **参数解释**： 规格ID。 **取值范围**： 不涉及。

        :param id: The id of this ProductUnitResp.
        :type id: str
        """
        self._id = id

    @property
    def code(self):
        r"""Gets the code of this ProductUnitResp.

        **参数解释**： 规格编码。 **取值范围**： 不涉及。

        :return: The code of this ProductUnitResp.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ProductUnitResp.

        **参数解释**： 规格编码。 **取值范围**： 不涉及。

        :param code: The code of this ProductUnitResp.
        :type code: str
        """
        self._code = code

    @property
    def default_capacity(self):
        r"""Gets the default_capacity of this ProductUnitResp.

        **参数解释**： 规格默认容量。 **取值范围**： 不涉及。

        :return: The default_capacity of this ProductUnitResp.
        :rtype: str
        """
        return self._default_capacity

    @default_capacity.setter
    def default_capacity(self, default_capacity):
        r"""Sets the default_capacity of this ProductUnitResp.

        **参数解释**： 规格默认容量。 **取值范围**： 不涉及。

        :param default_capacity: The default_capacity of this ProductUnitResp.
        :type default_capacity: str
        """
        self._default_capacity = default_capacity

    @property
    def classify(self):
        r"""Gets the classify of this ProductUnitResp.

        **参数解释**： 规格类型。 **取值范围**： 不涉及。

        :return: The classify of this ProductUnitResp.
        :rtype: str
        """
        return self._classify

    @classify.setter
    def classify(self, classify):
        r"""Sets the classify of this ProductUnitResp.

        **参数解释**： 规格类型。 **取值范围**： 不涉及。

        :param classify: The classify of this ProductUnitResp.
        :type classify: str
        """
        self._classify = classify

    @property
    def scenario(self):
        r"""Gets the scenario of this ProductUnitResp.

        **参数解释**： 规格适用场景。 **取值范围**： 不涉及。

        :return: The scenario of this ProductUnitResp.
        :rtype: str
        """
        return self._scenario

    @scenario.setter
    def scenario(self, scenario):
        r"""Sets the scenario of this ProductUnitResp.

        **参数解释**： 规格适用场景。 **取值范围**： 不涉及。

        :param scenario: The scenario of this ProductUnitResp.
        :type scenario: str
        """
        self._scenario = scenario

    @property
    def version(self):
        r"""Gets the version of this ProductUnitResp.

        **参数解释**： 规格版本信息。 **取值范围**： v1.0：一代规格。 v2.0：二代规格。

        :return: The version of this ProductUnitResp.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ProductUnitResp.

        **参数解释**： 规格版本信息。 **取值范围**： v1.0：一代规格。 v2.0：二代规格。

        :param version: The version of this ProductUnitResp.
        :type version: str
        """
        self._version = version

    @property
    def status(self):
        r"""Gets the status of this ProductUnitResp.

        **参数解释**： 规格状态。 **取值范围**： 不涉及。

        :return: The status of this ProductUnitResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ProductUnitResp.

        **参数解释**： 规格状态。 **取值范围**： 不涉及。

        :param status: The status of this ProductUnitResp.
        :type status: str
        """
        self._status = status

    @property
    def attribute(self):
        r"""Gets the attribute of this ProductUnitResp.

        **参数解释**： 扩展信息。 **取值范围**： 不涉及。

        :return: The attribute of this ProductUnitResp.
        :rtype: list[:class:`huaweicloudsdkdws.v2.ProductExtendResp`]
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        r"""Sets the attribute of this ProductUnitResp.

        **参数解释**： 扩展信息。 **取值范围**： 不涉及。

        :param attribute: The attribute of this ProductUnitResp.
        :type attribute: list[:class:`huaweicloudsdkdws.v2.ProductExtendResp`]
        """
        self._attribute = attribute

    @property
    def duplicate(self):
        r"""Gets the duplicate of this ProductUnitResp.

        **参数解释**： 规格使用副本数量。 **取值范围**： 不涉及。

        :return: The duplicate of this ProductUnitResp.
        :rtype: int
        """
        return self._duplicate

    @duplicate.setter
    def duplicate(self, duplicate):
        r"""Sets the duplicate of this ProductUnitResp.

        **参数解释**： 规格使用副本数量。 **取值范围**： 不涉及。

        :param duplicate: The duplicate of this ProductUnitResp.
        :type duplicate: int
        """
        self._duplicate = duplicate

    @property
    def default_node(self):
        r"""Gets the default_node of this ProductUnitResp.

        **参数解释**： 默认节点数量。 **取值范围**： 不涉及。

        :return: The default_node of this ProductUnitResp.
        :rtype: int
        """
        return self._default_node

    @default_node.setter
    def default_node(self, default_node):
        r"""Sets the default_node of this ProductUnitResp.

        **参数解释**： 默认节点数量。 **取值范围**： 不涉及。

        :param default_node: The default_node of this ProductUnitResp.
        :type default_node: int
        """
        self._default_node = default_node

    @property
    def min_node(self):
        r"""Gets the min_node of this ProductUnitResp.

        **参数解释**： 最小节点数。 **取值范围**： 不涉及。

        :return: The min_node of this ProductUnitResp.
        :rtype: int
        """
        return self._min_node

    @min_node.setter
    def min_node(self, min_node):
        r"""Sets the min_node of this ProductUnitResp.

        **参数解释**： 最小节点数。 **取值范围**： 不涉及。

        :param min_node: The min_node of this ProductUnitResp.
        :type min_node: int
        """
        self._min_node = min_node

    @property
    def max_node(self):
        r"""Gets the max_node of this ProductUnitResp.

        **参数解释**： 最大节点数。 **取值范围**： 不涉及。

        :return: The max_node of this ProductUnitResp.
        :rtype: int
        """
        return self._max_node

    @max_node.setter
    def max_node(self, max_node):
        r"""Sets the max_node of this ProductUnitResp.

        **参数解释**： 最大节点数。 **取值范围**： 不涉及。

        :param max_node: The max_node of this ProductUnitResp.
        :type max_node: int
        """
        self._max_node = max_node

    @property
    def product_version_list(self):
        r"""Gets the product_version_list of this ProductUnitResp.

        **参数解释**： 版本信息。 **取值范围**： 不涉及。

        :return: The product_version_list of this ProductUnitResp.
        :rtype: list[:class:`huaweicloudsdkdws.v2.ProductVersionResp`]
        """
        return self._product_version_list

    @product_version_list.setter
    def product_version_list(self, product_version_list):
        r"""Sets the product_version_list of this ProductUnitResp.

        **参数解释**： 版本信息。 **取值范围**： 不涉及。

        :param product_version_list: The product_version_list of this ProductUnitResp.
        :type product_version_list: list[:class:`huaweicloudsdkdws.v2.ProductVersionResp`]
        """
        self._product_version_list = product_version_list

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this ProductUnitResp.

        **参数解释**： 底层规格ID。有别于id字段，一般不会用到。 **取值范围**： 不涉及。

        :return: The flavor_id of this ProductUnitResp.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this ProductUnitResp.

        **参数解释**： 底层规格ID。有别于id字段，一般不会用到。 **取值范围**： 不涉及。

        :param flavor_id: The flavor_id of this ProductUnitResp.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def flavor_code(self):
        r"""Gets the flavor_code of this ProductUnitResp.

        **参数解释**： 规格的底层规格编码。 **取值范围**： 不涉及。

        :return: The flavor_code of this ProductUnitResp.
        :rtype: str
        """
        return self._flavor_code

    @flavor_code.setter
    def flavor_code(self, flavor_code):
        r"""Sets the flavor_code of this ProductUnitResp.

        **参数解释**： 规格的底层规格编码。 **取值范围**： 不涉及。

        :param flavor_code: The flavor_code of this ProductUnitResp.
        :type flavor_code: str
        """
        self._flavor_code = flavor_code

    @property
    def volume_num(self):
        r"""Gets the volume_num of this ProductUnitResp.

        **参数解释**： 规格的磁盘数。 **取值范围**： 不涉及。

        :return: The volume_num of this ProductUnitResp.
        :rtype: int
        """
        return self._volume_num

    @volume_num.setter
    def volume_num(self, volume_num):
        r"""Sets the volume_num of this ProductUnitResp.

        **参数解释**： 规格的磁盘数。 **取值范围**： 不涉及。

        :param volume_num: The volume_num of this ProductUnitResp.
        :type volume_num: int
        """
        self._volume_num = volume_num

    @property
    def volume_used(self):
        r"""Gets the volume_used of this ProductUnitResp.

        :return: The volume_used of this ProductUnitResp.
        :rtype: :class:`huaweicloudsdkdws.v2.ProductVolumeUsedResp`
        """
        return self._volume_used

    @volume_used.setter
    def volume_used(self, volume_used):
        r"""Sets the volume_used of this ProductUnitResp.

        :param volume_used: The volume_used of this ProductUnitResp.
        :type volume_used: :class:`huaweicloudsdkdws.v2.ProductVolumeUsedResp`
        """
        self._volume_used = volume_used

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
        if not isinstance(other, ProductUnitResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
