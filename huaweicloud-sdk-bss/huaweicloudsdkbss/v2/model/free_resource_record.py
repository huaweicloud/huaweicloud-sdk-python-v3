# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FreeResourceRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deduct_time': 'str',
        'free_resource_id': 'str',
        'resource_id': 'str',
        'resource_type_code': 'str',
        'resource_type_name': 'str',
        'resource_tag': 'str',
        'product_id': 'str',
        'product_name': 'str',
        'usage_type_code': 'str',
        'available_amount': 'str',
        'remaining_amount': 'str',
        'used_amount': 'str',
        'measure_id': 'int',
        'effective_time': 'str',
        'expire_time': 'str'
    }

    attribute_map = {
        'deduct_time': 'deduct_time',
        'free_resource_id': 'free_resource_id',
        'resource_id': 'resource_id',
        'resource_type_code': 'resource_type_code',
        'resource_type_name': 'resource_type_name',
        'resource_tag': 'resource_tag',
        'product_id': 'product_id',
        'product_name': 'product_name',
        'usage_type_code': 'usage_type_code',
        'available_amount': 'available_amount',
        'remaining_amount': 'remaining_amount',
        'used_amount': 'used_amount',
        'measure_id': 'measure_id',
        'effective_time': 'effective_time',
        'expire_time': 'expire_time'
    }

    def __init__(self, deduct_time=None, free_resource_id=None, resource_id=None, resource_type_code=None, resource_type_name=None, resource_tag=None, product_id=None, product_name=None, usage_type_code=None, available_amount=None, remaining_amount=None, used_amount=None, measure_id=None, effective_time=None, expire_time=None):
        r"""FreeResourceRecord

        The model defined in huaweicloud sdk

        :param deduct_time: 资源抵扣时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如\&quot;2021-10-13T10:01:49Z\&quot;。
        :type deduct_time: str
        :param free_resource_id: 资源项ID，一个资源包中会含有多个资源项，一个使用量类型对应一个资源项。
        :type free_resource_id: str
        :param resource_id: 资源ID。
        :type resource_id: str
        :param resource_type_code: 资源类型编码。例如ECS的VM为“hws.resource.type.vm”。
        :type resource_type_code: str
        :param resource_type_name: 资源类型名称。例如ECS的资源类型名称为“云主机”。
        :type resource_type_name: str
        :param resource_tag: 资源标签。
        :type resource_tag: str
        :param product_id: 产品ID，即资源包ID。
        :type product_id: str
        :param product_name: 产品名称，即资源包名称。
        :type product_name: str
        :param usage_type_code: 使用量类型。
        :type usage_type_code: str
        :param available_amount: 资源抵扣前余量。
        :type available_amount: str
        :param remaining_amount: 资源抵扣后余量。
        :type remaining_amount: str
        :param used_amount: 抵扣量。
        :type used_amount: str
        :param measure_id: 度量单位，免费资源套餐额度度量单位。您可以调用查询度量单位列表接口获取。
        :type measure_id: int
        :param effective_time: 资源使用的开始时间，UTC时间。
        :type effective_time: str
        :param expire_time: 资源使用的结束时间，UTC时间。
        :type expire_time: str
        """
        
        

        self._deduct_time = None
        self._free_resource_id = None
        self._resource_id = None
        self._resource_type_code = None
        self._resource_type_name = None
        self._resource_tag = None
        self._product_id = None
        self._product_name = None
        self._usage_type_code = None
        self._available_amount = None
        self._remaining_amount = None
        self._used_amount = None
        self._measure_id = None
        self._effective_time = None
        self._expire_time = None
        self.discriminator = None

        if deduct_time is not None:
            self.deduct_time = deduct_time
        if free_resource_id is not None:
            self.free_resource_id = free_resource_id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
        if resource_tag is not None:
            self.resource_tag = resource_tag
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name
        if usage_type_code is not None:
            self.usage_type_code = usage_type_code
        if available_amount is not None:
            self.available_amount = available_amount
        if remaining_amount is not None:
            self.remaining_amount = remaining_amount
        if used_amount is not None:
            self.used_amount = used_amount
        if measure_id is not None:
            self.measure_id = measure_id
        if effective_time is not None:
            self.effective_time = effective_time
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def deduct_time(self):
        r"""Gets the deduct_time of this FreeResourceRecord.

        资源抵扣时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如\"2021-10-13T10:01:49Z\"。

        :return: The deduct_time of this FreeResourceRecord.
        :rtype: str
        """
        return self._deduct_time

    @deduct_time.setter
    def deduct_time(self, deduct_time):
        r"""Sets the deduct_time of this FreeResourceRecord.

        资源抵扣时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如\"2021-10-13T10:01:49Z\"。

        :param deduct_time: The deduct_time of this FreeResourceRecord.
        :type deduct_time: str
        """
        self._deduct_time = deduct_time

    @property
    def free_resource_id(self):
        r"""Gets the free_resource_id of this FreeResourceRecord.

        资源项ID，一个资源包中会含有多个资源项，一个使用量类型对应一个资源项。

        :return: The free_resource_id of this FreeResourceRecord.
        :rtype: str
        """
        return self._free_resource_id

    @free_resource_id.setter
    def free_resource_id(self, free_resource_id):
        r"""Sets the free_resource_id of this FreeResourceRecord.

        资源项ID，一个资源包中会含有多个资源项，一个使用量类型对应一个资源项。

        :param free_resource_id: The free_resource_id of this FreeResourceRecord.
        :type free_resource_id: str
        """
        self._free_resource_id = free_resource_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this FreeResourceRecord.

        资源ID。

        :return: The resource_id of this FreeResourceRecord.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this FreeResourceRecord.

        资源ID。

        :param resource_id: The resource_id of this FreeResourceRecord.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type_code(self):
        r"""Gets the resource_type_code of this FreeResourceRecord.

        资源类型编码。例如ECS的VM为“hws.resource.type.vm”。

        :return: The resource_type_code of this FreeResourceRecord.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        r"""Sets the resource_type_code of this FreeResourceRecord.

        资源类型编码。例如ECS的VM为“hws.resource.type.vm”。

        :param resource_type_code: The resource_type_code of this FreeResourceRecord.
        :type resource_type_code: str
        """
        self._resource_type_code = resource_type_code

    @property
    def resource_type_name(self):
        r"""Gets the resource_type_name of this FreeResourceRecord.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :return: The resource_type_name of this FreeResourceRecord.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        r"""Sets the resource_type_name of this FreeResourceRecord.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :param resource_type_name: The resource_type_name of this FreeResourceRecord.
        :type resource_type_name: str
        """
        self._resource_type_name = resource_type_name

    @property
    def resource_tag(self):
        r"""Gets the resource_tag of this FreeResourceRecord.

        资源标签。

        :return: The resource_tag of this FreeResourceRecord.
        :rtype: str
        """
        return self._resource_tag

    @resource_tag.setter
    def resource_tag(self, resource_tag):
        r"""Sets the resource_tag of this FreeResourceRecord.

        资源标签。

        :param resource_tag: The resource_tag of this FreeResourceRecord.
        :type resource_tag: str
        """
        self._resource_tag = resource_tag

    @property
    def product_id(self):
        r"""Gets the product_id of this FreeResourceRecord.

        产品ID，即资源包ID。

        :return: The product_id of this FreeResourceRecord.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this FreeResourceRecord.

        产品ID，即资源包ID。

        :param product_id: The product_id of this FreeResourceRecord.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def product_name(self):
        r"""Gets the product_name of this FreeResourceRecord.

        产品名称，即资源包名称。

        :return: The product_name of this FreeResourceRecord.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this FreeResourceRecord.

        产品名称，即资源包名称。

        :param product_name: The product_name of this FreeResourceRecord.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def usage_type_code(self):
        r"""Gets the usage_type_code of this FreeResourceRecord.

        使用量类型。

        :return: The usage_type_code of this FreeResourceRecord.
        :rtype: str
        """
        return self._usage_type_code

    @usage_type_code.setter
    def usage_type_code(self, usage_type_code):
        r"""Sets the usage_type_code of this FreeResourceRecord.

        使用量类型。

        :param usage_type_code: The usage_type_code of this FreeResourceRecord.
        :type usage_type_code: str
        """
        self._usage_type_code = usage_type_code

    @property
    def available_amount(self):
        r"""Gets the available_amount of this FreeResourceRecord.

        资源抵扣前余量。

        :return: The available_amount of this FreeResourceRecord.
        :rtype: str
        """
        return self._available_amount

    @available_amount.setter
    def available_amount(self, available_amount):
        r"""Sets the available_amount of this FreeResourceRecord.

        资源抵扣前余量。

        :param available_amount: The available_amount of this FreeResourceRecord.
        :type available_amount: str
        """
        self._available_amount = available_amount

    @property
    def remaining_amount(self):
        r"""Gets the remaining_amount of this FreeResourceRecord.

        资源抵扣后余量。

        :return: The remaining_amount of this FreeResourceRecord.
        :rtype: str
        """
        return self._remaining_amount

    @remaining_amount.setter
    def remaining_amount(self, remaining_amount):
        r"""Sets the remaining_amount of this FreeResourceRecord.

        资源抵扣后余量。

        :param remaining_amount: The remaining_amount of this FreeResourceRecord.
        :type remaining_amount: str
        """
        self._remaining_amount = remaining_amount

    @property
    def used_amount(self):
        r"""Gets the used_amount of this FreeResourceRecord.

        抵扣量。

        :return: The used_amount of this FreeResourceRecord.
        :rtype: str
        """
        return self._used_amount

    @used_amount.setter
    def used_amount(self, used_amount):
        r"""Sets the used_amount of this FreeResourceRecord.

        抵扣量。

        :param used_amount: The used_amount of this FreeResourceRecord.
        :type used_amount: str
        """
        self._used_amount = used_amount

    @property
    def measure_id(self):
        r"""Gets the measure_id of this FreeResourceRecord.

        度量单位，免费资源套餐额度度量单位。您可以调用查询度量单位列表接口获取。

        :return: The measure_id of this FreeResourceRecord.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        r"""Sets the measure_id of this FreeResourceRecord.

        度量单位，免费资源套餐额度度量单位。您可以调用查询度量单位列表接口获取。

        :param measure_id: The measure_id of this FreeResourceRecord.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def effective_time(self):
        r"""Gets the effective_time of this FreeResourceRecord.

        资源使用的开始时间，UTC时间。

        :return: The effective_time of this FreeResourceRecord.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        r"""Sets the effective_time of this FreeResourceRecord.

        资源使用的开始时间，UTC时间。

        :param effective_time: The effective_time of this FreeResourceRecord.
        :type effective_time: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        r"""Gets the expire_time of this FreeResourceRecord.

        资源使用的结束时间，UTC时间。

        :return: The expire_time of this FreeResourceRecord.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this FreeResourceRecord.

        资源使用的结束时间，UTC时间。

        :param expire_time: The expire_time of this FreeResourceRecord.
        :type expire_time: str
        """
        self._expire_time = expire_time

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
        if not isinstance(other, FreeResourceRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
