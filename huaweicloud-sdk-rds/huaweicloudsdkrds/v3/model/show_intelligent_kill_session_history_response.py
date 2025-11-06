# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIntelligentKillSessionHistoryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'history': 'list[IntelligentKillSessionHistory]',
        'total_count': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'history': 'history',
        'total_count': 'total_count'
    }

    def __init__(self, instance_id=None, history=None, total_count=None):
        r"""ShowIntelligentKillSessionHistoryResponse

        The model defined in huaweicloud sdk

        :param instance_id: 实例id
        :type instance_id: str
        :param history: 限流信息列表
        :type history: list[:class:`huaweicloudsdkrds.v3.IntelligentKillSessionHistory`]
        :param total_count: 历史记录数量
        :type total_count: int
        """
        
        super().__init__()

        self._instance_id = None
        self._history = None
        self._total_count = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if history is not None:
            self.history = history
        if total_count is not None:
            self.total_count = total_count

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowIntelligentKillSessionHistoryResponse.

        实例id

        :return: The instance_id of this ShowIntelligentKillSessionHistoryResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowIntelligentKillSessionHistoryResponse.

        实例id

        :param instance_id: The instance_id of this ShowIntelligentKillSessionHistoryResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def history(self):
        r"""Gets the history of this ShowIntelligentKillSessionHistoryResponse.

        限流信息列表

        :return: The history of this ShowIntelligentKillSessionHistoryResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.IntelligentKillSessionHistory`]
        """
        return self._history

    @history.setter
    def history(self, history):
        r"""Sets the history of this ShowIntelligentKillSessionHistoryResponse.

        限流信息列表

        :param history: The history of this ShowIntelligentKillSessionHistoryResponse.
        :type history: list[:class:`huaweicloudsdkrds.v3.IntelligentKillSessionHistory`]
        """
        self._history = history

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowIntelligentKillSessionHistoryResponse.

        历史记录数量

        :return: The total_count of this ShowIntelligentKillSessionHistoryResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowIntelligentKillSessionHistoryResponse.

        历史记录数量

        :param total_count: The total_count of this ShowIntelligentKillSessionHistoryResponse.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        import warnings
        warnings.warn("ShowIntelligentKillSessionHistoryResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowIntelligentKillSessionHistoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
