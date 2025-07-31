# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttackTrendRespBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deny_count': 'int',
        'permit_count': 'int',
        'time': 'int'
    }

    attribute_map = {
        'deny_count': 'deny_count',
        'permit_count': 'permit_count',
        'time': 'time'
    }

    def __init__(self, deny_count=None, permit_count=None, time=None):
        r"""AttackTrendRespBody

        The model defined in huaweicloud sdk

        :param deny_count: **参数解释**： 阻断次数 **取值范围**： 不涉及
        :type deny_count: int
        :param permit_count: **参数解释**： 放行次数 **取值范围**： 不涉及
        :type permit_count: int
        :param time: **参数解释**： 聚合时间 **取值范围**： 不涉及
        :type time: int
        """
        
        

        self._deny_count = None
        self._permit_count = None
        self._time = None
        self.discriminator = None

        if deny_count is not None:
            self.deny_count = deny_count
        if permit_count is not None:
            self.permit_count = permit_count
        if time is not None:
            self.time = time

    @property
    def deny_count(self):
        r"""Gets the deny_count of this AttackTrendRespBody.

        **参数解释**： 阻断次数 **取值范围**： 不涉及

        :return: The deny_count of this AttackTrendRespBody.
        :rtype: int
        """
        return self._deny_count

    @deny_count.setter
    def deny_count(self, deny_count):
        r"""Sets the deny_count of this AttackTrendRespBody.

        **参数解释**： 阻断次数 **取值范围**： 不涉及

        :param deny_count: The deny_count of this AttackTrendRespBody.
        :type deny_count: int
        """
        self._deny_count = deny_count

    @property
    def permit_count(self):
        r"""Gets the permit_count of this AttackTrendRespBody.

        **参数解释**： 放行次数 **取值范围**： 不涉及

        :return: The permit_count of this AttackTrendRespBody.
        :rtype: int
        """
        return self._permit_count

    @permit_count.setter
    def permit_count(self, permit_count):
        r"""Sets the permit_count of this AttackTrendRespBody.

        **参数解释**： 放行次数 **取值范围**： 不涉及

        :param permit_count: The permit_count of this AttackTrendRespBody.
        :type permit_count: int
        """
        self._permit_count = permit_count

    @property
    def time(self):
        r"""Gets the time of this AttackTrendRespBody.

        **参数解释**： 聚合时间 **取值范围**： 不涉及

        :return: The time of this AttackTrendRespBody.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this AttackTrendRespBody.

        **参数解释**： 聚合时间 **取值范围**： 不涉及

        :param time: The time of this AttackTrendRespBody.
        :type time: int
        """
        self._time = time

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
        if not isinstance(other, AttackTrendRespBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
