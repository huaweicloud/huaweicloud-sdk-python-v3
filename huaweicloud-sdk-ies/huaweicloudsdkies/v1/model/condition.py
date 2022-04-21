# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Condition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'environment': 'int',
        'space': 'int',
        'transport': 'int'
    }

    attribute_map = {
        'environment': 'environment',
        'space': 'space',
        'transport': 'transport'
    }

    def __init__(self, environment=None, space=None, transport=None):
        """Condition

        The model defined in huaweicloud sdk

        :param environment: 机房环境条件 取值范围：   - 0：需做详细评估   - 1：机房内已部署华为FusionModule   - 2：机房等级满足T3或同等级国家标准
        :type environment: int
        :param space: 机柜空间条件 取值范围：   - 0：除首柜外，同机房无预留空间   - 1：除首柜外，同机房预留3柜以上空间   - 2：除首柜外，同机房预留1-3柜空间
        :type space: int
        :param transport: 运输条件 取值范围：   - 0：运输通道和机房门的高度或宽度不满足要求   - 1：运输通道，货梯，机房门均可满足整机柜滚轮搬运   - 2：运输通道，货梯，机房门不能支持整机柜滚轮搬运，沿途有台阶
        :type transport: int
        """
        
        

        self._environment = None
        self._space = None
        self._transport = None
        self.discriminator = None

        if environment is not None:
            self.environment = environment
        if space is not None:
            self.space = space
        if transport is not None:
            self.transport = transport

    @property
    def environment(self):
        """Gets the environment of this Condition.

        机房环境条件 取值范围：   - 0：需做详细评估   - 1：机房内已部署华为FusionModule   - 2：机房等级满足T3或同等级国家标准

        :return: The environment of this Condition.
        :rtype: int
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this Condition.

        机房环境条件 取值范围：   - 0：需做详细评估   - 1：机房内已部署华为FusionModule   - 2：机房等级满足T3或同等级国家标准

        :param environment: The environment of this Condition.
        :type environment: int
        """
        self._environment = environment

    @property
    def space(self):
        """Gets the space of this Condition.

        机柜空间条件 取值范围：   - 0：除首柜外，同机房无预留空间   - 1：除首柜外，同机房预留3柜以上空间   - 2：除首柜外，同机房预留1-3柜空间

        :return: The space of this Condition.
        :rtype: int
        """
        return self._space

    @space.setter
    def space(self, space):
        """Sets the space of this Condition.

        机柜空间条件 取值范围：   - 0：除首柜外，同机房无预留空间   - 1：除首柜外，同机房预留3柜以上空间   - 2：除首柜外，同机房预留1-3柜空间

        :param space: The space of this Condition.
        :type space: int
        """
        self._space = space

    @property
    def transport(self):
        """Gets the transport of this Condition.

        运输条件 取值范围：   - 0：运输通道和机房门的高度或宽度不满足要求   - 1：运输通道，货梯，机房门均可满足整机柜滚轮搬运   - 2：运输通道，货梯，机房门不能支持整机柜滚轮搬运，沿途有台阶

        :return: The transport of this Condition.
        :rtype: int
        """
        return self._transport

    @transport.setter
    def transport(self, transport):
        """Sets the transport of this Condition.

        运输条件 取值范围：   - 0：运输通道和机房门的高度或宽度不满足要求   - 1：运输通道，货梯，机房门均可满足整机柜滚轮搬运   - 2：运输通道，货梯，机房门不能支持整机柜滚轮搬运，沿途有台阶

        :param transport: The transport of this Condition.
        :type transport: int
        """
        self._transport = transport

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
        if not isinstance(other, Condition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
