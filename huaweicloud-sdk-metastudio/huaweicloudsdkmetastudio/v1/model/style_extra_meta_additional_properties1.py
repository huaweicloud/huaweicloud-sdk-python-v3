# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StyleExtraMetaAdditionalProperties1:

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
        'match_component': 'str',
        'files': 'list[str]',
        'classified_tags': 'dict(str, list[str])'
    }

    attribute_map = {
        'type': 'type',
        'match_component': 'match_component',
        'files': 'files',
        'classified_tags': 'classified_tags'
    }

    def __init__(self, type=None, match_component=None, files=None, classified_tags=None):
        """StyleExtraMetaAdditionalProperties1

        The model defined in huaweicloud sdk

        :param type: 算法类型枚举，\&quot;CREATE\&quot;还是\&quot;CLASSIFY\&quot;
        :type type: str
        :param match_component: 算法输出所匹配的组件名
        :type match_component: str
        :param files: 算法输出的文件名列表
        :type files: list[str]
        :param classified_tags: 分类算法的标签列表
        :type classified_tags: dict(str, list[str])
        """
        
        

        self._type = None
        self._match_component = None
        self._files = None
        self._classified_tags = None
        self.discriminator = None

        self.type = type
        if match_component is not None:
            self.match_component = match_component
        if files is not None:
            self.files = files
        if classified_tags is not None:
            self.classified_tags = classified_tags

    @property
    def type(self):
        """Gets the type of this StyleExtraMetaAdditionalProperties1.

        算法类型枚举，\"CREATE\"还是\"CLASSIFY\"

        :return: The type of this StyleExtraMetaAdditionalProperties1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StyleExtraMetaAdditionalProperties1.

        算法类型枚举，\"CREATE\"还是\"CLASSIFY\"

        :param type: The type of this StyleExtraMetaAdditionalProperties1.
        :type type: str
        """
        self._type = type

    @property
    def match_component(self):
        """Gets the match_component of this StyleExtraMetaAdditionalProperties1.

        算法输出所匹配的组件名

        :return: The match_component of this StyleExtraMetaAdditionalProperties1.
        :rtype: str
        """
        return self._match_component

    @match_component.setter
    def match_component(self, match_component):
        """Sets the match_component of this StyleExtraMetaAdditionalProperties1.

        算法输出所匹配的组件名

        :param match_component: The match_component of this StyleExtraMetaAdditionalProperties1.
        :type match_component: str
        """
        self._match_component = match_component

    @property
    def files(self):
        """Gets the files of this StyleExtraMetaAdditionalProperties1.

        算法输出的文件名列表

        :return: The files of this StyleExtraMetaAdditionalProperties1.
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this StyleExtraMetaAdditionalProperties1.

        算法输出的文件名列表

        :param files: The files of this StyleExtraMetaAdditionalProperties1.
        :type files: list[str]
        """
        self._files = files

    @property
    def classified_tags(self):
        """Gets the classified_tags of this StyleExtraMetaAdditionalProperties1.

        分类算法的标签列表

        :return: The classified_tags of this StyleExtraMetaAdditionalProperties1.
        :rtype: dict(str, list[str])
        """
        return self._classified_tags

    @classified_tags.setter
    def classified_tags(self, classified_tags):
        """Sets the classified_tags of this StyleExtraMetaAdditionalProperties1.

        分类算法的标签列表

        :param classified_tags: The classified_tags of this StyleExtraMetaAdditionalProperties1.
        :type classified_tags: dict(str, list[str])
        """
        self._classified_tags = classified_tags

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
        if not isinstance(other, StyleExtraMetaAdditionalProperties1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
