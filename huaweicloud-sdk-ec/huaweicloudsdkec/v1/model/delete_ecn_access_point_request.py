# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteEcnAccessPointRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ecn_id': 'str',
        'access_point_id': 'str'
    }

    attribute_map = {
        'ecn_id': 'ecn_id',
        'access_point_id': 'access_point_id'
    }

    def __init__(self, ecn_id=None, access_point_id=None):
        """DeleteEcnAccessPointRequest

        The model defined in huaweicloud sdk

        :param ecn_id: 企业连接网络ID
        :type ecn_id: str
        :param access_point_id: 企业连接网络接入点ID
        :type access_point_id: str
        """
        
        

        self._ecn_id = None
        self._access_point_id = None
        self.discriminator = None

        self.ecn_id = ecn_id
        self.access_point_id = access_point_id

    @property
    def ecn_id(self):
        """Gets the ecn_id of this DeleteEcnAccessPointRequest.

        企业连接网络ID

        :return: The ecn_id of this DeleteEcnAccessPointRequest.
        :rtype: str
        """
        return self._ecn_id

    @ecn_id.setter
    def ecn_id(self, ecn_id):
        """Sets the ecn_id of this DeleteEcnAccessPointRequest.

        企业连接网络ID

        :param ecn_id: The ecn_id of this DeleteEcnAccessPointRequest.
        :type ecn_id: str
        """
        self._ecn_id = ecn_id

    @property
    def access_point_id(self):
        """Gets the access_point_id of this DeleteEcnAccessPointRequest.

        企业连接网络接入点ID

        :return: The access_point_id of this DeleteEcnAccessPointRequest.
        :rtype: str
        """
        return self._access_point_id

    @access_point_id.setter
    def access_point_id(self, access_point_id):
        """Sets the access_point_id of this DeleteEcnAccessPointRequest.

        企业连接网络接入点ID

        :param access_point_id: The access_point_id of this DeleteEcnAccessPointRequest.
        :type access_point_id: str
        """
        self._access_point_id = access_point_id

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
        if not isinstance(other, DeleteEcnAccessPointRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
