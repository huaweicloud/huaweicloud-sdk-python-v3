# coding: utf-8

import re
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
        'num': 'str',
        'delay': 'int'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'num': 'num',
        'delay': 'delay'
    }

    def __init__(self, spec_code=None, num=None, delay=None):
        """AddReadonlyNodeRequestBody

        The model defined in huaweicloud sdk

        :param spec_code: 资源规格编码。获取方法请参见[查询数据库规格](x-wc://file&#x3D;zh-cn_topic_0000001321087266.xml)中参数“spec_code”的值。  示例：dds.mongodb.c6.xlarge.2.shard
        :type spec_code: str
        :param num: 待新增只读节点个数。 取值范围：1-5。
        :type num: str
        :param delay: 同步延迟时间。取值范围：0~1200毫秒。默认取值为0。
        :type delay: int
        """
        
        

        self._spec_code = None
        self._num = None
        self._delay = None
        self.discriminator = None

        self.spec_code = spec_code
        self.num = num
        if delay is not None:
            self.delay = delay

    @property
    def spec_code(self):
        """Gets the spec_code of this AddReadonlyNodeRequestBody.

        资源规格编码。获取方法请参见[查询数据库规格](x-wc://file=zh-cn_topic_0000001321087266.xml)中参数“spec_code”的值。  示例：dds.mongodb.c6.xlarge.2.shard

        :return: The spec_code of this AddReadonlyNodeRequestBody.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this AddReadonlyNodeRequestBody.

        资源规格编码。获取方法请参见[查询数据库规格](x-wc://file=zh-cn_topic_0000001321087266.xml)中参数“spec_code”的值。  示例：dds.mongodb.c6.xlarge.2.shard

        :param spec_code: The spec_code of this AddReadonlyNodeRequestBody.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def num(self):
        """Gets the num of this AddReadonlyNodeRequestBody.

        待新增只读节点个数。 取值范围：1-5。

        :return: The num of this AddReadonlyNodeRequestBody.
        :rtype: str
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this AddReadonlyNodeRequestBody.

        待新增只读节点个数。 取值范围：1-5。

        :param num: The num of this AddReadonlyNodeRequestBody.
        :type num: str
        """
        self._num = num

    @property
    def delay(self):
        """Gets the delay of this AddReadonlyNodeRequestBody.

        同步延迟时间。取值范围：0~1200毫秒。默认取值为0。

        :return: The delay of this AddReadonlyNodeRequestBody.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this AddReadonlyNodeRequestBody.

        同步延迟时间。取值范围：0~1200毫秒。默认取值为0。

        :param delay: The delay of this AddReadonlyNodeRequestBody.
        :type delay: int
        """
        self._delay = delay

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
