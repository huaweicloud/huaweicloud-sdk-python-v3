# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterDatastoreBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'type': 'str'
    }

    attribute_map = {
        'version': 'version',
        'type': 'type'
    }

    def __init__(self, version=None, type=None):
        r"""CreateClusterDatastoreBody

        The model defined in huaweicloud sdk

        :param version: Esasticsearch引擎版本号。详细请参考CSS[支持的集群版本](css_03_0056.xml)。
        :type version: str
        :param type: 引擎类型，目前只支持elasticsearch。
        :type type: str
        """
        
        

        self._version = None
        self._type = None
        self.discriminator = None

        self.version = version
        self.type = type

    @property
    def version(self):
        r"""Gets the version of this CreateClusterDatastoreBody.

        Esasticsearch引擎版本号。详细请参考CSS[支持的集群版本](css_03_0056.xml)。

        :return: The version of this CreateClusterDatastoreBody.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateClusterDatastoreBody.

        Esasticsearch引擎版本号。详细请参考CSS[支持的集群版本](css_03_0056.xml)。

        :param version: The version of this CreateClusterDatastoreBody.
        :type version: str
        """
        self._version = version

    @property
    def type(self):
        r"""Gets the type of this CreateClusterDatastoreBody.

        引擎类型，目前只支持elasticsearch。

        :return: The type of this CreateClusterDatastoreBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateClusterDatastoreBody.

        引擎类型，目前只支持elasticsearch。

        :param type: The type of this CreateClusterDatastoreBody.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, CreateClusterDatastoreBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
