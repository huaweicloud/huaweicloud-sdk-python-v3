# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAzAffinity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'az_minimum_healthy_member_percentage': 'int',
        'az_minimum_healthy_member_count': 'int',
        'az_unhealthy_fallback_strategy': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'az_minimum_healthy_member_percentage': 'az_minimum_healthy_member_percentage',
        'az_minimum_healthy_member_count': 'az_minimum_healthy_member_count',
        'az_unhealthy_fallback_strategy': 'az_unhealthy_fallback_strategy'
    }

    def __init__(self, enable=None, az_minimum_healthy_member_percentage=None, az_minimum_healthy_member_count=None, az_unhealthy_fallback_strategy=None):
        r"""UpdateAzAffinity

        The model defined in huaweicloud sdk

        :param enable: **参数解释**：后端服务器组可用区亲和开关。  **约束限制**： - 当后端服务器组中有未设置availability_zone属性的IP类型后端服务器时无法开启可用区亲和。 - 当后端服务器绑定TLS监听器时无法开启可用区亲和。 - 仅IP、UDP、TCP类型的后端服务器组支持开启可用区亲和。 - 当开启可用区亲和后，原本的pool_health配置失效。  **取值范围**：true或false，true表示开启，false表示关闭。  **默认取值**：不涉及
        :type enable: bool
        :param az_minimum_healthy_member_percentage: **参数解释**：后端服务器组单可用区百分比健康度最小阈值，当“后端服务器组单可用区百分比健康度”小于该阈值时，触发可用区异常退避策略。“后端服务器组单可用区百分比健康度”是指在一个后端服务器组中，同可用区中健康检查结果正常的服务器数量与该后端服务器组中属于该可用区的后端服务器总数量的比值，百分比结果向上取整。例如：后端服务器组中属于可用区A的后端服务器总数量为3，设置后端服务器组单可用区百分比健康度最小阈值为66时，3x0.66&#x3D;1.98向上取整为数量阈值2台，即属于可用区A的健康后端数小于2台时触发退避策略；设置后端服务器组单可用区百分比健康度最小阈值为67时，3x0.67&#x3D;2.01向上取整为数量阈值3台，即属于可用区A的健康后端数小于3台时触发退避策略。  **约束限制**： - enable为true时，az_minimum_healthy_member_percentage与az_minimum_healthy_member_count不能同时为-1 - enable为true时，az_minimum_healthy_member_percentage与az_minimum_healthy_member_count不能同时不为-1  **取值范围**：-1至100的整数，0-100为百分比范围，-1表示采用数量阈值。  **默认取值**：不涉及
        :type az_minimum_healthy_member_percentage: int
        :param az_minimum_healthy_member_count: **参数解释**：后端服务器组单可用区中数量健康度最小阈值，当“后端服务器组单可用区中数量健康度”小于该阈值时，触发可用区异常退避策略。“后端服务器组单可用区中数量健康度”是指在一个后端服务器组中，属于同一个可用区的健康检查结果正常的服务器数量。  **约束限制**： - enable为true时，az_minimum_healthy_member_percentage与az_minimum_healthy_member_count不能同时为-1 - enable为true时，az_minimum_healthy_member_percentage与az_minimum_healthy_member_count不能同时不为-1  **取值范围**：-1至10000的整数，0-10000为数量范围，-1表示采用百分比阈值。  **默认取值**：不涉及
        :type az_minimum_healthy_member_count: int
        :param az_unhealthy_fallback_strategy: **参数解释**：后端服务器组单可用区异常退避策略。后端服务器组的健康度小于所配置的最小阈值时，触发该退避策略。forward_to_all_member_of_local_az：转发至同可用区的所有后端服务器，无论健康检查结果是否正常；forward_to_healthy_member_of_remote_az：转发至非同可用区中所有健康检查结果正常的后端服务器；forward_to_all_healthy_member：转发至所有可用区中健康检查结果正常的后端服务器；forward_to_all_member：转发至所有可用区中的所有后端服务器，无论健康检查结果是否正常  **约束限制**：不涉及  **取值范围**：forward_to_all_member_of_local_az，forward_to_healthy_member_of_remote_az，forward_to_all_healthy_member，forward_to_all_member。  **默认取值**：forward_to_all_member_of_local_az
        :type az_unhealthy_fallback_strategy: str
        """
        
        

        self._enable = None
        self._az_minimum_healthy_member_percentage = None
        self._az_minimum_healthy_member_count = None
        self._az_unhealthy_fallback_strategy = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if az_minimum_healthy_member_percentage is not None:
            self.az_minimum_healthy_member_percentage = az_minimum_healthy_member_percentage
        if az_minimum_healthy_member_count is not None:
            self.az_minimum_healthy_member_count = az_minimum_healthy_member_count
        if az_unhealthy_fallback_strategy is not None:
            self.az_unhealthy_fallback_strategy = az_unhealthy_fallback_strategy

    @property
    def enable(self):
        r"""Gets the enable of this UpdateAzAffinity.

        **参数解释**：后端服务器组可用区亲和开关。  **约束限制**： - 当后端服务器组中有未设置availability_zone属性的IP类型后端服务器时无法开启可用区亲和。 - 当后端服务器绑定TLS监听器时无法开启可用区亲和。 - 仅IP、UDP、TCP类型的后端服务器组支持开启可用区亲和。 - 当开启可用区亲和后，原本的pool_health配置失效。  **取值范围**：true或false，true表示开启，false表示关闭。  **默认取值**：不涉及

        :return: The enable of this UpdateAzAffinity.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this UpdateAzAffinity.

        **参数解释**：后端服务器组可用区亲和开关。  **约束限制**： - 当后端服务器组中有未设置availability_zone属性的IP类型后端服务器时无法开启可用区亲和。 - 当后端服务器绑定TLS监听器时无法开启可用区亲和。 - 仅IP、UDP、TCP类型的后端服务器组支持开启可用区亲和。 - 当开启可用区亲和后，原本的pool_health配置失效。  **取值范围**：true或false，true表示开启，false表示关闭。  **默认取值**：不涉及

        :param enable: The enable of this UpdateAzAffinity.
        :type enable: bool
        """
        self._enable = enable

    @property
    def az_minimum_healthy_member_percentage(self):
        r"""Gets the az_minimum_healthy_member_percentage of this UpdateAzAffinity.

        **参数解释**：后端服务器组单可用区百分比健康度最小阈值，当“后端服务器组单可用区百分比健康度”小于该阈值时，触发可用区异常退避策略。“后端服务器组单可用区百分比健康度”是指在一个后端服务器组中，同可用区中健康检查结果正常的服务器数量与该后端服务器组中属于该可用区的后端服务器总数量的比值，百分比结果向上取整。例如：后端服务器组中属于可用区A的后端服务器总数量为3，设置后端服务器组单可用区百分比健康度最小阈值为66时，3x0.66=1.98向上取整为数量阈值2台，即属于可用区A的健康后端数小于2台时触发退避策略；设置后端服务器组单可用区百分比健康度最小阈值为67时，3x0.67=2.01向上取整为数量阈值3台，即属于可用区A的健康后端数小于3台时触发退避策略。  **约束限制**： - enable为true时，az_minimum_healthy_member_percentage与az_minimum_healthy_member_count不能同时为-1 - enable为true时，az_minimum_healthy_member_percentage与az_minimum_healthy_member_count不能同时不为-1  **取值范围**：-1至100的整数，0-100为百分比范围，-1表示采用数量阈值。  **默认取值**：不涉及

        :return: The az_minimum_healthy_member_percentage of this UpdateAzAffinity.
        :rtype: int
        """
        return self._az_minimum_healthy_member_percentage

    @az_minimum_healthy_member_percentage.setter
    def az_minimum_healthy_member_percentage(self, az_minimum_healthy_member_percentage):
        r"""Sets the az_minimum_healthy_member_percentage of this UpdateAzAffinity.

        **参数解释**：后端服务器组单可用区百分比健康度最小阈值，当“后端服务器组单可用区百分比健康度”小于该阈值时，触发可用区异常退避策略。“后端服务器组单可用区百分比健康度”是指在一个后端服务器组中，同可用区中健康检查结果正常的服务器数量与该后端服务器组中属于该可用区的后端服务器总数量的比值，百分比结果向上取整。例如：后端服务器组中属于可用区A的后端服务器总数量为3，设置后端服务器组单可用区百分比健康度最小阈值为66时，3x0.66=1.98向上取整为数量阈值2台，即属于可用区A的健康后端数小于2台时触发退避策略；设置后端服务器组单可用区百分比健康度最小阈值为67时，3x0.67=2.01向上取整为数量阈值3台，即属于可用区A的健康后端数小于3台时触发退避策略。  **约束限制**： - enable为true时，az_minimum_healthy_member_percentage与az_minimum_healthy_member_count不能同时为-1 - enable为true时，az_minimum_healthy_member_percentage与az_minimum_healthy_member_count不能同时不为-1  **取值范围**：-1至100的整数，0-100为百分比范围，-1表示采用数量阈值。  **默认取值**：不涉及

        :param az_minimum_healthy_member_percentage: The az_minimum_healthy_member_percentage of this UpdateAzAffinity.
        :type az_minimum_healthy_member_percentage: int
        """
        self._az_minimum_healthy_member_percentage = az_minimum_healthy_member_percentage

    @property
    def az_minimum_healthy_member_count(self):
        r"""Gets the az_minimum_healthy_member_count of this UpdateAzAffinity.

        **参数解释**：后端服务器组单可用区中数量健康度最小阈值，当“后端服务器组单可用区中数量健康度”小于该阈值时，触发可用区异常退避策略。“后端服务器组单可用区中数量健康度”是指在一个后端服务器组中，属于同一个可用区的健康检查结果正常的服务器数量。  **约束限制**： - enable为true时，az_minimum_healthy_member_percentage与az_minimum_healthy_member_count不能同时为-1 - enable为true时，az_minimum_healthy_member_percentage与az_minimum_healthy_member_count不能同时不为-1  **取值范围**：-1至10000的整数，0-10000为数量范围，-1表示采用百分比阈值。  **默认取值**：不涉及

        :return: The az_minimum_healthy_member_count of this UpdateAzAffinity.
        :rtype: int
        """
        return self._az_minimum_healthy_member_count

    @az_minimum_healthy_member_count.setter
    def az_minimum_healthy_member_count(self, az_minimum_healthy_member_count):
        r"""Sets the az_minimum_healthy_member_count of this UpdateAzAffinity.

        **参数解释**：后端服务器组单可用区中数量健康度最小阈值，当“后端服务器组单可用区中数量健康度”小于该阈值时，触发可用区异常退避策略。“后端服务器组单可用区中数量健康度”是指在一个后端服务器组中，属于同一个可用区的健康检查结果正常的服务器数量。  **约束限制**： - enable为true时，az_minimum_healthy_member_percentage与az_minimum_healthy_member_count不能同时为-1 - enable为true时，az_minimum_healthy_member_percentage与az_minimum_healthy_member_count不能同时不为-1  **取值范围**：-1至10000的整数，0-10000为数量范围，-1表示采用百分比阈值。  **默认取值**：不涉及

        :param az_minimum_healthy_member_count: The az_minimum_healthy_member_count of this UpdateAzAffinity.
        :type az_minimum_healthy_member_count: int
        """
        self._az_minimum_healthy_member_count = az_minimum_healthy_member_count

    @property
    def az_unhealthy_fallback_strategy(self):
        r"""Gets the az_unhealthy_fallback_strategy of this UpdateAzAffinity.

        **参数解释**：后端服务器组单可用区异常退避策略。后端服务器组的健康度小于所配置的最小阈值时，触发该退避策略。forward_to_all_member_of_local_az：转发至同可用区的所有后端服务器，无论健康检查结果是否正常；forward_to_healthy_member_of_remote_az：转发至非同可用区中所有健康检查结果正常的后端服务器；forward_to_all_healthy_member：转发至所有可用区中健康检查结果正常的后端服务器；forward_to_all_member：转发至所有可用区中的所有后端服务器，无论健康检查结果是否正常  **约束限制**：不涉及  **取值范围**：forward_to_all_member_of_local_az，forward_to_healthy_member_of_remote_az，forward_to_all_healthy_member，forward_to_all_member。  **默认取值**：forward_to_all_member_of_local_az

        :return: The az_unhealthy_fallback_strategy of this UpdateAzAffinity.
        :rtype: str
        """
        return self._az_unhealthy_fallback_strategy

    @az_unhealthy_fallback_strategy.setter
    def az_unhealthy_fallback_strategy(self, az_unhealthy_fallback_strategy):
        r"""Sets the az_unhealthy_fallback_strategy of this UpdateAzAffinity.

        **参数解释**：后端服务器组单可用区异常退避策略。后端服务器组的健康度小于所配置的最小阈值时，触发该退避策略。forward_to_all_member_of_local_az：转发至同可用区的所有后端服务器，无论健康检查结果是否正常；forward_to_healthy_member_of_remote_az：转发至非同可用区中所有健康检查结果正常的后端服务器；forward_to_all_healthy_member：转发至所有可用区中健康检查结果正常的后端服务器；forward_to_all_member：转发至所有可用区中的所有后端服务器，无论健康检查结果是否正常  **约束限制**：不涉及  **取值范围**：forward_to_all_member_of_local_az，forward_to_healthy_member_of_remote_az，forward_to_all_healthy_member，forward_to_all_member。  **默认取值**：forward_to_all_member_of_local_az

        :param az_unhealthy_fallback_strategy: The az_unhealthy_fallback_strategy of this UpdateAzAffinity.
        :type az_unhealthy_fallback_strategy: str
        """
        self._az_unhealthy_fallback_strategy = az_unhealthy_fallback_strategy

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
        if not isinstance(other, UpdateAzAffinity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
