# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRunRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'computing_resource_id': 'str',
        'conf': 'list[str]'
    }

    attribute_map = {
        'computing_resource_id': 'computing_resource_id',
        'conf': 'conf'
    }

    def __init__(self, computing_resource_id=None, conf=None):
        """CreateRunRequestBody

        The model defined in huaweicloud sdk

        :param computing_resource_id: 计算资源ID。
        :type computing_resource_id: str
        :param conf: 作业配置项。
        :type conf: list[str]
        """
        
        

        self._computing_resource_id = None
        self._conf = None
        self.discriminator = None

        self.computing_resource_id = computing_resource_id
        if conf is not None:
            self.conf = conf

    @property
    def computing_resource_id(self):
        """Gets the computing_resource_id of this CreateRunRequestBody.

        计算资源ID。

        :return: The computing_resource_id of this CreateRunRequestBody.
        :rtype: str
        """
        return self._computing_resource_id

    @computing_resource_id.setter
    def computing_resource_id(self, computing_resource_id):
        """Sets the computing_resource_id of this CreateRunRequestBody.

        计算资源ID。

        :param computing_resource_id: The computing_resource_id of this CreateRunRequestBody.
        :type computing_resource_id: str
        """
        self._computing_resource_id = computing_resource_id

    @property
    def conf(self):
        """Gets the conf of this CreateRunRequestBody.

        作业配置项。

        :return: The conf of this CreateRunRequestBody.
        :rtype: list[str]
        """
        return self._conf

    @conf.setter
    def conf(self, conf):
        """Sets the conf of this CreateRunRequestBody.

        作业配置项。

        :param conf: The conf of this CreateRunRequestBody.
        :type conf: list[str]
        """
        self._conf = conf

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
        if not isinstance(other, CreateRunRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
