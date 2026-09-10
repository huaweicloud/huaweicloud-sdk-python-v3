# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsAnalysisTaskFailureAffectedSessionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'sessions': 'list[OpsFailureSession]'
    }

    attribute_map = {
        'total': 'total',
        'sessions': 'sessions'
    }

    def __init__(self, total=None, sessions=None):
        r"""ListOpsAnalysisTaskFailureAffectedSessionsResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释：** 满足过滤条件的记录总数，用于计算分页总页数。 **取值范围：** 不涉及
        :type total: int
        :param sessions: **参数解释：** 满足过滤条件的session清单与错误详情。 **取值范围：** 不涉及
        :type sessions: list[:class:`huaweicloudsdkagentarts.v1.OpsFailureSession`]
        """
        
        super().__init__()

        self._total = None
        self._sessions = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if sessions is not None:
            self.sessions = sessions

    @property
    def total(self):
        r"""Gets the total of this ListOpsAnalysisTaskFailureAffectedSessionsResponse.

        **参数解释：** 满足过滤条件的记录总数，用于计算分页总页数。 **取值范围：** 不涉及

        :return: The total of this ListOpsAnalysisTaskFailureAffectedSessionsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListOpsAnalysisTaskFailureAffectedSessionsResponse.

        **参数解释：** 满足过滤条件的记录总数，用于计算分页总页数。 **取值范围：** 不涉及

        :param total: The total of this ListOpsAnalysisTaskFailureAffectedSessionsResponse.
        :type total: int
        """
        self._total = total

    @property
    def sessions(self):
        r"""Gets the sessions of this ListOpsAnalysisTaskFailureAffectedSessionsResponse.

        **参数解释：** 满足过滤条件的session清单与错误详情。 **取值范围：** 不涉及

        :return: The sessions of this ListOpsAnalysisTaskFailureAffectedSessionsResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsFailureSession`]
        """
        return self._sessions

    @sessions.setter
    def sessions(self, sessions):
        r"""Sets the sessions of this ListOpsAnalysisTaskFailureAffectedSessionsResponse.

        **参数解释：** 满足过滤条件的session清单与错误详情。 **取值范围：** 不涉及

        :param sessions: The sessions of this ListOpsAnalysisTaskFailureAffectedSessionsResponse.
        :type sessions: list[:class:`huaweicloudsdkagentarts.v1.OpsFailureSession`]
        """
        self._sessions = sessions

    def to_dict(self):
        import warnings
        warnings.warn("ListOpsAnalysisTaskFailureAffectedSessionsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListOpsAnalysisTaskFailureAffectedSessionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
