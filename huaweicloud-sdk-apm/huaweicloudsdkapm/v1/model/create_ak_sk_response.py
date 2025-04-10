# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAkSkResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ak': 'str',
        'sk': 'str'
    }

    attribute_map = {
        'ak': 'ak',
        'sk': 'sk'
    }

    def __init__(self, ak=None, sk=None):
        r"""CreateAkSkResponse

        The model defined in huaweicloud sdk

        :param ak: 创建/删除的ak信息。
        :type ak: str
        :param sk: 创建/删除的sk信息。
        :type sk: str
        """
        
        super(CreateAkSkResponse, self).__init__()

        self._ak = None
        self._sk = None
        self.discriminator = None

        if ak is not None:
            self.ak = ak
        if sk is not None:
            self.sk = sk

    @property
    def ak(self):
        r"""Gets the ak of this CreateAkSkResponse.

        创建/删除的ak信息。

        :return: The ak of this CreateAkSkResponse.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        r"""Sets the ak of this CreateAkSkResponse.

        创建/删除的ak信息。

        :param ak: The ak of this CreateAkSkResponse.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        r"""Gets the sk of this CreateAkSkResponse.

        创建/删除的sk信息。

        :return: The sk of this CreateAkSkResponse.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        r"""Sets the sk of this CreateAkSkResponse.

        创建/删除的sk信息。

        :param sk: The sk of this CreateAkSkResponse.
        :type sk: str
        """
        self._sk = sk

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
        if not isinstance(other, CreateAkSkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
