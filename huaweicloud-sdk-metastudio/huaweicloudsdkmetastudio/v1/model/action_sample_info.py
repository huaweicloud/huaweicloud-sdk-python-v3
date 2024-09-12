# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionSampleInfo:

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
        'action_tag': 'str',
        'catalog': 'str',
        'is_selected': 'bool',
        'sample_download_url': 'str'
    }

    attribute_map = {
        'action_name_zh': 'action_name_zh',
        'action_name_en': 'action_name_en',
        'action_tag': 'action_tag',
        'catalog': 'catalog',
        'is_selected': 'is_selected',
        'sample_download_url': 'sample_download_url'
    }

    def __init__(self, action_name_zh=None, action_name_en=None, action_tag=None, catalog=None, is_selected=None, sample_download_url=None):
        """ActionSampleInfo

        The model defined in huaweicloud sdk

        :param action_name_zh: 原子动作中文名称。
        :type action_name_zh: str
        :param action_name_en: 原子动作英文名称。
        :type action_name_en: str
        :param action_tag: 动作Tag。
        :type action_tag: str
        :param catalog: 动作分类名称。
        :type catalog: str
        :param is_selected: 是否选择此动作。
        :type is_selected: bool
        :param sample_download_url: 原子动作样例文件下载地址。24小时内有效。
        :type sample_download_url: str
        """
        
        

        self._action_name_zh = None
        self._action_name_en = None
        self._action_tag = None
        self._catalog = None
        self._is_selected = None
        self._sample_download_url = None
        self.discriminator = None

        if action_name_zh is not None:
            self.action_name_zh = action_name_zh
        if action_name_en is not None:
            self.action_name_en = action_name_en
        self.action_tag = action_tag
        if catalog is not None:
            self.catalog = catalog
        if is_selected is not None:
            self.is_selected = is_selected
        if sample_download_url is not None:
            self.sample_download_url = sample_download_url

    @property
    def action_name_zh(self):
        """Gets the action_name_zh of this ActionSampleInfo.

        原子动作中文名称。

        :return: The action_name_zh of this ActionSampleInfo.
        :rtype: str
        """
        return self._action_name_zh

    @action_name_zh.setter
    def action_name_zh(self, action_name_zh):
        """Sets the action_name_zh of this ActionSampleInfo.

        原子动作中文名称。

        :param action_name_zh: The action_name_zh of this ActionSampleInfo.
        :type action_name_zh: str
        """
        self._action_name_zh = action_name_zh

    @property
    def action_name_en(self):
        """Gets the action_name_en of this ActionSampleInfo.

        原子动作英文名称。

        :return: The action_name_en of this ActionSampleInfo.
        :rtype: str
        """
        return self._action_name_en

    @action_name_en.setter
    def action_name_en(self, action_name_en):
        """Sets the action_name_en of this ActionSampleInfo.

        原子动作英文名称。

        :param action_name_en: The action_name_en of this ActionSampleInfo.
        :type action_name_en: str
        """
        self._action_name_en = action_name_en

    @property
    def action_tag(self):
        """Gets the action_tag of this ActionSampleInfo.

        动作Tag。

        :return: The action_tag of this ActionSampleInfo.
        :rtype: str
        """
        return self._action_tag

    @action_tag.setter
    def action_tag(self, action_tag):
        """Sets the action_tag of this ActionSampleInfo.

        动作Tag。

        :param action_tag: The action_tag of this ActionSampleInfo.
        :type action_tag: str
        """
        self._action_tag = action_tag

    @property
    def catalog(self):
        """Gets the catalog of this ActionSampleInfo.

        动作分类名称。

        :return: The catalog of this ActionSampleInfo.
        :rtype: str
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        """Sets the catalog of this ActionSampleInfo.

        动作分类名称。

        :param catalog: The catalog of this ActionSampleInfo.
        :type catalog: str
        """
        self._catalog = catalog

    @property
    def is_selected(self):
        """Gets the is_selected of this ActionSampleInfo.

        是否选择此动作。

        :return: The is_selected of this ActionSampleInfo.
        :rtype: bool
        """
        return self._is_selected

    @is_selected.setter
    def is_selected(self, is_selected):
        """Sets the is_selected of this ActionSampleInfo.

        是否选择此动作。

        :param is_selected: The is_selected of this ActionSampleInfo.
        :type is_selected: bool
        """
        self._is_selected = is_selected

    @property
    def sample_download_url(self):
        """Gets the sample_download_url of this ActionSampleInfo.

        原子动作样例文件下载地址。24小时内有效。

        :return: The sample_download_url of this ActionSampleInfo.
        :rtype: str
        """
        return self._sample_download_url

    @sample_download_url.setter
    def sample_download_url(self, sample_download_url):
        """Sets the sample_download_url of this ActionSampleInfo.

        原子动作样例文件下载地址。24小时内有效。

        :param sample_download_url: The sample_download_url of this ActionSampleInfo.
        :type sample_download_url: str
        """
        self._sample_download_url = sample_download_url

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
        if not isinstance(other, ActionSampleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
