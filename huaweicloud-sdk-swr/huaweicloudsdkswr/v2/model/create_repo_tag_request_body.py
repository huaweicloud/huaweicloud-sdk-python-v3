# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRepoTagRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_tag': 'str',
        'destination_tag': 'str',
        'override': 'bool'
    }

    attribute_map = {
        'source_tag': 'source_tag',
        'destination_tag': 'destination_tag',
        'override': 'override'
    }

    def __init__(self, source_tag=None, destination_tag=None, override=None):
        r"""CreateRepoTagRequestBody

        The model defined in huaweicloud sdk

        :param source_tag: 源镜像版本名称
        :type source_tag: str
        :param destination_tag: 目标镜像版本名称
        :type destination_tag: str
        :param override: 是否覆盖
        :type override: bool
        """
        
        

        self._source_tag = None
        self._destination_tag = None
        self._override = None
        self.discriminator = None

        self.source_tag = source_tag
        self.destination_tag = destination_tag
        if override is not None:
            self.override = override

    @property
    def source_tag(self):
        r"""Gets the source_tag of this CreateRepoTagRequestBody.

        源镜像版本名称

        :return: The source_tag of this CreateRepoTagRequestBody.
        :rtype: str
        """
        return self._source_tag

    @source_tag.setter
    def source_tag(self, source_tag):
        r"""Sets the source_tag of this CreateRepoTagRequestBody.

        源镜像版本名称

        :param source_tag: The source_tag of this CreateRepoTagRequestBody.
        :type source_tag: str
        """
        self._source_tag = source_tag

    @property
    def destination_tag(self):
        r"""Gets the destination_tag of this CreateRepoTagRequestBody.

        目标镜像版本名称

        :return: The destination_tag of this CreateRepoTagRequestBody.
        :rtype: str
        """
        return self._destination_tag

    @destination_tag.setter
    def destination_tag(self, destination_tag):
        r"""Sets the destination_tag of this CreateRepoTagRequestBody.

        目标镜像版本名称

        :param destination_tag: The destination_tag of this CreateRepoTagRequestBody.
        :type destination_tag: str
        """
        self._destination_tag = destination_tag

    @property
    def override(self):
        r"""Gets the override of this CreateRepoTagRequestBody.

        是否覆盖

        :return: The override of this CreateRepoTagRequestBody.
        :rtype: bool
        """
        return self._override

    @override.setter
    def override(self, override):
        r"""Sets the override of this CreateRepoTagRequestBody.

        是否覆盖

        :param override: The override of this CreateRepoTagRequestBody.
        :type override: bool
        """
        self._override = override

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
        if not isinstance(other, CreateRepoTagRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
