# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SchedulerAffinity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'az': 'list[str]',
        'node': 'list[str]',
        'application': 'list[str]'
    }

    attribute_map = {
        'az': 'az',
        'node': 'node',
        'application': 'application'
    }

    def __init__(self, az=None, node=None, application=None):
        r"""SchedulerAffinity

        The model defined in huaweicloud sdk

        :param az: 
        :type az: list[str]
        :param node: 
        :type node: list[str]
        :param application: 
        :type application: list[str]
        """
        
        

        self._az = None
        self._node = None
        self._application = None
        self.discriminator = None

        if az is not None:
            self.az = az
        if node is not None:
            self.node = node
        if application is not None:
            self.application = application

    @property
    def az(self):
        r"""Gets the az of this SchedulerAffinity.

        :return: The az of this SchedulerAffinity.
        :rtype: list[str]
        """
        return self._az

    @az.setter
    def az(self, az):
        r"""Sets the az of this SchedulerAffinity.

        :param az: The az of this SchedulerAffinity.
        :type az: list[str]
        """
        self._az = az

    @property
    def node(self):
        r"""Gets the node of this SchedulerAffinity.

        :return: The node of this SchedulerAffinity.
        :rtype: list[str]
        """
        return self._node

    @node.setter
    def node(self, node):
        r"""Sets the node of this SchedulerAffinity.

        :param node: The node of this SchedulerAffinity.
        :type node: list[str]
        """
        self._node = node

    @property
    def application(self):
        r"""Gets the application of this SchedulerAffinity.

        :return: The application of this SchedulerAffinity.
        :rtype: list[str]
        """
        return self._application

    @application.setter
    def application(self, application):
        r"""Sets the application of this SchedulerAffinity.

        :param application: The application of this SchedulerAffinity.
        :type application: list[str]
        """
        self._application = application

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
        if not isinstance(other, SchedulerAffinity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
