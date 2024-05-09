# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDrugDatabaseFileReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file': 'DatabaseFile',
        'description': 'str'
    }

    attribute_map = {
        'file': 'file',
        'description': 'description'
    }

    def __init__(self, file=None, description=None):
        """AddDrugDatabaseFileReq

        The model defined in huaweicloud sdk

        :param file: 
        :type file: :class:`huaweicloudsdkeihealth.v1.DatabaseFile`
        :param description: 数据库描述
        :type description: str
        """
        
        

        self._file = None
        self._description = None
        self.discriminator = None

        self.file = file
        if description is not None:
            self.description = description

    @property
    def file(self):
        """Gets the file of this AddDrugDatabaseFileReq.

        :return: The file of this AddDrugDatabaseFileReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DatabaseFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this AddDrugDatabaseFileReq.

        :param file: The file of this AddDrugDatabaseFileReq.
        :type file: :class:`huaweicloudsdkeihealth.v1.DatabaseFile`
        """
        self._file = file

    @property
    def description(self):
        """Gets the description of this AddDrugDatabaseFileReq.

        数据库描述

        :return: The description of this AddDrugDatabaseFileReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddDrugDatabaseFileReq.

        数据库描述

        :param description: The description of this AddDrugDatabaseFileReq.
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
        if not isinstance(other, AddDrugDatabaseFileReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
