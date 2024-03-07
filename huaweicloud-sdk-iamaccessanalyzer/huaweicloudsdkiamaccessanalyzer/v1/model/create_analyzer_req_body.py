# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAnalyzerReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('name')

    openapi_types = {
        'name': 'str',
        'tags': 'list[Tag]',
        'type': 'AnalyzerType'
    }

    attribute_map = {
        'name': 'name',
        'tags': 'tags',
        'type': 'type'
    }

    def __init__(self, name=None, tags=None, type=None):
        """CreateAnalyzerReqBody

        The model defined in huaweicloud sdk

        :param name: 分析器的名称。
        :type name: str
        :param tags: 自定义标签列表。
        :type tags: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.Tag`]
        :param type: 
        :type type: :class:`huaweicloudsdkiamaccessanalyzer.v1.AnalyzerType`
        """
        
        

        self._name = None
        self._tags = None
        self._type = None
        self.discriminator = None

        self.name = name
        if tags is not None:
            self.tags = tags
        self.type = type

    @property
    def name(self):
        """Gets the name of this CreateAnalyzerReqBody.

        分析器的名称。

        :return: The name of this CreateAnalyzerReqBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAnalyzerReqBody.

        分析器的名称。

        :param name: The name of this CreateAnalyzerReqBody.
        :type name: str
        """
        self._name = name

    @property
    def tags(self):
        """Gets the tags of this CreateAnalyzerReqBody.

        自定义标签列表。

        :return: The tags of this CreateAnalyzerReqBody.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateAnalyzerReqBody.

        自定义标签列表。

        :param tags: The tags of this CreateAnalyzerReqBody.
        :type tags: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.Tag`]
        """
        self._tags = tags

    @property
    def type(self):
        """Gets the type of this CreateAnalyzerReqBody.

        :return: The type of this CreateAnalyzerReqBody.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.AnalyzerType`
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateAnalyzerReqBody.

        :param type: The type of this CreateAnalyzerReqBody.
        :type type: :class:`huaweicloudsdkiamaccessanalyzer.v1.AnalyzerType`
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
        if not isinstance(other, CreateAnalyzerReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
