# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchImportConfigRequestBody:

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
        'value': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'value': 'value',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, value=None, description=None):
        r"""BatchImportConfigRequestBody

        The model defined in huaweicloud sdk

        :param id: 配置项ID
        :type id: str
        :param name: 配置项名称
        :type name: str
        :param value: 配置项详情，长度2MB以内
        :type value: str
        :param description: 配置项描述
        :type description: str
        """
        
        

        self._id = None
        self._name = None
        self._value = None
        self._description = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.value = value
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this BatchImportConfigRequestBody.

        配置项ID

        :return: The id of this BatchImportConfigRequestBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchImportConfigRequestBody.

        配置项ID

        :param id: The id of this BatchImportConfigRequestBody.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BatchImportConfigRequestBody.

        配置项名称

        :return: The name of this BatchImportConfigRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchImportConfigRequestBody.

        配置项名称

        :param name: The name of this BatchImportConfigRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this BatchImportConfigRequestBody.

        配置项详情，长度2MB以内

        :return: The value of this BatchImportConfigRequestBody.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this BatchImportConfigRequestBody.

        配置项详情，长度2MB以内

        :param value: The value of this BatchImportConfigRequestBody.
        :type value: str
        """
        self._value = value

    @property
    def description(self):
        r"""Gets the description of this BatchImportConfigRequestBody.

        配置项描述

        :return: The description of this BatchImportConfigRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BatchImportConfigRequestBody.

        配置项描述

        :param description: The description of this BatchImportConfigRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, BatchImportConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
