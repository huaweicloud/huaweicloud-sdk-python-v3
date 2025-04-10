# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddBridge:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bridge_name': 'str',
        'bridge_id': 'str'
    }

    attribute_map = {
        'bridge_name': 'bridge_name',
        'bridge_id': 'bridge_id'
    }

    def __init__(self, bridge_name=None, bridge_id=None):
        r"""AddBridge

        The model defined in huaweicloud sdk

        :param bridge_name: 网桥名称。**取值范围**：长度不超过64，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合。
        :type bridge_name: str
        :param bridge_id: 网桥ID。**取值范围**：长度不超过36，只允许字母、数字、_-字符的组合。
        :type bridge_id: str
        """
        
        

        self._bridge_name = None
        self._bridge_id = None
        self.discriminator = None

        self.bridge_name = bridge_name
        if bridge_id is not None:
            self.bridge_id = bridge_id

    @property
    def bridge_name(self):
        r"""Gets the bridge_name of this AddBridge.

        网桥名称。**取值范围**：长度不超过64，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :return: The bridge_name of this AddBridge.
        :rtype: str
        """
        return self._bridge_name

    @bridge_name.setter
    def bridge_name(self, bridge_name):
        r"""Sets the bridge_name of this AddBridge.

        网桥名称。**取值范围**：长度不超过64，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :param bridge_name: The bridge_name of this AddBridge.
        :type bridge_name: str
        """
        self._bridge_name = bridge_name

    @property
    def bridge_id(self):
        r"""Gets the bridge_id of this AddBridge.

        网桥ID。**取值范围**：长度不超过36，只允许字母、数字、_-字符的组合。

        :return: The bridge_id of this AddBridge.
        :rtype: str
        """
        return self._bridge_id

    @bridge_id.setter
    def bridge_id(self, bridge_id):
        r"""Sets the bridge_id of this AddBridge.

        网桥ID。**取值范围**：长度不超过36，只允许字母、数字、_-字符的组合。

        :param bridge_id: The bridge_id of this AddBridge.
        :type bridge_id: str
        """
        self._bridge_id = bridge_id

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
        if not isinstance(other, AddBridge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
