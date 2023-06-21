# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationLifecycle:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'entrypoint': 'LifecycleEntrypoint',
        'post_start': 'LifecycleProcess',
        'pre_stop': 'LifecycleProcess'
    }

    attribute_map = {
        'entrypoint': 'entrypoint',
        'post_start': 'post-start',
        'pre_stop': 'pre-stop'
    }

    def __init__(self, entrypoint=None, post_start=None, pre_stop=None):
        """ConfigurationLifecycle

        The model defined in huaweicloud sdk

        :param entrypoint: 
        :type entrypoint: :class:`huaweicloudsdkservicestage.v2.LifecycleEntrypoint`
        :param post_start: 
        :type post_start: :class:`huaweicloudsdkservicestage.v2.LifecycleProcess`
        :param pre_stop: 
        :type pre_stop: :class:`huaweicloudsdkservicestage.v2.LifecycleProcess`
        """
        
        

        self._entrypoint = None
        self._post_start = None
        self._pre_stop = None
        self.discriminator = None

        if entrypoint is not None:
            self.entrypoint = entrypoint
        if post_start is not None:
            self.post_start = post_start
        if pre_stop is not None:
            self.pre_stop = pre_stop

    @property
    def entrypoint(self):
        """Gets the entrypoint of this ConfigurationLifecycle.

        :return: The entrypoint of this ConfigurationLifecycle.
        :rtype: :class:`huaweicloudsdkservicestage.v2.LifecycleEntrypoint`
        """
        return self._entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint):
        """Sets the entrypoint of this ConfigurationLifecycle.

        :param entrypoint: The entrypoint of this ConfigurationLifecycle.
        :type entrypoint: :class:`huaweicloudsdkservicestage.v2.LifecycleEntrypoint`
        """
        self._entrypoint = entrypoint

    @property
    def post_start(self):
        """Gets the post_start of this ConfigurationLifecycle.

        :return: The post_start of this ConfigurationLifecycle.
        :rtype: :class:`huaweicloudsdkservicestage.v2.LifecycleProcess`
        """
        return self._post_start

    @post_start.setter
    def post_start(self, post_start):
        """Sets the post_start of this ConfigurationLifecycle.

        :param post_start: The post_start of this ConfigurationLifecycle.
        :type post_start: :class:`huaweicloudsdkservicestage.v2.LifecycleProcess`
        """
        self._post_start = post_start

    @property
    def pre_stop(self):
        """Gets the pre_stop of this ConfigurationLifecycle.

        :return: The pre_stop of this ConfigurationLifecycle.
        :rtype: :class:`huaweicloudsdkservicestage.v2.LifecycleProcess`
        """
        return self._pre_stop

    @pre_stop.setter
    def pre_stop(self, pre_stop):
        """Sets the pre_stop of this ConfigurationLifecycle.

        :param pre_stop: The pre_stop of this ConfigurationLifecycle.
        :type pre_stop: :class:`huaweicloudsdkservicestage.v2.LifecycleProcess`
        """
        self._pre_stop = pre_stop

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
        if not isinstance(other, ConfigurationLifecycle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
