# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerHooks:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'post_start': 'Config',
        'pre_start': 'Config'
    }

    attribute_map = {
        'post_start': 'post_start',
        'pre_start': 'pre_start'
    }

    def __init__(self, post_start=None, pre_start=None):
        r"""ContainerHooks

        The model defined in huaweicloud sdk

        :param post_start: 
        :type post_start: :class:`huaweicloudsdkmodelarts.v1.Config`
        :param pre_start: 
        :type pre_start: :class:`huaweicloudsdkmodelarts.v1.Config`
        """
        
        

        self._post_start = None
        self._pre_start = None
        self.discriminator = None

        if post_start is not None:
            self.post_start = post_start
        if pre_start is not None:
            self.pre_start = pre_start

    @property
    def post_start(self):
        r"""Gets the post_start of this ContainerHooks.

        :return: The post_start of this ContainerHooks.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Config`
        """
        return self._post_start

    @post_start.setter
    def post_start(self, post_start):
        r"""Sets the post_start of this ContainerHooks.

        :param post_start: The post_start of this ContainerHooks.
        :type post_start: :class:`huaweicloudsdkmodelarts.v1.Config`
        """
        self._post_start = post_start

    @property
    def pre_start(self):
        r"""Gets the pre_start of this ContainerHooks.

        :return: The pre_start of this ContainerHooks.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Config`
        """
        return self._pre_start

    @pre_start.setter
    def pre_start(self, pre_start):
        r"""Sets the pre_start of this ContainerHooks.

        :param pre_start: The pre_start of this ContainerHooks.
        :type pre_start: :class:`huaweicloudsdkmodelarts.v1.Config`
        """
        self._pre_start = pre_start

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
        if not isinstance(other, ContainerHooks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
