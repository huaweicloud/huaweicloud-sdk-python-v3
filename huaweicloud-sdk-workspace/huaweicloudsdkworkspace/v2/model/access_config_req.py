# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessConfigReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_mode': 'str',
        'dedicated_cidrs': 'str'
    }

    attribute_map = {
        'access_mode': 'access_mode',
        'dedicated_cidrs': 'dedicated_cidrs'
    }

    def __init__(self, access_mode=None, dedicated_cidrs=None):
        r"""AccessConfigReq

        The model defined in huaweicloud sdk

        :param access_mode: 接入方式。 - INTERNET：表示Internet接入。 - DEDICATED：表示专线接入。 - BOTH：表示两种接入方式都支持。
        :type access_mode: str
        :param dedicated_cidrs: 专线接入网段列表，多个网段信息用分号隔开，列表长度不超过5。
        :type dedicated_cidrs: str
        """
        
        

        self._access_mode = None
        self._dedicated_cidrs = None
        self.discriminator = None

        self.access_mode = access_mode
        if dedicated_cidrs is not None:
            self.dedicated_cidrs = dedicated_cidrs

    @property
    def access_mode(self):
        r"""Gets the access_mode of this AccessConfigReq.

        接入方式。 - INTERNET：表示Internet接入。 - DEDICATED：表示专线接入。 - BOTH：表示两种接入方式都支持。

        :return: The access_mode of this AccessConfigReq.
        :rtype: str
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        r"""Sets the access_mode of this AccessConfigReq.

        接入方式。 - INTERNET：表示Internet接入。 - DEDICATED：表示专线接入。 - BOTH：表示两种接入方式都支持。

        :param access_mode: The access_mode of this AccessConfigReq.
        :type access_mode: str
        """
        self._access_mode = access_mode

    @property
    def dedicated_cidrs(self):
        r"""Gets the dedicated_cidrs of this AccessConfigReq.

        专线接入网段列表，多个网段信息用分号隔开，列表长度不超过5。

        :return: The dedicated_cidrs of this AccessConfigReq.
        :rtype: str
        """
        return self._dedicated_cidrs

    @dedicated_cidrs.setter
    def dedicated_cidrs(self, dedicated_cidrs):
        r"""Sets the dedicated_cidrs of this AccessConfigReq.

        专线接入网段列表，多个网段信息用分号隔开，列表长度不超过5。

        :param dedicated_cidrs: The dedicated_cidrs of this AccessConfigReq.
        :type dedicated_cidrs: str
        """
        self._dedicated_cidrs = dedicated_cidrs

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
        if not isinstance(other, AccessConfigReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
