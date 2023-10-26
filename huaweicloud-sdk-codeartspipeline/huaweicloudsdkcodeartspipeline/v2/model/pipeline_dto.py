# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'is_publish': 'bool',
        'sources': 'list[CodeSource]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'is_publish': 'is_publish',
        'sources': 'sources'
    }

    def __init__(self, name=None, description=None, is_publish=None, sources=None):
        """PipelineDTO

        The model defined in huaweicloud sdk

        :param name: 流水线名称
        :type name: str
        :param description: 流水线描述
        :type description: str
        :param is_publish: 是否为发布流水线
        :type is_publish: bool
        :param sources: 流水线源
        :type sources: list[:class:`huaweicloudsdkcodeartspipeline.v2.CodeSource`]
        """
        
        

        self._name = None
        self._description = None
        self._is_publish = None
        self._sources = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if is_publish is not None:
            self.is_publish = is_publish
        if sources is not None:
            self.sources = sources

    @property
    def name(self):
        """Gets the name of this PipelineDTO.

        流水线名称

        :return: The name of this PipelineDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PipelineDTO.

        流水线名称

        :param name: The name of this PipelineDTO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this PipelineDTO.

        流水线描述

        :return: The description of this PipelineDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PipelineDTO.

        流水线描述

        :param description: The description of this PipelineDTO.
        :type description: str
        """
        self._description = description

    @property
    def is_publish(self):
        """Gets the is_publish of this PipelineDTO.

        是否为发布流水线

        :return: The is_publish of this PipelineDTO.
        :rtype: bool
        """
        return self._is_publish

    @is_publish.setter
    def is_publish(self, is_publish):
        """Sets the is_publish of this PipelineDTO.

        是否为发布流水线

        :param is_publish: The is_publish of this PipelineDTO.
        :type is_publish: bool
        """
        self._is_publish = is_publish

    @property
    def sources(self):
        """Gets the sources of this PipelineDTO.

        流水线源

        :return: The sources of this PipelineDTO.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.CodeSource`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this PipelineDTO.

        流水线源

        :param sources: The sources of this PipelineDTO.
        :type sources: list[:class:`huaweicloudsdkcodeartspipeline.v2.CodeSource`]
        """
        self._sources = sources

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
        if not isinstance(other, PipelineDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
