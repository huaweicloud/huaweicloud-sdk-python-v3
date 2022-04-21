# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataCenterV2Do:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'int',
        'region_id': 'str',
        'region_name': 'str',
        'is_sensitive': 'int'
    }

    attribute_map = {
        'type': 'type',
        'region_id': 'region_id',
        'region_name': 'region_name',
        'is_sensitive': 'is_sensitive'
    }

    def __init__(self, type=None, region_id=None, region_name=None, is_sensitive=None):
        """DataCenterV2Do

        The model defined in huaweicloud sdk

        :param type: 区域类型0大陆 1国际
        :type type: int
        :param region_id: 区域id
        :type region_id: str
        :param region_name: 区域名称
        :type region_name: str
        :param is_sensitive: 是否敏感
        :type is_sensitive: int
        """
        
        

        self._type = None
        self._region_id = None
        self._region_name = None
        self._is_sensitive = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if region_id is not None:
            self.region_id = region_id
        if region_name is not None:
            self.region_name = region_name
        if is_sensitive is not None:
            self.is_sensitive = is_sensitive

    @property
    def type(self):
        """Gets the type of this DataCenterV2Do.

        区域类型0大陆 1国际

        :return: The type of this DataCenterV2Do.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DataCenterV2Do.

        区域类型0大陆 1国际

        :param type: The type of this DataCenterV2Do.
        :type type: int
        """
        self._type = type

    @property
    def region_id(self):
        """Gets the region_id of this DataCenterV2Do.

        区域id

        :return: The region_id of this DataCenterV2Do.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this DataCenterV2Do.

        区域id

        :param region_id: The region_id of this DataCenterV2Do.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def region_name(self):
        """Gets the region_name of this DataCenterV2Do.

        区域名称

        :return: The region_name of this DataCenterV2Do.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this DataCenterV2Do.

        区域名称

        :param region_name: The region_name of this DataCenterV2Do.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def is_sensitive(self):
        """Gets the is_sensitive of this DataCenterV2Do.

        是否敏感

        :return: The is_sensitive of this DataCenterV2Do.
        :rtype: int
        """
        return self._is_sensitive

    @is_sensitive.setter
    def is_sensitive(self, is_sensitive):
        """Sets the is_sensitive of this DataCenterV2Do.

        是否敏感

        :param is_sensitive: The is_sensitive of this DataCenterV2Do.
        :type is_sensitive: int
        """
        self._is_sensitive = is_sensitive

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
        if not isinstance(other, DataCenterV2Do):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
