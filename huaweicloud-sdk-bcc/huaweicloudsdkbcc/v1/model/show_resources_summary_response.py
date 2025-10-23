# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourcesSummaryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ep_id': 'str',
        'provider': 'str',
        'region_id': 'str',
        'counts': 'list[ResourceCountItem]'
    }

    attribute_map = {
        'ep_id': 'ep_id',
        'provider': 'provider',
        'region_id': 'region_id',
        'counts': 'counts'
    }

    def __init__(self, ep_id=None, provider=None, region_id=None, counts=None):
        r"""ShowResourcesSummaryResponse

        The model defined in huaweicloud sdk

        :param ep_id: 企业项目ID
        :type ep_id: str
        :param provider: 云服务类型
        :type provider: str
        :param region_id: 区域ID
        :type region_id: str
        :param counts: 统计体
        :type counts: list[:class:`huaweicloudsdkbcc.v1.ResourceCountItem`]
        """
        
        super(ShowResourcesSummaryResponse, self).__init__()

        self._ep_id = None
        self._provider = None
        self._region_id = None
        self._counts = None
        self.discriminator = None

        if ep_id is not None:
            self.ep_id = ep_id
        if provider is not None:
            self.provider = provider
        if region_id is not None:
            self.region_id = region_id
        if counts is not None:
            self.counts = counts

    @property
    def ep_id(self):
        r"""Gets the ep_id of this ShowResourcesSummaryResponse.

        企业项目ID

        :return: The ep_id of this ShowResourcesSummaryResponse.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        r"""Sets the ep_id of this ShowResourcesSummaryResponse.

        企业项目ID

        :param ep_id: The ep_id of this ShowResourcesSummaryResponse.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def provider(self):
        r"""Gets the provider of this ShowResourcesSummaryResponse.

        云服务类型

        :return: The provider of this ShowResourcesSummaryResponse.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this ShowResourcesSummaryResponse.

        云服务类型

        :param provider: The provider of this ShowResourcesSummaryResponse.
        :type provider: str
        """
        self._provider = provider

    @property
    def region_id(self):
        r"""Gets the region_id of this ShowResourcesSummaryResponse.

        区域ID

        :return: The region_id of this ShowResourcesSummaryResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ShowResourcesSummaryResponse.

        区域ID

        :param region_id: The region_id of this ShowResourcesSummaryResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def counts(self):
        r"""Gets the counts of this ShowResourcesSummaryResponse.

        统计体

        :return: The counts of this ShowResourcesSummaryResponse.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.ResourceCountItem`]
        """
        return self._counts

    @counts.setter
    def counts(self, counts):
        r"""Sets the counts of this ShowResourcesSummaryResponse.

        统计体

        :param counts: The counts of this ShowResourcesSummaryResponse.
        :type counts: list[:class:`huaweicloudsdkbcc.v1.ResourceCountItem`]
        """
        self._counts = counts

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
        if not isinstance(other, ShowResourcesSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
