# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadDataReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'DownloadDataTypeEnum',
        'url': 'str'
    }

    attribute_map = {
        'type': 'type',
        'url': 'url'
    }

    def __init__(self, type=None, url=None):
        """DownloadDataReq

        The model defined in huaweicloud sdk

        :param type: 
        :type type: :class:`huaweicloudsdkeihealth.v1.DownloadDataTypeEnum`
        :param url: 资源地址(支持https、obs地址)
        :type url: str
        """
        
        

        self._type = None
        self._url = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if url is not None:
            self.url = url

    @property
    def type(self):
        """Gets the type of this DownloadDataReq.

        :return: The type of this DownloadDataReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DownloadDataTypeEnum`
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DownloadDataReq.

        :param type: The type of this DownloadDataReq.
        :type type: :class:`huaweicloudsdkeihealth.v1.DownloadDataTypeEnum`
        """
        self._type = type

    @property
    def url(self):
        """Gets the url of this DownloadDataReq.

        资源地址(支持https、obs地址)

        :return: The url of this DownloadDataReq.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DownloadDataReq.

        资源地址(支持https、obs地址)

        :param url: The url of this DownloadDataReq.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, DownloadDataReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
