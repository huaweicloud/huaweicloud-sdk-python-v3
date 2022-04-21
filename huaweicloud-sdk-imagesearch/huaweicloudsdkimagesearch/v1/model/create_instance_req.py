# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceReq:

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
        'model': 'str',
        'description': 'str',
        'level': 'int',
        'tags': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'model': 'model',
        'description': 'description',
        'level': 'level',
        'tags': 'tags'
    }

    def __init__(self, name=None, model=None, description=None, level=None, tags=None):
        """CreateInstanceReq

        The model defined in huaweicloud sdk

        :param name: 实例名称。  - 仅支持小写字母（a-z）、数字，横杠和下划线。  - 以字母开头，长度在16位以内。 
        :type name: str
        :param model: 模型名称，支持如下模型名称：  - common-search，通用图片搜索，适用于图片库中搜索相似内容或类别的图片。  - image-recommend，版权图片推荐，适用于版权摄影图片库中查找并推荐相同或相似版权图片。  - image-copyright，图片版权，适用于从海量图片库中快速识别侵权盗用图片。 
        :type model: str
        :param description: 描述。
        :type description: str
        :param level: 规格，即实例的图片数量规格。默认为30000000（单位：张），当前仅支持默认规格。
        :type level: int
        :param tags: 图片自定义标签，每个实例最多支持10个标签，自定义标签不支持英文字母大写。
        :type tags: list[str]
        """
        
        

        self._name = None
        self._model = None
        self._description = None
        self._level = None
        self._tags = None
        self.discriminator = None

        self.name = name
        self.model = model
        if description is not None:
            self.description = description
        if level is not None:
            self.level = level
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this CreateInstanceReq.

        实例名称。  - 仅支持小写字母（a-z）、数字，横杠和下划线。  - 以字母开头，长度在16位以内。 

        :return: The name of this CreateInstanceReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateInstanceReq.

        实例名称。  - 仅支持小写字母（a-z）、数字，横杠和下划线。  - 以字母开头，长度在16位以内。 

        :param name: The name of this CreateInstanceReq.
        :type name: str
        """
        self._name = name

    @property
    def model(self):
        """Gets the model of this CreateInstanceReq.

        模型名称，支持如下模型名称：  - common-search，通用图片搜索，适用于图片库中搜索相似内容或类别的图片。  - image-recommend，版权图片推荐，适用于版权摄影图片库中查找并推荐相同或相似版权图片。  - image-copyright，图片版权，适用于从海量图片库中快速识别侵权盗用图片。 

        :return: The model of this CreateInstanceReq.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this CreateInstanceReq.

        模型名称，支持如下模型名称：  - common-search，通用图片搜索，适用于图片库中搜索相似内容或类别的图片。  - image-recommend，版权图片推荐，适用于版权摄影图片库中查找并推荐相同或相似版权图片。  - image-copyright，图片版权，适用于从海量图片库中快速识别侵权盗用图片。 

        :param model: The model of this CreateInstanceReq.
        :type model: str
        """
        self._model = model

    @property
    def description(self):
        """Gets the description of this CreateInstanceReq.

        描述。

        :return: The description of this CreateInstanceReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateInstanceReq.

        描述。

        :param description: The description of this CreateInstanceReq.
        :type description: str
        """
        self._description = description

    @property
    def level(self):
        """Gets the level of this CreateInstanceReq.

        规格，即实例的图片数量规格。默认为30000000（单位：张），当前仅支持默认规格。

        :return: The level of this CreateInstanceReq.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this CreateInstanceReq.

        规格，即实例的图片数量规格。默认为30000000（单位：张），当前仅支持默认规格。

        :param level: The level of this CreateInstanceReq.
        :type level: int
        """
        self._level = level

    @property
    def tags(self):
        """Gets the tags of this CreateInstanceReq.

        图片自定义标签，每个实例最多支持10个标签，自定义标签不支持英文字母大写。

        :return: The tags of this CreateInstanceReq.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateInstanceReq.

        图片自定义标签，每个实例最多支持10个标签，自定义标签不支持英文字母大写。

        :param tags: The tags of this CreateInstanceReq.
        :type tags: list[str]
        """
        self._tags = tags

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
        if not isinstance(other, CreateInstanceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
