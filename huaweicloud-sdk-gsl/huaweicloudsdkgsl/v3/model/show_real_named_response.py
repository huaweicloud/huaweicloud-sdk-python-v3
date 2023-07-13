# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRealNamedResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iccid': 'str',
        'real_named': 'bool'
    }

    attribute_map = {
        'iccid': 'iccid',
        'real_named': 'real_named'
    }

    def __init__(self, iccid=None, real_named=None):
        """ShowRealNamedResponse

        The model defined in huaweicloud sdk

        :param iccid: ICCID
        :type iccid: str
        :param real_named: 是否已实名认证: true表示是，false表示否。
        :type real_named: bool
        """
        
        super(ShowRealNamedResponse, self).__init__()

        self._iccid = None
        self._real_named = None
        self.discriminator = None

        if iccid is not None:
            self.iccid = iccid
        if real_named is not None:
            self.real_named = real_named

    @property
    def iccid(self):
        """Gets the iccid of this ShowRealNamedResponse.

        ICCID

        :return: The iccid of this ShowRealNamedResponse.
        :rtype: str
        """
        return self._iccid

    @iccid.setter
    def iccid(self, iccid):
        """Sets the iccid of this ShowRealNamedResponse.

        ICCID

        :param iccid: The iccid of this ShowRealNamedResponse.
        :type iccid: str
        """
        self._iccid = iccid

    @property
    def real_named(self):
        """Gets the real_named of this ShowRealNamedResponse.

        是否已实名认证: true表示是，false表示否。

        :return: The real_named of this ShowRealNamedResponse.
        :rtype: bool
        """
        return self._real_named

    @real_named.setter
    def real_named(self, real_named):
        """Sets the real_named of this ShowRealNamedResponse.

        是否已实名认证: true表示是，false表示否。

        :param real_named: The real_named of this ShowRealNamedResponse.
        :type real_named: bool
        """
        self._real_named = real_named

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
        if not isinstance(other, ShowRealNamedResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
