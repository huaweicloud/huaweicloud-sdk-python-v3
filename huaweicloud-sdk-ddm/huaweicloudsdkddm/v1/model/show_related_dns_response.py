# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRelatedDnsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'related_data_nodes': 'list[RelatedDnVO]',
        'latest_restorable_time': 'str'
    }

    attribute_map = {
        'related_data_nodes': 'related_data_nodes',
        'latest_restorable_time': 'latest_restorable_time'
    }

    def __init__(self, related_data_nodes=None, latest_restorable_time=None):
        r"""ShowRelatedDnsResponse

        The model defined in huaweicloud sdk

        :param related_data_nodes: 关联DN。
        :type related_data_nodes: list[:class:`huaweicloudsdkddm.v1.RelatedDnVO`]
        :param latest_restorable_time: 最近恢复时间点。
        :type latest_restorable_time: str
        """
        
        super().__init__()

        self._related_data_nodes = None
        self._latest_restorable_time = None
        self.discriminator = None

        if related_data_nodes is not None:
            self.related_data_nodes = related_data_nodes
        if latest_restorable_time is not None:
            self.latest_restorable_time = latest_restorable_time

    @property
    def related_data_nodes(self):
        r"""Gets the related_data_nodes of this ShowRelatedDnsResponse.

        关联DN。

        :return: The related_data_nodes of this ShowRelatedDnsResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.RelatedDnVO`]
        """
        return self._related_data_nodes

    @related_data_nodes.setter
    def related_data_nodes(self, related_data_nodes):
        r"""Sets the related_data_nodes of this ShowRelatedDnsResponse.

        关联DN。

        :param related_data_nodes: The related_data_nodes of this ShowRelatedDnsResponse.
        :type related_data_nodes: list[:class:`huaweicloudsdkddm.v1.RelatedDnVO`]
        """
        self._related_data_nodes = related_data_nodes

    @property
    def latest_restorable_time(self):
        r"""Gets the latest_restorable_time of this ShowRelatedDnsResponse.

        最近恢复时间点。

        :return: The latest_restorable_time of this ShowRelatedDnsResponse.
        :rtype: str
        """
        return self._latest_restorable_time

    @latest_restorable_time.setter
    def latest_restorable_time(self, latest_restorable_time):
        r"""Sets the latest_restorable_time of this ShowRelatedDnsResponse.

        最近恢复时间点。

        :param latest_restorable_time: The latest_restorable_time of this ShowRelatedDnsResponse.
        :type latest_restorable_time: str
        """
        self._latest_restorable_time = latest_restorable_time

    def to_dict(self):
        import warnings
        warnings.warn("ShowRelatedDnsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowRelatedDnsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
