# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateArchiveRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'urn': 'str'
    }

    attribute_map = {
        'id': 'id',
        'urn': 'urn'
    }

    def __init__(self, id=None, urn=None):
        """CreateArchiveRuleResponse

        The model defined in huaweicloud sdk

        :param id: 存档规则的唯一标识符。
        :type id: str
        :param urn: 唯一的资源名称。
        :type urn: str
        """
        
        super(CreateArchiveRuleResponse, self).__init__()

        self._id = None
        self._urn = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if urn is not None:
            self.urn = urn

    @property
    def id(self):
        """Gets the id of this CreateArchiveRuleResponse.

        存档规则的唯一标识符。

        :return: The id of this CreateArchiveRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateArchiveRuleResponse.

        存档规则的唯一标识符。

        :param id: The id of this CreateArchiveRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def urn(self):
        """Gets the urn of this CreateArchiveRuleResponse.

        唯一的资源名称。

        :return: The urn of this CreateArchiveRuleResponse.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this CreateArchiveRuleResponse.

        唯一的资源名称。

        :param urn: The urn of this CreateArchiveRuleResponse.
        :type urn: str
        """
        self._urn = urn

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
        if not isinstance(other, CreateArchiveRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
