# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineTemplateInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'detail': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'detail': 'detail'
    }

    def __init__(self, id=None, name=None, detail=None):
        """PipelineTemplateInfo

        The model defined in huaweicloud sdk

        :param id: 流水线模板的id。
        :type id: str
        :param name: 流水线模板的名称。
        :type name: str
        :param detail: 流水线模板的详细信息。
        :type detail: str
        """
        
        

        self._id = None
        self._name = None
        self._detail = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if detail is not None:
            self.detail = detail

    @property
    def id(self):
        """Gets the id of this PipelineTemplateInfo.

        流水线模板的id。

        :return: The id of this PipelineTemplateInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PipelineTemplateInfo.

        流水线模板的id。

        :param id: The id of this PipelineTemplateInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this PipelineTemplateInfo.

        流水线模板的名称。

        :return: The name of this PipelineTemplateInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PipelineTemplateInfo.

        流水线模板的名称。

        :param name: The name of this PipelineTemplateInfo.
        :type name: str
        """
        self._name = name

    @property
    def detail(self):
        """Gets the detail of this PipelineTemplateInfo.

        流水线模板的详细信息。

        :return: The detail of this PipelineTemplateInfo.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this PipelineTemplateInfo.

        流水线模板的详细信息。

        :param detail: The detail of this PipelineTemplateInfo.
        :type detail: str
        """
        self._detail = detail

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
        if not isinstance(other, PipelineTemplateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
