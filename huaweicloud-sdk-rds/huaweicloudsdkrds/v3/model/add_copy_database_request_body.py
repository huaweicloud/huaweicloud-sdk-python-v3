# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddCopyDatabaseRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'procedure_name': 'str',
        'params': 'object'
    }

    attribute_map = {
        'procedure_name': 'procedure_name',
        'params': 'params'
    }

    def __init__(self, procedure_name=None, params=None):
        r"""AddCopyDatabaseRequestBody

        The model defined in huaweicloud sdk

        :param procedure_name: 操作名称(copy_database)
        :type procedure_name: str
        :param params: 源库和目的库信息
        :type params: object
        """
        
        

        self._procedure_name = None
        self._params = None
        self.discriminator = None

        if procedure_name is not None:
            self.procedure_name = procedure_name
        if params is not None:
            self.params = params

    @property
    def procedure_name(self):
        r"""Gets the procedure_name of this AddCopyDatabaseRequestBody.

        操作名称(copy_database)

        :return: The procedure_name of this AddCopyDatabaseRequestBody.
        :rtype: str
        """
        return self._procedure_name

    @procedure_name.setter
    def procedure_name(self, procedure_name):
        r"""Sets the procedure_name of this AddCopyDatabaseRequestBody.

        操作名称(copy_database)

        :param procedure_name: The procedure_name of this AddCopyDatabaseRequestBody.
        :type procedure_name: str
        """
        self._procedure_name = procedure_name

    @property
    def params(self):
        r"""Gets the params of this AddCopyDatabaseRequestBody.

        源库和目的库信息

        :return: The params of this AddCopyDatabaseRequestBody.
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this AddCopyDatabaseRequestBody.

        源库和目的库信息

        :param params: The params of this AddCopyDatabaseRequestBody.
        :type params: object
        """
        self._params = params

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
        if not isinstance(other, AddCopyDatabaseRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
