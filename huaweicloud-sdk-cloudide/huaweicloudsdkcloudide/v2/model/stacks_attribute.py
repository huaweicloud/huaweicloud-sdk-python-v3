# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StacksAttribute:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'specs': 'list[str]',
        'suggest': 'str',
        'suggest_title': 'str',
        'volumes': 'list[str]'
    }

    attribute_map = {
        'specs': 'specs',
        'suggest': 'suggest',
        'suggest_title': 'suggest_title',
        'volumes': 'volumes'
    }

    def __init__(self, specs=None, suggest=None, suggest_title=None, volumes=None):
        """StacksAttribute

        The model defined in huaweicloud sdk

        :param specs: 规格列表
        :type specs: list[str]
        :param suggest: 提示id
        :type suggest: str
        :param suggest_title: 提示信息
        :type suggest_title: str
        :param volumes: 卷容量列表
        :type volumes: list[str]
        """
        
        

        self._specs = None
        self._suggest = None
        self._suggest_title = None
        self._volumes = None
        self.discriminator = None

        if specs is not None:
            self.specs = specs
        if suggest is not None:
            self.suggest = suggest
        if suggest_title is not None:
            self.suggest_title = suggest_title
        if volumes is not None:
            self.volumes = volumes

    @property
    def specs(self):
        """Gets the specs of this StacksAttribute.

        规格列表

        :return: The specs of this StacksAttribute.
        :rtype: list[str]
        """
        return self._specs

    @specs.setter
    def specs(self, specs):
        """Sets the specs of this StacksAttribute.

        规格列表

        :param specs: The specs of this StacksAttribute.
        :type specs: list[str]
        """
        self._specs = specs

    @property
    def suggest(self):
        """Gets the suggest of this StacksAttribute.

        提示id

        :return: The suggest of this StacksAttribute.
        :rtype: str
        """
        return self._suggest

    @suggest.setter
    def suggest(self, suggest):
        """Sets the suggest of this StacksAttribute.

        提示id

        :param suggest: The suggest of this StacksAttribute.
        :type suggest: str
        """
        self._suggest = suggest

    @property
    def suggest_title(self):
        """Gets the suggest_title of this StacksAttribute.

        提示信息

        :return: The suggest_title of this StacksAttribute.
        :rtype: str
        """
        return self._suggest_title

    @suggest_title.setter
    def suggest_title(self, suggest_title):
        """Sets the suggest_title of this StacksAttribute.

        提示信息

        :param suggest_title: The suggest_title of this StacksAttribute.
        :type suggest_title: str
        """
        self._suggest_title = suggest_title

    @property
    def volumes(self):
        """Gets the volumes of this StacksAttribute.

        卷容量列表

        :return: The volumes of this StacksAttribute.
        :rtype: list[str]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this StacksAttribute.

        卷容量列表

        :param volumes: The volumes of this StacksAttribute.
        :type volumes: list[str]
        """
        self._volumes = volumes

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
        if not isinstance(other, StacksAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
