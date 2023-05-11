# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartProtectionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'body': 'ProtectionInfoRequestInfo'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'body': 'body'
    }

    def __init__(self, region=None, enterprise_project_id=None, body=None):
        """StartProtectionRequest

        The model defined in huaweicloud sdk

        :param region: region id
        :type region: str
        :param enterprise_project_id: 企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param body: Body of the StartProtectionRequest
        :type body: :class:`huaweicloudsdkhss.v5.ProtectionInfoRequestInfo`
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._body = None
        self.discriminator = None

        self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if body is not None:
            self.body = body

    @property
    def region(self):
        """Gets the region of this StartProtectionRequest.

        region id

        :return: The region of this StartProtectionRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this StartProtectionRequest.

        region id

        :param region: The region of this StartProtectionRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this StartProtectionRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this StartProtectionRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this StartProtectionRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this StartProtectionRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def body(self):
        """Gets the body of this StartProtectionRequest.

        :return: The body of this StartProtectionRequest.
        :rtype: :class:`huaweicloudsdkhss.v5.ProtectionInfoRequestInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this StartProtectionRequest.

        :param body: The body of this StartProtectionRequest.
        :type body: :class:`huaweicloudsdkhss.v5.ProtectionInfoRequestInfo`
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
        if not isinstance(other, StartProtectionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
