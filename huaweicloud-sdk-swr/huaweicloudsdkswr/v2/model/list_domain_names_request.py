# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDomainNamesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'uid': 'str',
        'domain_name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'uid': 'uid',
        'domain_name': 'domain_name'
    }

    def __init__(self, instance_id=None, uid=None, domain_name=None):
        r"""ListDomainNamesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 企业仓库实例ID
        :type instance_id: str
        :param uid: 域名ID
        :type uid: str
        :param domain_name: 域名
        :type domain_name: str
        """
        
        

        self._instance_id = None
        self._uid = None
        self._domain_name = None
        self.discriminator = None

        self.instance_id = instance_id
        if uid is not None:
            self.uid = uid
        if domain_name is not None:
            self.domain_name = domain_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListDomainNamesRequest.

        企业仓库实例ID

        :return: The instance_id of this ListDomainNamesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListDomainNamesRequest.

        企业仓库实例ID

        :param instance_id: The instance_id of this ListDomainNamesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def uid(self):
        r"""Gets the uid of this ListDomainNamesRequest.

        域名ID

        :return: The uid of this ListDomainNamesRequest.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this ListDomainNamesRequest.

        域名ID

        :param uid: The uid of this ListDomainNamesRequest.
        :type uid: str
        """
        self._uid = uid

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ListDomainNamesRequest.

        域名

        :return: The domain_name of this ListDomainNamesRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ListDomainNamesRequest.

        域名

        :param domain_name: The domain_name of this ListDomainNamesRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

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
        if not isinstance(other, ListDomainNamesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
