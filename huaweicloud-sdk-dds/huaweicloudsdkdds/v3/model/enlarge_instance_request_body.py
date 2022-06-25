# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnlargeInstanceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'spec_code': 'str',
        'num': 'str',
        'volume': 'AddShardingNodeVolumeOption',
        'is_auto_pay': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'spec_code': 'spec_code',
        'num': 'num',
        'volume': 'volume',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, type=None, spec_code=None, num=None, volume=None, is_auto_pay=None):
        """EnlargeInstanceRequestBody

        The model defined in huaweicloud sdk

        :param type: 待扩容的对象类型。 - 扩容mongos节点时，取值为“mongos”。 - 扩容shard组时，取值为“shard”。
        :type type: str
        :param spec_code: 资源规格编码。
        :type spec_code: str
        :param num: 一个集群实例下，最多支持16个mongos节点和16个shard组。
        :type num: str
        :param volume: 
        :type volume: :class:`huaweicloudsdkdds.v3.AddShardingNodeVolumeOption`
        :param is_auto_pay: 扩容包年包月实例的节点数量时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 - true，表示自动从账户中支付。 - false，表示手动从账户中支付，默认为该方式。
        :type is_auto_pay: bool
        """
        
        

        self._type = None
        self._spec_code = None
        self._num = None
        self._volume = None
        self._is_auto_pay = None
        self.discriminator = None

        self.type = type
        self.spec_code = spec_code
        self.num = num
        if volume is not None:
            self.volume = volume
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def type(self):
        """Gets the type of this EnlargeInstanceRequestBody.

        待扩容的对象类型。 - 扩容mongos节点时，取值为“mongos”。 - 扩容shard组时，取值为“shard”。

        :return: The type of this EnlargeInstanceRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EnlargeInstanceRequestBody.

        待扩容的对象类型。 - 扩容mongos节点时，取值为“mongos”。 - 扩容shard组时，取值为“shard”。

        :param type: The type of this EnlargeInstanceRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def spec_code(self):
        """Gets the spec_code of this EnlargeInstanceRequestBody.

        资源规格编码。

        :return: The spec_code of this EnlargeInstanceRequestBody.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this EnlargeInstanceRequestBody.

        资源规格编码。

        :param spec_code: The spec_code of this EnlargeInstanceRequestBody.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def num(self):
        """Gets the num of this EnlargeInstanceRequestBody.

        一个集群实例下，最多支持16个mongos节点和16个shard组。

        :return: The num of this EnlargeInstanceRequestBody.
        :rtype: str
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this EnlargeInstanceRequestBody.

        一个集群实例下，最多支持16个mongos节点和16个shard组。

        :param num: The num of this EnlargeInstanceRequestBody.
        :type num: str
        """
        self._num = num

    @property
    def volume(self):
        """Gets the volume of this EnlargeInstanceRequestBody.


        :return: The volume of this EnlargeInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkdds.v3.AddShardingNodeVolumeOption`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this EnlargeInstanceRequestBody.


        :param volume: The volume of this EnlargeInstanceRequestBody.
        :type volume: :class:`huaweicloudsdkdds.v3.AddShardingNodeVolumeOption`
        """
        self._volume = volume

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this EnlargeInstanceRequestBody.

        扩容包年包月实例的节点数量时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 - true，表示自动从账户中支付。 - false，表示手动从账户中支付，默认为该方式。

        :return: The is_auto_pay of this EnlargeInstanceRequestBody.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this EnlargeInstanceRequestBody.

        扩容包年包月实例的节点数量时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 - true，表示自动从账户中支付。 - false，表示手动从账户中支付，默认为该方式。

        :param is_auto_pay: The is_auto_pay of this EnlargeInstanceRequestBody.
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
        if not isinstance(other, EnlargeInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
