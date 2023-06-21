# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVmsTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tplid': 'str'
    }

    attribute_map = {
        'tplid': 'tplid'
    }

    def __init__(self, tplid=None):
        """CreateVmsTemplateResponse

        The model defined in huaweicloud sdk

        :param tplid: 智能信息基础版模板ID，用来唯一标识上传的模板。
        :type tplid: str
        """
        
        super(CreateVmsTemplateResponse, self).__init__()

        self._tplid = None
        self.discriminator = None

        if tplid is not None:
            self.tplid = tplid

    @property
    def tplid(self):
        """Gets the tplid of this CreateVmsTemplateResponse.

        智能信息基础版模板ID，用来唯一标识上传的模板。

        :return: The tplid of this CreateVmsTemplateResponse.
        :rtype: str
        """
        return self._tplid

    @tplid.setter
    def tplid(self, tplid):
        """Sets the tplid of this CreateVmsTemplateResponse.

        智能信息基础版模板ID，用来唯一标识上传的模板。

        :param tplid: The tplid of this CreateVmsTemplateResponse.
        :type tplid: str
        """
        self._tplid = tplid

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
        if not isinstance(other, CreateVmsTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
