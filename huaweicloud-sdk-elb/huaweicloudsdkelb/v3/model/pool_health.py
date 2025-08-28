# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolHealth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'minimum_healthy_member_count': 'int'
    }

    attribute_map = {
        'minimum_healthy_member_count': 'minimum_healthy_member_count'
    }

    def __init__(self, minimum_healthy_member_count=None):
        r"""PoolHealth

        The model defined in huaweicloud sdk

        :param minimum_healthy_member_count: **参数解释**：当健康检查在线的member个数小于该个数，判定pool的state为不健康。  **取值范围**： - 0：默认值，不生效。 - 1：全下线转发生效。  [不支持该字段，请勿使用。](tag:hws_eu,hws_eu_wb,hws_test,fcs,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42)
        :type minimum_healthy_member_count: int
        """
        
        

        self._minimum_healthy_member_count = None
        self.discriminator = None

        if minimum_healthy_member_count is not None:
            self.minimum_healthy_member_count = minimum_healthy_member_count

    @property
    def minimum_healthy_member_count(self):
        r"""Gets the minimum_healthy_member_count of this PoolHealth.

        **参数解释**：当健康检查在线的member个数小于该个数，判定pool的state为不健康。  **取值范围**： - 0：默认值，不生效。 - 1：全下线转发生效。  [不支持该字段，请勿使用。](tag:hws_eu,hws_eu_wb,hws_test,fcs,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42)

        :return: The minimum_healthy_member_count of this PoolHealth.
        :rtype: int
        """
        return self._minimum_healthy_member_count

    @minimum_healthy_member_count.setter
    def minimum_healthy_member_count(self, minimum_healthy_member_count):
        r"""Sets the minimum_healthy_member_count of this PoolHealth.

        **参数解释**：当健康检查在线的member个数小于该个数，判定pool的state为不健康。  **取值范围**： - 0：默认值，不生效。 - 1：全下线转发生效。  [不支持该字段，请勿使用。](tag:hws_eu,hws_eu_wb,hws_test,fcs,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42)

        :param minimum_healthy_member_count: The minimum_healthy_member_count of this PoolHealth.
        :type minimum_healthy_member_count: int
        """
        self._minimum_healthy_member_count = minimum_healthy_member_count

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
        if not isinstance(other, PoolHealth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
