# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddReadonlyNodeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_code': 'str',
        'num': 'int',
        'delay': 'int',
        'is_auto_pay': 'bool'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'num': 'num',
        'delay': 'delay',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, spec_code=None, num=None, delay=None, is_auto_pay=None):
        r"""AddReadonlyNodeRequestBody

        The model defined in huaweicloud sdk

        :param spec_code: 资源规格编码。获取方法请参见[查询数据库规格](x-wc://file&#x3D;zh-cn_topic_0000001321087266.xml)中参数“spec_code”的值。  示例：dds.mongodb.c6.xlarge.2.shard
        :type spec_code: str
        :param num: 待新增只读节点个数。 取值范围：1-5。
        :type num: int
        :param delay: 同步延迟时间。取值范围：0~1200毫秒。默认取值为0。
        :type delay: int
        :param is_auto_pay: 新增包年包月实例的只读节点时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 - true，表示自动从账户中支付。 - false，表示手动从账户中支付，默认为该方式。
        :type is_auto_pay: bool
        """
        
        

        self._spec_code = None
        self._num = None
        self._delay = None
        self._is_auto_pay = None
        self.discriminator = None

        self.spec_code = spec_code
        self.num = num
        if delay is not None:
            self.delay = delay
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def spec_code(self):
        r"""Gets the spec_code of this AddReadonlyNodeRequestBody.

        资源规格编码。获取方法请参见[查询数据库规格](x-wc://file=zh-cn_topic_0000001321087266.xml)中参数“spec_code”的值。  示例：dds.mongodb.c6.xlarge.2.shard

        :return: The spec_code of this AddReadonlyNodeRequestBody.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this AddReadonlyNodeRequestBody.

        资源规格编码。获取方法请参见[查询数据库规格](x-wc://file=zh-cn_topic_0000001321087266.xml)中参数“spec_code”的值。  示例：dds.mongodb.c6.xlarge.2.shard

        :param spec_code: The spec_code of this AddReadonlyNodeRequestBody.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def num(self):
        r"""Gets the num of this AddReadonlyNodeRequestBody.

        待新增只读节点个数。 取值范围：1-5。

        :return: The num of this AddReadonlyNodeRequestBody.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this AddReadonlyNodeRequestBody.

        待新增只读节点个数。 取值范围：1-5。

        :param num: The num of this AddReadonlyNodeRequestBody.
        :type num: int
        """
        self._num = num

    @property
    def delay(self):
        r"""Gets the delay of this AddReadonlyNodeRequestBody.

        同步延迟时间。取值范围：0~1200毫秒。默认取值为0。

        :return: The delay of this AddReadonlyNodeRequestBody.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this AddReadonlyNodeRequestBody.

        同步延迟时间。取值范围：0~1200毫秒。默认取值为0。

        :param delay: The delay of this AddReadonlyNodeRequestBody.
        :type delay: int
        """
        self._delay = delay

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this AddReadonlyNodeRequestBody.

        新增包年包月实例的只读节点时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 - true，表示自动从账户中支付。 - false，表示手动从账户中支付，默认为该方式。

        :return: The is_auto_pay of this AddReadonlyNodeRequestBody.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this AddReadonlyNodeRequestBody.

        新增包年包月实例的只读节点时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 - true，表示自动从账户中支付。 - false，表示手动从账户中支付，默认为该方式。

        :param is_auto_pay: The is_auto_pay of this AddReadonlyNodeRequestBody.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, AddReadonlyNodeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
