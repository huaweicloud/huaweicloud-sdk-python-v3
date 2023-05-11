# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCategoryListRequest:

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
        'scene_name': 'str',
        'support_ide': 'int',
        'type': 'int'
    }

    attribute_map = {
        'page_num': 'page_num',
        'page_size': 'page_size',
        'scene_name': 'scene_name',
        'support_ide': 'support_ide',
        'type': 'type'
    }

    def __init__(self, page_num=None, page_size=None, scene_name=None, support_ide=None, type=None):
        """ShowCategoryListRequest

        The model defined in huaweicloud sdk

        :param page_num: 页码
        :type page_num: int
        :param page_size: 分页大小
        :type page_size: int
        :param scene_name: 场景名称
        :type scene_name: str
        :param support_ide: 支持的ide
        :type support_ide: int
        :param type: 数据来源
        :type type: int
        """
        
        

        self._page_num = None
        self._page_size = None
        self._scene_name = None
        self._support_ide = None
        self._type = None
        self.discriminator = None

        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size
        if scene_name is not None:
            self.scene_name = scene_name
        if support_ide is not None:
            self.support_ide = support_ide
        if type is not None:
            self.type = type

    @property
    def page_num(self):
        """Gets the page_num of this ShowCategoryListRequest.

        页码

        :return: The page_num of this ShowCategoryListRequest.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this ShowCategoryListRequest.

        页码

        :param page_num: The page_num of this ShowCategoryListRequest.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this ShowCategoryListRequest.

        分页大小

        :return: The page_size of this ShowCategoryListRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ShowCategoryListRequest.

        分页大小

        :param page_size: The page_size of this ShowCategoryListRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def scene_name(self):
        """Gets the scene_name of this ShowCategoryListRequest.

        场景名称

        :return: The scene_name of this ShowCategoryListRequest.
        :rtype: str
        """
        return self._scene_name

    @scene_name.setter
    def scene_name(self, scene_name):
        """Sets the scene_name of this ShowCategoryListRequest.

        场景名称

        :param scene_name: The scene_name of this ShowCategoryListRequest.
        :type scene_name: str
        """
        self._scene_name = scene_name

    @property
    def support_ide(self):
        """Gets the support_ide of this ShowCategoryListRequest.

        支持的ide

        :return: The support_ide of this ShowCategoryListRequest.
        :rtype: int
        """
        return self._support_ide

    @support_ide.setter
    def support_ide(self, support_ide):
        """Sets the support_ide of this ShowCategoryListRequest.

        支持的ide

        :param support_ide: The support_ide of this ShowCategoryListRequest.
        :type support_ide: int
        """
        self._support_ide = support_ide

    @property
    def type(self):
        """Gets the type of this ShowCategoryListRequest.

        数据来源

        :return: The type of this ShowCategoryListRequest.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowCategoryListRequest.

        数据来源

        :param type: The type of this ShowCategoryListRequest.
        :type type: int
        """
        self._type = type

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
        if not isinstance(other, ShowCategoryListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
