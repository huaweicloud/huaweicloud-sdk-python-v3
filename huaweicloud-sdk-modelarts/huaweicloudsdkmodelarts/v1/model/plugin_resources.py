# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginResources:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'involved_object': 'ObjectReference',
        'replicas': 'int',
        'limits': 'dict(str, str)',
        'requests': 'dict(str, str)'
    }

    attribute_map = {
        'involved_object': 'involvedObject',
        'replicas': 'replicas',
        'limits': 'limits',
        'requests': 'requests'
    }

    def __init__(self, involved_object=None, replicas=None, limits=None, requests=None):
        r"""PluginResources

        The model defined in huaweicloud sdk

        :param involved_object: 
        :type involved_object: :class:`huaweicloudsdkmodelarts.v1.ObjectReference`
        :param replicas: **参数解释**： 资源对象的副本数。 **取值范围**： 不涉及。
        :type replicas: int
        :param limits: **参数解释**： 申请的资源限制。
        :type limits: dict(str, str)
        :param requests: **参数解释**： 申请的资源需求。
        :type requests: dict(str, str)
        """
        
        

        self._involved_object = None
        self._replicas = None
        self._limits = None
        self._requests = None
        self.discriminator = None

        if involved_object is not None:
            self.involved_object = involved_object
        if replicas is not None:
            self.replicas = replicas
        if limits is not None:
            self.limits = limits
        if requests is not None:
            self.requests = requests

    @property
    def involved_object(self):
        r"""Gets the involved_object of this PluginResources.

        :return: The involved_object of this PluginResources.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ObjectReference`
        """
        return self._involved_object

    @involved_object.setter
    def involved_object(self, involved_object):
        r"""Sets the involved_object of this PluginResources.

        :param involved_object: The involved_object of this PluginResources.
        :type involved_object: :class:`huaweicloudsdkmodelarts.v1.ObjectReference`
        """
        self._involved_object = involved_object

    @property
    def replicas(self):
        r"""Gets the replicas of this PluginResources.

        **参数解释**： 资源对象的副本数。 **取值范围**： 不涉及。

        :return: The replicas of this PluginResources.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        r"""Sets the replicas of this PluginResources.

        **参数解释**： 资源对象的副本数。 **取值范围**： 不涉及。

        :param replicas: The replicas of this PluginResources.
        :type replicas: int
        """
        self._replicas = replicas

    @property
    def limits(self):
        r"""Gets the limits of this PluginResources.

        **参数解释**： 申请的资源限制。

        :return: The limits of this PluginResources.
        :rtype: dict(str, str)
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        r"""Sets the limits of this PluginResources.

        **参数解释**： 申请的资源限制。

        :param limits: The limits of this PluginResources.
        :type limits: dict(str, str)
        """
        self._limits = limits

    @property
    def requests(self):
        r"""Gets the requests of this PluginResources.

        **参数解释**： 申请的资源需求。

        :return: The requests of this PluginResources.
        :rtype: dict(str, str)
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        r"""Sets the requests of this PluginResources.

        **参数解释**： 申请的资源需求。

        :param requests: The requests of this PluginResources.
        :type requests: dict(str, str)
        """
        self._requests = requests

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PluginResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
