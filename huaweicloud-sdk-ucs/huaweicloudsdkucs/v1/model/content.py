# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Content:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'verbs': 'list[str]',
        'resources': 'list[str]'
    }

    attribute_map = {
        'verbs': 'verbs',
        'resources': 'resources'
    }

    def __init__(self, verbs=None, resources=None):
        r"""Content

        The model defined in huaweicloud sdk

        :param verbs: 动作列表
        :type verbs: list[str]
        :param resources: 资源列表
        :type resources: list[str]
        """
        
        

        self._verbs = None
        self._resources = None
        self.discriminator = None

        if verbs is not None:
            self.verbs = verbs
        if resources is not None:
            self.resources = resources

    @property
    def verbs(self):
        r"""Gets the verbs of this Content.

        动作列表

        :return: The verbs of this Content.
        :rtype: list[str]
        """
        return self._verbs

    @verbs.setter
    def verbs(self, verbs):
        r"""Sets the verbs of this Content.

        动作列表

        :param verbs: The verbs of this Content.
        :type verbs: list[str]
        """
        self._verbs = verbs

    @property
    def resources(self):
        r"""Gets the resources of this Content.

        资源列表

        :return: The resources of this Content.
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this Content.

        资源列表

        :param resources: The resources of this Content.
        :type resources: list[str]
        """
        self._resources = resources

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
        if not isinstance(other, Content):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
