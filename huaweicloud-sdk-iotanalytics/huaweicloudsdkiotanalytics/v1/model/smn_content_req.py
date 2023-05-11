# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmnContentReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'ak': 'str',
        'sk': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'ak': 'ak',
        'sk': 'sk'
    }

    def __init__(self, project_id=None, ak=None, sk=None):
        """SmnContentReq

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param ak: 租户的AK
        :type ak: str
        :param sk: 租户的SK
        :type sk: str
        """
        
        

        self._project_id = None
        self._ak = None
        self._sk = None
        self.discriminator = None

        self.project_id = project_id
        self.ak = ak
        self.sk = sk

    @property
    def project_id(self):
        """Gets the project_id of this SmnContentReq.

        项目id

        :return: The project_id of this SmnContentReq.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SmnContentReq.

        项目id

        :param project_id: The project_id of this SmnContentReq.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def ak(self):
        """Gets the ak of this SmnContentReq.

        租户的AK

        :return: The ak of this SmnContentReq.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        """Sets the ak of this SmnContentReq.

        租户的AK

        :param ak: The ak of this SmnContentReq.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        """Gets the sk of this SmnContentReq.

        租户的SK

        :return: The sk of this SmnContentReq.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        """Sets the sk of this SmnContentReq.

        租户的SK

        :param sk: The sk of this SmnContentReq.
        :type sk: str
        """
        self._sk = sk

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
        if not isinstance(other, SmnContentReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
