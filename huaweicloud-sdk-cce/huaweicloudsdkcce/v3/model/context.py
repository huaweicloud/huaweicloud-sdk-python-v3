# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Context:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster': 'str',
        'user': 'str'
    }

    attribute_map = {
        'cluster': 'cluster',
        'user': 'user'
    }

    def __init__(self, cluster=None, user=None):
        """Context

        The model defined in huaweicloud sdk

        :param cluster: 上下文cluster信息。 
        :type cluster: str
        :param user: 上下文user信息。 
        :type user: str
        """
        
        

        self._cluster = None
        self._user = None
        self.discriminator = None

        if cluster is not None:
            self.cluster = cluster
        if user is not None:
            self.user = user

    @property
    def cluster(self):
        """Gets the cluster of this Context.

        上下文cluster信息。 

        :return: The cluster of this Context.
        :rtype: str
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this Context.

        上下文cluster信息。 

        :param cluster: The cluster of this Context.
        :type cluster: str
        """
        self._cluster = cluster

    @property
    def user(self):
        """Gets the user of this Context.

        上下文user信息。 

        :return: The user of this Context.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Context.

        上下文user信息。 

        :param user: The user of this Context.
        :type user: str
        """
        self._user = user

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
        if not isinstance(other, Context):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
