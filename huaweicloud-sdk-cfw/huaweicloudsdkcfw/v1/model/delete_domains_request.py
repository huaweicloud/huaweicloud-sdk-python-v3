# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDomainsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'set_id': 'str',
        'enterprise_project_id': 'str',
        'body': 'DeleteDomainDto'
    }

    attribute_map = {
        'set_id': 'set_id',
        'enterprise_project_id': 'enterprise_project_id',
        'body': 'body'
    }

    def __init__(self, set_id=None, enterprise_project_id=None, body=None):
        """DeleteDomainsRequest

        The model defined in huaweicloud sdk

        :param set_id: 域名组id
        :type set_id: str
        :param enterprise_project_id: 企业项目id，用户支持企业项目后，由企业项目生成的id。
        :type enterprise_project_id: str
        :param body: Body of the DeleteDomainsRequest
        :type body: :class:`huaweicloudsdkcfw.v1.DeleteDomainDto`
        """
        
        

        self._set_id = None
        self._enterprise_project_id = None
        self._body = None
        self.discriminator = None

        self.set_id = set_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if body is not None:
            self.body = body

    @property
    def set_id(self):
        """Gets the set_id of this DeleteDomainsRequest.

        域名组id

        :return: The set_id of this DeleteDomainsRequest.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        """Sets the set_id of this DeleteDomainsRequest.

        域名组id

        :param set_id: The set_id of this DeleteDomainsRequest.
        :type set_id: str
        """
        self._set_id = set_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this DeleteDomainsRequest.

        企业项目id，用户支持企业项目后，由企业项目生成的id。

        :return: The enterprise_project_id of this DeleteDomainsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this DeleteDomainsRequest.

        企业项目id，用户支持企业项目后，由企业项目生成的id。

        :param enterprise_project_id: The enterprise_project_id of this DeleteDomainsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def body(self):
        """Gets the body of this DeleteDomainsRequest.

        :return: The body of this DeleteDomainsRequest.
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteDomainDto`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DeleteDomainsRequest.

        :param body: The body of this DeleteDomainsRequest.
        :type body: :class:`huaweicloudsdkcfw.v1.DeleteDomainDto`
        """
        self._body = body

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
        if not isinstance(other, DeleteDomainsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
