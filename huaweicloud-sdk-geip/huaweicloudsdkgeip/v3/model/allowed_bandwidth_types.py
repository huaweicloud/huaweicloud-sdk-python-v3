# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AllowedBandwidthTypes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'cn_name': 'str',
        'en_name': 'str'
    }

    attribute_map = {
        'type': 'type',
        'cn_name': 'cn_name',
        'en_name': 'en_name'
    }

    def __init__(self, type=None, cn_name=None, en_name=None):
        r"""AllowedBandwidthTypes

        The model defined in huaweicloud sdk

        :param type: 全域公网带宽类型名称
        :type type: str
        :param cn_name: 中文名称
        :type cn_name: str
        :param en_name: 英文名称
        :type en_name: str
        """
        
        

        self._type = None
        self._cn_name = None
        self._en_name = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if cn_name is not None:
            self.cn_name = cn_name
        if en_name is not None:
            self.en_name = en_name

    @property
    def type(self):
        r"""Gets the type of this AllowedBandwidthTypes.

        全域公网带宽类型名称

        :return: The type of this AllowedBandwidthTypes.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AllowedBandwidthTypes.

        全域公网带宽类型名称

        :param type: The type of this AllowedBandwidthTypes.
        :type type: str
        """
        self._type = type

    @property
    def cn_name(self):
        r"""Gets the cn_name of this AllowedBandwidthTypes.

        中文名称

        :return: The cn_name of this AllowedBandwidthTypes.
        :rtype: str
        """
        return self._cn_name

    @cn_name.setter
    def cn_name(self, cn_name):
        r"""Sets the cn_name of this AllowedBandwidthTypes.

        中文名称

        :param cn_name: The cn_name of this AllowedBandwidthTypes.
        :type cn_name: str
        """
        self._cn_name = cn_name

    @property
    def en_name(self):
        r"""Gets the en_name of this AllowedBandwidthTypes.

        英文名称

        :return: The en_name of this AllowedBandwidthTypes.
        :rtype: str
        """
        return self._en_name

    @en_name.setter
    def en_name(self, en_name):
        r"""Sets the en_name of this AllowedBandwidthTypes.

        英文名称

        :param en_name: The en_name of this AllowedBandwidthTypes.
        :type en_name: str
        """
        self._en_name = en_name

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
        if not isinstance(other, AllowedBandwidthTypes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
