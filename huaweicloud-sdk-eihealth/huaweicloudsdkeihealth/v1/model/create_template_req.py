# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTemplateReq:

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
        'columns': 'list[DatabaseColumnDto]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'columns': 'columns'
    }

    def __init__(self, name=None, description=None, columns=None):
        """CreateTemplateReq

        The model defined in huaweicloud sdk

        :param name: 模板名称
        :type name: str
        :param description: 模板描述
        :type description: str
        :param columns: 数据库列信息
        :type columns: list[:class:`huaweicloudsdkeihealth.v1.DatabaseColumnDto`]
        """
        
        

        self._name = None
        self._description = None
        self._columns = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.columns = columns

    @property
    def name(self):
        """Gets the name of this CreateTemplateReq.

        模板名称

        :return: The name of this CreateTemplateReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateTemplateReq.

        模板名称

        :param name: The name of this CreateTemplateReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateTemplateReq.

        模板描述

        :return: The description of this CreateTemplateReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateTemplateReq.

        模板描述

        :param description: The description of this CreateTemplateReq.
        :type description: str
        """
        self._description = description

    @property
    def columns(self):
        """Gets the columns of this CreateTemplateReq.

        数据库列信息

        :return: The columns of this CreateTemplateReq.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.DatabaseColumnDto`]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this CreateTemplateReq.

        数据库列信息

        :param columns: The columns of this CreateTemplateReq.
        :type columns: list[:class:`huaweicloudsdkeihealth.v1.DatabaseColumnDto`]
        """
        self._columns = columns

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
        if not isinstance(other, CreateTemplateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
