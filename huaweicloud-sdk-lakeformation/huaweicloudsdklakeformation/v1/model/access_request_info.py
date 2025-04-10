# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpcep_id': 'str',
        'domain': 'str'
    }

    attribute_map = {
        'vpcep_id': 'vpcep_id',
        'domain': 'domain'
    }

    def __init__(self, vpcep_id=None, domain=None):
        r"""AccessRequestInfo

        The model defined in huaweicloud sdk

        :param vpcep_id: 服务创建的id
        :type vpcep_id: str
        :param domain: 分组独立域名
        :type domain: str
        """
        
        

        self._vpcep_id = None
        self._domain = None
        self.discriminator = None

        self.vpcep_id = vpcep_id
        self.domain = domain

    @property
    def vpcep_id(self):
        r"""Gets the vpcep_id of this AccessRequestInfo.

        服务创建的id

        :return: The vpcep_id of this AccessRequestInfo.
        :rtype: str
        """
        return self._vpcep_id

    @vpcep_id.setter
    def vpcep_id(self, vpcep_id):
        r"""Sets the vpcep_id of this AccessRequestInfo.

        服务创建的id

        :param vpcep_id: The vpcep_id of this AccessRequestInfo.
        :type vpcep_id: str
        """
        self._vpcep_id = vpcep_id

    @property
    def domain(self):
        r"""Gets the domain of this AccessRequestInfo.

        分组独立域名

        :return: The domain of this AccessRequestInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this AccessRequestInfo.

        分组独立域名

        :param domain: The domain of this AccessRequestInfo.
        :type domain: str
        """
        self._domain = domain

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
        if not isinstance(other, AccessRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
