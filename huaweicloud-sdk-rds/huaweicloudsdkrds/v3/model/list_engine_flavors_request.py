# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEngineFlavorsRequest:

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
        'availability_zone_ids': 'str',
        'ha_mode': 'str',
        'spec_code_like': 'str',
        'flavor_category_type': 'str',
        'is_rha_flavor': 'bool',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'availability_zone_ids': 'availability_zone_ids',
        'ha_mode': 'ha_mode',
        'spec_code_like': 'spec_code_like',
        'flavor_category_type': 'flavor_category_type',
        'is_rha_flavor': 'is_rha_flavor',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, availability_zone_ids=None, ha_mode=None, spec_code_like=None, flavor_category_type=None, is_rha_flavor=None, offset=None, limit=None):
        r"""ListEngineFlavorsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param availability_zone_ids: 可用区，多个用\&quot;,\&quot;分割，如cn-southwest-244a,cn-southwest-244b
        :type availability_zone_ids: str
        :param ha_mode: 模式，包括如下类型： ha：主备实例。 replica：只读实例。 single：单实例。
        :type ha_mode: str
        :param spec_code_like: 性能规格,如rds.dec.pg.s1.medium，模糊匹配该规格类型
        :type spec_code_like: str
        :param flavor_category_type: 规格类型，包括如下类型：simple、dec
        :type flavor_category_type: str
        :param is_rha_flavor: 是否显示高可用只读类型
        :type is_rha_flavor: bool
        :param offset: 索引位置，偏移量。 从第一条数据偏移offset条数据后开始查询，默认为0。 取值必须为数字，且不能为负数。
        :type offset: int
        :param limit: 查询个数上限值。 取值范围：1~100。 不传该参数时，默认查询前100条信息。
        :type limit: int
        """
        
        

        self._instance_id = None
        self._availability_zone_ids = None
        self._ha_mode = None
        self._spec_code_like = None
        self._flavor_category_type = None
        self._is_rha_flavor = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        self.availability_zone_ids = availability_zone_ids
        self.ha_mode = ha_mode
        if spec_code_like is not None:
            self.spec_code_like = spec_code_like
        if flavor_category_type is not None:
            self.flavor_category_type = flavor_category_type
        if is_rha_flavor is not None:
            self.is_rha_flavor = is_rha_flavor
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListEngineFlavorsRequest.

        实例ID

        :return: The instance_id of this ListEngineFlavorsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListEngineFlavorsRequest.

        实例ID

        :param instance_id: The instance_id of this ListEngineFlavorsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def availability_zone_ids(self):
        r"""Gets the availability_zone_ids of this ListEngineFlavorsRequest.

        可用区，多个用\",\"分割，如cn-southwest-244a,cn-southwest-244b

        :return: The availability_zone_ids of this ListEngineFlavorsRequest.
        :rtype: str
        """
        return self._availability_zone_ids

    @availability_zone_ids.setter
    def availability_zone_ids(self, availability_zone_ids):
        r"""Sets the availability_zone_ids of this ListEngineFlavorsRequest.

        可用区，多个用\",\"分割，如cn-southwest-244a,cn-southwest-244b

        :param availability_zone_ids: The availability_zone_ids of this ListEngineFlavorsRequest.
        :type availability_zone_ids: str
        """
        self._availability_zone_ids = availability_zone_ids

    @property
    def ha_mode(self):
        r"""Gets the ha_mode of this ListEngineFlavorsRequest.

        模式，包括如下类型： ha：主备实例。 replica：只读实例。 single：单实例。

        :return: The ha_mode of this ListEngineFlavorsRequest.
        :rtype: str
        """
        return self._ha_mode

    @ha_mode.setter
    def ha_mode(self, ha_mode):
        r"""Sets the ha_mode of this ListEngineFlavorsRequest.

        模式，包括如下类型： ha：主备实例。 replica：只读实例。 single：单实例。

        :param ha_mode: The ha_mode of this ListEngineFlavorsRequest.
        :type ha_mode: str
        """
        self._ha_mode = ha_mode

    @property
    def spec_code_like(self):
        r"""Gets the spec_code_like of this ListEngineFlavorsRequest.

        性能规格,如rds.dec.pg.s1.medium，模糊匹配该规格类型

        :return: The spec_code_like of this ListEngineFlavorsRequest.
        :rtype: str
        """
        return self._spec_code_like

    @spec_code_like.setter
    def spec_code_like(self, spec_code_like):
        r"""Sets the spec_code_like of this ListEngineFlavorsRequest.

        性能规格,如rds.dec.pg.s1.medium，模糊匹配该规格类型

        :param spec_code_like: The spec_code_like of this ListEngineFlavorsRequest.
        :type spec_code_like: str
        """
        self._spec_code_like = spec_code_like

    @property
    def flavor_category_type(self):
        r"""Gets the flavor_category_type of this ListEngineFlavorsRequest.

        规格类型，包括如下类型：simple、dec

        :return: The flavor_category_type of this ListEngineFlavorsRequest.
        :rtype: str
        """
        return self._flavor_category_type

    @flavor_category_type.setter
    def flavor_category_type(self, flavor_category_type):
        r"""Sets the flavor_category_type of this ListEngineFlavorsRequest.

        规格类型，包括如下类型：simple、dec

        :param flavor_category_type: The flavor_category_type of this ListEngineFlavorsRequest.
        :type flavor_category_type: str
        """
        self._flavor_category_type = flavor_category_type

    @property
    def is_rha_flavor(self):
        r"""Gets the is_rha_flavor of this ListEngineFlavorsRequest.

        是否显示高可用只读类型

        :return: The is_rha_flavor of this ListEngineFlavorsRequest.
        :rtype: bool
        """
        return self._is_rha_flavor

    @is_rha_flavor.setter
    def is_rha_flavor(self, is_rha_flavor):
        r"""Sets the is_rha_flavor of this ListEngineFlavorsRequest.

        是否显示高可用只读类型

        :param is_rha_flavor: The is_rha_flavor of this ListEngineFlavorsRequest.
        :type is_rha_flavor: bool
        """
        self._is_rha_flavor = is_rha_flavor

    @property
    def offset(self):
        r"""Gets the offset of this ListEngineFlavorsRequest.

        索引位置，偏移量。 从第一条数据偏移offset条数据后开始查询，默认为0。 取值必须为数字，且不能为负数。

        :return: The offset of this ListEngineFlavorsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListEngineFlavorsRequest.

        索引位置，偏移量。 从第一条数据偏移offset条数据后开始查询，默认为0。 取值必须为数字，且不能为负数。

        :param offset: The offset of this ListEngineFlavorsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListEngineFlavorsRequest.

        查询个数上限值。 取值范围：1~100。 不传该参数时，默认查询前100条信息。

        :return: The limit of this ListEngineFlavorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEngineFlavorsRequest.

        查询个数上限值。 取值范围：1~100。 不传该参数时，默认查询前100条信息。

        :param limit: The limit of this ListEngineFlavorsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListEngineFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
