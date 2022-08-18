# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CatalogTargetParameters:

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
        'label': 'str',
        'metadata': 'object'
    }

    attribute_map = {
        'name': 'name',
        'label': 'label',
        'metadata': 'metadata'
    }

    def __init__(self, name=None, label=None, metadata=None):
        """CatalogTargetParameters

        The model defined in huaweicloud sdk

        :param name: 目标参数名称
        :type name: str
        :param label: 目标参数名称展示说明
        :type label: str
        :param metadata: 参数展示元数据，比如是否必选，输入框类型等等
        :type metadata: object
        """
        
        

        self._name = None
        self._label = None
        self._metadata = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if label is not None:
            self.label = label
        if metadata is not None:
            self.metadata = metadata

    @property
    def name(self):
        """Gets the name of this CatalogTargetParameters.

        目标参数名称

        :return: The name of this CatalogTargetParameters.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CatalogTargetParameters.

        目标参数名称

        :param name: The name of this CatalogTargetParameters.
        :type name: str
        """
        self._name = name

    @property
    def label(self):
        """Gets the label of this CatalogTargetParameters.

        目标参数名称展示说明

        :return: The label of this CatalogTargetParameters.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CatalogTargetParameters.

        目标参数名称展示说明

        :param label: The label of this CatalogTargetParameters.
        :type label: str
        """
        self._label = label

    @property
    def metadata(self):
        """Gets the metadata of this CatalogTargetParameters.

        参数展示元数据，比如是否必选，输入框类型等等

        :return: The metadata of this CatalogTargetParameters.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CatalogTargetParameters.

        参数展示元数据，比如是否必选，输入框类型等等

        :param metadata: The metadata of this CatalogTargetParameters.
        :type metadata: object
        """
        self._metadata = metadata

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
        if not isinstance(other, CatalogTargetParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
