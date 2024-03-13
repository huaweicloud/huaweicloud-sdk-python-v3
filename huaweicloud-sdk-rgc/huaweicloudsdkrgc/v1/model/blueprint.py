# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Blueprint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'blueprint_product_id': 'str',
        'blueprint_product_version': 'str'
    }

    attribute_map = {
        'blueprint_product_id': 'blueprint_product_id',
        'blueprint_product_version': 'blueprint_product_version'
    }

    def __init__(self, blueprint_product_id=None, blueprint_product_version=None):
        """Blueprint

        The model defined in huaweicloud sdk

        :param blueprint_product_id: 模板ID。
        :type blueprint_product_id: str
        :param blueprint_product_version: 模板版本。
        :type blueprint_product_version: str
        """
        
        

        self._blueprint_product_id = None
        self._blueprint_product_version = None
        self.discriminator = None

        if blueprint_product_id is not None:
            self.blueprint_product_id = blueprint_product_id
        if blueprint_product_version is not None:
            self.blueprint_product_version = blueprint_product_version

    @property
    def blueprint_product_id(self):
        """Gets the blueprint_product_id of this Blueprint.

        模板ID。

        :return: The blueprint_product_id of this Blueprint.
        :rtype: str
        """
        return self._blueprint_product_id

    @blueprint_product_id.setter
    def blueprint_product_id(self, blueprint_product_id):
        """Sets the blueprint_product_id of this Blueprint.

        模板ID。

        :param blueprint_product_id: The blueprint_product_id of this Blueprint.
        :type blueprint_product_id: str
        """
        self._blueprint_product_id = blueprint_product_id

    @property
    def blueprint_product_version(self):
        """Gets the blueprint_product_version of this Blueprint.

        模板版本。

        :return: The blueprint_product_version of this Blueprint.
        :rtype: str
        """
        return self._blueprint_product_version

    @blueprint_product_version.setter
    def blueprint_product_version(self, blueprint_product_version):
        """Sets the blueprint_product_version of this Blueprint.

        模板版本。

        :param blueprint_product_version: The blueprint_product_version of this Blueprint.
        :type blueprint_product_version: str
        """
        self._blueprint_product_version = blueprint_product_version

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
        if not isinstance(other, Blueprint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
