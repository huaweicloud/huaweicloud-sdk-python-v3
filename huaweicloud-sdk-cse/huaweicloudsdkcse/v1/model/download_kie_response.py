# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadKieResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metadata': 'DownloadKieResponseBodyMetadata',
        'data': 'list[CreateKieReq]'
    }

    attribute_map = {
        'metadata': 'metadata',
        'data': 'data'
    }

    def __init__(self, metadata=None, data=None):
        """DownloadKieResponse

        The model defined in huaweicloud sdk

        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcse.v1.DownloadKieResponseBodyMetadata`
        :param data: 导出的配置项列表。
        :type data: list[:class:`huaweicloudsdkcse.v1.CreateKieReq`]
        """
        
        super(DownloadKieResponse, self).__init__()

        self._metadata = None
        self._data = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if data is not None:
            self.data = data

    @property
    def metadata(self):
        """Gets the metadata of this DownloadKieResponse.

        :return: The metadata of this DownloadKieResponse.
        :rtype: :class:`huaweicloudsdkcse.v1.DownloadKieResponseBodyMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DownloadKieResponse.

        :param metadata: The metadata of this DownloadKieResponse.
        :type metadata: :class:`huaweicloudsdkcse.v1.DownloadKieResponseBodyMetadata`
        """
        self._metadata = metadata

    @property
    def data(self):
        """Gets the data of this DownloadKieResponse.

        导出的配置项列表。

        :return: The data of this DownloadKieResponse.
        :rtype: list[:class:`huaweicloudsdkcse.v1.CreateKieReq`]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this DownloadKieResponse.

        导出的配置项列表。

        :param data: The data of this DownloadKieResponse.
        :type data: list[:class:`huaweicloudsdkcse.v1.CreateKieReq`]
        """
        self._data = data

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
        if not isinstance(other, DownloadKieResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
