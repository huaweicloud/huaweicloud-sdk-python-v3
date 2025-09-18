# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DirectionalConnection:

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
        'id': 'str',
        'local_site_code': 'str',
        'remote_site_code': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'local_site_code': 'local_site_code',
        'remote_site_code': 'remote_site_code'
    }

    def __init__(self, name=None, id=None, local_site_code=None, remote_site_code=None):
        r"""DirectionalConnection

        The model defined in huaweicloud sdk

        :param name: 实例名称。
        :type name: str
        :param id: 实例ID。
        :type id: str
        :param local_site_code: 功能说明：本端接入点的编码。
        :type local_site_code: str
        :param remote_site_code: 功能说明：远端接入点的编码。
        :type remote_site_code: str
        """
        
        

        self._name = None
        self._id = None
        self._local_site_code = None
        self._remote_site_code = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.id = id
        if local_site_code is not None:
            self.local_site_code = local_site_code
        if remote_site_code is not None:
            self.remote_site_code = remote_site_code

    @property
    def name(self):
        r"""Gets the name of this DirectionalConnection.

        实例名称。

        :return: The name of this DirectionalConnection.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DirectionalConnection.

        实例名称。

        :param name: The name of this DirectionalConnection.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this DirectionalConnection.

        实例ID。

        :return: The id of this DirectionalConnection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DirectionalConnection.

        实例ID。

        :param id: The id of this DirectionalConnection.
        :type id: str
        """
        self._id = id

    @property
    def local_site_code(self):
        r"""Gets the local_site_code of this DirectionalConnection.

        功能说明：本端接入点的编码。

        :return: The local_site_code of this DirectionalConnection.
        :rtype: str
        """
        return self._local_site_code

    @local_site_code.setter
    def local_site_code(self, local_site_code):
        r"""Sets the local_site_code of this DirectionalConnection.

        功能说明：本端接入点的编码。

        :param local_site_code: The local_site_code of this DirectionalConnection.
        :type local_site_code: str
        """
        self._local_site_code = local_site_code

    @property
    def remote_site_code(self):
        r"""Gets the remote_site_code of this DirectionalConnection.

        功能说明：远端接入点的编码。

        :return: The remote_site_code of this DirectionalConnection.
        :rtype: str
        """
        return self._remote_site_code

    @remote_site_code.setter
    def remote_site_code(self, remote_site_code):
        r"""Sets the remote_site_code of this DirectionalConnection.

        功能说明：远端接入点的编码。

        :param remote_site_code: The remote_site_code of this DirectionalConnection.
        :type remote_site_code: str
        """
        self._remote_site_code = remote_site_code

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
        if not isinstance(other, DirectionalConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
