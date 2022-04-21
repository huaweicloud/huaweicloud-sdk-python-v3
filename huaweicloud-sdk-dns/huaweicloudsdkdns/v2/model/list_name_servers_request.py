# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNameServersRequest:

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
        'region': 'str'
    }

    attribute_map = {
        'type': 'type',
        'region': 'region'
    }

    def __init__(self, type=None, region=None):
        """ListNameServersRequest

        The model defined in huaweicloud sdk

        :param type: 待查询名称服务器的类型。 取值范围: public, private。 如果为空，表示查询所有类型的名称服务器。 如果为public，表示查询公网的名称服务器。 如果为private，表示查询内网的名称服务器。 搜索模式精确搜索。 默认值为空。
        :type type: str
        :param region: 待查询的region ID。 当查询公网的名称服务器时，此处不填。 搜索模式精确搜索。 默认值为空。
        :type region: str
        """
        
        

        self._type = None
        self._region = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if region is not None:
            self.region = region

    @property
    def type(self):
        """Gets the type of this ListNameServersRequest.

        待查询名称服务器的类型。 取值范围: public, private。 如果为空，表示查询所有类型的名称服务器。 如果为public，表示查询公网的名称服务器。 如果为private，表示查询内网的名称服务器。 搜索模式精确搜索。 默认值为空。

        :return: The type of this ListNameServersRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListNameServersRequest.

        待查询名称服务器的类型。 取值范围: public, private。 如果为空，表示查询所有类型的名称服务器。 如果为public，表示查询公网的名称服务器。 如果为private，表示查询内网的名称服务器。 搜索模式精确搜索。 默认值为空。

        :param type: The type of this ListNameServersRequest.
        :type type: str
        """
        self._type = type

    @property
    def region(self):
        """Gets the region of this ListNameServersRequest.

        待查询的region ID。 当查询公网的名称服务器时，此处不填。 搜索模式精确搜索。 默认值为空。

        :return: The region of this ListNameServersRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListNameServersRequest.

        待查询的region ID。 当查询公网的名称服务器时，此处不填。 搜索模式精确搜索。 默认值为空。

        :param region: The region of this ListNameServersRequest.
        :type region: str
        """
        self._region = region

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
        if not isinstance(other, ListNameServersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
