# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCondition:

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
        'transport': 'int',
        'installation': 'str'
    }

    attribute_map = {
        'environment': 'environment',
        'space': 'space',
        'transport': 'transport',
        'installation': 'installation'
    }

    def __init__(self, environment=None, space=None, transport=None, installation=None):
        r"""UpdateCondition

        The model defined in huaweicloud sdk

        :param environment: 机房环境条件 取值范围：   - 0：机房条件不属于上述任何一种情况   - 1：机房使用模块化数据中心方案进行建设   - 2：机房已通过国家级或行业级标准化认证
        :type environment: int
        :param space: 机柜空间条件   - 0：暂无扩容计划，不考虑额外余量   - 1：机柜余量相对充裕，可放置空间超过3柜   - 2：机柜余量相对紧张，可放置空间3柜以内
        :type space: int
        :param transport: 运输条件 取值范围：   - 0：运输通道和机房门的高度或宽度不满足要求   - 1：运输通道，货梯，机房门均可满足整机柜滚轮搬运   - 2：运输通道，货梯，机房门不能支持整机柜滚轮搬运，沿途有台阶
        :type transport: int
        :param installation: 整柜安装评估 取值范围：   - UNCLEAR：不清楚是否允许整柜安装，需要评估   - UNSUPPORT：不允许整柜安装，需将设备放入现有机柜   - SUPPORT：可支持整柜安装，并入现有机柜组
        :type installation: str
        """
        
        

        self._environment = None
        self._space = None
        self._transport = None
        self._installation = None
        self.discriminator = None

        if environment is not None:
            self.environment = environment
        if space is not None:
            self.space = space
        if transport is not None:
            self.transport = transport
        if installation is not None:
            self.installation = installation

    @property
    def environment(self):
        r"""Gets the environment of this UpdateCondition.

        机房环境条件 取值范围：   - 0：机房条件不属于上述任何一种情况   - 1：机房使用模块化数据中心方案进行建设   - 2：机房已通过国家级或行业级标准化认证

        :return: The environment of this UpdateCondition.
        :rtype: int
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        r"""Sets the environment of this UpdateCondition.

        机房环境条件 取值范围：   - 0：机房条件不属于上述任何一种情况   - 1：机房使用模块化数据中心方案进行建设   - 2：机房已通过国家级或行业级标准化认证

        :param environment: The environment of this UpdateCondition.
        :type environment: int
        """
        self._environment = environment

    @property
    def space(self):
        r"""Gets the space of this UpdateCondition.

        机柜空间条件   - 0：暂无扩容计划，不考虑额外余量   - 1：机柜余量相对充裕，可放置空间超过3柜   - 2：机柜余量相对紧张，可放置空间3柜以内

        :return: The space of this UpdateCondition.
        :rtype: int
        """
        return self._space

    @space.setter
    def space(self, space):
        r"""Sets the space of this UpdateCondition.

        机柜空间条件   - 0：暂无扩容计划，不考虑额外余量   - 1：机柜余量相对充裕，可放置空间超过3柜   - 2：机柜余量相对紧张，可放置空间3柜以内

        :param space: The space of this UpdateCondition.
        :type space: int
        """
        self._space = space

    @property
    def transport(self):
        r"""Gets the transport of this UpdateCondition.

        运输条件 取值范围：   - 0：运输通道和机房门的高度或宽度不满足要求   - 1：运输通道，货梯，机房门均可满足整机柜滚轮搬运   - 2：运输通道，货梯，机房门不能支持整机柜滚轮搬运，沿途有台阶

        :return: The transport of this UpdateCondition.
        :rtype: int
        """
        return self._transport

    @transport.setter
    def transport(self, transport):
        r"""Sets the transport of this UpdateCondition.

        运输条件 取值范围：   - 0：运输通道和机房门的高度或宽度不满足要求   - 1：运输通道，货梯，机房门均可满足整机柜滚轮搬运   - 2：运输通道，货梯，机房门不能支持整机柜滚轮搬运，沿途有台阶

        :param transport: The transport of this UpdateCondition.
        :type transport: int
        """
        self._transport = transport

    @property
    def installation(self):
        r"""Gets the installation of this UpdateCondition.

        整柜安装评估 取值范围：   - UNCLEAR：不清楚是否允许整柜安装，需要评估   - UNSUPPORT：不允许整柜安装，需将设备放入现有机柜   - SUPPORT：可支持整柜安装，并入现有机柜组

        :return: The installation of this UpdateCondition.
        :rtype: str
        """
        return self._installation

    @installation.setter
    def installation(self, installation):
        r"""Sets the installation of this UpdateCondition.

        整柜安装评估 取值范围：   - UNCLEAR：不清楚是否允许整柜安装，需要评估   - UNSUPPORT：不允许整柜安装，需将设备放入现有机柜   - SUPPORT：可支持整柜安装，并入现有机柜组

        :param installation: The installation of this UpdateCondition.
        :type installation: str
        """
        self._installation = installation

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
        if not isinstance(other, UpdateCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
