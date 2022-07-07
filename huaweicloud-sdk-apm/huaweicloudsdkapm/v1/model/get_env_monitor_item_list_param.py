# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetEnvMonitorItemListParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'env_id': 'int',
        'page': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'env_id': 'env_id',
        'page': 'page',
        'page_size': 'page_size'
    }

    def __init__(self, env_id=None, page=None, page_size=None):
        """GetEnvMonitorItemListParam

        The model defined in huaweicloud sdk

        :param env_id: 环境id
        :type env_id: int
        :param page: 页码
        :type page: int
        :param page_size: 每页数量
        :type page_size: int
        """
        
        

        self._env_id = None
        self._page = None
        self._page_size = None
        self.discriminator = None

        self.env_id = env_id
        self.page = page
        self.page_size = page_size

    @property
    def env_id(self):
        """Gets the env_id of this GetEnvMonitorItemListParam.

        环境id

        :return: The env_id of this GetEnvMonitorItemListParam.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this GetEnvMonitorItemListParam.

        环境id

        :param env_id: The env_id of this GetEnvMonitorItemListParam.
        :type env_id: int
        """
        self._env_id = env_id

    @property
    def page(self):
        """Gets the page of this GetEnvMonitorItemListParam.

        页码

        :return: The page of this GetEnvMonitorItemListParam.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this GetEnvMonitorItemListParam.

        页码

        :param page: The page of this GetEnvMonitorItemListParam.
        :type page: int
        """
        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this GetEnvMonitorItemListParam.

        每页数量

        :return: The page_size of this GetEnvMonitorItemListParam.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GetEnvMonitorItemListParam.

        每页数量

        :param page_size: The page_size of this GetEnvMonitorItemListParam.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, GetEnvMonitorItemListParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
