# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAiOpsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aiops_list': 'list[AiOps]',
        'total_size': 'int'
    }

    attribute_map = {
        'aiops_list': 'aiops_list',
        'total_size': 'total_size'
    }

    def __init__(self, aiops_list=None, total_size=None):
        r"""ListAiOpsResponse

        The model defined in huaweicloud sdk

        :param aiops_list: 
        :type aiops_list: list[:class:`huaweicloudsdkcss.v1.AiOps`]
        :param total_size: 参数解释： 集群风险检测任务总数。 取值范围： 不涉及
        :type total_size: int
        """
        
        super().__init__()

        self._aiops_list = None
        self._total_size = None
        self.discriminator = None

        if aiops_list is not None:
            self.aiops_list = aiops_list
        if total_size is not None:
            self.total_size = total_size

    @property
    def aiops_list(self):
        r"""Gets the aiops_list of this ListAiOpsResponse.

        :return: The aiops_list of this ListAiOpsResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.AiOps`]
        """
        return self._aiops_list

    @aiops_list.setter
    def aiops_list(self, aiops_list):
        r"""Sets the aiops_list of this ListAiOpsResponse.

        :param aiops_list: The aiops_list of this ListAiOpsResponse.
        :type aiops_list: list[:class:`huaweicloudsdkcss.v1.AiOps`]
        """
        self._aiops_list = aiops_list

    @property
    def total_size(self):
        r"""Gets the total_size of this ListAiOpsResponse.

        参数解释： 集群风险检测任务总数。 取值范围： 不涉及

        :return: The total_size of this ListAiOpsResponse.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        r"""Sets the total_size of this ListAiOpsResponse.

        参数解释： 集群风险检测任务总数。 取值范围： 不涉及

        :param total_size: The total_size of this ListAiOpsResponse.
        :type total_size: int
        """
        self._total_size = total_size

    def to_dict(self):
        import warnings
        warnings.warn("ListAiOpsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAiOpsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
