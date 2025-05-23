# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDataspaceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dataspace_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'dataspace_name': 'dataspace_name',
        'description': 'description'
    }

    def __init__(self, dataspace_name=None, description=None):
        r"""CreateDataspaceRequestBody

        The model defined in huaweicloud sdk

        :param dataspace_name: 数据空间名称
        :type dataspace_name: str
        :param description: 描述
        :type description: str
        """
        
        

        self._dataspace_name = None
        self._description = None
        self.discriminator = None

        self.dataspace_name = dataspace_name
        self.description = description

    @property
    def dataspace_name(self):
        r"""Gets the dataspace_name of this CreateDataspaceRequestBody.

        数据空间名称

        :return: The dataspace_name of this CreateDataspaceRequestBody.
        :rtype: str
        """
        return self._dataspace_name

    @dataspace_name.setter
    def dataspace_name(self, dataspace_name):
        r"""Sets the dataspace_name of this CreateDataspaceRequestBody.

        数据空间名称

        :param dataspace_name: The dataspace_name of this CreateDataspaceRequestBody.
        :type dataspace_name: str
        """
        self._dataspace_name = dataspace_name

    @property
    def description(self):
        r"""Gets the description of this CreateDataspaceRequestBody.

        描述

        :return: The description of this CreateDataspaceRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateDataspaceRequestBody.

        描述

        :param description: The description of this CreateDataspaceRequestBody.
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
        if not isinstance(other, CreateDataspaceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
