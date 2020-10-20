# coding: utf-8

import pprint
import re

import six





class Quota:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'certificate': 'int',
        'healthmonitor': 'int',
        'l7policy': 'int',
        'listener': 'int',
        'loadbalancer': 'int',
        'member': 'int',
        'pool': 'int',
        'project_id': 'str'
    }

    attribute_map = {
        'certificate': 'certificate',
        'healthmonitor': 'healthmonitor',
        'l7policy': 'l7policy',
        'listener': 'listener',
        'loadbalancer': 'loadbalancer',
        'member': 'member',
        'pool': 'pool',
        'project_id': 'project_id'
    }

    def __init__(self, certificate=None, healthmonitor=None, l7policy=None, listener=None, loadbalancer=None, member=None, pool=None, project_id=None):
        """Quota - a model defined in huaweicloud sdk"""
        
        

        self._certificate = None
        self._healthmonitor = None
        self._l7policy = None
        self._listener = None
        self._loadbalancer = None
        self._member = None
        self._pool = None
        self._project_id = None
        self.discriminator = None

        self.certificate = certificate
        self.healthmonitor = healthmonitor
        self.l7policy = l7policy
        self.listener = listener
        self.loadbalancer = loadbalancer
        self.member = member
        self.pool = pool
        self.project_id = project_id

    @property
    def certificate(self):
        """Gets the certificate of this Quota.

        证书配额。 -1表示无配额限制。

        :return: The certificate of this Quota.
        :rtype: int
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this Quota.

        证书配额。 -1表示无配额限制。

        :param certificate: The certificate of this Quota.
        :type: int
        """
        self._certificate = certificate

    @property
    def healthmonitor(self):
        """Gets the healthmonitor of this Quota.

        健康检查配额。 -1表示无配额限制。

        :return: The healthmonitor of this Quota.
        :rtype: int
        """
        return self._healthmonitor

    @healthmonitor.setter
    def healthmonitor(self, healthmonitor):
        """Sets the healthmonitor of this Quota.

        健康检查配额。 -1表示无配额限制。

        :param healthmonitor: The healthmonitor of this Quota.
        :type: int
        """
        self._healthmonitor = healthmonitor

    @property
    def l7policy(self):
        """Gets the l7policy of this Quota.

        转发策略配额。 -1表示无配额限制。

        :return: The l7policy of this Quota.
        :rtype: int
        """
        return self._l7policy

    @l7policy.setter
    def l7policy(self, l7policy):
        """Sets the l7policy of this Quota.

        转发策略配额。 -1表示无配额限制。

        :param l7policy: The l7policy of this Quota.
        :type: int
        """
        self._l7policy = l7policy

    @property
    def listener(self):
        """Gets the listener of this Quota.

        监听器配额。 -1表示无配额限制。

        :return: The listener of this Quota.
        :rtype: int
        """
        return self._listener

    @listener.setter
    def listener(self, listener):
        """Sets the listener of this Quota.

        监听器配额。 -1表示无配额限制。

        :param listener: The listener of this Quota.
        :type: int
        """
        self._listener = listener

    @property
    def loadbalancer(self):
        """Gets the loadbalancer of this Quota.

        负载均衡器配额。 -1表示无配额限制。

        :return: The loadbalancer of this Quota.
        :rtype: int
        """
        return self._loadbalancer

    @loadbalancer.setter
    def loadbalancer(self, loadbalancer):
        """Sets the loadbalancer of this Quota.

        负载均衡器配额。 -1表示无配额限制。

        :param loadbalancer: The loadbalancer of this Quota.
        :type: int
        """
        self._loadbalancer = loadbalancer

    @property
    def member(self):
        """Gets the member of this Quota.

        后端云服务器配额。 -1表示无配额限制。

        :return: The member of this Quota.
        :rtype: int
        """
        return self._member

    @member.setter
    def member(self, member):
        """Sets the member of this Quota.

        后端云服务器配额。 -1表示无配额限制。

        :param member: The member of this Quota.
        :type: int
        """
        self._member = member

    @property
    def pool(self):
        """Gets the pool of this Quota.

        后端云服务器组配额。 -1表示无配额限制。

        :return: The pool of this Quota.
        :rtype: int
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this Quota.

        后端云服务器组配额。 -1表示无配额限制。

        :param pool: The pool of this Quota.
        :type: int
        """
        self._pool = pool

    @property
    def project_id(self):
        """Gets the project_id of this Quota.

        项目ID。

        :return: The project_id of this Quota.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Quota.

        项目ID。

        :param project_id: The project_id of this Quota.
        :type: str
        """
        self._project_id = project_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Quota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
