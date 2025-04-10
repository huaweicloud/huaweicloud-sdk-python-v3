# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDatabaseReq:

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
        'template_id': 'str',
        'description': 'str',
        'import_data': 'ImportDatabaseDataReq'
    }

    attribute_map = {
        'name': 'name',
        'template_id': 'template_id',
        'description': 'description',
        'import_data': 'import_data'
    }

    def __init__(self, name=None, template_id=None, description=None, import_data=None):
        r"""CreateDatabaseReq

        The model defined in huaweicloud sdk

        :param name: 实例名称
        :type name: str
        :param template_id: 模板id
        :type template_id: str
        :param description: 实例描述
        :type description: str
        :param import_data: 
        :type import_data: :class:`huaweicloudsdkeihealth.v1.ImportDatabaseDataReq`
        """
        
        

        self._name = None
        self._template_id = None
        self._description = None
        self._import_data = None
        self.discriminator = None

        self.name = name
        self.template_id = template_id
        if description is not None:
            self.description = description
        if import_data is not None:
            self.import_data = import_data

    @property
    def name(self):
        r"""Gets the name of this CreateDatabaseReq.

        实例名称

        :return: The name of this CreateDatabaseReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateDatabaseReq.

        实例名称

        :param name: The name of this CreateDatabaseReq.
        :type name: str
        """
        self._name = name

    @property
    def template_id(self):
        r"""Gets the template_id of this CreateDatabaseReq.

        模板id

        :return: The template_id of this CreateDatabaseReq.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this CreateDatabaseReq.

        模板id

        :param template_id: The template_id of this CreateDatabaseReq.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def description(self):
        r"""Gets the description of this CreateDatabaseReq.

        实例描述

        :return: The description of this CreateDatabaseReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateDatabaseReq.

        实例描述

        :param description: The description of this CreateDatabaseReq.
        :type description: str
        """
        self._description = description

    @property
    def import_data(self):
        r"""Gets the import_data of this CreateDatabaseReq.

        :return: The import_data of this CreateDatabaseReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportDatabaseDataReq`
        """
        return self._import_data

    @import_data.setter
    def import_data(self, import_data):
        r"""Sets the import_data of this CreateDatabaseReq.

        :param import_data: The import_data of this CreateDatabaseReq.
        :type import_data: :class:`huaweicloudsdkeihealth.v1.ImportDatabaseDataReq`
        """
        self._import_data = import_data

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
        if not isinstance(other, CreateDatabaseReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
