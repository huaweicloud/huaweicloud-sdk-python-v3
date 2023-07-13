# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddVmsCallBackRequestBody:

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
        """AddVmsCallBackRequestBody

        The model defined in huaweicloud sdk

        :param url_type: 回调类型。  - 0：发送状态回执 - 1：上行消息回执 
        :type url_type: int
        :param callback_url: 回调地址，必须是http或https开头的字符串，不能为空。  &gt; 建议使用https。 
        :type callback_url: str
        :param remark: 备注。
        :type remark: str
        """
        
        

        self._url_type = None
        self._callback_url = None
        self._remark = None
        self.discriminator = None

        self.url_type = url_type
        self.callback_url = callback_url
        if remark is not None:
            self.remark = remark

    @property
    def url_type(self):
        """Gets the url_type of this AddVmsCallBackRequestBody.

        回调类型。  - 0：发送状态回执 - 1：上行消息回执 

        :return: The url_type of this AddVmsCallBackRequestBody.
        :rtype: int
        """
        return self._url_type

    @url_type.setter
    def url_type(self, url_type):
        """Sets the url_type of this AddVmsCallBackRequestBody.

        回调类型。  - 0：发送状态回执 - 1：上行消息回执 

        :param url_type: The url_type of this AddVmsCallBackRequestBody.
        :type url_type: int
        """
        self._url_type = url_type

    @property
    def callback_url(self):
        """Gets the callback_url of this AddVmsCallBackRequestBody.

        回调地址，必须是http或https开头的字符串，不能为空。  > 建议使用https。 

        :return: The callback_url of this AddVmsCallBackRequestBody.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """Sets the callback_url of this AddVmsCallBackRequestBody.

        回调地址，必须是http或https开头的字符串，不能为空。  > 建议使用https。 

        :param callback_url: The callback_url of this AddVmsCallBackRequestBody.
        :type callback_url: str
        """
        self._callback_url = callback_url

    @property
    def remark(self):
        """Gets the remark of this AddVmsCallBackRequestBody.

        备注。

        :return: The remark of this AddVmsCallBackRequestBody.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this AddVmsCallBackRequestBody.

        备注。

        :param remark: The remark of this AddVmsCallBackRequestBody.
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
        if not isinstance(other, AddVmsCallBackRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
