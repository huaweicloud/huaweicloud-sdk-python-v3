# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTopologyTreeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'business_id': 'int',
        'env_tag_id': 'int',
        'env_keyword': 'str',
        'x_business_id': 'int'
    }

    attribute_map = {
        'region_id': 'region_id',
        'business_id': 'business_id',
        'env_tag_id': 'env_tag_id',
        'env_keyword': 'env_keyword',
        'x_business_id': 'x-business-id'
    }

    def __init__(self, region_id=None, business_id=None, env_tag_id=None, env_keyword=None, x_business_id=None):
        """ShowTopologyTreeRequest

        The model defined in huaweicloud sdk

        :param region_id: 区域id。
        :type region_id: str
        :param business_id: 应用id。
        :type business_id: int
        :param env_tag_id: 环境标签id。
        :type env_tag_id: int
        :param env_keyword: 环境关键字。
        :type env_keyword: str
        :param x_business_id: 应用id。
        :type x_business_id: int
        """
        
        

        self._region_id = None
        self._business_id = None
        self._env_tag_id = None
        self._env_keyword = None
        self._x_business_id = None
        self.discriminator = None

        if region_id is not None:
            self.region_id = region_id
        self.business_id = business_id
        if env_tag_id is not None:
            self.env_tag_id = env_tag_id
        if env_keyword is not None:
            self.env_keyword = env_keyword
        self.x_business_id = x_business_id

    @property
    def region_id(self):
        """Gets the region_id of this ShowTopologyTreeRequest.

        区域id。

        :return: The region_id of this ShowTopologyTreeRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ShowTopologyTreeRequest.

        区域id。

        :param region_id: The region_id of this ShowTopologyTreeRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def business_id(self):
        """Gets the business_id of this ShowTopologyTreeRequest.

        应用id。

        :return: The business_id of this ShowTopologyTreeRequest.
        :rtype: int
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this ShowTopologyTreeRequest.

        应用id。

        :param business_id: The business_id of this ShowTopologyTreeRequest.
        :type business_id: int
        """
        self._business_id = business_id

    @property
    def env_tag_id(self):
        """Gets the env_tag_id of this ShowTopologyTreeRequest.

        环境标签id。

        :return: The env_tag_id of this ShowTopologyTreeRequest.
        :rtype: int
        """
        return self._env_tag_id

    @env_tag_id.setter
    def env_tag_id(self, env_tag_id):
        """Sets the env_tag_id of this ShowTopologyTreeRequest.

        环境标签id。

        :param env_tag_id: The env_tag_id of this ShowTopologyTreeRequest.
        :type env_tag_id: int
        """
        self._env_tag_id = env_tag_id

    @property
    def env_keyword(self):
        """Gets the env_keyword of this ShowTopologyTreeRequest.

        环境关键字。

        :return: The env_keyword of this ShowTopologyTreeRequest.
        :rtype: str
        """
        return self._env_keyword

    @env_keyword.setter
    def env_keyword(self, env_keyword):
        """Sets the env_keyword of this ShowTopologyTreeRequest.

        环境关键字。

        :param env_keyword: The env_keyword of this ShowTopologyTreeRequest.
        :type env_keyword: str
        """
        self._env_keyword = env_keyword

    @property
    def x_business_id(self):
        """Gets the x_business_id of this ShowTopologyTreeRequest.

        应用id。

        :return: The x_business_id of this ShowTopologyTreeRequest.
        :rtype: int
        """
        return self._x_business_id

    @x_business_id.setter
    def x_business_id(self, x_business_id):
        """Sets the x_business_id of this ShowTopologyTreeRequest.

        应用id。

        :param x_business_id: The x_business_id of this ShowTopologyTreeRequest.
        :type x_business_id: int
        """
        self._x_business_id = x_business_id

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
        if not isinstance(other, ShowTopologyTreeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
