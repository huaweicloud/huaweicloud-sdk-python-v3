# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSlowSqlPlanResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gs_explain': 'str'
    }

    attribute_map = {
        'gs_explain': 'gs_explain'
    }

    def __init__(self, gs_explain=None):
        r"""ShowSlowSqlPlanResponse

        The model defined in huaweicloud sdk

        :param gs_explain: **参数解释**: 执行计划信息。 **取值范围**: 不涉及。
        :type gs_explain: str
        """
        
        super(ShowSlowSqlPlanResponse, self).__init__()

        self._gs_explain = None
        self.discriminator = None

        if gs_explain is not None:
            self.gs_explain = gs_explain

    @property
    def gs_explain(self):
        r"""Gets the gs_explain of this ShowSlowSqlPlanResponse.

        **参数解释**: 执行计划信息。 **取值范围**: 不涉及。

        :return: The gs_explain of this ShowSlowSqlPlanResponse.
        :rtype: str
        """
        return self._gs_explain

    @gs_explain.setter
    def gs_explain(self, gs_explain):
        r"""Sets the gs_explain of this ShowSlowSqlPlanResponse.

        **参数解释**: 执行计划信息。 **取值范围**: 不涉及。

        :param gs_explain: The gs_explain of this ShowSlowSqlPlanResponse.
        :type gs_explain: str
        """
        self._gs_explain = gs_explain

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
        if not isinstance(other, ShowSlowSqlPlanResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
