# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionTagInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_name_zh': 'str',
        'action_name_en': 'str',
        'catalog': 'str',
        'file_name': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'action_name_zh': 'action_name_zh',
        'action_name_en': 'action_name_en',
        'catalog': 'catalog',
        'file_name': 'file_name',
        'tag': 'tag'
    }

    def __init__(self, action_name_zh=None, action_name_en=None, catalog=None, file_name=None, tag=None):
        """ActionTagInfo

        The model defined in huaweicloud sdk

        :param action_name_zh: 原子动作中文名称。
        :type action_name_zh: str
        :param action_name_en: 原子动作英文名称。
        :type action_name_en: str
        :param catalog: 动作分类名称。
        :type catalog: str
        :param file_name: 样例视频文件名，最大长度256，最小长度1。
        :type file_name: str
        :param tag: 动作标签。
        :type tag: str
        """
        
        

        self._action_name_zh = None
        self._action_name_en = None
        self._catalog = None
        self._file_name = None
        self._tag = None
        self.discriminator = None

        self.action_name_zh = action_name_zh
        self.action_name_en = action_name_en
        if catalog is not None:
            self.catalog = catalog
        if file_name is not None:
            self.file_name = file_name
        if tag is not None:
            self.tag = tag

    @property
    def action_name_zh(self):
        """Gets the action_name_zh of this ActionTagInfo.

        原子动作中文名称。

        :return: The action_name_zh of this ActionTagInfo.
        :rtype: str
        """
        return self._action_name_zh

    @action_name_zh.setter
    def action_name_zh(self, action_name_zh):
        """Sets the action_name_zh of this ActionTagInfo.

        原子动作中文名称。

        :param action_name_zh: The action_name_zh of this ActionTagInfo.
        :type action_name_zh: str
        """
        self._action_name_zh = action_name_zh

    @property
    def action_name_en(self):
        """Gets the action_name_en of this ActionTagInfo.

        原子动作英文名称。

        :return: The action_name_en of this ActionTagInfo.
        :rtype: str
        """
        return self._action_name_en

    @action_name_en.setter
    def action_name_en(self, action_name_en):
        """Sets the action_name_en of this ActionTagInfo.

        原子动作英文名称。

        :param action_name_en: The action_name_en of this ActionTagInfo.
        :type action_name_en: str
        """
        self._action_name_en = action_name_en

    @property
    def catalog(self):
        """Gets the catalog of this ActionTagInfo.

        动作分类名称。

        :return: The catalog of this ActionTagInfo.
        :rtype: str
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        """Sets the catalog of this ActionTagInfo.

        动作分类名称。

        :param catalog: The catalog of this ActionTagInfo.
        :type catalog: str
        """
        self._catalog = catalog

    @property
    def file_name(self):
        """Gets the file_name of this ActionTagInfo.

        样例视频文件名，最大长度256，最小长度1。

        :return: The file_name of this ActionTagInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ActionTagInfo.

        样例视频文件名，最大长度256，最小长度1。

        :param file_name: The file_name of this ActionTagInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def tag(self):
        """Gets the tag of this ActionTagInfo.

        动作标签。

        :return: The tag of this ActionTagInfo.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ActionTagInfo.

        动作标签。

        :param tag: The tag of this ActionTagInfo.
        :type tag: str
        """
        self._tag = tag

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
        if not isinstance(other, ActionTagInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
