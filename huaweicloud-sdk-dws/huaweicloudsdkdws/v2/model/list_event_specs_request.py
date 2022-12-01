# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventSpecsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_name': 'str',
        'category': 'str',
        'severity': 'str',
        'source_type': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'spec_name': 'spec_name',
        'category': 'category',
        'severity': 'severity',
        'source_type': 'source_type',
        'tag': 'tag'
    }

    def __init__(self, spec_name=None, category=None, severity=None, source_type=None, tag=None):
        """ListEventSpecsRequest

        The model defined in huaweicloud sdk

        :param spec_name: 事件配置名称
        :type spec_name: str
        :param category: 事件类别
        :type category: str
        :param severity: 事件级别
        :type severity: str
        :param source_type: 事件源类别
        :type source_type: str
        :param tag: 事件标签
        :type tag: str
        """
        
        

        self._spec_name = None
        self._category = None
        self._severity = None
        self._source_type = None
        self._tag = None
        self.discriminator = None

        if spec_name is not None:
            self.spec_name = spec_name
        if category is not None:
            self.category = category
        if severity is not None:
            self.severity = severity
        if source_type is not None:
            self.source_type = source_type
        if tag is not None:
            self.tag = tag

    @property
    def spec_name(self):
        """Gets the spec_name of this ListEventSpecsRequest.

        事件配置名称

        :return: The spec_name of this ListEventSpecsRequest.
        :rtype: str
        """
        return self._spec_name

    @spec_name.setter
    def spec_name(self, spec_name):
        """Sets the spec_name of this ListEventSpecsRequest.

        事件配置名称

        :param spec_name: The spec_name of this ListEventSpecsRequest.
        :type spec_name: str
        """
        self._spec_name = spec_name

    @property
    def category(self):
        """Gets the category of this ListEventSpecsRequest.

        事件类别

        :return: The category of this ListEventSpecsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ListEventSpecsRequest.

        事件类别

        :param category: The category of this ListEventSpecsRequest.
        :type category: str
        """
        self._category = category

    @property
    def severity(self):
        """Gets the severity of this ListEventSpecsRequest.

        事件级别

        :return: The severity of this ListEventSpecsRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this ListEventSpecsRequest.

        事件级别

        :param severity: The severity of this ListEventSpecsRequest.
        :type severity: str
        """
        self._severity = severity

    @property
    def source_type(self):
        """Gets the source_type of this ListEventSpecsRequest.

        事件源类别

        :return: The source_type of this ListEventSpecsRequest.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this ListEventSpecsRequest.

        事件源类别

        :param source_type: The source_type of this ListEventSpecsRequest.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def tag(self):
        """Gets the tag of this ListEventSpecsRequest.

        事件标签

        :return: The tag of this ListEventSpecsRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ListEventSpecsRequest.

        事件标签

        :param tag: The tag of this ListEventSpecsRequest.
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
        if not isinstance(other, ListEventSpecsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
