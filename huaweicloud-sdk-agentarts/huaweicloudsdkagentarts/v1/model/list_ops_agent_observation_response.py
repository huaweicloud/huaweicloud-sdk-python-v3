# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsAgentObservationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_info_list': 'list[AgentInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'app_info_list': 'app_info_list',
        'total_count': 'total_count'
    }

    def __init__(self, app_info_list=None, total_count=None):
        r"""ListOpsAgentObservationResponse

        The model defined in huaweicloud sdk

        :param app_info_list: 智能体详情
        :type app_info_list: list[:class:`huaweicloudsdkagentarts.v1.AgentInfo`]
        :param total_count: 总数
        :type total_count: int
        """
        
        super().__init__()

        self._app_info_list = None
        self._total_count = None
        self.discriminator = None

        if app_info_list is not None:
            self.app_info_list = app_info_list
        if total_count is not None:
            self.total_count = total_count

    @property
    def app_info_list(self):
        r"""Gets the app_info_list of this ListOpsAgentObservationResponse.

        智能体详情

        :return: The app_info_list of this ListOpsAgentObservationResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.AgentInfo`]
        """
        return self._app_info_list

    @app_info_list.setter
    def app_info_list(self, app_info_list):
        r"""Sets the app_info_list of this ListOpsAgentObservationResponse.

        智能体详情

        :param app_info_list: The app_info_list of this ListOpsAgentObservationResponse.
        :type app_info_list: list[:class:`huaweicloudsdkagentarts.v1.AgentInfo`]
        """
        self._app_info_list = app_info_list

    @property
    def total_count(self):
        r"""Gets the total_count of this ListOpsAgentObservationResponse.

        总数

        :return: The total_count of this ListOpsAgentObservationResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListOpsAgentObservationResponse.

        总数

        :param total_count: The total_count of this ListOpsAgentObservationResponse.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        import warnings
        warnings.warn("ListOpsAgentObservationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListOpsAgentObservationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
