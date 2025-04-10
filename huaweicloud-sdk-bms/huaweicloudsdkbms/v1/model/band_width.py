# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BandWidth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'sharetype': 'str',
        'id': 'str',
        'size': 'int',
        'chargemode': 'str'
    }

    attribute_map = {
        'name': 'name',
        'sharetype': 'sharetype',
        'id': 'id',
        'size': 'size',
        'chargemode': 'chargemode'
    }

    def __init__(self, name=None, sharetype=None, id=None, size=None, chargemode=None):
        r"""BandWidth

        The model defined in huaweicloud sdk

        :param name: 带宽名称
        :type name: str
        :param sharetype: 带宽的共享类型。共享类型枚举：PER，表示独享；WHOLE，表示共享
        :type sharetype: str
        :param id: 共享带宽ID。创建WHOLE类型带宽的弹性公网IP时可以指定之前的共享带宽创建。共享带宽的使用限制请参见“共享带宽简介”。 说明：当创建WHOLE类型的带宽时，该字段必选。
        :type id: str
        :param size: 取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各Region配置为准，请参见管理控制台对应页面显示）。功能说明：带宽大小。共享带宽的大小有最小值限制，默认为5M。 说明：如果传入的参数为小数（如10.2）或者字符类型（如10），会自动强制转换为整数。带宽小于300Mbit/s时，步长支持1Mbit/s；带宽为300Mbit/s~1000Mbit/s时，步长支持50Mbit/s；带宽为1000Mbit/s~2000Mbit/s时，步长支持1000Mbit/s。如果sharetype是PER，该参数必选；如果sharetype是WHOLE并且id有值，该参数会忽略。
        :type size: int
        :param chargemode: 带宽的计费类型。取值为：traffic（按流量计费）、bandwidth（按带宽计费）未传该字段，表示按带宽计费。字段值为空，表示按带宽计费。 说明：如果sharetype是WHOLE并且id有值，仅支持按带宽计费，该参数会忽略。
        :type chargemode: str
        """
        
        

        self._name = None
        self._sharetype = None
        self._id = None
        self._size = None
        self._chargemode = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.sharetype = sharetype
        if id is not None:
            self.id = id
        self.size = size
        if chargemode is not None:
            self.chargemode = chargemode

    @property
    def name(self):
        r"""Gets the name of this BandWidth.

        带宽名称

        :return: The name of this BandWidth.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BandWidth.

        带宽名称

        :param name: The name of this BandWidth.
        :type name: str
        """
        self._name = name

    @property
    def sharetype(self):
        r"""Gets the sharetype of this BandWidth.

        带宽的共享类型。共享类型枚举：PER，表示独享；WHOLE，表示共享

        :return: The sharetype of this BandWidth.
        :rtype: str
        """
        return self._sharetype

    @sharetype.setter
    def sharetype(self, sharetype):
        r"""Sets the sharetype of this BandWidth.

        带宽的共享类型。共享类型枚举：PER，表示独享；WHOLE，表示共享

        :param sharetype: The sharetype of this BandWidth.
        :type sharetype: str
        """
        self._sharetype = sharetype

    @property
    def id(self):
        r"""Gets the id of this BandWidth.

        共享带宽ID。创建WHOLE类型带宽的弹性公网IP时可以指定之前的共享带宽创建。共享带宽的使用限制请参见“共享带宽简介”。 说明：当创建WHOLE类型的带宽时，该字段必选。

        :return: The id of this BandWidth.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BandWidth.

        共享带宽ID。创建WHOLE类型带宽的弹性公网IP时可以指定之前的共享带宽创建。共享带宽的使用限制请参见“共享带宽简介”。 说明：当创建WHOLE类型的带宽时，该字段必选。

        :param id: The id of this BandWidth.
        :type id: str
        """
        self._id = id

    @property
    def size(self):
        r"""Gets the size of this BandWidth.

        取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各Region配置为准，请参见管理控制台对应页面显示）。功能说明：带宽大小。共享带宽的大小有最小值限制，默认为5M。 说明：如果传入的参数为小数（如10.2）或者字符类型（如10），会自动强制转换为整数。带宽小于300Mbit/s时，步长支持1Mbit/s；带宽为300Mbit/s~1000Mbit/s时，步长支持50Mbit/s；带宽为1000Mbit/s~2000Mbit/s时，步长支持1000Mbit/s。如果sharetype是PER，该参数必选；如果sharetype是WHOLE并且id有值，该参数会忽略。

        :return: The size of this BandWidth.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this BandWidth.

        取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各Region配置为准，请参见管理控制台对应页面显示）。功能说明：带宽大小。共享带宽的大小有最小值限制，默认为5M。 说明：如果传入的参数为小数（如10.2）或者字符类型（如10），会自动强制转换为整数。带宽小于300Mbit/s时，步长支持1Mbit/s；带宽为300Mbit/s~1000Mbit/s时，步长支持50Mbit/s；带宽为1000Mbit/s~2000Mbit/s时，步长支持1000Mbit/s。如果sharetype是PER，该参数必选；如果sharetype是WHOLE并且id有值，该参数会忽略。

        :param size: The size of this BandWidth.
        :type size: int
        """
        self._size = size

    @property
    def chargemode(self):
        r"""Gets the chargemode of this BandWidth.

        带宽的计费类型。取值为：traffic（按流量计费）、bandwidth（按带宽计费）未传该字段，表示按带宽计费。字段值为空，表示按带宽计费。 说明：如果sharetype是WHOLE并且id有值，仅支持按带宽计费，该参数会忽略。

        :return: The chargemode of this BandWidth.
        :rtype: str
        """
        return self._chargemode

    @chargemode.setter
    def chargemode(self, chargemode):
        r"""Sets the chargemode of this BandWidth.

        带宽的计费类型。取值为：traffic（按流量计费）、bandwidth（按带宽计费）未传该字段，表示按带宽计费。字段值为空，表示按带宽计费。 说明：如果sharetype是WHOLE并且id有值，仅支持按带宽计费，该参数会忽略。

        :param chargemode: The chargemode of this BandWidth.
        :type chargemode: str
        """
        self._chargemode = chargemode

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
        if not isinstance(other, BandWidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
