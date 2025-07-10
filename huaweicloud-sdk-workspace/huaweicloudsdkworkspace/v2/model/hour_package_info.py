# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HourPackageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'root_order_id': 'str',
        'package_resource_id': 'str',
        'package_instance_id': 'str',
        'package_spec_code': 'str',
        'combined_product_type_code': 'str',
        'use_up_policy': 'str',
        'package_duration': 'int',
        'use_duration': 'int'
    }

    attribute_map = {
        'root_order_id': 'root_order_id',
        'package_resource_id': 'package_resource_id',
        'package_instance_id': 'package_instance_id',
        'package_spec_code': 'package_spec_code',
        'combined_product_type_code': 'combined_product_type_code',
        'use_up_policy': 'use_up_policy',
        'package_duration': 'package_duration',
        'use_duration': 'use_duration'
    }

    def __init__(self, root_order_id=None, package_resource_id=None, package_instance_id=None, package_spec_code=None, combined_product_type_code=None, use_up_policy=None, package_duration=None, use_duration=None):
        r"""HourPackageInfo

        The model defined in huaweicloud sdk

        :param root_order_id: 小时包根订单ID。
        :type root_order_id: str
        :param package_resource_id: 小时包资源ID。
        :type package_resource_id: str
        :param package_instance_id: 小时包实例ID。
        :type package_instance_id: str
        :param package_spec_code: 小时包specCode。
        :type package_spec_code: str
        :param combined_product_type_code: 组合商品resourceTypeCode。
        :type combined_product_type_code: str
        :param use_up_policy: 小时包用完策略：SHUTDOWN_OR_HIBERNATE：自动关机/休眠；PAY_PER_USE：自动按需计费。
        :type use_up_policy: str
        :param package_duration: 小时包总时长。
        :type package_duration: int
        :param use_duration: 小时包已用时长。
        :type use_duration: int
        """
        
        

        self._root_order_id = None
        self._package_resource_id = None
        self._package_instance_id = None
        self._package_spec_code = None
        self._combined_product_type_code = None
        self._use_up_policy = None
        self._package_duration = None
        self._use_duration = None
        self.discriminator = None

        if root_order_id is not None:
            self.root_order_id = root_order_id
        if package_resource_id is not None:
            self.package_resource_id = package_resource_id
        if package_instance_id is not None:
            self.package_instance_id = package_instance_id
        if package_spec_code is not None:
            self.package_spec_code = package_spec_code
        if combined_product_type_code is not None:
            self.combined_product_type_code = combined_product_type_code
        if use_up_policy is not None:
            self.use_up_policy = use_up_policy
        if package_duration is not None:
            self.package_duration = package_duration
        if use_duration is not None:
            self.use_duration = use_duration

    @property
    def root_order_id(self):
        r"""Gets the root_order_id of this HourPackageInfo.

        小时包根订单ID。

        :return: The root_order_id of this HourPackageInfo.
        :rtype: str
        """
        return self._root_order_id

    @root_order_id.setter
    def root_order_id(self, root_order_id):
        r"""Sets the root_order_id of this HourPackageInfo.

        小时包根订单ID。

        :param root_order_id: The root_order_id of this HourPackageInfo.
        :type root_order_id: str
        """
        self._root_order_id = root_order_id

    @property
    def package_resource_id(self):
        r"""Gets the package_resource_id of this HourPackageInfo.

        小时包资源ID。

        :return: The package_resource_id of this HourPackageInfo.
        :rtype: str
        """
        return self._package_resource_id

    @package_resource_id.setter
    def package_resource_id(self, package_resource_id):
        r"""Sets the package_resource_id of this HourPackageInfo.

        小时包资源ID。

        :param package_resource_id: The package_resource_id of this HourPackageInfo.
        :type package_resource_id: str
        """
        self._package_resource_id = package_resource_id

    @property
    def package_instance_id(self):
        r"""Gets the package_instance_id of this HourPackageInfo.

        小时包实例ID。

        :return: The package_instance_id of this HourPackageInfo.
        :rtype: str
        """
        return self._package_instance_id

    @package_instance_id.setter
    def package_instance_id(self, package_instance_id):
        r"""Sets the package_instance_id of this HourPackageInfo.

        小时包实例ID。

        :param package_instance_id: The package_instance_id of this HourPackageInfo.
        :type package_instance_id: str
        """
        self._package_instance_id = package_instance_id

    @property
    def package_spec_code(self):
        r"""Gets the package_spec_code of this HourPackageInfo.

        小时包specCode。

        :return: The package_spec_code of this HourPackageInfo.
        :rtype: str
        """
        return self._package_spec_code

    @package_spec_code.setter
    def package_spec_code(self, package_spec_code):
        r"""Sets the package_spec_code of this HourPackageInfo.

        小时包specCode。

        :param package_spec_code: The package_spec_code of this HourPackageInfo.
        :type package_spec_code: str
        """
        self._package_spec_code = package_spec_code

    @property
    def combined_product_type_code(self):
        r"""Gets the combined_product_type_code of this HourPackageInfo.

        组合商品resourceTypeCode。

        :return: The combined_product_type_code of this HourPackageInfo.
        :rtype: str
        """
        return self._combined_product_type_code

    @combined_product_type_code.setter
    def combined_product_type_code(self, combined_product_type_code):
        r"""Sets the combined_product_type_code of this HourPackageInfo.

        组合商品resourceTypeCode。

        :param combined_product_type_code: The combined_product_type_code of this HourPackageInfo.
        :type combined_product_type_code: str
        """
        self._combined_product_type_code = combined_product_type_code

    @property
    def use_up_policy(self):
        r"""Gets the use_up_policy of this HourPackageInfo.

        小时包用完策略：SHUTDOWN_OR_HIBERNATE：自动关机/休眠；PAY_PER_USE：自动按需计费。

        :return: The use_up_policy of this HourPackageInfo.
        :rtype: str
        """
        return self._use_up_policy

    @use_up_policy.setter
    def use_up_policy(self, use_up_policy):
        r"""Sets the use_up_policy of this HourPackageInfo.

        小时包用完策略：SHUTDOWN_OR_HIBERNATE：自动关机/休眠；PAY_PER_USE：自动按需计费。

        :param use_up_policy: The use_up_policy of this HourPackageInfo.
        :type use_up_policy: str
        """
        self._use_up_policy = use_up_policy

    @property
    def package_duration(self):
        r"""Gets the package_duration of this HourPackageInfo.

        小时包总时长。

        :return: The package_duration of this HourPackageInfo.
        :rtype: int
        """
        return self._package_duration

    @package_duration.setter
    def package_duration(self, package_duration):
        r"""Sets the package_duration of this HourPackageInfo.

        小时包总时长。

        :param package_duration: The package_duration of this HourPackageInfo.
        :type package_duration: int
        """
        self._package_duration = package_duration

    @property
    def use_duration(self):
        r"""Gets the use_duration of this HourPackageInfo.

        小时包已用时长。

        :return: The use_duration of this HourPackageInfo.
        :rtype: int
        """
        return self._use_duration

    @use_duration.setter
    def use_duration(self, use_duration):
        r"""Sets the use_duration of this HourPackageInfo.

        小时包已用时长。

        :param use_duration: The use_duration of this HourPackageInfo.
        :type use_duration: int
        """
        self._use_duration = use_duration

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
        if not isinstance(other, HourPackageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
