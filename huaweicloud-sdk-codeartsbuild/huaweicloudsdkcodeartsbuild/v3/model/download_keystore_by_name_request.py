# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadKeystoreByNameRequest:

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
        'domain_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'domain_id': 'domain_id',
        'id': 'id'
    }

    def __init__(self, name=None, domain_id=None, id=None):
        r"""DownloadKeystoreByNameRequest

        The model defined in huaweicloud sdk

        :param name: 文件名
        :type name: str
        :param domain_id: 租户ID
        :type domain_id: str
        :param id: 文件ID
        :type id: str
        """
        
        

        self._name = None
        self._domain_id = None
        self._id = None
        self.discriminator = None

        self.name = name
        self.domain_id = domain_id
        self.id = id

    @property
    def name(self):
        r"""Gets the name of this DownloadKeystoreByNameRequest.

        文件名

        :return: The name of this DownloadKeystoreByNameRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DownloadKeystoreByNameRequest.

        文件名

        :param name: The name of this DownloadKeystoreByNameRequest.
        :type name: str
        """
        self._name = name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this DownloadKeystoreByNameRequest.

        租户ID

        :return: The domain_id of this DownloadKeystoreByNameRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this DownloadKeystoreByNameRequest.

        租户ID

        :param domain_id: The domain_id of this DownloadKeystoreByNameRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def id(self):
        r"""Gets the id of this DownloadKeystoreByNameRequest.

        文件ID

        :return: The id of this DownloadKeystoreByNameRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DownloadKeystoreByNameRequest.

        文件ID

        :param id: The id of this DownloadKeystoreByNameRequest.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, DownloadKeystoreByNameRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
