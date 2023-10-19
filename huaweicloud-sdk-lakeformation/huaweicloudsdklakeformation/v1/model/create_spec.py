# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_id': 'str',
        'spec_code': 'str',
        'stride_num': 'int'
    }

    attribute_map = {
        'product_id': 'product_id',
        'spec_code': 'spec_code',
        'stride_num': 'stride_num'
    }

    def __init__(self, product_id=None, spec_code=None, stride_num=None):
        """CreateSpec

        The model defined in huaweicloud sdk

        :param product_id: 商品ID。由系统自动生成，如OFFI8XXXXXXXXXXXXXXXX4。
        :type product_id: str
        :param spec_code: 规格编码。由系统自动生成，例如lakeformation.unit.basic.qps。
        :type spec_code: str
        :param stride_num: 步数。QPS为每秒最大请求数步长，最小为5，步长为1。
        :type stride_num: int
        """
        
        

        self._product_id = None
        self._spec_code = None
        self._stride_num = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        self.spec_code = spec_code
        self.stride_num = stride_num

    @property
    def product_id(self):
        """Gets the product_id of this CreateSpec.

        商品ID。由系统自动生成，如OFFI8XXXXXXXXXXXXXXXX4。

        :return: The product_id of this CreateSpec.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this CreateSpec.

        商品ID。由系统自动生成，如OFFI8XXXXXXXXXXXXXXXX4。

        :param product_id: The product_id of this CreateSpec.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def spec_code(self):
        """Gets the spec_code of this CreateSpec.

        规格编码。由系统自动生成，例如lakeformation.unit.basic.qps。

        :return: The spec_code of this CreateSpec.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this CreateSpec.

        规格编码。由系统自动生成，例如lakeformation.unit.basic.qps。

        :param spec_code: The spec_code of this CreateSpec.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def stride_num(self):
        """Gets the stride_num of this CreateSpec.

        步数。QPS为每秒最大请求数步长，最小为5，步长为1。

        :return: The stride_num of this CreateSpec.
        :rtype: int
        """
        return self._stride_num

    @stride_num.setter
    def stride_num(self, stride_num):
        """Sets the stride_num of this CreateSpec.

        步数。QPS为每秒最大请求数步长，最小为5，步长为1。

        :param stride_num: The stride_num of this CreateSpec.
        :type stride_num: int
        """
        self._stride_num = stride_num

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
        if not isinstance(other, CreateSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
