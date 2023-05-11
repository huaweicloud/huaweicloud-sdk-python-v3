# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlavorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'engine_name': 'str'
    }

    attribute_map = {
        'region': 'region',
        'engine_name': 'engine_name'
    }

    def __init__(self, region=None, engine_name=None):
        """ListFlavorsRequest

        The model defined in huaweicloud sdk

        :param region: 实例所在区域。
        :type region: str
        :param engine_name: 数据库版本类型。取值为“DDS-Community”。
        :type engine_name: str
        """
        
        

        self._region = None
        self._engine_name = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if engine_name is not None:
            self.engine_name = engine_name

    @property
    def region(self):
        """Gets the region of this ListFlavorsRequest.

        实例所在区域。

        :return: The region of this ListFlavorsRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListFlavorsRequest.

        实例所在区域。

        :param region: The region of this ListFlavorsRequest.
        :type region: str
        """
        self._region = region

    @property
    def engine_name(self):
        """Gets the engine_name of this ListFlavorsRequest.

        数据库版本类型。取值为“DDS-Community”。

        :return: The engine_name of this ListFlavorsRequest.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        """Sets the engine_name of this ListFlavorsRequest.

        数据库版本类型。取值为“DDS-Community”。

        :param engine_name: The engine_name of this ListFlavorsRequest.
        :type engine_name: str
        """
        self._engine_name = engine_name

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
        if not isinstance(other, ListFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
