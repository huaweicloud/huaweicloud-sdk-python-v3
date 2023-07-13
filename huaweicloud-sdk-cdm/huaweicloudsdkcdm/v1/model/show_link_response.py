# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLinkResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'links': 'list[Links]',
        'from_to_un_mapping': 'str',
        'batch_from_to_mapping': 'str'
    }

    attribute_map = {
        'links': 'links',
        'from_to_un_mapping': 'fromTo-unMapping',
        'batch_from_to_mapping': 'batchFromTo-mapping'
    }

    def __init__(self, links=None, from_to_un_mapping=None, batch_from_to_mapping=None):
        """ShowLinkResponse

        The model defined in huaweicloud sdk

        :param links: 连接列表，请参见links数据结构说明
        :type links: list[:class:`huaweicloudsdkcdm.v1.Links`]
        :param from_to_un_mapping: 表/文件迁移不支持哪些数据源迁移到哪些数据源
        :type from_to_un_mapping: str
        :param batch_from_to_mapping: 整库迁移支持哪些数据源迁移到哪些数据源
        :type batch_from_to_mapping: str
        """
        
        super(ShowLinkResponse, self).__init__()

        self._links = None
        self._from_to_un_mapping = None
        self._batch_from_to_mapping = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if from_to_un_mapping is not None:
            self.from_to_un_mapping = from_to_un_mapping
        if batch_from_to_mapping is not None:
            self.batch_from_to_mapping = batch_from_to_mapping

    @property
    def links(self):
        """Gets the links of this ShowLinkResponse.

        连接列表，请参见links数据结构说明

        :return: The links of this ShowLinkResponse.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.Links`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ShowLinkResponse.

        连接列表，请参见links数据结构说明

        :param links: The links of this ShowLinkResponse.
        :type links: list[:class:`huaweicloudsdkcdm.v1.Links`]
        """
        self._links = links

    @property
    def from_to_un_mapping(self):
        """Gets the from_to_un_mapping of this ShowLinkResponse.

        表/文件迁移不支持哪些数据源迁移到哪些数据源

        :return: The from_to_un_mapping of this ShowLinkResponse.
        :rtype: str
        """
        return self._from_to_un_mapping

    @from_to_un_mapping.setter
    def from_to_un_mapping(self, from_to_un_mapping):
        """Sets the from_to_un_mapping of this ShowLinkResponse.

        表/文件迁移不支持哪些数据源迁移到哪些数据源

        :param from_to_un_mapping: The from_to_un_mapping of this ShowLinkResponse.
        :type from_to_un_mapping: str
        """
        self._from_to_un_mapping = from_to_un_mapping

    @property
    def batch_from_to_mapping(self):
        """Gets the batch_from_to_mapping of this ShowLinkResponse.

        整库迁移支持哪些数据源迁移到哪些数据源

        :return: The batch_from_to_mapping of this ShowLinkResponse.
        :rtype: str
        """
        return self._batch_from_to_mapping

    @batch_from_to_mapping.setter
    def batch_from_to_mapping(self, batch_from_to_mapping):
        """Sets the batch_from_to_mapping of this ShowLinkResponse.

        整库迁移支持哪些数据源迁移到哪些数据源

        :param batch_from_to_mapping: The batch_from_to_mapping of this ShowLinkResponse.
        :type batch_from_to_mapping: str
        """
        self._batch_from_to_mapping = batch_from_to_mapping

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
        if not isinstance(other, ShowLinkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
