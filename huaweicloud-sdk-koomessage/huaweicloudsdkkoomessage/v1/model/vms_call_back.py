# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VmsCallBack:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url_type': 'int',
        'callback_url': 'str',
        'remark': 'str'
    }

    attribute_map = {
        'url_type': 'url_type',
        'callback_url': 'callback_url',
        'remark': 'remark'
    }

    def __init__(self, url_type=None, callback_url=None, remark=None):
        r"""VmsCallBack

        The model defined in huaweicloud sdk

        :param url_type: 回调类型。  - 0：发送状态回执 - 1：上行消息回执 
        :type url_type: int
        :param callback_url: 回调地址。
        :type callback_url: str
        :param remark: 备注。
        :type remark: str
        """
        
        

        self._url_type = None
        self._callback_url = None
        self._remark = None
        self.discriminator = None

        if url_type is not None:
            self.url_type = url_type
        if callback_url is not None:
            self.callback_url = callback_url
        if remark is not None:
            self.remark = remark

    @property
    def url_type(self):
        r"""Gets the url_type of this VmsCallBack.

        回调类型。  - 0：发送状态回执 - 1：上行消息回执 

        :return: The url_type of this VmsCallBack.
        :rtype: int
        """
        return self._url_type

    @url_type.setter
    def url_type(self, url_type):
        r"""Sets the url_type of this VmsCallBack.

        回调类型。  - 0：发送状态回执 - 1：上行消息回执 

        :param url_type: The url_type of this VmsCallBack.
        :type url_type: int
        """
        self._url_type = url_type

    @property
    def callback_url(self):
        r"""Gets the callback_url of this VmsCallBack.

        回调地址。

        :return: The callback_url of this VmsCallBack.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        r"""Sets the callback_url of this VmsCallBack.

        回调地址。

        :param callback_url: The callback_url of this VmsCallBack.
        :type callback_url: str
        """
        self._callback_url = callback_url

    @property
    def remark(self):
        r"""Gets the remark of this VmsCallBack.

        备注。

        :return: The remark of this VmsCallBack.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this VmsCallBack.

        备注。

        :param remark: The remark of this VmsCallBack.
        :type remark: str
        """
        self._remark = remark

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
        if not isinstance(other, VmsCallBack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
