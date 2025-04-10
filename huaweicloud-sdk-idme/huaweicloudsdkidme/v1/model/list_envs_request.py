# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnvsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_num': 'int',
        'page_size': 'int',
        'env_types': 'str'
    }

    attribute_map = {
        'page_num': 'page_num',
        'page_size': 'page_size',
        'env_types': 'env_types'
    }

    def __init__(self, page_num=None, page_size=None, env_types=None):
        r"""ListEnvsRequest

        The model defined in huaweicloud sdk

        :param page_num: 页码
        :type page_num: int
        :param page_size: 当前页大小
        :type page_size: int
        :param env_types: 云服务类型 - STUDIO：设计态服务。 - CLOUD_BASIC：公有云基础版数据建模引擎。 - CLOUD_TRIAL：公有云体验版数据建模引擎。 - EDGE_BASIC：边缘云基础版数据建模引擎。 - CLOUD_LINKX：公有云基础版数字主线引擎。 - EDGE_LINKX：边缘云基础版数字主线引擎。
        :type env_types: str
        """
        
        

        self._page_num = None
        self._page_size = None
        self._env_types = None
        self.discriminator = None

        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size
        if env_types is not None:
            self.env_types = env_types

    @property
    def page_num(self):
        r"""Gets the page_num of this ListEnvsRequest.

        页码

        :return: The page_num of this ListEnvsRequest.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        r"""Sets the page_num of this ListEnvsRequest.

        页码

        :param page_num: The page_num of this ListEnvsRequest.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        r"""Gets the page_size of this ListEnvsRequest.

        当前页大小

        :return: The page_size of this ListEnvsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListEnvsRequest.

        当前页大小

        :param page_size: The page_size of this ListEnvsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def env_types(self):
        r"""Gets the env_types of this ListEnvsRequest.

        云服务类型 - STUDIO：设计态服务。 - CLOUD_BASIC：公有云基础版数据建模引擎。 - CLOUD_TRIAL：公有云体验版数据建模引擎。 - EDGE_BASIC：边缘云基础版数据建模引擎。 - CLOUD_LINKX：公有云基础版数字主线引擎。 - EDGE_LINKX：边缘云基础版数字主线引擎。

        :return: The env_types of this ListEnvsRequest.
        :rtype: str
        """
        return self._env_types

    @env_types.setter
    def env_types(self, env_types):
        r"""Sets the env_types of this ListEnvsRequest.

        云服务类型 - STUDIO：设计态服务。 - CLOUD_BASIC：公有云基础版数据建模引擎。 - CLOUD_TRIAL：公有云体验版数据建模引擎。 - EDGE_BASIC：边缘云基础版数据建模引擎。 - CLOUD_LINKX：公有云基础版数字主线引擎。 - EDGE_LINKX：边缘云基础版数字主线引擎。

        :param env_types: The env_types of this ListEnvsRequest.
        :type env_types: str
        """
        self._env_types = env_types

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
        if not isinstance(other, ListEnvsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
