# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TicketCreateSubTicketInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'region': 'str',
        'target_type': 'str',
        'target_value': 'str',
        'expected_start_time': 'int',
        'expected_end_time': 'int',
        'executors': 'str',
        'cooperators': 'str'
    }

    attribute_map = {
        'app_name': 'app_name',
        'region': 'region',
        'target_type': 'target_type',
        'target_value': 'target_value',
        'expected_start_time': 'expected_start_time',
        'expected_end_time': 'expected_end_time',
        'executors': 'executors',
        'cooperators': 'cooperators'
    }

    def __init__(self, app_name=None, region=None, target_type=None, target_value=None, expected_start_time=None, expected_end_time=None, executors=None, cooperators=None):
        r"""TicketCreateSubTicketInfo

        The model defined in huaweicloud sdk

        :param app_name: **参数解释：** 变更服务。 **约束限制：** 当target_type为change_scope时，该字段需传递对应的变更服务中文名称。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type app_name: str
        :param region: **参数解释：** 变更Region。 **约束限制：** 当target_type为change_scope时，该字段需传递对应的变更RegionID。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type region: str
        :param target_type: **参数解释：** 目标选项信息，该值可传递不同的信息，当传递变更应用时，该值传递change_scope，当传递变更计划时，该值传递child_ticket。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type target_type: str
        :param target_value: **参数解释：** 传递变更单RegionID，需和target_type配合使用。 **约束限制：** 当target_type值为child_ticket时，该值有效。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type target_value: str
        :param expected_start_time: **参数解释：** 变更单计划开始时间时间戳。 **约束限制：** 当target_type值为child_ticket时，该值有效。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type expected_start_time: int
        :param expected_end_time: **参数解释：** 变更单计划结束时间时间戳。 **约束限制：** 当target_type值为child_ticket时，该值有效。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type expected_end_time: int
        :param executors: **参数解释：** 变更单实施人。 **约束限制：** 当target_type值为child_ticket时，该值有效。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type executors: str
        :param cooperators: **参数解释：** 变更单配合人。 **约束限制：** 当target_type值为child_ticket时，该值有效。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type cooperators: str
        """
        
        

        self._app_name = None
        self._region = None
        self._target_type = None
        self._target_value = None
        self._expected_start_time = None
        self._expected_end_time = None
        self._executors = None
        self._cooperators = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if region is not None:
            self.region = region
        if target_type is not None:
            self.target_type = target_type
        if target_value is not None:
            self.target_value = target_value
        if expected_start_time is not None:
            self.expected_start_time = expected_start_time
        if expected_end_time is not None:
            self.expected_end_time = expected_end_time
        if executors is not None:
            self.executors = executors
        if cooperators is not None:
            self.cooperators = cooperators

    @property
    def app_name(self):
        r"""Gets the app_name of this TicketCreateSubTicketInfo.

        **参数解释：** 变更服务。 **约束限制：** 当target_type为change_scope时，该字段需传递对应的变更服务中文名称。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The app_name of this TicketCreateSubTicketInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this TicketCreateSubTicketInfo.

        **参数解释：** 变更服务。 **约束限制：** 当target_type为change_scope时，该字段需传递对应的变更服务中文名称。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param app_name: The app_name of this TicketCreateSubTicketInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def region(self):
        r"""Gets the region of this TicketCreateSubTicketInfo.

        **参数解释：** 变更Region。 **约束限制：** 当target_type为change_scope时，该字段需传递对应的变更RegionID。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The region of this TicketCreateSubTicketInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this TicketCreateSubTicketInfo.

        **参数解释：** 变更Region。 **约束限制：** 当target_type为change_scope时，该字段需传递对应的变更RegionID。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param region: The region of this TicketCreateSubTicketInfo.
        :type region: str
        """
        self._region = region

    @property
    def target_type(self):
        r"""Gets the target_type of this TicketCreateSubTicketInfo.

        **参数解释：** 目标选项信息，该值可传递不同的信息，当传递变更应用时，该值传递change_scope，当传递变更计划时，该值传递child_ticket。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The target_type of this TicketCreateSubTicketInfo.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this TicketCreateSubTicketInfo.

        **参数解释：** 目标选项信息，该值可传递不同的信息，当传递变更应用时，该值传递change_scope，当传递变更计划时，该值传递child_ticket。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param target_type: The target_type of this TicketCreateSubTicketInfo.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def target_value(self):
        r"""Gets the target_value of this TicketCreateSubTicketInfo.

        **参数解释：** 传递变更单RegionID，需和target_type配合使用。 **约束限制：** 当target_type值为child_ticket时，该值有效。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The target_value of this TicketCreateSubTicketInfo.
        :rtype: str
        """
        return self._target_value

    @target_value.setter
    def target_value(self, target_value):
        r"""Sets the target_value of this TicketCreateSubTicketInfo.

        **参数解释：** 传递变更单RegionID，需和target_type配合使用。 **约束限制：** 当target_type值为child_ticket时，该值有效。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param target_value: The target_value of this TicketCreateSubTicketInfo.
        :type target_value: str
        """
        self._target_value = target_value

    @property
    def expected_start_time(self):
        r"""Gets the expected_start_time of this TicketCreateSubTicketInfo.

        **参数解释：** 变更单计划开始时间时间戳。 **约束限制：** 当target_type值为child_ticket时，该值有效。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The expected_start_time of this TicketCreateSubTicketInfo.
        :rtype: int
        """
        return self._expected_start_time

    @expected_start_time.setter
    def expected_start_time(self, expected_start_time):
        r"""Sets the expected_start_time of this TicketCreateSubTicketInfo.

        **参数解释：** 变更单计划开始时间时间戳。 **约束限制：** 当target_type值为child_ticket时，该值有效。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param expected_start_time: The expected_start_time of this TicketCreateSubTicketInfo.
        :type expected_start_time: int
        """
        self._expected_start_time = expected_start_time

    @property
    def expected_end_time(self):
        r"""Gets the expected_end_time of this TicketCreateSubTicketInfo.

        **参数解释：** 变更单计划结束时间时间戳。 **约束限制：** 当target_type值为child_ticket时，该值有效。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The expected_end_time of this TicketCreateSubTicketInfo.
        :rtype: int
        """
        return self._expected_end_time

    @expected_end_time.setter
    def expected_end_time(self, expected_end_time):
        r"""Sets the expected_end_time of this TicketCreateSubTicketInfo.

        **参数解释：** 变更单计划结束时间时间戳。 **约束限制：** 当target_type值为child_ticket时，该值有效。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param expected_end_time: The expected_end_time of this TicketCreateSubTicketInfo.
        :type expected_end_time: int
        """
        self._expected_end_time = expected_end_time

    @property
    def executors(self):
        r"""Gets the executors of this TicketCreateSubTicketInfo.

        **参数解释：** 变更单实施人。 **约束限制：** 当target_type值为child_ticket时，该值有效。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The executors of this TicketCreateSubTicketInfo.
        :rtype: str
        """
        return self._executors

    @executors.setter
    def executors(self, executors):
        r"""Sets the executors of this TicketCreateSubTicketInfo.

        **参数解释：** 变更单实施人。 **约束限制：** 当target_type值为child_ticket时，该值有效。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param executors: The executors of this TicketCreateSubTicketInfo.
        :type executors: str
        """
        self._executors = executors

    @property
    def cooperators(self):
        r"""Gets the cooperators of this TicketCreateSubTicketInfo.

        **参数解释：** 变更单配合人。 **约束限制：** 当target_type值为child_ticket时，该值有效。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The cooperators of this TicketCreateSubTicketInfo.
        :rtype: str
        """
        return self._cooperators

    @cooperators.setter
    def cooperators(self, cooperators):
        r"""Sets the cooperators of this TicketCreateSubTicketInfo.

        **参数解释：** 变更单配合人。 **约束限制：** 当target_type值为child_ticket时，该值有效。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param cooperators: The cooperators of this TicketCreateSubTicketInfo.
        :type cooperators: str
        """
        self._cooperators = cooperators

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
        if not isinstance(other, TicketCreateSubTicketInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
