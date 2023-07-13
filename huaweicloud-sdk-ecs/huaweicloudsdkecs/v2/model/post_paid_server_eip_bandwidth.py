# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostPaidServerEipBandwidth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'sharetype': 'str',
        'chargemode': 'str',
        'id': 'str'
    }

    attribute_map = {
        'size': 'size',
        'sharetype': 'sharetype',
        'chargemode': 'chargemode',
        'id': 'id'
    }

    def __init__(self, size=None, sharetype=None, chargemode=None, id=None):
        """PostPaidServerEipBandwidth

        The model defined in huaweicloud sdk

        :param size: 功能说明：带宽大小  带宽（Mbit/s），取值范围为[1,2000]。  调整带宽时的最小单位会根据带宽范围不同存在差异。  - 小于等于300Mbit/s：默认最小单位为1Mbit/s。 - 300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。 - 大于1000Mbit/s：默认最小单位为500Mbit/s。  &gt; 说明： &gt;  &gt; 如果share_type是PER，该参数必选项；如果share_type是WHOLE并且id有值，该参数会忽略。
        :type size: int
        :param sharetype: 带宽的共享类型。  共享类型枚举：PER，表示独享。WHOLE，表示共享。
        :type sharetype: str
        :param chargemode: 带宽的计费类型。  - 未传该字段，表示按带宽计费。 - 字段值为空，表示按带宽计费。 - 字段值为“traffic”，表示按流量计费。 - 字段为其它值，会导致创建云服务器失败。  &gt; 说明： &gt;  &gt; 如果share_type是WHOLE并且id有值，该参数会忽略。
        :type chargemode: str
        :param id: 带宽ID，创建WHOLE类型带宽的弹性IP时可以指定之前的共享带宽创建。  取值范围：WHOLE类型的带宽ID。  &gt; 说明： &gt;  &gt; 当创建WHOLE类型的带宽时，该字段必选。
        :type id: str
        """
        
        

        self._size = None
        self._sharetype = None
        self._chargemode = None
        self._id = None
        self.discriminator = None

        if size is not None:
            self.size = size
        self.sharetype = sharetype
        if chargemode is not None:
            self.chargemode = chargemode
        if id is not None:
            self.id = id

    @property
    def size(self):
        """Gets the size of this PostPaidServerEipBandwidth.

        功能说明：带宽大小  带宽（Mbit/s），取值范围为[1,2000]。  调整带宽时的最小单位会根据带宽范围不同存在差异。  - 小于等于300Mbit/s：默认最小单位为1Mbit/s。 - 300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。 - 大于1000Mbit/s：默认最小单位为500Mbit/s。  > 说明： >  > 如果share_type是PER，该参数必选项；如果share_type是WHOLE并且id有值，该参数会忽略。

        :return: The size of this PostPaidServerEipBandwidth.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PostPaidServerEipBandwidth.

        功能说明：带宽大小  带宽（Mbit/s），取值范围为[1,2000]。  调整带宽时的最小单位会根据带宽范围不同存在差异。  - 小于等于300Mbit/s：默认最小单位为1Mbit/s。 - 300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。 - 大于1000Mbit/s：默认最小单位为500Mbit/s。  > 说明： >  > 如果share_type是PER，该参数必选项；如果share_type是WHOLE并且id有值，该参数会忽略。

        :param size: The size of this PostPaidServerEipBandwidth.
        :type size: int
        """
        self._size = size

    @property
    def sharetype(self):
        """Gets the sharetype of this PostPaidServerEipBandwidth.

        带宽的共享类型。  共享类型枚举：PER，表示独享。WHOLE，表示共享。

        :return: The sharetype of this PostPaidServerEipBandwidth.
        :rtype: str
        """
        return self._sharetype

    @sharetype.setter
    def sharetype(self, sharetype):
        """Sets the sharetype of this PostPaidServerEipBandwidth.

        带宽的共享类型。  共享类型枚举：PER，表示独享。WHOLE，表示共享。

        :param sharetype: The sharetype of this PostPaidServerEipBandwidth.
        :type sharetype: str
        """
        self._sharetype = sharetype

    @property
    def chargemode(self):
        """Gets the chargemode of this PostPaidServerEipBandwidth.

        带宽的计费类型。  - 未传该字段，表示按带宽计费。 - 字段值为空，表示按带宽计费。 - 字段值为“traffic”，表示按流量计费。 - 字段为其它值，会导致创建云服务器失败。  > 说明： >  > 如果share_type是WHOLE并且id有值，该参数会忽略。

        :return: The chargemode of this PostPaidServerEipBandwidth.
        :rtype: str
        """
        return self._chargemode

    @chargemode.setter
    def chargemode(self, chargemode):
        """Sets the chargemode of this PostPaidServerEipBandwidth.

        带宽的计费类型。  - 未传该字段，表示按带宽计费。 - 字段值为空，表示按带宽计费。 - 字段值为“traffic”，表示按流量计费。 - 字段为其它值，会导致创建云服务器失败。  > 说明： >  > 如果share_type是WHOLE并且id有值，该参数会忽略。

        :param chargemode: The chargemode of this PostPaidServerEipBandwidth.
        :type chargemode: str
        """
        self._chargemode = chargemode

    @property
    def id(self):
        """Gets the id of this PostPaidServerEipBandwidth.

        带宽ID，创建WHOLE类型带宽的弹性IP时可以指定之前的共享带宽创建。  取值范围：WHOLE类型的带宽ID。  > 说明： >  > 当创建WHOLE类型的带宽时，该字段必选。

        :return: The id of this PostPaidServerEipBandwidth.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PostPaidServerEipBandwidth.

        带宽ID，创建WHOLE类型带宽的弹性IP时可以指定之前的共享带宽创建。  取值范围：WHOLE类型的带宽ID。  > 说明： >  > 当创建WHOLE类型的带宽时，该字段必选。

        :param id: The id of this PostPaidServerEipBandwidth.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, PostPaidServerEipBandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
