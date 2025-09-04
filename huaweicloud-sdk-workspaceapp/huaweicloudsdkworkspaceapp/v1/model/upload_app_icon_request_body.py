# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadAppIconRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'file',
        'icon_url': 'str'
    }

    attribute_map = {
        'data': 'data',
        'icon_url': 'icon_url'
    }

    def __init__(self, data=None, icon_url=None):
        r"""UploadAppIconRequestBody

        The model defined in huaweicloud sdk

        :param data: 应用图标，png格式，限制大小8KB。
        :type data: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param icon_url: base64编码后的png格式图标。
        :type icon_url: str
        """
        
        

        self._data = None
        self._icon_url = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if icon_url is not None:
            self.icon_url = icon_url

    @property
    def data(self):
        r"""Gets the data of this UploadAppIconRequestBody.

        应用图标，png格式，限制大小8KB。

        :return: The data of this UploadAppIconRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this UploadAppIconRequestBody.

        应用图标，png格式，限制大小8KB。

        :param data: The data of this UploadAppIconRequestBody.
        :type data: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._data = data

    @property
    def icon_url(self):
        r"""Gets the icon_url of this UploadAppIconRequestBody.

        base64编码后的png格式图标。

        :return: The icon_url of this UploadAppIconRequestBody.
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        r"""Sets the icon_url of this UploadAppIconRequestBody.

        base64编码后的png格式图标。

        :param icon_url: The icon_url of this UploadAppIconRequestBody.
        :type icon_url: str
        """
        self._icon_url = icon_url

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
        if not isinstance(other, UploadAppIconRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
