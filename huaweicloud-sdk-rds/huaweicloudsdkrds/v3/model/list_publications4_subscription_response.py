# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPublications4SubscriptionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_publications': 'list[InstancePublicatiosInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'instance_publications': 'instance_publications',
        'total_count': 'total_count'
    }

    def __init__(self, instance_publications=None, total_count=None):
        r"""ListPublications4SubscriptionResponse

        The model defined in huaweicloud sdk

        :param instance_publications: 实例发布列表。
        :type instance_publications: list[:class:`huaweicloudsdkrds.v3.InstancePublicatiosInfo`]
        :param total_count: 发布总数。
        :type total_count: int
        """
        
        super().__init__()

        self._instance_publications = None
        self._total_count = None
        self.discriminator = None

        if instance_publications is not None:
            self.instance_publications = instance_publications
        if total_count is not None:
            self.total_count = total_count

    @property
    def instance_publications(self):
        r"""Gets the instance_publications of this ListPublications4SubscriptionResponse.

        实例发布列表。

        :return: The instance_publications of this ListPublications4SubscriptionResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.InstancePublicatiosInfo`]
        """
        return self._instance_publications

    @instance_publications.setter
    def instance_publications(self, instance_publications):
        r"""Sets the instance_publications of this ListPublications4SubscriptionResponse.

        实例发布列表。

        :param instance_publications: The instance_publications of this ListPublications4SubscriptionResponse.
        :type instance_publications: list[:class:`huaweicloudsdkrds.v3.InstancePublicatiosInfo`]
        """
        self._instance_publications = instance_publications

    @property
    def total_count(self):
        r"""Gets the total_count of this ListPublications4SubscriptionResponse.

        发布总数。

        :return: The total_count of this ListPublications4SubscriptionResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListPublications4SubscriptionResponse.

        发布总数。

        :param total_count: The total_count of this ListPublications4SubscriptionResponse.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        import warnings
        warnings.warn("ListPublications4SubscriptionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListPublications4SubscriptionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
