# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDefectRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'defect_id': 'str',
        'defect_status': 'str',
        'approver': 'str',
        'comment': 'str',
        'ignore_type': 'str'
    }

    attribute_map = {
        'defect_id': 'defect_id',
        'defect_status': 'defect_status',
        'approver': 'approver',
        'comment': 'comment',
        'ignore_type': 'ignoreType'
    }

    def __init__(self, defect_id=None, defect_status=None, approver=None, comment=None, ignore_type=None):
        r"""UpdateDefectRequestBody

        The model defined in huaweicloud sdk

        :param defect_id: **参数解释：** MergeKey，问题ID。[[查询缺陷详情](ShowTaskDefectsV2.xml)](tag:hws,hws_hk)[查询缺陷详情](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm)响应中的defect_id字段 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type defect_id: str
        :param defect_status: **参数解释：** 问题状态。 **约束限制：** [不涉及。](tag:hws,hws_hk)[状态为0、1的问题无法直接修改到状态3。](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm) **取值范围：** - 0：待处理。 - 1：已解决。 - 2：已忽略。 [- 3：重新打开（需打开忽略审核开关）。](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm) [- 4：待审核（需打开忽略审核开关）。](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm) **默认取值：** 不涉及。
        :type defect_status: str
        :param approver: **参数解释：** 问题忽略的审核人用户名。 **约束限制：** defect_status取值为4（需打开忽略审核开关）时，必填。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type approver: str
        :param comment: **参数解释：** 本次修改问题状态操作的备注。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type comment: str
        :param ignore_type: **参数解释：** [忽略类型，将问题修改为待审核状态时选填。](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm)[废弃字段。](tag:hws,hws_hk) **约束限制：** 不涉及。 **取值范围：** - NO_RISK：评估无风险暂不解决。 - FALSE_POSITIVES：纯属工具误报。 - THIRD_PARTY：开源及第三方。 - EFFUCUENCY_RETAIN：性能敏感保留危险函数。 - NO_SUPPORT_INKERNEL：不支持的内核危险函数。 - EXCLUDE_SCENES：规范例外场景。 - COMPATIBLE_THIRD_PARTY：兼容第三方。 **默认取值：** NO_RISK
        :type ignore_type: str
        """
        
        

        self._defect_id = None
        self._defect_status = None
        self._approver = None
        self._comment = None
        self._ignore_type = None
        self.discriminator = None

        if defect_id is not None:
            self.defect_id = defect_id
        if defect_status is not None:
            self.defect_status = defect_status
        if approver is not None:
            self.approver = approver
        if comment is not None:
            self.comment = comment
        if ignore_type is not None:
            self.ignore_type = ignore_type

    @property
    def defect_id(self):
        r"""Gets the defect_id of this UpdateDefectRequestBody.

        **参数解释：** MergeKey，问题ID。[[查询缺陷详情](ShowTaskDefectsV2.xml)](tag:hws,hws_hk)[查询缺陷详情](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm)响应中的defect_id字段 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The defect_id of this UpdateDefectRequestBody.
        :rtype: str
        """
        return self._defect_id

    @defect_id.setter
    def defect_id(self, defect_id):
        r"""Sets the defect_id of this UpdateDefectRequestBody.

        **参数解释：** MergeKey，问题ID。[[查询缺陷详情](ShowTaskDefectsV2.xml)](tag:hws,hws_hk)[查询缺陷详情](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm)响应中的defect_id字段 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param defect_id: The defect_id of this UpdateDefectRequestBody.
        :type defect_id: str
        """
        self._defect_id = defect_id

    @property
    def defect_status(self):
        r"""Gets the defect_status of this UpdateDefectRequestBody.

        **参数解释：** 问题状态。 **约束限制：** [不涉及。](tag:hws,hws_hk)[状态为0、1的问题无法直接修改到状态3。](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm) **取值范围：** - 0：待处理。 - 1：已解决。 - 2：已忽略。 [- 3：重新打开（需打开忽略审核开关）。](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm) [- 4：待审核（需打开忽略审核开关）。](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm) **默认取值：** 不涉及。

        :return: The defect_status of this UpdateDefectRequestBody.
        :rtype: str
        """
        return self._defect_status

    @defect_status.setter
    def defect_status(self, defect_status):
        r"""Sets the defect_status of this UpdateDefectRequestBody.

        **参数解释：** 问题状态。 **约束限制：** [不涉及。](tag:hws,hws_hk)[状态为0、1的问题无法直接修改到状态3。](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm) **取值范围：** - 0：待处理。 - 1：已解决。 - 2：已忽略。 [- 3：重新打开（需打开忽略审核开关）。](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm) [- 4：待审核（需打开忽略审核开关）。](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm) **默认取值：** 不涉及。

        :param defect_status: The defect_status of this UpdateDefectRequestBody.
        :type defect_status: str
        """
        self._defect_status = defect_status

    @property
    def approver(self):
        r"""Gets the approver of this UpdateDefectRequestBody.

        **参数解释：** 问题忽略的审核人用户名。 **约束限制：** defect_status取值为4（需打开忽略审核开关）时，必填。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The approver of this UpdateDefectRequestBody.
        :rtype: str
        """
        return self._approver

    @approver.setter
    def approver(self, approver):
        r"""Sets the approver of this UpdateDefectRequestBody.

        **参数解释：** 问题忽略的审核人用户名。 **约束限制：** defect_status取值为4（需打开忽略审核开关）时，必填。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param approver: The approver of this UpdateDefectRequestBody.
        :type approver: str
        """
        self._approver = approver

    @property
    def comment(self):
        r"""Gets the comment of this UpdateDefectRequestBody.

        **参数解释：** 本次修改问题状态操作的备注。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The comment of this UpdateDefectRequestBody.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this UpdateDefectRequestBody.

        **参数解释：** 本次修改问题状态操作的备注。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param comment: The comment of this UpdateDefectRequestBody.
        :type comment: str
        """
        self._comment = comment

    @property
    def ignore_type(self):
        r"""Gets the ignore_type of this UpdateDefectRequestBody.

        **参数解释：** [忽略类型，将问题修改为待审核状态时选填。](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm)[废弃字段。](tag:hws,hws_hk) **约束限制：** 不涉及。 **取值范围：** - NO_RISK：评估无风险暂不解决。 - FALSE_POSITIVES：纯属工具误报。 - THIRD_PARTY：开源及第三方。 - EFFUCUENCY_RETAIN：性能敏感保留危险函数。 - NO_SUPPORT_INKERNEL：不支持的内核危险函数。 - EXCLUDE_SCENES：规范例外场景。 - COMPATIBLE_THIRD_PARTY：兼容第三方。 **默认取值：** NO_RISK

        :return: The ignore_type of this UpdateDefectRequestBody.
        :rtype: str
        """
        return self._ignore_type

    @ignore_type.setter
    def ignore_type(self, ignore_type):
        r"""Sets the ignore_type of this UpdateDefectRequestBody.

        **参数解释：** [忽略类型，将问题修改为待审核状态时选填。](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm)[废弃字段。](tag:hws,hws_hk) **约束限制：** 不涉及。 **取值范围：** - NO_RISK：评估无风险暂不解决。 - FALSE_POSITIVES：纯属工具误报。 - THIRD_PARTY：开源及第三方。 - EFFUCUENCY_RETAIN：性能敏感保留危险函数。 - NO_SUPPORT_INKERNEL：不支持的内核危险函数。 - EXCLUDE_SCENES：规范例外场景。 - COMPATIBLE_THIRD_PARTY：兼容第三方。 **默认取值：** NO_RISK

        :param ignore_type: The ignore_type of this UpdateDefectRequestBody.
        :type ignore_type: str
        """
        self._ignore_type = ignore_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateDefectRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
