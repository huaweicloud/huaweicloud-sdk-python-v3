# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetKvResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kv_doc': 'dict'
    }

    attribute_map = {
        'kv_doc': 'kv_doc'
    }

    def __init__(self, kv_doc=None):
        r"""GetKvResponse

        The model defined in huaweicloud sdk

        :param kv_doc: 对kv_doc有效。 &gt; 内容字段：主键字段+投影字段或者全部字段。
        :type kv_doc: dict
        """
        
        super(GetKvResponse, self).__init__()

        self._kv_doc = None
        self.discriminator = None

        if kv_doc is not None:
            self.kv_doc = kv_doc

    @property
    def kv_doc(self):
        r"""Gets the kv_doc of this GetKvResponse.

        对kv_doc有效。 > 内容字段：主键字段+投影字段或者全部字段。

        :return: The kv_doc of this GetKvResponse.
        :rtype: dict
        """
        return self._kv_doc

    @kv_doc.setter
    def kv_doc(self, kv_doc):
        r"""Sets the kv_doc of this GetKvResponse.

        对kv_doc有效。 > 内容字段：主键字段+投影字段或者全部字段。

        :param kv_doc: The kv_doc of this GetKvResponse.
        :type kv_doc: dict
        """
        self._kv_doc = kv_doc

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
        if not isinstance(other, GetKvResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
